# Json is commonly used with data APIS. Here we show how to parse JSON into a python dictionary.
import json
#from json import loads
# Sample Json
userJson = '{"first_name": "Emmanuel", "last_name": "Brain", "age":12}'

#Parse to dictionary
# loads method take a JSON and parse it to a dictionary
user = json.loads(userJson)

print(user)
print(user['first_name'])

bus = {'make': 'Mercedes','model':'Br', 'year': 2011}
# dumps method take a dictionary and parse it to JSON
busJSON = json.dumps(bus)

print(busJSON)
