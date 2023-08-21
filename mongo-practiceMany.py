import pymongo
import bson.objectid
client=pymongo.MongoClient(
    "mongodb+srv://milk:milk0000@milkteam.vyzjimd.mongodb.net/?retryWrites=true&w=majority"
)

#如果一開始沒有創立資料庫和集合，使用後會自動新增

db=client.traning_mongo_copy #選擇操作的資料庫(traning_mongoMany)
collection=db.users_copy #選擇操作 test_users 集合

#新增一筆資料 集合.insert_one({文件:資料})
#新增多筆資料 集合.insert_many([{文件:資料},{文件:資料},...])


data_insert=[
    {"name":"test","gender":"test"},
    {"name":"test1","gender":"test1"}
]
result=collection.insert_many(data_insert) #result為編號

#取得新增的一筆資料id:result.inserted_id
#取得新增的多筆資料的id:result.inserted_ids

print("資料新增成功")
print(result.inserted_ids)