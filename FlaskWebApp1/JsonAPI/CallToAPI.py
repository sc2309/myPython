import requests

headers = {'Accept': 'application/json'}
user_data = input("Enter Data Number - ")
api_url = 'https://jsonplaceholder.typicode.com/todos/'+user_data
r = requests.get(api_url, headers=headers)
getData = r.json()
2
print(f"Json Response is -  {getData}")