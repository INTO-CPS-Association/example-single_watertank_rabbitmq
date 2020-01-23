#!/usr/bin/env python3
import pika
import json
import datetime
import csv

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

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


connection.close()
