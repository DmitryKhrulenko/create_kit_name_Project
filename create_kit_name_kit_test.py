# Чек-лист.
import sender_stand_request
import data
import requests
import configuration

# Запрос на создание нового пользователя
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers= {
    "Content-Type": "application/json"
})

response = post_new_user(data.user_body)
authToken = response.json()["authToken"]



# Эта функция меняет значения в параметре name
def get_kit_body(name):
    # копирование словаря с телом запроса из файла data, чтобы не потерять данные в исходном словаре
    current_body = data.kit_body.copy()
    # изменение значения в поле name
    current_body["name"] = name
    # возвращается новый словарь с нужным значением name
    return current_body

    # Функция для позитивной проверки
def positive_assert(name):

    # В переменную kit_body сохраняется обновлённое тело запроса
    kit_body = get_kit_body(name)
    # В переменную kit_response сохраняется результат запроса на создание пользователя:
    kit_response = sender_stand_request.post_new_client_kit(kit_body, authToken)

    # Проверяется, что код ответа равен 201
    assert kit_response.status_code == 201
    # Проверка, что в ответе поле "name" совпадает с полем "name" в запросе
    assert kit_response.json()["name"] == name


    # Функция для негативной проверки
def negative_assert(name):

    # В переменную kit_body сохраняется обновлённое тело запроса
    kit_body = get_kit_body(name)
    # В переменную kit_response сохраняется результат запроса на создание пользователя:
    kit_response = sender_stand_request.post_new_client_kit(kit_body, authToken)

    # Проверяется, что код ответа равен 400
    assert kit_response.status_code == 400


# Тест 1. Допустимое количество символов (1)
# Параметр name состоит из 1 символa: "a"

def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("а")

# Тест 2. Допустимое количество символов (511)
# Параметр name состоит из 511 символов: "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"

def test_create_kit_511_letter_in_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")


# Тест 3. Количество символов меньше допустимого (0)
# Параметр name состоит из 0 символов: ""

def test_create_kit_0_letter_in_name_get_error_response():
    negative_assert("")


# Тест 4. Количество символов больше допустимого (512)
# Параметр name состоит из 512 символов

def test_create_kit_512_letters_in_name_get_error_response():
    negative_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")


# Тест 5. Разрешены английские буквы
# Параметр name состоит из "QWErty"

def test_create_kit_eng_letters_in_name_get_success_response():
    positive_assert("QWErty")

# Тест 6. Разрешены русские  буквы
# Параметр name состоит из "Мария"

def test_create_kit_rus_letters_in_name_get_success_response():
    positive_assert("Мария")


# Тест 7. Разрешены спецсимволы
# Параметр name состоит из "№%@,"

def test_create_kit_symbols_in_name_get_success_response():
    positive_assert("№%@,")

# Тест 8. Разрешены пробелы
# Параметр name состоит из " Человек и КО "

def test_create_kit_space_in_name_get_success_response():
    positive_assert(" Человек и КО ")


# Тест 9. Разрешены цифры
# Параметр name состоит из "123"

def test_create_kit_numbers_in_name_get_success_response():
    positive_assert("123")


# Тест 10. Параметр не передан в запросе

def test_create_kit_no_name_get_error_response():
    # Копируется словарь с телом запроса из файла data в переменную kit_body
    kit_body = data.kit_body.copy()
    # Удаление параметра name из запроса
    kit_body.pop("name")
    # Проверка полученного ответа
    negative_assert("")


# Тест 11. Передан другой тип параметра (число)

def test_create_kit_number_type_name_get_error_response():
    # В переменную kit_body сохраняется обновлённое тело запроса
    kit_body = get_kit_body(123)
    # В переменную kit_response сохраняется результат запроса на создание набора
    kit_response = sender_stand_request.post_new_client_kit(kit_body, authToken)
    # Проверка полученного ответа
    assert kit_response.status_code == 400

