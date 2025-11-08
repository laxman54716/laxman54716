
from flask import Blueprint, request, jsonify
from app import db
from models import Product
product_bp = Blueprint('product', __name__)

@product_bp.route('/', methods=['GET'])
def list_products():
    prods = Product.query.all()
    data = [{
        'id': p.id, 'name': p.name, 'category': p.category,
        'quantity': p.quantity, 'price': p.price, 'supplier_id': p.supplier_id
    } for p in prods]
    return jsonify(data)

@product_bp.route('/', methods=['POST'])
def add_product():
    d = request.get_json() or {}
    p = Product(name=d.get('name'), category=d.get('category'), quantity=d.get('quantity',0), price=d.get('price',0.0), supplier_id=d.get('supplier_id'))
    db.session.add(p)
    db.session.commit()
    return jsonify({'msg':'created','id':p.id}), 201

@product_bp.route('/<int:pid>', methods=['PUT'])
def edit_product(pid):
    p = Product.query.get_or_404(pid)
    d = request.get_json() or {}
    p.name = d.get('name', p.name)
    p.category = d.get('category', p.category)
    p.quantity = d.get('quantity', p.quantity)
    p.price = d.get('price', p.price)
    db.session.commit()
    return jsonify({'msg':'updated'})

@product_bp.route('/<int:pid>', methods=['DELETE'])
def delete_product(pid):
    p = Product.query.get_or_404(pid)
    db.session.delete(p)
    db.session.commit()
    return jsonify({'msg':'deleted'})
