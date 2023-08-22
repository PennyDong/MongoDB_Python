import pymongo
from bson.objectid import ObjectId
client=pymongo.MongoClient(
    "mongodb+srv://milk:milk0000@milkteam.vyzjimd.mongodb.net/?retryWrites=true&w=majority"
)

db=client.traning_mongo_copy 
collection=db.users_copy

#取得第一筆文件資料
data=collection.find_one()
print(data)
print("------------------")

#使用id取得文件
data=collection.find_one(
    ObjectId("64e301e741f19641b897ae73")
    )
print(data)
print("------------------")

#取得文件資料中的欄位
print(data["name"])
print(data["gender"])
print("------------------")

#一次取得多筆文件資料
cursor=collection.find()
print(cursor) #只會得到cursor物件的編號

for n in cursor:
    print(n["gender"])