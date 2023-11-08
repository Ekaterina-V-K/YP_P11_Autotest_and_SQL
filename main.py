# Екатерина Кузнецова, 10-я когорта — Финальный проект. Инженер по тестированию плюс
import requests
URL_SERVICE = "https://f318a62c-7420-4c30-82e6-f39c9b1a87b4.serverhub.praktikum-services.ru"
CREATE_ORDER_PATH = "/api/v1/orders"
GET_ORDER_PATH = "/api/v1/orders/track"
TRACK_NUM = "00000"
order_body = {
    "firstName": "Naruto",    "lastName": "Uchiha",    "address": "Konoha, 8888 apt.",    "metroStation": 4,    "phone": "+7 800 355 35 35",
    "rentTime": 5,    "deliveryDate": "2020-11-04",    "comment": "Saske"
}
#Функция создание заказа
def post_create_order(order_body_in_func):
    return requests.post(URL_SERVICE + CREATE_ORDER_PATH, json=order_body_in_func)
#Функция получения заказа по трэку
def get_order(track_in_func):
    return requests.get(URL_SERVICE + GET_ORDER_PATH, params={'t': track_in_func})
#Автотест
def test_create_order():
    # Выполнить запрос на создание заказа.
    response = post_create_order(order_body)
    # Сохранить номер трека заказа.
    TRACK_NUM = response.json()["track"]
    # Выполнить запрос на получения заказа по треку заказа.
    response = get_order(TRACK_NUM)
    # Проверяется, что код ответа равен 200
    assert response.status_code == 200