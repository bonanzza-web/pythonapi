from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/api/service_a', methods=['GET'])
def service_a():
    # Обращаемся к Service B
    response = requests.get('http://service_b:5001/api/service_b')
    return jsonify({
        "message": "Hello from Service A",
        "service_b_response": response.json()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
