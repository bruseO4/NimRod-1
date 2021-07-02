import json
import mysql.connector

with open('keys.json') as f:
    keys = json.load(f)

mydb = mysql.connector.connect(
    host=keys['mysql']['host'],
    user=keys['mysql']['user'],
    password=keys['mysql']['password']
)

print(mydb)
