import asyncio
from producer import create_producer
from pymongo import MongoClient

URL = "mongodb+srv://mohammadsalah:j3jAEhUOvjxSOUG4@cluster0.35szzhv.mongodb.net/?retryWrites=true&w=majority"

async def create_db():
    client = await MongoClient.connect(URL)
    try:
        db = client["test"]
        collection = await db.create_collection("testcoll")
        print("Koleksiyon oluşturuldu.")
    except Exception as e:
        print(e)
    finally:
        client.close()

async def get_data():
    client = await MongoClient.connect(URL)
    db = client["test"]
    collection = await db.collection("testcoll")
    result = await collection.find()
    data = await result.to_list(length=None)
    await client.close()
    return data

async def main():
    await create_db()

    before_data = [{}]
    while True:
        print("Yeni kayıt var mı kontrol ediliyor...")
        current_data = await get_data()
        if current_data:
            new_data = []
            for cd in current_data:
                data = next((bd for bd in before_data if bd["_id"].toString() == cd["_id"].toString()), None)
                if not data:
                    new_data.append(cd)
            before_data = current_data
            if new_data:
                await create_producer(new_data)
        await asyncio.sleep(10)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
