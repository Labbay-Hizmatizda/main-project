import requests

BASE_URL = "http://127.0.0.1:8000/api/"


def get_employer(user_id):
    response = requests.get(f'{BASE_URL}employers/?user_id={user_id}') 
    if response.status_code == 200:
        if response.json() == []:
            return False
        else:
            return response.json()
    else:
        # return [{'Status_code': response.status_code,
        #                 'Json': response.json()}]
        return None
print(get_employer(1231138963), '\n')                                          # @shahriorovv_a - USER_ID = 1231138963 
    

def get_employer_order(user_id):
    get_id_from = requests.get(f'{BASE_URL}employers/?user_id={user_id}')
    id = get_id_from.json()
    id_value = id[0]['id']
    out_json = requests.get(f'{BASE_URL}orders/?owner_id={id_value}')
    return out_json.json()



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
# print(post_employer())


def patch_employers():
    data = {
        'user_id': 3097,
    }

    response = requests.patch('http://127.0.0.1:8000/api/employers/4/', json=data)
    if response.status_code == 200:
        return response.json()
    else:
        return [{'Status_code': response.status_code,
                        'Json': response.json()}]

# print(patch_employers())


def post_cv(bio, owner_id):
    data = {
        'media': 'media/cv/cv_image.jpg',
        'bio': bio,
        'rating': 0,
        'owner_id': owner_id,
    }
    response = requests.post(f'{BASE_URL}cvs/', json=data)
    if response.status_code == 200:
        return response.json()  
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