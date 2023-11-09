# Екатерина Кузнецова, 10-я когорта — Финальный проект. Инженер по тестированию плюс
import data
import sender_stand_request

#Автотест
def test_create_order():
    # Выполнить запрос на создание заказа.
    response = sender_stand_request.post_create_order(data.order_body)
    # Сохранить номер трека заказа.
    data.TRACK_NUM = response.json()["track"]
    # Выполнить запрос на получения заказа по треку заказа.
    response = sender_stand_request.get_order(data.TRACK_NUM)
    # Проверяется, что код ответа равен 200
    assert response.status_code == 200