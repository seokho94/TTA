import jwt 
import uuid
import time
from dotenv import load_dotenv
import os

class Autorization:
    def __init__(self):
        self.set_api_key()

    def set_api_key(self):
        load_dotenv()
        self.access_key = os.getenv('access_key')
        self.secret_key = os.getenv('secret_key')

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
token  = authorization.get_authorization_token()
print(token)