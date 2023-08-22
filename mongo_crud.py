import pymongo
client=pymongo.MongoClient(
    "mongodb+srv://milk:milk0000@milkteam.vyzjimd.mongodb.net/?retryWrites=true&w=majority"
)

db=client.traning_mongo_copy
collection=db.users_copy



result=collection.update_one(
    { "name":"test"},{
    "$set":{"gender":"apple"}
    }
)

print("符合篩選條件的文件數量")
print(result.matched_count)
print("實際更新的文件數量")
print(result.modified_count)