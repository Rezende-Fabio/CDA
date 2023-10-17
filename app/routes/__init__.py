from flask import Blueprint
from flask_apscheduler import APScheduler

tasks_bp = Blueprint('tasks', __name__)
