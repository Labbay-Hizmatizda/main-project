import requests
BASE_URL = "http://127.0.0.1:8000/api/"
"""
url = 'http://127.0.0.1:8000/api/orders/'

data = {
    'owner_id': 1,
    'category': 1,
    'description': 'Test description',
    'media': 'test.jpg',
    'location': 'Test location',
    'location_link': 'https://example.com',
    'price': 100.00,
    'is_active': True
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())
"""

def get_employers():
    response = requests.get(f'{BASE_URL}employers')
    if response.status_code == 200:
        employers = response.json()  
        return employers
    else:
        print("Error while fetching categories:", response.status_code)
        return []

get_employers()