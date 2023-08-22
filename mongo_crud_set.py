import pymongo
client=pymongo.MongoClient(
    "mongodb+srv://milk:milk0000@milkteam.vyzjimd.mongodb.net/?retryWrites=true&w=majority"
)

db=client.traning_mongo_copy
collection=db.users_copy


"""
更新一筆資料:

result=collection.update_one(
    { "name":"test"},{
    "$set":{"address":6} #此欄位和資料原本沒有，會自動幫你新增
    }
)

result=collection.update_one(
    { "name":"test"},{
    "$unset":{"address":""} #刪除欄位和欄位內容
    }
)

result=collection.update_one(
{ "name":"test"},{
    "$mul":{"address":5} #進行乘法與除法
    }
)
"""

result=collection.update_many({
    "address":30
},{
    "$set":{
    "address":40
    }
})


print("符合篩選條件的文件數量")
print(result.matched_count)
print("實際更新的文件數量")
print(result.modified_count)