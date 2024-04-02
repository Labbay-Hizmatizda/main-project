import requests
BASE_URL = "http://127.0.0.1:8000/api/employers/?user_id=456"

# def get_employers():
#     response = requests.get(f'{BASE_URL}employers')
#     if response.status_code == 200:
#         employers = response.json()  
#         return employers
#     else:
#         print("Error while fetching categories:", response.status_code)
#         return []


# def post_employers():

# data = {
#     'owner_id': f"{owner_id}",
#     'category': 1,
#     'description': 'Test description',
#     'media': 'test.jpg',
#     'location': 'Test location',
#     'location_link': 'https://example.com',
#     'price': 100.00,
#     'is_active': True
# }


# print(get_employers())




data = {
    'surname': 'Updated',  # Здесь можно указать любые поля, которые вы хотите обновить
}
response = requests.patch(BASE_URL, json=data)

print(response.status_code)
print(response.json())





















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