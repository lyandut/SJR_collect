'''
Created on Jun 4, 2018

@author: SHAREIDEAS
URL:www.shareideas.net
'''

from pymongo import MongoClient

client = MongoClient('210.30.97.43',
                     username='userR',
                     password='thealphaR',
                     authSource='ms-datasets',
                     authMechanism='SCRAM-SHA-1')

database = client["ms-datasets"]
print database
collection = database["mag_papers_0"]

document = collection.find()
for each in document:
    print each

#Created with Studio 3T, the IDE for MongoDB - https://studio3t.com/
# query = {}
# cursor = collection.find(query)
# 
# try:
#     for doc in cursor :
#             print(doc)
# finally:
#     MongoClient.close()
