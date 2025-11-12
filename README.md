# 🧠 Project Nexus Documentation
**Repository:** `alx-project-nexus`

---

## 🎯 Overview

**Project Nexus** serves as a documentation hub summarizing my key learnings, experiences, and practical implementations during the **ProDev Backend Engineering** program.  

The centerpiece of my learning journey is the **E-Commerce Backend - ProDev BE**, a real-world inspired backend project that simulates scalable, secure, and high-performance backend development using Django and PostgreSQL.

---

## 🛒 E-Commerce Backend - ProDev BE

### 🔍 Real-World Application

The **E-Commerce Backend** mimics a real-world product catalog system that supports:
- CRUD operations for products and categories.
- Secure JWT authentication.
- Filtering, sorting, and pagination for efficient product browsing.
- Database indexing for performance optimization.
- Swagger UI documentation for frontend integration.

---

### 🧱 Project Goals

| Goal | Description |
|------|--------------|
| **CRUD APIs** | Build endpoints to create, read, update, and delete products, categories, and users. |
| **Filtering & Sorting** | Enable dynamic product discovery by category, price, or name. |
| **Pagination** | Manage large datasets efficiently. |
| **Database Optimization** | Design schema and indexes for high-performance queries. |
| **API Documentation** | Generate developer-friendly API docs via Swagger UI. |

---

## ⚙️ Technologies Used

| Category | Tools |
|-----------|-------|
| **Backend Framework** | Django |
| **Database** | PostgreSQL |
| **Authentication** | JWT |
| **Documentation** | Swagger / drf-yasg |
| **Testing** | Postman + Frontend Template |
| **Version Control** | Git & GitHub |

---

## 🧩 Implementation Process

### 🪄 Git Commit Workflow

| Commit Message | Description |
|----------------|--------------|
| `feat: set up Django project with PostgreSQL` | Initialize project and connect to PostgreSQL |
| `feat: implement user authentication with JWT` | Add secure login/register APIs |
| `feat: add product APIs with filtering and pagination` | Implement product CRUD and discovery |
| `feat: integrate Swagger documentation` | Add drf-yasg Swagger UI |
| `perf: optimize database queries with indexing` | Add indexing for performance |
| `docs: add API usage instructions in Swagger` | Document endpoints for frontend use |

---

## 🧰 Example API Endpoints

| Endpoint | Method | Description |
|-----------|---------|-------------|
| `/api/auth/register/` | POST | Register a new user |
| `/api/auth/login/` | POST | Obtain JWT tokens |
| `/api/products/` | GET, POST | View or add products |
| `/api/products/<id>/` | PUT, DELETE | Update or remove a product |
| `/api/products/?category=electronics&sort=price` | GET | Filter and sort |
| `/api/products/?page=2` | GET | Paginate |

---

## 🧪 Testing Setup (Swagger + Frontend Template)

### 1️⃣ **Swagger UI Integration**

To visualize and test APIs:
```python
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
        title="E-Commerce API",
        default_version="v1",
        description="ProDev BE E-Commerce Backend",
    ),
    public=True,
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
]
"# alx-project-nexus" 
