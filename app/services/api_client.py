import requests

BASE_URL = "https://financial-tracker-back-pt2-67e49ab4fe24.herokuapp.com"

# USER ACTIONS
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

def get_user(nickname):
    payload = {"nickname": nickname}
    response = requests.get(BASE_URL + f"/auth/user/{nickname}", json = payload)
    response.raise_for_status()
    return response.json()

def update_account(nickname, email, password, currency):
    payload = {"nickname": nickname, "email": email, "password": password, "currency": currency}
    response = requests.patch(BASE_URL + "/auth/update", json = payload)
    response.raise_for_status()
    return response.json()

def delete_account(nickname):
    payload = {"nickname": nickname}
    response = requests.delete(BASE_URL + "/auth/delete", json = payload)
    response.raise_for_status()
    return response.json()

# TRANSACTION ACTIONS
def create_transaction(nickname, description, category, type, amount, payment_method):
    payload = {"nickname": nickname, "description": description, "category": category, "type": type, "amount": amount, "payment_method": payment_method}
    response = requests.post(BASE_URL + "/transactions/", json = payload)
    response.raise_for_status()
    return response.json()

def get_transactions(nickname):
    payload = {"nickname": nickname}
    response = requests.get(BASE_URL + "/transactions/", json = payload)
    response.raise_for_status()
    return response.json()

def update_transaction(transaction_id):
    payload = {"transaction_id": transaction_id}
    response = requests.patch(BASE_URL + f"/transactions/{transaction_id}", json = payload)
    response.raise_for_status()
    return response.json()

def delete_transaction(transaction_id):
    payload = {"transaction_id": transaction_id}
    response = requests.delete(BASE_URL + f"/transactions/{transaction_id}", json = payload)
    response.raise_for_status()
    return response.json()