import requests

BASE_URL = "https://financial-tracker-back-pt2-67e49ab4fe24.herokuapp.com"

def login_request(nickname, password):
    payload = {"nickname": nickname, "password":password}
    response = requests.post(BASE_URL + "/auth/login", json = payload)
    response.raise_for_status()
    return response.json()

def register_request(email, nickname, password):
    payload = {"email": email, "nickname": nickname, "password": password}
    response = requests.post(BASE_URL + "/auth/register", json = payload)
    response.raise_for_status()
    return response.json()