import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "raulillo82"
TOKEN = "mykeyforpixela_123456"
#Not such an important key, generated upon creation of a new graph
#Kind of useless if graph is deleted, like in this program
GRAPH = "graph1"

#CREATE ACCOUNT

user_params = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
        }

response = requests.post(url=pixela_endpoint, json=user_params) 
print(response.text)

#CREATE A GRAPH INTO THE ACCOUNT

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
        "id": "graph1",
        "name": "Cycling Graph",
        "unit": "km",
        "type": "float",
        "color": "ajisai",
        }

headers = {
        "X-USER-TOKEN": TOKEN
        }

#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)

#CREATE A PIXEL INTO THE PREVIOUS GRAPAH

pixel_endpoint = f"{graph_endpoint}/{GRAPH}"
pixel_params = {
        "date": datetime.today().strftime("%Y%m%d"),
        "quantity": "5.1",
        }
#response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
#print(response.text)

#CREATE YET ANOTHER PIXEL INTO THE PREVIOUS GRAPAH

pixel_endpoint = f"{graph_endpoint}/{GRAPH}"
pixel_params = {
        "date": datetime(year=2023, month=11, day=3).strftime("%Y%m%d"),
        "quantity": "5.1",
        }
#response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
#print(response.text)

#UPDATE AN EXISTING PIXEL FROM THE GRAPH

ammend_endpoint = f"{graph_endpoint}/{GRAPH}/{datetime(year=2023, month=11, day=3).strftime('%Y%m%d')}"
pixel_params = {
        "quantity": "18.1",
        }
#response = requests.put(url=ammend_endpoint, json=pixel_params, headers=headers)
#print(response.text)

delete_endpoint = ammend_endpoint

#DELETE THE VERY SAME PREVIOUS PIXEL FROM THE GRAPH

#response = requests.delete(url=delete_endpoint, json=pixel_params, headers=headers)
#print(response.text)

#DELETE THE FULL GRAPH

#response = requests.delete(url=pixel_endpoint, headers=headers)
#print(response.text)

#DELETE THE FULL ACCOUNT
user_endpoint = "https://pixe.la/v1/users/raulillo82"
#response = requests.delete(url=user_endpoint, headers=headers)
#print(response.text)

