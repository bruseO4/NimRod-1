import mysql_connection
import request

user_input = input("Simply describe what you want to see in HTML:\n")

response = request.openai_request(user_input)
# python3 main.py

mysql_connection.save_data(user_input, response)

print(response)
