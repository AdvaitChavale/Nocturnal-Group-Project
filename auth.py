import firebase_admin
from firebase_admin import auth
from firebase_admin import credentials


cred = credentials.Certificate("./credentials.json")

firebase_admin.initialize_app(cred)

def register_user(email, password):
    try:
        user = auth.create_user_with_email_and_password(email=email, password=password)
        return "succesfull"
    except:
        print("registration fail")
        return "unseccfull"

def login(email,password):
    try:
        user = auth.sign_in_with_email_and_password(email=email, password=password)
        return "succesfull"
    except:
        print("Error")
        return "unsucessfull"