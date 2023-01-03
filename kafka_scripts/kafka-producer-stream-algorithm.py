from kafka import KafkaProducer
import json
import random
from time import sleep
from datetime import datetime

# Create an instance of the Kafka producer
producer = KafkaProducer(bootstrap_servers='kafka-server:9092',
                         value_serializer=lambda m: json.dumps(
                             m).enco