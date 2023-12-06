from flask import render_template
from app import app

@app.route('/')
def index():
    return render_template('index.html')

# Add more routes for other non-API views if needed
