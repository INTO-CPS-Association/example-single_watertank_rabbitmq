#!/usr/bin/env python3
import pika
import json
import datetime
import time
import csv
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
print("Declaring exchange")
channel.exchange_declare(exchange='fmi_digital_twin', exchange_type='direct')
print("Creating queue")
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue
channel.queue_bind(exchange='fmi_digital_twin', queue=queue_name,
                   routing_key='linefollower')
print(' [*] Waiting for logs. To exit press CTRL+C')
def publish():
	dt=datetime.datetime.strptime('2019-01-04T16:41:24+0200', "%Y-%m-%dT%H:%M:%S%z")
	print(dt);
	msg = {}
	msg['time']= dt.isoformat()
	msg['level']=0
	with open('outputs.csv', newline='') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			t = float(row['time'])
			v = float(row['{tank}.tankInstance.level'])
			msg['level']=v
			dt = dt+ datetime.timedelta(seconds=float(row['step-size']))
			msg['time']= dt.isoformat()
			print(" [x] Sent %s" % json.dumps(msg))
			channel.basic_publish(exchange='fmi_digital_twin',
						routing_key='linefollower',
						body=json.dumps(msg))
   
def callback(ch, method, properties, body):
    print(" [x] %r" % body)
    if "waiting for input data for simulation" in str(body):
      publish()
channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)
channel.start_consuming()
connection.close()