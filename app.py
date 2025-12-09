from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-blog', methods=['POST'])
def generate_blog():
    data = request.json
    prompt = data['prompt']
    # Call Ollama API
    response = requests.post(
        'http://localhost:11434/api/generate',
        json={
            'model': 'gemma2:2b',
            'prompt': f"Write a 1000-word blog about: {prompt}",
            'stream': False
        }
    )
    result = response.json()
    return jsonify({'blog': result['response']})

if __name__ == '__main__':
    app.run(debug=True, port=5500)
