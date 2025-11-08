
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Basic config - use SQLite for easy local demo (change to MySQL in production)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'super-secret-key')

db = SQLAlchemy(app)
jwt = JWTManager(app)

from models import User, Product, Supplier
from routes.auth_routes import auth_bp
from routes.product_routes import product_bp
from routes.supplier_routes import supplier_bp

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(product_bp, url_prefix='/products')
app.register_blueprint(supplier_bp, url_prefix='/suppliers')

@app.route('/dashboard/summary')
def dashboard_summary():
    total_products = Product.query.count()
    total_suppliers = Supplier.query.count()
    low_stock = Product.query.filter(Product.quantity < 5).count()
    return jsonify({
        'total_products': total_products,
        'total_suppliers': total_suppliers,
        'low_stock_count': low_stock
    })

if __name__ == '__main__':
    # create tables and add sample data if empty
    db.create_all()
    if User.query.count() == 0:
        # add admin user
        admin = User(username='admin', role='admin')
        admin.set_password('admin123')
        db.session.add(admin)
        # sample suppliers
        s1 = Supplier(name='Fresh Farms', contact='9876543210')
        s2 = Supplier(name='Daily Supplies', contact='9123456780')
        db.session.add_all([s1, s2])
        db.session.commit()
        # sample products
        p1 = Product(name='Apples', category='Fruits', quantity=10, supplier_id=s1.id, price=40.0)
        p2 = Product(name='Rice 5kg', category='Grains', quantity=3, supplier_id=s2.id, price=250.0)
        db.session.add_all([p1, p2])
        db.session.commit()
    app.run(host='0.0.0.0', port=5000, debug=True)
