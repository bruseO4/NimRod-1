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