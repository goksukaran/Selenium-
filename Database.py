'''
Created on 24 Dec 2018

@author: goksukara
'''
import pymysql
import json
import pandas as pd
from sqlalchemy import create_engine
from asn1crypto._ffi import null

pymysql.install_as_MySQLdb()
global DatabaseName
DatabaseName = "UK_data"

global DatabaseInstance


class database():
    def __init__(self):
         self.engine=0
         
    
    def connectdatabase(self):

        # import password
    
        with open("password.json", encoding="utf-8") as f:
            data = json.load(f)
    
        # Create a connection object
    
        databaseServerIP = "localhost"  # IP address of the MySQL database server
    
        databaseUserName = "root"  # User name of the database server
    
        DatabaseName = "Wg_gesucht"
    
        # Password for the database user
        databaseUserPassword = data["password"]
    
        # Name of the database that is to be created
    
       #  charSet = "utf8mb4"   Character set
    
        try:
            engine = create_engine(
                "mysql://" + 
                databaseUserName + 
                ":" + 
                databaseUserPassword + 
                "@" + 
                databaseServerIP + 
                "/" + 
                DatabaseName)
            # =======================================================================
            # connectionInstance = pymysql.connect(
            #     host=databaseServerIP,
            #     user=databaseUserName,
            #     password=databaseUserPassword,
            #     charset=charSet,
            #     cursorclass=cusrorType)
            # =======================================================================
    
        except Exception as e:
    
            print("connection failed".format(e))
        
        self.engine=engine    
        return engine
    
    def is_primarykey_exsist(self, tablename, query_id):
        with self.engine.connect() as con:
    
            sqlQuery = "SELECT * FROM `" + tablename + "` WHERE id= " + query_id
    
            result = con.execute(sqlQuery).fetchall()
            con.close()
            if (result is null):
    
                return True
            
            return False
    
    def insert_data(self, df):
        for index, row in df.iterrows():
            if(self.is_primarykey_exsist(row["cust_id"], self.engine, str(row["id"]))):
    
                print(df)
                df[index:index + 1].to_sql(name=row["cust_id"],
                                           con=self.engine, if_exists='append', index=False)
