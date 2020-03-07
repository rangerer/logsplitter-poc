from time import sleep
import sys

from kafka import KafkaConsumer, KafkaProducer
from kafka.errors import KafkaError, NoBrokersAvailable

def error(message):
    print(message, file=sys.stderr)

bootstrap_servers = ["kafka:9092"]

# connect consumer process to test topic (10 retries w/ 30s delay = 5 minutes)
for i in range(10):
    try:
        consumer = KafkaConsumer("test", bootstrap_servers=bootstrap_servers)
        break
    except NoBrokersAvailable:
        error("unable to connect to bootstrap servers {} - retrying in 30 seconds".format(bootstrap_servers))
        sleep(30)
else:
    error("unable to connect to bootstrap servers {} for 5 minutes - stopping".format(bootstrap_servers))
    quit(100)

# connect producer process
producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

# receive message from test and filter into test_hello topic
for message in consumer:
    payload = message.value.decode("utf-8")
    print("> {}".format(payload))
    if payload.find("hello") != -1:
        try:
            producer.send("test_hello", message.value, message.key)
            print("< {}".format(payload))
        except KafkaError:
            error("unable to send message {}".format(payload))
