import requests
import json 

url = 'https://randomuser.me/api'
n = 30
users = []
while len(users) != n:
    r = requests.get(url=url)

    if r.status_code == 200:
        user = r.json()['results'][0]

        if user['gender'] == 'male':
            users.append(
    {
         "full_name" : f"{user['name']['first']}{user['name']['last']}",
         "age": user['dob']['age'],
         "email": user['email'],
         "city": user['location']['city']

    }
)
with open('users.json', mode='w') as file:
    json_data = json.dumps(users, indent=4)
    file.write(json_data)
            

