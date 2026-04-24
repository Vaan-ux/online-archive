from flask import Blueprint, request, send_file
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.features.research.published.service import (
    get_user_research, delete_research, edit_research
)
from src.features.research.upload.validator import (
    validate_title, validate_authors, validate_year
)
from src.core.response import success_response, error_response
from src.models.research_model import Research

published_bp = Blueprint('published', __name__)


@published_bp.route('/published', methods=['GET'])
@jwt_required()
def get_published():
    pass


@published_bp.route('/published/<int:research_id>/view', methods=['GET'])
@jwt_required()
def view(research_id):
    pass


@published_bp.route('/published/<int:research_id>/download', methods=['GET'])
@jwt_required()
def download(research_id):
    pass


@published_bp.route('/published/<int:research_id>', methods=['PUT'])
@jwt_required()
def edit(research_id):
    pass


@published_bp.route('/published/<int:research_id>', methods=['DELETE'])
@jwt_required()
def delete(research_id):
    pass
