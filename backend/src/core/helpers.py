import os
from werkzeug.utils import secure_filename


def save_file(file, upload_folder: str) -> str:
    filename = secure_filename(file.filename)
    os.makedirs(upload_folder, exist_ok=True)
    filepath = os.path.join(os.path.abspath(upload_folder), filename)
    file.save(filepath)
    return filepath


def get_file_size(file) -> int:
    file.seek(0, 2)
    size = file.tell()
    file.seek(0)
    return size
