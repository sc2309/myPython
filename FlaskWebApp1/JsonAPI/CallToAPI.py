import requests
from MapData.MapData import User 

headers = {'Accept': 'application/json'}
user_data = input("Enter Data Number - ")
api_url = 'https://jsonplaceholder.typicode.com/todos/'+user_data
r = requests.get(api_url, headers=headers)
getData = r.json()
User.id = getData["title"]
print(User.id)