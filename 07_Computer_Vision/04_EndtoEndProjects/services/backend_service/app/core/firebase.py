# app/core/firebase.py
import firebase_admin
from firebase_admin import credentials, auth
from fastapi import HTTPException, Depends, Request, status

# Initialize Firebase once
cred = credentials.Certificate("app/core/secrets/pizza-store-4fcd5-firebase-adminsdk-fbsvc-270c5921c4.json")
firebase_admin.initialize_app(cred)

def verify_firebase_token(request: Request):
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing Authorization header")

    id_token = auth_header.split(" ").pop()
    try:
        decoded_token = auth.verify_id_token(id_token)
        return decoded_token  # includes uid, email, etc.
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

