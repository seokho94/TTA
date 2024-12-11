import jwt 
import uuid
import time
from dotenv import load_dotenv
import os

class Autorization:
    @staticmethod
    def make_jwt_token(platform):
        access_key = os.getenv(f"{platform}_access")
        secret_key = os.getenv(f"{platform}_secret")
        payload = {
            'access_key': access_key,
            'nonce': str(uuid.uuid4()),
            'timestamp': round(time.time() * 1000)
        }
        jwt_token = jwt.encode(payload, secret_key)

        return 'Bearer {}'.format(jwt_token)

# Example Code
# token  = Autorization.make_jwt_token('bithumb')
# print(token)