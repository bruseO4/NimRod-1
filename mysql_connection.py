import json
import mysql.connector

with open('keys.json') as f:
    keys = json.load(f)
    mydb = mysql.connector.connect(
        database=keys['mysql']['name'],
        host=keys['mysql']['host'],
        user=keys['mysql']['user'],
        password=keys['mysql']['password']
    )


def save_data(request, response):
    mycursor = mydb.cursor()

    sql = "INSERT INTO request (request, response) VALUES (%s, %s)"
    val = (request, response)
    mycursor.execute(sql, val)

    mydb.commit()
