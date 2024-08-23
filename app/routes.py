from flask import jsonify

@app.route('/api/status', methods=['GET'])
def status():
    return jsonify({"status": "MT4-AI API is running"})
