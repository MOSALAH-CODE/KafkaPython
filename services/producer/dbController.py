import asyncio
from pymongo import MongoClient

URL = "mongodb://mongo:27017"

def create_db():
    client = MongoClient(URL)
    try:
        db = client["test"]
        collection = db.create_collection("testcoll")
        print("Koleksiyon oluşturuldu.")
    except Exception as e:
        print(e)
    finally:
        client.close()

def get_data():
    client = MongoClient(URL)
    db = client["test"]
    collection = db["testcoll"]
    result = collection.find()
    data = list(result)
    client.close()
    return data

async def execute_async():
    create_db()

    before_data = [{}]
    while True:
        print("Yeni kayıt var mı kontrol ediliyor...")
        current_data = get_data()
        if current_data:
            new_data = []
            for cd in current_data:
                data = next((bd for bd in before_data if bd["_id"].toString() == cd["_id"].toString()), None)
                if not data:
                    new_data.append(cd)
            before_data = current_data
            if new_data:
                print("Gönderilecek yeni veriler:", new_data)
                # Call your message producer function here
        await asyncio.sleep(10)

def main():
    loop = asyncio.get_event_loop()
    loop.create_task(execute_async())
    loop.run_forever()

if __name__ == "__main__":
    main()
