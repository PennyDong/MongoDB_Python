import pymongo

client=pymongo.MongoClient(
    "mongodb+srv://milk:milk0000@milkteam.vyzjimd.mongodb.net/?retryWrites=true&w=majority"
)
db=client.traning_mongo #選擇操作的資料庫(milk)
collection=db.users #選擇操作 users 集合

collection.insert_one({
    "name":"Penny",
    "gender":"男"
})

print("資料新增成功")