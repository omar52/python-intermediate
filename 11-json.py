# Encoding or serialization: converting python objects to json format 
import json
data = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "is_student": False,
    "courses": ["Math", "Science"],
    "address": {
        "street": "123 Main St",
        "zipcode": "10001"
    }
}

# Convert Python object to JSON string
json_string = json.dumps(data, indent=4)
# print("JSON String:")
# print(json_string)

# convert python data to json file
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)
    
    
# cnvert json to python:
jason_file = json.loads(json_string)
print(jason_file) 