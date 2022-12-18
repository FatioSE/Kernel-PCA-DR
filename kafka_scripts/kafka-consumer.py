from kafka import KafkaConsumer

# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer('kafka-python-topic',
                        api_version=(0,11,5),
                        bootstrap_servers=['kafka-server:9092'])

for message in consumer:
    # me