import requests

BASE_URL = "http://127.0.0.1:8000/api/"

# 1231138963

def get_employee(user_id):
    response = requests.get(f'{BASE_URL}employees/?user_id={user_id}') 
    if response.status_code == 200:
        if response.json() == []:
            return None
        else:
            return response.json()
    else:
        return None    


def get_cv(user_id):
    response = requests.get(f'{BASE_URL}cvs/?user_id={user_id}')
    response.json()
    if response.status_code == 200:
        if response.json() == []:
            return None
        else:
            return response[0]['media']
    else:
        return response.json() 
        

def get_categories():
    response = requests.get(f'{BASE_URL}category')
    if response.status_code == 200:
        if response.json() == []:
            return None
        else:
            return response.json()


def get_proposals(user_id, which):
    get_id_from = requests.get(f'{BASE_URL}employees/?user_id={user_id}')
    id = get_id_from.json()
    id_value = id[0]['id']
    if which == 'true':
        response = requests.get(f'{BASE_URL}proposals/?owner_id={id_value}&is_active=True')
    elif which == 'false':
        response = requests.get(f'{BASE_URL}proposals/?owner_id={id_value}&is_active=False')

    if response.status_code == 200:
        if response.json() == []:
            return None
        else:
            return response.json()

 
def get_lang(user_id):
    response = requests.get(f'{BASE_URL}employees/?user_id={user_id}')
    id = response.json()
    try:
        id_value = id[0]['language']
    except:
        ...
    
    if response.status_code == 200:
        
        if response.json() == []:
            return []
        elif id_value == []:
            return None
        elif id_value == 7 or id_value == 8:
            if id_value == 7:
                return 'ru' 
            return 'uz'

print(get_lang(1231138963))














def post_employer(user_id, name, surname, phone_number):

    data = {
        'user_id': user_id,
        'name': name,
        'surname': surname,
        'phone_number': phone_number,
    }

    response = requests.post(f'{BASE_URL}employers/', json=data)
    if response.status_code == 200:
        return response.json()  
    else:
        return [{'Status_code': response.status_code,
                        'Json': response.json()}]
    

def post_proposal(order_id, price, user_id):
    get_id_from = requests.get(f'{BASE_URL}employees/?user_id={user_id}')
    id = get_id_from.json()
    print(id)
    if not id:  # Check if the list is empty
        return [{'Error': 'No data found for the given user_id'}]
    
    owner_id = id[0]['id']
    print(owner_id)
    data = {
        'owner_id': owner_id,
        'order_id': order_id,
        'price': price
    }
    response = requests.post(f'{BASE_URL}proposals/', json=data)
    if response.status_code == 200:
        return response.json()
    else:
        return [{'Status_code': response.status_code, 'Json': response.json()}]

def post_passport(user_id, url):
    get_id_from = requests.get(f'{BASE_URL}employees/?user_id={user_id}')
    id = get_id_from.json()
    owner_id = id[0]['id']

    data = {
        'images_dir' : url,
        'owner_id' : owner_id,
    }
    response = requests.post(f'{BASE_URL}employee_passports/', json=data)
    if response.status_code == 200:
        return response.json()   
    else:
        return [{'Status_code': response.status_code,
                        'Json': response.json()}]   


def post_cv(image, bio, owner_id):
    data = {
        'media': image,
        'bio': bio,
        'owner_id': owner_id,
    }
    response = requests.post(f'{BASE_URL}cvs/', json=data)
    if response.status_code == 200:
        return response.json()   
    else:
        return [{'Status_code': response.status_code,
                        'Json': response.json()}]
    








def patch_employees(user_id, value, which):
    get_id_from = requests.get(f'{BASE_URL}employees/?user_id={user_id}')
    id = get_id_from.json()
    id_value = id[0]['id']
    print(id_value)
    if which == 'name':
        data = {
            'name': value,
        }
    elif which == 'surname':
        data = {
            'surname': value,
        }
    elif which == 'phone':
        data = {
            'phone_number': value,
        }

    response = requests.patch(f'http://127.0.0.1:8000/api/employees/{id_value}/', json=data)
    if response.status_code == 200:
        try:
            return response.json()
        except ValueError:
            return [{'Status_code': response.status_code,
                     'Message': 'Response is not in JSON format.'}]
    else:
        return [{'Status_code': response.status_code,
                 'Json': response.json()}]
    

def patch_cv(user_id, value, which):
    get_id_from = requests.get(f'{BASE_URL}employees/?user_id={user_id}')
    id = get_id_from.json()
    id_value = id[0]['id']
    if which == ' media':
        data = {
            'media': value,
        }
    elif which == 'bio':
        data = {
            'bio': value,
        }

    response = requests.patch(f'http://127.0.0.1:8000/api/cvs/{id_value}/', json=data)
    if response.status_code == 200:
        try:
            return response.json()
        except ValueError:
            return [{'Status_code': response.status_code,
                     'Message': 'Response is not in JSON format.'}]
    else:
        return [{'Status_code': response.status_code,
                 'Json': response.json()}]


def patch_lang(user_id, which):
    
    if which == 'ru':
        data = {
            'language' : 7
        }
    elif which == 'uz':
        data = {
            'language' : 8
        }

    response = requests.get(f'{BASE_URL}employees/?user_id={user_id}')
    id = response.json()
    owner_id = id[0]['id']
        
    response = requests.patch(f'{BASE_URL}employees/{owner_id}/', json=data)
    if response.status_code == 200:
        return response.json()
    else:
        print(1)
        return [{'Status_code': response.status_code,
                'Json': response.json()}]    


# 1231138963



# СЕКУНДОМЕР
import time

def stopwatch():
    start_time = time.time()
    # print(get_proposals(1231138963, 'true'))
    # print(get_proposals(1231138963, 'false'))
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"\n\nПрошло времени: {elapsed_time:.3f} секунд")

stopwatch()
