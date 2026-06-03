import requests # Requests is a Python library used to send and receive data from websites.
import json
response = requests.get(
    "https://catfact.ninja/fact"
)

print(response.status_code) # used to find the status code of the website 
print(response.text)# used to generate a plain text like str..
data = response.json()#used to convert the respones into json
print(data["fact"])# it is used to get the value from the specific datas from json


#json 
stud_id = {
    'name' : 'Gowshik',
     'age' : 18
}
json_format = json.dumps(stud_id)#convert normal dict into json
print(json_format)
