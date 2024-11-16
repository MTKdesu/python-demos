'''
Author: William Li
Created At: Oct 15, 2024
Description: 
This is a demo to show how to read a csv file using python. 
This demo has the following features: 
    OOD
    General python code structure
    Parameters
    Csv data source
    Time estimation
    Detail comments
'''
import datetime
import csv

class csvReader:

    def __init__(self, csvFile):
        self.csvFile = csvFile

    # Read csv file and display each row.
    def openCsvFile(self):
        with open(self.csvFile,newline="") as csvfilet:
            reader = csv.reader(csvfilet)
            # List rows of the csv file.
            print("List rows of the csv file.")
            for row in reader:
                print(', '.join(row))

def main():
    print("Started at")
    print (datetime.datetime.now())
    csvFile = r"student.csv"
    objCsvReader = csvReader(csvFile)
    objCsvReader.openCsvFile()
    print("Ended at")
    print (datetime.datetime.now())
    
if __name__ == '__main__':
    main()