import requests

url = 'https://bayut.onrender.com/predict/riyadh'

data = {

    "Type_encoding": 0,
    "Price": 795000.0,
    "Area_m2": 158,
}

response = requests.post(url, json=data)

print(response.json())