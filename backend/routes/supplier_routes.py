
from flask import Blueprint, request, jsonify
from app import db
from models import Supplier
supplier_bp = Blueprint('supplier', __name__)

@supplier_bp.route('/', methods=['GET'])
def list_suppliers():
    s = Supplier.query.all()
    data = [{'id':x.id,'name':x.name,'contact':x.contact} for x in s]
    return jsonify(data)

@supplier_bp.route('/', methods=['POST'])
def add_supplier():
    d = request.get_json() or {}
    s = Supplier(name=d.get('name'), contact=d.get('contact'))
    db.session.add(s)
    db.session.commit()
    return jsonify({'msg':'created','id':s.id}), 201
