from flask import Blueprint, send_from_directory
from flask import current_app as app

bootstrap_bp = Blueprint('bootstrap_bp', __name__)

@bootstrap_bp.route('/css/<name>', methods=['GET'])
def css(name):
    return send_from_directory('/app/css/', name)