import json
import settings.json


# Parse the JSON data
data = json.loads(json_data)

print(json_data)
while input == "name" or "age" or "city":
    edit = input("What field would you like to update?: ")
    if edit == "name":
        field_key = 'name'
        data[field_key] = input("Please write your name: ")
    elif edit == "age":
        field_key = 'age'
        data[field_key] = input("Please write your age: ")
    elif edit == "city":
        field_key = 'city'
        data[field_key] = input("What city are you in?: ")
    else:
        break
# Convert the modified data back to JSON
modified_json = json.dumps(data)

print('Before Modifying:', json_data)
print('After Modifying:', modified_json)
