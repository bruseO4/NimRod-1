import json

with open('keys.json') as f:
    keys = json.load(f)
    print(keys['openapi'])