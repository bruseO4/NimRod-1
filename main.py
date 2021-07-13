from bs4 import BeautifulSoup
import mysql_connection
import request
import app
import tup

user_input = input("Simply describe what you want to see in HTML:\n")
#user_input = app.my_form

response = request.openai_request(user_input)
# python3 main.py
response=tup.convertTuple(response)
soup=BeautifulSoup(response, "html.parser")
with open("output.html", "w", encoding = 'utf-8') as file:
    file.write(soup.prettify())

mysql_connection.save_data(user_input, response)


#print(soup.prettify())
