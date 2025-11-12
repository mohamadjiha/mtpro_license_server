from flask import Flask, request, jsonify

app = Flask(__name__)

# قاعدة بيانات مؤقتة للتراخيص (يمكن تعديلها لاحقاً)
valid_keys = ["MTPro_Secret_2025", "MTPro_Test_001"]

@app.route('/')
def home():
    return "MTPro License Server is running ✅"

@app.route('/check', methods=['GET'])
def check_license():
    key = request.args.get('key', '')
    if key in valid_keys:
        return jsonify({"status": "success", "msg": "License is valid ✅"})
    else:
        return jsonify({"status": "error", "msg": "Invalid license ❌"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
