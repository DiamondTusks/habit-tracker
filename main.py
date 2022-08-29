import requests
from datetime import datetime

TOKEN = "fhsi4dwi9jw2wd9"
USERNAME = "holytusks"
GRAPH_ID = "graph3"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Meditation Graph",
    "unit": "mins",
    "type": "int",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
formatted_date = today.strftime("%Y%m%d")

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many minutes did you meditate today? ")
}
#
response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{formatted_date}"

pixel_update = {
    "quantity": "12"
}

# response = requests.put(url=pixel_update_endpoint, json=pixel_update, headers=headers)
# print(response.text)

pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# requests.delete(url=pixel_delete_endpoint, headers=headers)