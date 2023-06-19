from pymongo import MongoClient

URL = "mongodb://mongo:27017"

def add_data():
    with MongoClient(URL) as client:
        db = client["test"]
        # datetime = datetime.datetime.now()
        collection = db["testcoll"]
        data = [{"adi": "Emirhan", "soyadi": "Tulimat"}]
        result = collection.insert_many(data)
        print("Yeni kayıt eklendi.")
        # print(f"{result.inserted_count} kayıt eklendi.")

if __name__ == "__main__":
    add_data()
