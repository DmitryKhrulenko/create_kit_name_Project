import configuration
import requests
import data

# Запрос на создание нового пользователя
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers= {
    "Content-Type": "application/json"
})

response = post_new_user(data.user_body)
authToken = response.json()["authToken"]


# Функция создания нового набора:
def post_new_client_kit(kit_body, authToken):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KITS_PATH, json=kit_body,
                         headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + authToken
})

response = post_new_client_kit(data.kit_body, authToken)
