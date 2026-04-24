from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from src.core.response import error_response


def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            verify_jwt_in_request()
            return f(*args, **kwargs)
        except Exception:
            return error_response('Unauthorized', 401)
    return decorated


def get_current_user_id():
    return get_jwt_identity()
