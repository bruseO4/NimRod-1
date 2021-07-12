import json
import os
import openai

user_input = input("Simply describe what you want to see in CSS:\n")
start_sequence ="",
print("\nLet me see what I can do...\n")

with open('keys.json') as f:
  keys = json.load(f)

openai.api_key = keys['openapi']

css_request ="body{\n"

response = openai.Completion.create(
engine="curie-instruct-beta", 
prompt=css_request, 
temperature=0.01,
max_tokens=800,
top_p=1,
best_of=1,
frequency_penalty=1,
presence_penalty=1,
logprobs=10,
logit_bias={
  "92": 5, #}
  "1391": -100, #"space"{
},
)
print(css_request+response.choices[0].text)

#python3 codecss.py


css_request_1 = "body{" + "\n" + "\nbackgroundcolor:(100,"

response_1 = openai.Completion.create(
engine="curie-instruct-beta", 
prompt=css_request, 
temperature=0.3,
max_tokens=800,
top_p=1,
best_of=1,
frequency_penalty=.9,
presence_penalty=.5,
logprobs=10,
logit_bias={
  "1391": -100, #"space"{
  "27": -100, #<
  "29": -100, #>
  "27" and "7146" and "29": -100, #<div>
  "27" and "71" and "16" and "29": -100, #<h1>
  "3556" and "71" and "16" and "29": -100, #</h1>
  "3556" and "71": -100, #</h
  "27" and "71": -100, #<h
  "3556" and "7635" and "29": -100, #</style>
  "3556" and "7635" and "6927": -100, #</style><
  "27" and "220": -100, #< "space"
  "1279": -100, #"space" <
  "29" and "220": -100, #> "space"
  "3556": -100, #</
  "2618" and "90": -100, #body{
  "2618" and "1391": -100, #body "space" {
  "2618" and "90" and "10331": -100, #body{font
  "2618" and "90" and "10331" and "12" and "7857" and "25": -100, #body{font-size:
  "10331" and "12" and "7857" and "90": -100, #font-size{
  "92" and "1782": -100, #} "space" }
  "10331" and "12" and "7857": -10, #font-size
  #"2" and "20972": -5, ##fff
  #"2" and "830": -5, ##000
  #"2" and "10535": -5, ##000000
  "6": -100, #'
  "90":-90, #{
  "92": -50, #}
  "10331" and "12" and "10394": -100, #font-width
  #"25": -5, #:
  "26": -5, #;
  "12": -5, #-
  "198" and "90": -100, #"enter" {
  "90": -100, #{
  "92": -100, #}
  "13": -50, #.
  #positive
  "8043": 1, #color
  "10331": 5, #font
  "71" and  "16" and "90": 10, #h1{
  "71" and "90": 10, #h{
  "79" and "90": 10, #p{
  "5239" and "12" and "31494" and "25": 5, #text-align:
  "26": 5, #;
  "404" and "4355" and "25" and "220": 5, #opacity: "space"
  "36153" and "12": 5, #margin-
  "9150" and "25" and "9037" and "26": 1, #position: static;
  "9150" and "25" and "3585" and "26": 1, #position: relative;
  "9150" and "25" and "5969" and "26": 1, #position: fixed;
  "9150" and "25" and "4112" and "26": 1, #position: absolute;
  "9150" and "25" and "23408" and "26": 1, #position: sticky;
  "13812" and "25" and "26098" and "26": 5, #display: inline;
  "39231" and "25" and "220": 5, #padding: "space"
  #"25249" and "12" and "8043" and "25" and "220": 5, #background-color: "space"
  "36153" and "25" and "220": 5, #margin: "space"
  "10331" and "12" and "17989" and "25" and "220": 1, #font-family: "space"
  #"25249" and "12" and "8043" and "25": 5, #background-color:
  #"25249": 5, #background
  "220": 1, #"space"
  "198": -10, #"enter"
  "26" and "198": 100, #; "enter"
  "198" and "92": 1, #"enter" }
  
},
)
css_code=css_request+response.choices[0].text
print(css_code) 

"""
#html begins
html_request = "\n<html>" + "\n<head>" + "\n<script src='Script.js'></script>" + "\n<link rel='stylesheet'href='Style.css'>" + "\n<title>" + user_input + " </title>" + "\n</header>" + "\n<body>" + "\n<"

html_response = openai.Completion.create(
engine="curie-instruct-beta", 
prompt=html_request, 
temperature=0.3,
max_tokens=800,
top_p=1,
best_of=1,
frequency_penalty=0.99,
presence_penalty=0.9,
logprobs=10,
logit_bias={
  "27":10, #<
  "29":1, #>
  "3556" and "6494" and "29":-50, #</html>
  "3556" and "2618" and "29": -10, #</
  #"27" and "28112": 50, 
  "31373" and "995":-100,
  "48" and "25":-100, #Q:
  "32" and "25":-100, #A:
  "5450":-100, #
  "48" and "13":-100, #Q.
  "27" and "59" and "6494":-100, #<\html
  "27" and "7635" and "29": -99.99, #<style>
  "27" and "12048" and "29": -99.99, 
  "3556" and "28656" and "29": -100, #</HTML>
  "3556" and "27711" and "1875":-100, #</ html >
  "48" and "220" and "532":-100, #Q  -
  "3556" and "27711":-100, #</ html
  "39" and "20369":-100, #Html
  "28656":-100, #HTML
  "27" and "220":-100, #< "space"
  "27" and "0" and "18227" and "4177" and "56" and "11401" and "11532" and "44731": -100, #<!DOCTYPE HTML PUBLIC
  "27" and "0" and "18227" and "4177" and "56" and "11401" and "27711" and "44731": -100, #<!DOCTYPE html PUBLIC
  "27" and "12048" and "12351" and "2625":-100, #<script src="
  "27" and "8726" and "823" and "28":-100, #<link rel=
  "11037":-100, #"space" />
  "90":-100, #{
  "14" and "17566" and "14":-100, #/images/
  "14" and "17566":-100, #/images
  #"27" and "3955" and "38" and "311" and "7397" and "35922": -100, #<IMG SRC="/
  "48" and "1058":-100, #Q :
  "1875": -100, #"space" >
  "33257" and "2625" and "4023": -100, #href="http
  "2411" and "2625" and "7635": -100, #rel="style
  "27" and "7635" and "29": -100, #<style>
  "27" and "12048" and "29": -100, #<script>
  "27" and "2257" and "56" and "2538" and "29": -100, #<STYLE>
  "27" and "6173" and "46023" and "29": -100, #<SCRIPT>
  "2257" and "56" and "2538" and "2625": -100, #STYLE="
  "46786" and "2625": -100, #COLOR="
  "3556" and "2257" and "56" and "28378" and "13909" and "2767" and "29": -100, #</STYLESHEET>
  "37815" and "3525" and "11639": -100, #CONTENT='
  "35904" and "8043": -100, #bgcolor
  "33" and "15916" and "3535" and "581": -100, #BGCOLOR
  "54" and "2389" and "4221": -100, #WIDTH
  "13909" and "9947": -100, #HEIGHT
  "10394": -100,#width
  "17015": -100,#height
  "31098" and "46025" and "46786": -100, #BACKGROUNDCOLOR
  "4211": -100, #>>
  "16791": -100, #<<
  "15931": -100, #""
  "7635" and "2625": -100, #style="
  "7635" and "33151": -100, #style=""
  "14" and "2618": -100, #/body
  "27" and "8726" and "823": -100, #<link rel
  "25471": -100, #css
  "37495": -100, #javascript
  "6927": -100, #><
  "796" and "220": -100, # = 
  "92": -100, #}
  "90": -100, #{
  "27" and "12048" and "12351" and "796": -100, #<script src =
  "7635" and "28": -100, #style=
  "12": -100,#-
  "25249" and "12" and "8043" and "25": -100, #background-color:
  "25249" and "12" and "8043" and "25" and "1303" and "69" and "17" and "69" and "17" and "69" and "17" and "26": -100, #background-color: #f2f2f2;
  "13" and "8457": -100, #.js
  "2618" and "90": -100, #body{
  "14" and "16159" and "29": -100, #/center>
  "438": -100, #--
  "26": -100, #;
  "3556": -20, #</
  "7785": -50, #var
  #Positive ones
  "27" and "71": 5, #<h
  "27" and "79": 5, #<p
  "27" and "65" and "29": 5, #<b>
  "27" and "1671" and "29": 5, #<br>
  "312" and "2625": 5, #id="
  "27" and "377" and "29": 10, #<ul>
  "27" and "4528" and "29": 5, #<li>
  "27" and "64": 5, #<a
  "27" and "16539": 1, #<button
  "27" and "9600" and "12351" and "796" and "220": 5, #<img src = 
  "27" and "11487" and "3918" and "2625": 5, #<table style="
  "27" and "64" and "13291" and "2625": 5, #<a href="
  "27" and "72" and "29": 5, #<i>
  "312" and "2625": 5, #id="
  "27" and "16539" and "29": 5, #<button>
  "27" and "687" and "29": 5, #<form>
  "27" and "15414" and "2099" and "2625": 5, #<input type="
  "5372" and "13829" and "2625": 5, #placeholder="
},
) 

html_code=html_request+html_response.choices[0].text
print(html_code)

#CSS generation starts here 
print("\nGenerating CSS...\n")


print("\n <!--This is where the css begins--> \n")

css_request = "body{\n" + "\nbackgroundcolor:(" 
css_response = openai.Completion.create(
engine="curie-instruct-beta", 
prompt=css_request, 
temperature=0.3,
max_tokens=800,
top_p=1,
best_of=1,
frequency_penalty=.9,
presence_penalty=.5,
logprobs=10,
logit_bias={
  "1391": -100, #"space"{
  "27": -100, #<
  "29": -100, #>
  "27" and "7146" and "29": -100, #<div>
  "27" and "71" and "16" and "29": -100, #<h1>
  "3556" and "71" and "16" and "29": -100, #</h1>
  "3556" and "71": -100, #</h
  "27" and "71": -100, #<h
  "3556" and "7635" and "29": -100, #</style>
  "3556" and "7635" and "6927": -100, #</style><
  "27" and "220": -100, #< "space"
  "1279": -100, #"space" <
  "29" and "220": -100, #> "space"
  "3556": -100, #</
  #positive
}
),

#python3 codehtml.py
css_code=css_request+css_response.choices[0].text
print(css_code)


""" 