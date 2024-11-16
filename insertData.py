'''
Author: William Li
Created At: June 5, 2023
Description: 
This is a demo to show how to insert data into MySql database using python. 
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

class dataInserter:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor  = None

    #Connect to the database
    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()
        print("Connected to the database.")
    
    #Insert data into the database
    def insertData(self, sql, values):
        self.cursor.executemany(sql,values)
        self.connection.commit()

    #Fetch data from the database and display them
    def fetchData(self, sql):
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        print("Table data after update:\n")
        for row in results:
            print(row)

    #Close the connection of the database
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
    insertSql = "INSERT INTO student (name, id) VALUES (%s, %s)"
    data = [
        ('William', 1),
        ('Ben', 2),
        ('Michael', 3),
        ('Amy', 4),
        ('Zoe', 5),
    ]
    selectSql = "SELECT * FROM student"

    Inserter=dataInserter(**dbParams)
    Inserter.connect()
    Inserter.insertData(insertSql,data)
    Inserter.fetchData(selectSql)
    Inserter.closeConnection()
    print("Ended at:")
    print(datetime.datetime.now())

if __name__ == '__main__':
    main()