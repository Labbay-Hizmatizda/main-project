import requests

BASE_URL = "http://127.0.0.1:8000/api/"


def get_employers():
    response = requests.get(f'{BASE_URL}employers/')
    if response.status_code == 200:
        return [{'Status_code': response.status_code,
                        'Json': response.json()}]
    else:
        return [{'Status_code': response.status_code,
                        'Json': response.json()}]
# print(get_employers())
    

def post_employers():
    data = {
        'user_id': 698569,
        'name': 'Test1',
        'surname': 'TEST1',
        'phone_number': '+987675956',
    }
    response = requests.post(f'{BASE_URL}employers/', json=data)
    if response.status_code == 200:
        return [{'Status_code': response.status_code,
                        'Json': response.json()}]   
    else:
        return [{'Status_code': response.status_code,
                        'Json': response.json()}]
# print(post_employers())


def patch_employers():
    data = {
        'user_id': 3097,
    }

    response = requests.patch('http://127.0.0.1:8000/api/employers/4/', json=data)
    if response.status_code == 200:
        return [{'Status_code': response.status_code,
                        'Json': response.json()}]
    else:
        return [{'Status_code': response.status_code,
                        'Json': response.json()}]

# print(patch_employers())








''' Template for outputing any information

if response.status_code == 200:
        return [{'Status_code': response.status_code,
                        'Json': response.json()}]
    else:
        return [{'Status_code': response.status_code,
                        'Json': response.json()}]

'''