from kafka import KafkaProducer
import json

clientId = "mock-up-kafka-producer-client"
brokers = ["kafka:9092"]
topic = "testtopic"
kafka = KafkaProducer(bootstrap_servers=['localhost:9092'],
                      api_version=(0,11,5),
                      value_serializer=lambda x: json.dumps(x).encode('utf-8'))

async def create_producer(mess):
    try:
        for m in mess:
            kafka.send(topic, value=m, partition=0)
        kafka.flush()
        print("Gönderim işlemi başarılıdır")
    except Exception as e:
        print("Hata:", e)
    finally:
        kafka.close()
