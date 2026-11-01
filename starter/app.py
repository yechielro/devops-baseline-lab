from flask import Flask, jsonify
from pathlib import Path

app = Flask(__name__)


def version():
    return (Path(__file__).parent / 'VERSION').read_text(encoding='utf-8').strip()


@app.get('/')
def home():
    return jsonify(service='devops-course', message='Hello DevOps', version=version())


@app.get('/health')
def health():
    return jsonify(status='ok')


@app.get('/version')
def get_version():
    return jsonify(version=version())


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
