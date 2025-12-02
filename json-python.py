import json

json_str = '{"userId": 1, "id": 1, "title": "Learn API", "completed": false}'

data = json.loads(json_str)

print("Converted Python Dictionary:")
print(data)
