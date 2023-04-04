from rocketry import Rocketry
import pandas as pd
import requests
import psycopg2
import csv

file = "D:\AI_ML\Run.bat"

application = Rocketry()

connectTopostgresql = psycopg2.connect(
    database = "postgres",
    user = 'postgres',
    password = '*****************',
    host = '127.0.0.1',
    port = '5432'
)

@application.task('every 5 second')
def do_something():
    curr = connectTopostgresql.cursor()
    curr.execute("select version()")

    data = curr.fetchone()
    print("Connection Established To :", data)



if __name__=="__main__":
    application.run()