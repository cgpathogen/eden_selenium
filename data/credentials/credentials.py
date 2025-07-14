import os
from dotenv import load_dotenv

load_dotenv()

class Credentials:

    login = os.getenv("qa_login")
    password = os.getenv("qa_password")
