from flask import Blueprint
comments_bp = Blueprint('comments', __name__)
from blueprints.comments import routes
