from flask import Blueprint, render_template, request, jsonify, current_app
from app.services.thread_gen import generate_thread

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET'])
def index():
    social_links = {
        'twitter': current_app.config.get('TWITTER_URL'),
        'tiktok': current_app.config.get('TIKTOK_URL'),
        'github': current_app.config.get('GITHUB_URL'),
    }
    return render_template('index.html', social_links=social_links)

@main_bp.route('/generate', methods=['POST'])
def generate():
    content = request.form.get('content')
    if not content:
        return jsonify({'error': 'No content provided'}), 400
    
    try:
        thread = generate_thread(content)
        return jsonify({'thread': thread})
    except Exception as e:
        return jsonify({'error': str(e)}), 500 