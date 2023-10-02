from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

URI = 'mongodb://localhost:27017/'

# Create a new client and connect to the server
client = MongoClient(URI, server_api=ServerApi('1'))


try:
    client.admin.command('ping')
    print('Te has conectado a mongo con exito')
except Exception as e:
    print(e)


#conectar a una coleccion

db = client.test 

collection = db.CRUD