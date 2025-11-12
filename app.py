from flask import Flask, request, jsonify

app = Flask(__name__)

# 🔑 مفاتيح الترخيص المقبولة
VALID_KEYS = [
    "MTPro_Secret_2025",
    "MTPro_Elite_2025",
    "MTPro_VIP_2026"
]

@app.route('/')
def home():
    return "✅ MTPro License Server Active!"

@app.route('/license/check', methods=['POST'])
def check_license():
    data = request.get_json()
    key = data.get("license_key", "").strip()

    if key in VALID_KEYS:
        return jsonify({"status": "valid"}), 200
    else:
        return jsonify({"status": "invalid"}), 403


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)