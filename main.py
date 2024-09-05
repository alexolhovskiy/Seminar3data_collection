
from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi
import json
from pprint import pprint
import time
from key import password


# db="alex_olhovskiy_test_db"
uri = f"mongodb+srv://python-user1:{password}@cluster0.mu4c0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
0
client = MongoClient(uri)#, server_api=ServerApi('1'))

db = client['alex_olhovskiy_test_db']

collection=db['Books']

#Закидываю дату с книгами
# with open('books.json','r') as f:
#     data=json.load(f)

# pprint(data)

# n=0
# for item in data:
#     collection.insert_one(item)
#     print(n)
#     n+=1
#     time.sleep(1)


#Запросил по названию тестово
# cursor=collection.find({"title": "The Dirty Little Secrets of Getting Your Dream Job"})

# for doc in cursor:
#     pprint(doc)



#Забыл преобразовать количество книг для продажи в int - исправляемся
# cursor = collection.find({"in_stock": {"$type": "string"}})

# for doc in cursor:
#     try:
#         in_stock_as_int = int(doc['in_stock'])
#         collection.update_one(
#             {"_id": doc["_id"]},
#             {"$set": {"in_stock": in_stock_as_int}}
#         )
#         print(f"Документ с _id: {doc['_id']} обновлён!")
#     except ValueError:
#         print(f"Не удалось преобразовать поле 'in_stock' для документа с _id: {doc['_id']}")

# print("Все документы обновлены!")


#Тоже делаем и с ценой! А загагулину выносим в поле units - типа денежная еденица
# cursor = collection.find({"price": {"$type": "string"}})

# for doc in cursor:
#     try:

#         price_str = doc['price']
#         price_int=float(price_str[2:])
#         price_unit=price_str[1:2]
#         print(f"price:{price_int},units:{price_unit}")
#         collection.update_one(
#             {"_id": doc["_id"]},
#             {"$set": {"price": price_int,"units": price_unit}}
#         )


#         print(f"Документ с _id: {doc['_id']} обновлён! price:{price_int},units:{price_unit}")
#     except ValueError:
#         print(f"Не удалось преобразовать поле 'price' и/или добавить 'units' для документа с _id: {doc['_id']}")

# print("Все документы обновлены!")


#Примеры запросов:
#1)Запросим книженции которых в наличии больше 20 или которые дешевле 30 карлюк
print("More than 20")
cursor = collection.find({"$or":[{"in_stock": {"$gt": 20}},{"price":{"$lt":11}}]},{"_id":0,"title":1,"price":1,"in_stock":1})
for doc in cursor:
    pprint(doc)

print()
#2)Запросим книги, которых больше 5 в наличии и цена которых от 40 до 50 загагулин
print("More than 15 and 50-55")
cursor = collection.find({"in_stock": {"$gt": 19},"price":{"$gt":50,"$lt":55}},{"_id":0,"title":1,"price":1,"in_stock":1})
for doc in cursor:
    pprint(doc)
print()
#3)5 самых дорогих
print("most exspensive")
cursor = collection.find({},{"_id":0,"title":1,"price":1,"in_stock":1}).sort("price", -1).limit(5)
for doc in cursor:
    pprint(doc)
