# Creating Python object from JSON

import json

input_json_string = '{ "name" : "John", "age" : "31", "city" : "New York"}'
result = json.loads(input_json_string)

print(result)
print(type(result))

print(f'{result["name"]} lives in {result["city"]}')

