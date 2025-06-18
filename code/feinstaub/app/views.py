from flask import Blueprint, render_template
from datetime import datetime

views = Blueprint('views', __name__)

@views.route('/')
def index():
    start = datetime(2022, 1, 1).strftime("%Y-%m-%d")
    end = datetime(2022, 1, 10).strftime("%Y-%m-%d")
    return render_template(
        'index.html',
        startDate=start,
        endDate=end
                           )  # Lädt index.html aus dem templates-Ordner