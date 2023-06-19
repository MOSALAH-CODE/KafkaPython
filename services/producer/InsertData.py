from pymongo import MongoClient

URL = "mongodb+srv://mohammadsalah:j3jAEhUOvjxSOUG4@cluster0.35szzhv.mongodb.net/?retryWrites=true&w=majority"

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
