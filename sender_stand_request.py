import configuration
import requests


def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,  # подставляем полный url
                         json=body)  # тело запроса


def get_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.TRACK_ORDER + str(track))
