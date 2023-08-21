import pymongo

client=pymongo.MongoClient(
    "mongodb+srv://milk:milk0000@milkteam.vyzjimd.mongodb.net/?retryWrites=true&w=majority"
)

#如果一開始沒有創立資料庫和集合，使用後會自動新增

db=client.traning_mongo #選擇操作的資料庫(traning_mongo)
collection=db.users #選擇操作 users 集合

#新增一筆資料 集合.insert_one({文件:資料})
#新增多筆資料 集合.insert_many([{文件:資料},{文件:資料},...])

result=collection.insert_one({ #result為編號
    "name":"test",
    "gender":"test"
})

#取得新增的一筆資料id:result.inserted_id

#取得新增的多筆資料的id:result.inserted_ids

print("資料新增成功")