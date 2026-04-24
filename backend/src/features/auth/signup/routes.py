from flask import Blueprint, request
from src.features.auth.signup.service import signup_user
from src.features.auth.signup.username.validator import validate_username
from src.features.auth.signup.password.validator import validate_password
from src.features.auth.signup.phone.validator import validate_phone
from src.features.auth.signup.email.validator import validate_email
from src.core.response import success_response, error_response

signup_bp = Blueprint('signup', __name__)


@signup_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json() or {}

    errors = []
    errors += validate_username(data.get('username', '').strip())
    errors += validate_password(data.get('password', ''), data.get('confirm_password', ''))
    errors += validate_phone(data.get('phone', '').strip())
    errors += validate_email(data.get('email', '').strip())

    if errors:
        return error_response('Validation failed', 400, errors)

    user = signup_user(data)
    return success_response(user, 'Signup successful', 201)
