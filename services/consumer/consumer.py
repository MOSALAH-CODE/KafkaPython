import sys

from kafka import KafkaConsumer

client_id = "mock-up-kafka-producer-client"
brokers = ["kafka:9092"]
topic = "testtopic"

def consume():
    group_id = sys.argv[1] if len(sys.argv) > 1 else "group1"
    consumer = KafkaConsumer(
        topic,
        group_id=group_id,
        bootstrap_servers=brokers,
    )
    data = []
    for message in consumer:
        print(f"{group_id}.consumer received message: {message.value.decode('utf-8')}")
        data.append(message.value)
    return data

if __name__ == "__main__":
    try:
        data = consume()
        print("consumed successfully")
    except Exception as e:
        print(e)
