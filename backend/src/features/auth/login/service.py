from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token
from src.models.user_model import User


def login_user(username: str, password: str):
    user = User.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password, password):
        return None, 'login failed: incorrect username and password'

    token = create_access_token(identity=user.id)
    return {'token': token, 'user': user.to_dict()}, None
