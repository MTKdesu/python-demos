'''
Author: William Li
Created At: June 11, 2023
Description: 
This is a demo to show how to export data from MySql database to a csv file using python. 
This demo has the following features: 
    OOD
    General python code structure
    Parameters
    MySQL data source
    Time estimation
    Detail comments
'''

import datetime
import mysql.connector
import csv

class dataExporter:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor  = None
    
    # Connect to the database
    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()
        print("Connected to the database.")

    # Export table into a csv file
    def exportData(self,sql):
        self.cursor.execute(sql)
        with open("output.csv","w",newline="") as csvfilet:
            writer = csv.writer(csvfilet)
            writer.writerow(self.cursor)

    # Close the connection of the database
    def closeConnection(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("Database connection closed.") 

def main():

    print("Started at")
    print (datetime.datetime.now())
    dbParams = {
        "host": "localhost",
        "user": "root",
        "password": "4859",
        "database": "demodb"
    }
    selectSql = "SELECT * FROM student"
    Exporter=dataExporter(**dbParams)
    Exporter.connect()
    Exporter.exportData(selectSql)
    Exporter.closeConnection()
    print("Ended at:")
    print(datetime.datetime.now())

if __name__ == '__main__':
    main()