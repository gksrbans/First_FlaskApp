from dataclasses import dataclass
from flask import Blueprint, render_template, url_for, jsonify

from werkzeug.utils import redirect
from pybo.models import Question
from ..models import Question
import json

bp = Blueprint('main', __name__, url_prefix='/')





@bp.route('/hello')
def hello_pybo():
    return 'Hello, Kyumoon!'


@bp.route('/')
def index():
    return redirect(url_for('question._list'))



