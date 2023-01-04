from kafka import KafkaProducer
import json
import random
from time import sleep
from datetime import datetime

# Create an instance of the Kafka producer
producer = KafkaProducer(bootstrap_servers='kafka-server:9092',
                         value_serializer=lambda m: json.dumps(
                             m).encode('utf-8'),
                         api_version=(0, 11, 5))

stream_algorithm_str = {"id":"1","import_str": "from sklearn.