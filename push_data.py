import os  
import sys  
import json  

from dotenv import load_dotenv 
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

import certifi 
ca = certifi.where()

import pandas as pd 
import numpy as np
import pymongo 
from networkSecurity.exception.exception import NetworkSecurityException
from networkSecurity.logging.logger import logging

class NetworkDataExtact():

    def __init__(self):

        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def csv_to_json(self, file_path):
        try:
            
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records =list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def insert_data_mongodb(self, records, database, collection):
        try:
            self.database = database    
            self.collection = collection
            self.records = records

            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]

            self.collection.insert_many(self.records)

            return (len(self.records), "Records inserted successfully")
        except Exception as e:
            raise NetworkSecurityException(e, sys)

if __name__ == "__main__":
    FILE_PATH = "Network_Data\phisingData.csv"
    DATABASE = "NetworkSecurity"
    Collection = "NetworkData"

    networkObj = NetworkDataExtact()
    records = networkObj.csv_to_json(file_path = FILE_PATH)
    print(records)  # Print the first record to verify
    no_of_records = networkObj.insert_data_mongodb(records, DATABASE, Collection)
    print(no_of_records)




