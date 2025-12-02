import requests

todo_id = input("Enter Todo ID: ")

url = f"https://jsonplaceholder.typicode.com/todos/{todo_id}"

response = requests.get(url)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())
