🧠 Project Nexus Documentation

**Repository:** [`alx-project-nexus`](https://github.com/ufuos/alx-project-nexus)  


Repository:** [`alx-project-nexus`](https://github.com/ufuos/alx-project-nexus)  

---

## 🏷️ Badges  

![Django](https://img.shields.io/badge/Django-4.2-green?logo=django&logoColor=white)  
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue?logo=postgresql&logoColor=white)  
![Python](https://img.shields.io/badge/Python-3.10-yellow?logo=python&logoColor=white)  
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED?logo=docker&logoColor=white)  
![GitHub](https://img.shields.io/badge/GitHub-Repo-black?logo=github&logoColor=white)  
![License](https://img.shields.io/badge/License-MIT-green.svg)  













CI/CD Status:




🎯 Overview

Project Nexus serves as a documentation hub summarizing key learnings and implementations from the ProDev Backend Engineering program.

The centerpiece is the E-Commerce Backend – ProDev BE, a real-world inspired project demonstrating scalable, secure, and performant backend development with Django and PostgreSQL.

This backend powers 🍽️ MealWorld — Your Global Meal Marketplace, a platform for global meal discovery, ordering, and management.

🛒 MealWorld — Your Global Meal Marketplace
🌍 About the Platform

MealWorld connects local meal vendors and global customers through a smooth e-commerce experience with:

🔐 Authentication

🛍️ Product Discovery

🧾 Order Management

⚙️ E-Commerce Backend - ProDev BE
🔍 Real-World Application

This backend mirrors a production-grade product catalog system, offering:

✅ CRUD operations for products & categories

🔐 Secure JWT authentication

🔍 Filtering, sorting & pagination

⚡ Database indexing & optimization

📘 Swagger UI API documentation

🧱 Project Goals
Goal	Description
CRUD APIs	Endpoints for products, categories & users
Filtering & Sorting	Product discovery by category, price, etc.
Pagination	Efficient browsing with large datasets
Database Optimization	Schema design with indexes
API Documentation	Swagger-based developer docs
⚙️ Technologies Used
Category	Tools
Backend Framework	Django
Database	PostgreSQL
Authentication	JWT
Documentation	Swagger / drf-yasg
Testing	Postman + DRF Tests
CI/CD	GitHub Actions
Containerization	Docker & Docker Compose
Version Control	Git & GitHub
🧩 Implementation Process
🪄 Commit Workflow
Commit Message	Description
feat: setup Django with PostgreSQL	Initialize project
feat: add JWT authentication	Secure login/register APIs
feat: add product CRUD	Product endpoints
feat: integrate Swagger UI	Developer docs
perf: add DB indexing	Query optimization
docs: add API usage	Update docs
🧰 Example API Endpoints
Endpoint	Method	Description
/api/auth/register/	POST	Register user
/api/auth/login/	POST	Login with JWT
/api/products/	GET, POST	View or create products
/api/products/<id>/	PUT, DELETE	Update/delete product
/api/products/?category=meals&sort=price	GET	Filter/sort
/api/products/?page=2	GET	Paginate results
🧪 Testing Setup (Swagger + Frontend Template)
1️⃣ Swagger UI Integration
# settings.py
INSTALLED_APPS = [
    ...
    'rest_framework',
    'drf_yasg',
]

# urls.py
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="MealWorld E-Commerce API",
        default_version="v1",
        description="ProDev BE E-Commerce Backend for MealWorld — Your Global Meal Marketplace",
    ),
    public=True,
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
]

🚀 Getting Started
🔧 Prerequisites

Ensure you have:

Python 3.10+

PostgreSQL

Docker & Docker Compose

Git

📦 Installation
# Clone repository
git clone https://github.com/ufuos/alx-project-nexus.git
cd alx-project-nexus

# Create virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run development server
python manage.py runserver

🧩 Environment Variables

Create a .env file:

# .env template
DEBUG=True
SECRET_KEY=your_django_secret_key
ALLOWED_HOSTS=localhost,127.0.0.1

DATABASE_NAME=mealworld_db
DATABASE_USER=postgres
DATABASE_PASSWORD=postgres
DATABASE_HOST=db
DATABASE_PORT=5432

# JWT Settings
ACCESS_TOKEN_LIFETIME=60
REFRESH_TOKEN_LIFETIME=1440

🐳 Docker Setup
🧱 Dockerfile
FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

CMD ["gunicorn", "mealworld.wsgi:application", "--bind", "0.0.0.0:8000"]

⚙️ docker-compose.yml
version: '3.9'

services:
  web:
    build: .
    command: gunicorn mealworld.wsgi:application --bind 0.0.0.0:8000
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    env_file:
      - .env
    depends_on:
      - db

  db:
    image: postgres:15
    restart: always
    environment:
      POSTGRES_DB: ${DATABASE_NAME}
      POSTGRES_USER: ${DATABASE_USER}
      POSTGRES_PASSWORD: ${DATABASE_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data/

volumes:
  postgres_data:

💻 Run with Docker
docker-compose up --build
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py collectstatic --noinput


Access the API via 👉 http://localhost:8000/swagger/

⚙️ CI/CD Setup with GitHub Actions
✅ .github/workflows/tests.yml
name: Django Tests

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest

    services:
      postgres:
        image: postgres:15
        env:
          POSTGRES_DB: test_db
          POSTGRES_USER: postgres
          POSTGRES_PASSWORD: postgres
        ports: ["5432:5432"]
        options: >-
          --health-cmd "pg_isready -U postgres"
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5

    env:
      DATABASE_URL: postgres://postgres:postgres@localhost:5432/test_db
      SECRET_KEY: ci_secret
      DEBUG: false

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.10"

      - name: Install dependencies
        run: |
          pip install -r requirements.txt

      - name: Run Django Tests
        run: |
          python manage.py test

🐳 .github/workflows/docker-build.yml
name: Docker Build

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  docker-build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Build Docker image
        uses: docker/build-push-action@v5
        with:
          context: .
          push: false
          tags: mealworld-backend:latest

🤝 Contributing

Contributions, issues, and feature requests are welcome!
Please open a Pull Request to collaborate.

🧾 License

This project is licensed under the MIT License.

💬 Acknowledgments

Empowering backend excellence through MealWorld — Your Global Meal Marketplace 🌍🍴