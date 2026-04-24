from flask import Blueprint, request
from src.features.auth.login.service import login_user
from src.features.auth.login.validator import validate_login
from src.core.response import success_response, error_response

login_bp = Blueprint('login', __name__)


@login_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json() or {}

    errors = validate_login(data)
    if errors:
        return error_response('Validation failed', 400, errors)

    result, err = login_user(data['username'], data['password'])
    if err:
        return error_response(err, 401)

    return success_response(result, 'Login successful')
