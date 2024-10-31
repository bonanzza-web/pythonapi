from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/service_b', methods=['GET'])
def service_b():
    return jsonify({
        "message": "Hello from Service B"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)