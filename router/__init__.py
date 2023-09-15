# router/__init__.py
from flask import Blueprint

tts_app = Blueprint('tts_api', __name__)


from .tts_api import *

