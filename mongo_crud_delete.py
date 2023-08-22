import pymongo
client=pymongo.MongoClient(
    "mongodb+srv://milk:milk0000@milkteam.vyzjimd.mongodb.net/?retryWrites=true&w=majority"
)

db=client.traning_mongo_copy
collection=db.users_copy
"""
result=collection.delete_one({
    "address":40
})

print("實際刪除的資料數量",result.deleted_count)
"""
result=collection.delete_many({
    "gender":"apple"
})

print("實際刪除的資料數量",result.deleted_count)
