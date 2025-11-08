
# Smart Inventory Manager (Advanced - Demo)

A simple full-stack inventory manager demo (Flask backend + React frontend). This is a GitHub-ready starter project built to showcase backend APIs, frontend integration, and Docker setup.

## Features
- Flask REST API (auth, products, suppliers)
- SQLite used for demo (switch to MySQL/Postgres in production)
- React frontend (Vite) with a simple dashboard and product list
- Docker + docker-compose for local setup
- Seed/sample data included for demo (admin/admin123)

## Quick start (local, Python & Node required)
1. Backend:

```bash
cd backend
python -m venv venv
source venv/bin/activate   # on Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

2. Frontend:

```bash
cd frontend
npm install
npm run dev   # or npm run preview after build
```

3. Or with Docker (recommended):

```bash
docker-compose up --build
```

Backend runs at http://localhost:5000 and frontend preview at http://localhost:5173 (or Vite dev on 5173).

## API Endpoints (examples)
- POST /auth/register - register user (payload: {username,password})
- POST /auth/login - login -> returns access_token
- GET /products/ - list products
- POST /products/ - create product
- GET /suppliers/ - list suppliers
- POST /suppliers/ - create supplier
- GET /dashboard/summary - basic dashboard numbers

## Notes
- SQLite is used for simple demo; update SQLALCHEMY_DATABASE_URI in backend/app.py to use MySQL.
- This repo is intentionally simple for quick demonstration. You can expand features: role-based routes, JWT-required endpoints, pagination, search, UI improvements, CI/CD, tests, etc.
