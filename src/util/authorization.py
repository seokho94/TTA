import jwt 
import uuid
import time
import tkinter as tk
from tkinter import simpledialog
import pyautogui

class Autorization:
    def __init__(self):
        self.set_api_key()

    def set_api_key(self):
        self.access_key = self.set_access_key()
        self.secret_key = self.set_secret_key()

    def set_access_key(self):
        access_key = pyautogui.prompt(title="입력", text="Access Key를 입력해주세요.")
        return access_key

    def set_secret_key(self):
        secret_key = pyautogui.prompt(title="입력", text="Secret Key를 입력해주세요.")
        return secret_key

    def make_jwt_token(self):
        payload = {
            'access_key': self.access_key,
            'nonce': str(uuid.uuid4()),
            'timestamp': round(time.time() * 1000)
        }
        jwt_token = jwt.encode(payload, self.secret_key)
        return jwt_token

    def get_authorization_token(self):
        return 'Bearer {}'.format(self.make_jwt_token())
    


authorization = Autorization()
token = authorization.get_authorization_token()
print(token)