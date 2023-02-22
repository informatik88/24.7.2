from api import PetFriends
from settings import valid_email, valid_password
import os

pf = PetFriends()

def test_get_api_key_for_invalid_user_email(email= "informatik888@mail.ru", password= "4616353s"):
    """ Проверяем что запрос api ключа не возвращает статус 200 с некорректным логином, для этого в значении параметра email добавляем либо меняем любой символ"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'key' in result

def test_get_api_key_for_invalid_user_password(email= "informatik88@mail.ru", password= "4616353ss"):
    """ Проверяем что запрос api ключа не возвращает статус 200 с некорректным паролем, для этого в значении параметра password добавляем либо меняем любой символ"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'key' in result


def test_add_new_pet_with_invalid_name(name='', animal_type='двортерьер',
                                     age='4', pet_photo='images/dikobraz.jpg'):
    """Проверяем что можно добавить питомца с пустым значением поля параметра name"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name

def test_add_new_pet_with_invalid_animal_type(name='Кеша', animal_type='',
                                     age='4', pet_photo='images/dikobraz.jpg'):
    """Проверяем что можно добавить питомца с пустым значением параметра animal_type"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name

def test_add_new_pet_with_invalid_age(name='Кеша', animal_type='собака',
                                     age='', pet_photo='images/dikobraz.jpg'):
    """Проверяем что можно добавить питомца с пустым значением параметра age"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name

def test_add_new_pet_without_photo(name='Кеша', animal_type='двортерьер', age='4'):
    """Проверяем что можно добавить питомца  без фото"""

        # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name

def test_add_photo_pet(pet_photo='images/kane-korso.jpg'):
    """Проверяем что можно добавить фото питомца"""

            # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

        # Получаем  список своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

   # Добавляем фото питомца
    status, result = pf.add_photo_pet(auth_key, my_pets['pets'][0]['id'], pet_photo)

      # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200


def test_get_my_pets_with_valid_key(filter='my_pets'):
    """ Проверяем что запрос моих питомцев возвращает не пустой список.
    Для этого сначала получаем api ключ и сохраняем в переменную auth_key. Далее используя этого ключ
    запрашиваем список моих питомцев и проверяем что список не пустой, значение параметра filter='my_pets'"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_my_pets(auth_key, filter)

    assert status == 200
    assert (result)



def test_update_pet_info(name='Жан', animal_type='158', age=5):
    """Проверяем возможность обновления информации о питомце не верным значением параметра animal_type"""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
    assert status == 200
    assert result['name'] == name


def test_update_pet_info_2(name='Жан', animal_type='Кролик', age='игуана'):
    """Проверяем возможность обновления информации о питомце не верным значением параметра age"""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
    assert status == 200
    assert result['name'] == name
