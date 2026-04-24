from flask import Blueprint, request, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.features.research.upload.service import upload_research
from src.features.research.upload.validator import (
    validate_title, validate_authors, validate_year, validate_pdf
)
from src.core.response import success_response, error_response

upload_bp = Blueprint('upload', __name__)


@upload_bp.route('/upload', methods=['POST'])
@jwt_required()
def upload():
    pass
