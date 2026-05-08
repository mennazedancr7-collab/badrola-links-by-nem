from flask import Flask, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)

@app.route('/api/data')
def get_data():
    try:
        # استدعاء ملف الجافا
        result = subprocess.check_output(['java', 'linkhelper'], encoding='utf-8')
    except Exception as e:
        result = "Java Error"

    # بيانات الروابط الخاصة
    data = {
        "message": result,
        "links": [
            {"name": "Instagram", "url": "https://instagram.com"},
            {"name": "YouTube", "url": "https://youtube.com"},
            {"name": "Discord", "url": "https://discord.com"}
        ]
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(port=5000, debug=True)