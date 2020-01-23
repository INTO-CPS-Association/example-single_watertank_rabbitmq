
bash
```
# start rabbitmq
docker-compose up -d --build

# Start the simulation and then
python3 publish.py

# Stop and remove the server
docker-compose down -v
```
