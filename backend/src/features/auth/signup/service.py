from werkzeug.security import generate_password_hash
from src.extensions import db
from src.models.user_model import User


def signup_user(data: dict) -> dict:
    user = User(
        username=data['username'],
        email=data['email'],
        phone=data['phone'],
        password=generate_password_hash(data['password'])
    )
    db.session.add(user)
    db.session.commit()
    return user.to_dict()
