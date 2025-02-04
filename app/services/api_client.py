import requests
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
print(BASE_URL)

# USER ACTIONS
def login_request(user_name, password):
    payload = {"user_name": user_name, "password":password}
    response = requests.post(BASE_URL + "/auth/login", json = payload)
    response.raise_for_status()
    return response.json()

def register_request(email, user_name, password):
    payload = {"email": email, "user_name": user_name, "password": password}
    response = requests.post(BASE_URL + "/auth/register", json = payload)
    response.raise_for_status()
    return response.json()

def get_user(user_id):
    payload = {"user_id": user_id}
    response = requests.get(BASE_URL + f"/auth/user/{user_id}", json = payload)
    response.raise_for_status()
    return response.json()

def update_account(user_name, email, password, currency):
    payload = {"user_name": user_name, "email": email, "password": password, "currency": currency}
    response = requests.patch(BASE_URL + "/auth/update", json = payload)
    response.raise_for_status()
    return response.json()

def delete_account(user_name):
    payload = {"user_name": user_name}
    response = requests.delete(BASE_URL + "/auth/delete", json = payload)
    response.raise_for_status()
    return response.json()

# TRANSACTION ACTIONS
def create_transaction(user_name, description, category, type, amount, payment_method):
    payload = {"user_name": user_name, "description": description, "category": category, "type": type, "amount": amount, "payment_method": payment_method}
    response = requests.post(BASE_URL + "/transactions/", json = payload)
    response.raise_for_status()
    return response.json()

def get_transactions(user_id):
    payload = {"user_id": user_id}
    response = requests.get(BASE_URL + f"/transactions/?user_id={user_id}", json = payload)
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