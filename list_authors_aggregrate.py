'''
Created on Jun 4, 2018

@author: SHAREIDEAS
URL:www.shareideas.net
'''
from pymongo import MongoClient
print("Program is running...")
fp = open("ouput.txt", 'a')
client = MongoClient('210.30.97.43',
                     username='userR',
                     password='thealphaR',
                     authSource='ms-datasets',
                     authMechanism='SCRAM-SHA-1')

database = client["ms-datasets"]
insertcoll = database["fields_rank"]


# pipeline = [{"$unwind":"$authors"},
#             {"$group":{"_id":"$authors","count":{"$sum":1}}},
#             {"$sort":{"count":-1}}
#             ,{"$limit":20}] 

pipeline = [{"$project":{"authors.name":1}}
             ,{"$unwind":"$authors"}
             ,{"$group":{"_id":"$authors","count":{"$sum":1}}}
             ,{"$sort":{"count":-1}}]
#              ,{"$limit":0}] 



#cursor = collection.find({},{"fos": 1,"_id":0},limit = 100)
  
# pipeline = [{"$project":{"fos":1}},
#             {"$group":{"_id":"$fos","count":{"$sum":1}}},
#             {"$sort":{"count":-1}},
#             {"$limit":15}]  
try:
    for i in [8]:
        collection = database["mag_papers_"+str(i)]
        cursor = collection.aggregate(pipeline,allowDiskUse = True).batch_size(10000)
        print("Document:"+str(i))
        fp.writelines("Document:"+str(i)+'\n') 
        
        for doc in cursor:
            #print(doc["_id"],doc["count"])
            fp.writelines(str(doc["_id"])+" "+str(doc["count"])+'\n') 
            
        cursor.close()    
          
finally:
    client.close()
    fp.close()
print("Program is end.")

















