from kafka import KafkaProducer
import json
import traceback

class MessageProducer:
    broker = ""
    topic = ""
    producer = None

    def __init__(self, broker, topic):
        self.broker = broker
        self.topic = topic
        self.producer = KafkaProducer(bootstrap_servers=self.broker,
                                      api_version=(0, 11, 5),
                                      value_serializer=lambda x: json.dumps(x).encode('utf-8'))

    def send_msg(self, msg):
        print("sending message...")
        try:
            future = self.producer.send(self.topic, msg)
            self.producer.flush()
            future.get(timeout=60)
            print("message sent successfully...")
            return {"status_code": 200, "error": None}
        except Exception as ex:
            traceback.print_exc()
            return str(ex)


broker = "localhost:9092"
topic = "testtopic"
message_producer = MessageProducer(broker, topic)

# data = {"adi": "Mo", "soyadi": "Salah"}
# resp = message_producer.send_msg(data)
# print(resp)
