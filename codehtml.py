import json
import os
import openai
import constant
import logit_bias_2 
import logit_bias_1 

user_input = input("Simply describe what you want your website to be:\n")

print("\nLet me see what I can do...\n")

with open('keys.json') as f:
  keys = json.load(f)

openai.api_key = keys['openapi']

def openai_request(request):
    with open('keys.json') as f:
      keys = json.load(f)
      
      openai.api_key = keys['openapi']

start_request = "\n<html>" + "\n<head>" +"\n<link rel='icon' href='1.ico' type='image/x-icon'/>" + "\n<title>" + user_input + "</title>\n"+ "<script src='script.js'></script>\n" + "<style>\n" + "body{\n" + "background-color:"

response = openai.Completion.create(
      prompt=start_request,
      engine=constant.ENGINE,
      max_tokens=constant.MAX_TOKENS,
      frequency_penalty=constant.FREQUENCY_PENALTY,
      logit_bias=logit_bias_1.logit_bias_1,
      presence_penalty=constant.PRESENCE_PENALTY,
      temperature=constant.TEMPERATURE,
      top_p=constant.TOP_P,
    
  )
response.choices[0].text
css_code = start_request+response.choices[0].text + "\n</style>" + "\n<body>\n"

start_request = css_code
response2 = openai.Completion.create(
      prompt=start_request,
      engine=constant.ENGINE,
      max_tokens=constant.MAX_TOKENS,
      frequency_penalty=constant.FREQUENCY_PENALTY,
      logit_bias=logit_bias_2.logit_bias_2,
      presence_penalty=constant.PRESENCE_PENALTY,
      temperature=constant.TEMPERATURE,
      top_p=constant.TOP_P,
    
  )
response2.choices[0].text
html_code = css_code+ "\n\n<!--This is where the html starts...-->\n\n"+response2.choices[0].text + "\n </html>"
html_code = html_code.lower()
print(html_code)

