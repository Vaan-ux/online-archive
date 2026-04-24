from flask import Blueprint, request, send_file
from src.features.library.service import get_all_research, search_research
from src.core.response import success_response, error_response
from src.models.research_model import Research

library_bp = Blueprint('library', __name__)


@library_bp.route('/', methods=['GET'])
def library():
    pass


@library_bp.route('/search', methods=['GET'])
def search():
    pass


@library_bp.route('/<int:research_id>/view', methods=['GET'])
def view(research_id):
    pass


@library_bp.route('/<int:research_id>/download', methods=['GET'])
def download(research_id):
    pass
