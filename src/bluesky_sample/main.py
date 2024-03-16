from atproto import Client
from dotenv import load_dotenv
import os

load_dotenv()
email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')

client = Client()
client.login(email, password)
client.send_post(text='From atproto client')