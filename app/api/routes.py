from flask import Blueprint, render_template, request, redirect, jsonify
from app.api.service import shorten_url, get_original_url

url_shortener_bp = Blueprint('url_shortener', __name__)

# Home page with form
@url_shortener_bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.get_json()
        long_url = data.get('long_url')
        short_url = shorten_url(long_url)
        return jsonify({"short_url": short_url})
    return render_template('index.html')

# Redirect short URL
@url_shortener_bp.route('/<short_code>')
def redirect_short_url(short_code):
    original_url = get_original_url(short_code)
    if original_url:
        return redirect(original_url)
    return "URL not found", 404
