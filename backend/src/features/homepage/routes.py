from flask import Blueprint
from src.features.homepage.service import get_homepage_data
from src.core.response import success_response

homepage_bp = Blueprint('homepage', __name__)


@homepage_bp.route('/', methods=['GET'])
def homepage():
    pass
