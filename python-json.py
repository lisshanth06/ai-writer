import json

data = {
    "userId": 1,
    "id": 1,
    "title": "Learn API",
    "completed": False
}

with open("output.json", "w") as f:
    json.dump(data, f, indent=4)

print("Dictionary written to output.json")
