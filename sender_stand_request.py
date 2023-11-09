import requests
import configuration
#Функция создание заказа
def post_create_order(order_body_in_func):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH, json=order_body_in_func)
#Функция получения заказа по трэку
def get_order(track_in_func):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH, params={'t': track_in_func})