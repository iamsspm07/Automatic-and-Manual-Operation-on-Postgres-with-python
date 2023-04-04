
# Import Required Library
import pandas as pd
import requests
import psycopg2
import csv

# Declaring empty collable variable
csvFile = ""

# Database Connection Parameters
connectTopostgresql = psycopg2.connect(
    database = "postgres",
    user = 'postgres',
    password = '*****************',
    host = '127.0.0.1',
    port = '5432'
)

# Database Connection Initialize
curr = connectTopostgresql.cursor()
curr.execute("select version()")

data = curr.fetchone()
print("Connection Established To :", data)

# Insert Python Csv to Postgresql 
filePath = "D:\AI_ML\combined_dataset.csv"
with open(filePath, mode='r') as file:
    count = 0
    csvFile = csv.reader(file)
    for row in csvFile:
        curr.execute("INSERT INTO connection.heart_diseas(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, num)VALUES ('"+str(row[0])+"', '"+str(row[1])+"', '"+str(row[2])+"', '"+str(row[3])+"', '"+str(row[4])+"', '"+str(row[5])+"', '"+str(row[6])+"', '"+str(row[7])+"', '"+str(row[8])+"', '"+str(row[9])+"');")
connectTopostgresql.commit()


curr.close()
connectTopostgresql.close()