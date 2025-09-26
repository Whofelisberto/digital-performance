from flask import Blueprint, request, jsonify
from models.user_model import authenticate
from models.metric_model import get_metrics

api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")
    user = authenticate(email, password)
    if not user:
        return jsonify({"error": "Credenciais inválidas"}), 401
    return jsonify({
        "email": user["email"],
        "username": user["username"],
        "role": user["role"]
    })

@api_bp.route('/metrics', methods=['GET'])
def metrics():
    role = request.args.get("role", "user")
    date_from = request.args.get("date_from")
    date_to = request.args.get("date_to")
    sort_by = request.args.get("sort_by")
    order = request.args.get("order", "asc")
    df = get_metrics(date_from, date_to, sort_by, order, role)
    records = df.to_dict(orient="records")
    return jsonify({"metrics": records})
