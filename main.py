from bs4 import BeautifulSoup
import open_ai
import mysql_connection
import tup
import flask_server
import unsplash
from flask import request

user_input = input("Simply describe what you want to see in HTML:\n")
#user_input = flask_server.root()

response = open_ai.openai_request(user_input)
# python3 main.py
response=tup.convertTuple(response)
soup=BeautifulSoup(response, "html.parser")
with open("output.html", "w", encoding = 'utf-8') as file:
    file.write(soup.prettify())

mysql_connection.save_data(user_input, response)


#print(soup.prettify())
