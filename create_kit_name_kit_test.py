# Бугаков Павел, 11-я когорта — Финальный проект. Инженер по тестированию плю
import data
import sender_stand_request


def put_new_order_track():
    # копирование словаря с телом запроса из файла data, чтобы не потерять данные в исходном словаре
    current_body = data.order_body.copy()
    # создаем заказ
    kit_response = sender_stand_request.post_new_order(current_body)
    track = kit_response.json()["track"]
    # возвращается новый словарь с нужным значением track
    return track


def positive_assert(track):
    print(track)
    # В переменную kit_response сохраняется результат запроса на создание набора:
    kit_response = sender_stand_request.get_order(track)
    # Проверяется, что код ответа равен 200
    assert kit_response.status_code == 200


# Тест 1. Успешное получение статуса заказа
def test_get_order_track():
    positive_assert(put_new_order_track())
