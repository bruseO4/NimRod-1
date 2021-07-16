import constant
import json
import logit_bias_2
import logit_bias_1
import openai
from bs4 import BeautifulSoup
import tup
import mysql_connection
import unsplash


def openai_request(user_input):
    with open('keys.json') as f:
        keys = json.load(f)
    openai.api_key = keys['openapi']
    #photos=unsplash.search_unslash(user_input,unsplash.photo_features, unsplash.photo_ids, 1)
    #photos=tup.convertTuple(photos)
    #start_request = "\n<html>" + "\n<head>" +  "\n<title>" + user_input + "</title>\n" + \
        #"<script src='script.js'></script>\n" + "<img src='" + photos + "' alt='Girl in a jacket' width='500' height='600'>" + "<style>\n" + "<!--style only-->\n" + "body{\n"

    response = openai.Completion.create(
        prompt= "#Text to HTML Code: \nText: a website for a pizza shop \n HTML code: \n<html> \n<head> \n<title> + user_input + </title>\n <script src='script.js'></script>\n <img src=”” photos alt='pizza' width='500' height='600'> <style>\n <!--style only-->\n body{\n <h1 style='color: #FDD7E3;font-family: sans-serif'>Welcome to Pizza Pie!</h1><br /> <p style='font-size:14px'><strong>We pride ourselves on fresh pizzas made with real ingredients in a cozy environment.</strong></p><br /> <img src ='http://www.pizzapieonline.com/' width ='233' height ='80'/> </body> </html>",
        engine=constant.ENGINE,
        max_tokens=constant.MAX_TOKENS,
        frequency_penalty=constant.FREQUENCY_PENALTY,
        logit_bias=logit_bias_1.logit_bias_1,
        # logit_bias=logit_bias_1.logit_bias_1,
        presence_penalty=constant.PRESENCE_PENALTY,
        temperature=constant.TEMPERATURE,
        top_p=constant.TOP_P,

    )
    response=tup.convertTuple(response) 
    """
    response.choices[0].text
    css_code = start_request + \
        response.choices[0].text + "\n</style>" + "\n<body>\n"
    
        html_code = start_request+response.choices[0].text
        print(html_code)
        return response.choices[0].text
    

    #start_request = css_code
    response2 = openai.Completion.create(
        prompt=css_code,
        engine=constant.ENGINE,
        max_tokens=constant.MAX_TOKENS,
        frequency_penalty=constant.FREQUENCY_PENALTY,
        logit_bias=logit_bias_2.logit_bias_2,
        presence_penalty=constant.PRESENCE_PENALTY,
        temperature=constant.TEMPERATURE,
        top_p=constant.TOP_P,

    )
    
    response2.choices[0].text
    html_code = css_code + "\n\n<!--This is where the html starts...-->\n\n" + \
        response2.choices[0].text + "\n </html>"
    html_code = html_code.lower()
    print(html_code)
    
    return response.choices[0].text + response2.choices[0].text
    
"""