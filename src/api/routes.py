from flask import Blueprint
from werkzeug.exceptions import HTTPException

api = Blueprint('api', __name__)

class APIException(HTTPException):
    code = 400

    def __init__(self, message, status_code=None, payload=None):
        super().__init__(message, payload)
        if status_code is not None:
            self.code = status_code