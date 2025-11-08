
from flask import Blueprint, request, jsonify
from app import db
from models import User
from flask_jwt_extended import create_access_token
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json() or {}
    if not data.get('username') or not data.get('password'):
        return jsonify({'msg':'username and password required'}), 400
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'msg':'user exists'}), 400
    user = User(username=data['username'], role=data.get('role','staff'))
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'msg':'user created'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json() or {}
    user = User.query.filter_by(username=data.get('username')).first()
    if not user or not user.check_password(data.get('password','')):
        return jsonify({'msg':'bad credentials'}), 401
    token = create_access_token(identity={'username':user.username,'role':user.role})
    return jsonify({'access_token': token})
