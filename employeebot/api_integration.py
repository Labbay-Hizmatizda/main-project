import requests

BASE_URL = "http://127.0.0.1:8000/api/"


def get_employee(user_id):
    response = requests.get(f'{BASE_URL}employees/?user_id={user_id}')
    if response.status_code == 200:
        if response.json() == []:
            return False
        else:
            return response.json()
    else:
        # return [{'Status_code': response.status_code,
        #                 'Json': response.json()}]
        return None


def get_employee_proposal(user_id):
    get_id_from = requests.get(f'{BASE_URL}employees/?user_id={user_id}')
    id = get_id_from.json()
    id_value = id[0]['id']
    out_json = requests.get(f'{BASE_URL}proposals/?id={id_value}')
    return out_json.json()




def post_employee(user_id, name, surname, phone_number):
    data = {
        'user_id': user_id,
        'name': name,
        'surname': surname,
        'phone_number': phone_number,
    }
    response = requests.post(f'{BASE_URL}employees/', json=data)
    if response.status_code == 200:
        return [{'Status_code': response.status_code,
                        'Json': response.json()}]   
    else:
        return [{'Status_code': response.status_code,
                        'Json': response.json()}]


def patch_employees():
    data = {
        'user_id': 3097,
    }

    response = requests.patch('http://127.0.0.1:8000/api/employees/4/', json=data)
    if response.status_code == 200:
        return [{'Status_code': response.status_code,
                        'Json': response.json()}]
    else:
        return [{'Status_code': response.status_code,
                        'Json': response.json()}]

# print(patch_employers())








# СЕКУНДОМЕР
import time

def stopwatch():
    start_time = time.time()
    print(get_employee_proposal(1))  
    print(get_employee(1))
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Прошло времени: {elapsed_time:.3f} секунд")

stopwatch()









def post_cv(bio, owner_id):
    data = {
        'media': 'media/cv/cv_image.jpg',
        'bio': bio,
        'rating': 0,
        'owner_id': owner_id,
    }
    response = requests.post(f'{BASE_URL}cvs/', json=data)
    if response.status_code == 200:
        return [{'Status_code': response.status_code,
                        'Json': response.json()}]   
    else:
        print('sv')
        return [{'Status_code': response.status_code,
                        'Json': response.json()}]
    





''' Template for outputing any information

if response.status_code == 200:
        return [{'Status_code': response.status_code,
                        'Json': response.json()}]
    else:
        return [{'Status_code': response.status_code,
                        'Json': response.json()}]

'''