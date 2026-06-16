# 🎓 Student Management REST API

A Student Management REST API built using Django, Django REST Framework (DRF), PostgreSQL, and Docker. The project demonstrates clean backend architecture by separating Models, Serializers, Services, and API Views while integrating a Dockerized PostgreSQL database.

---

# 🚀 Features

- Create Student Records
- Retrieve All Students
- PostgreSQL Database Integration
- Dockerized Database Setup
- Django ORM
- Django REST Framework APIs
- Service Layer Architecture
- Database-Level Duplicate Prevention
- Serializer-Based Validation
- Clean Project Structure

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|----------|
| Django | Backend Framework |
| Django REST Framework | API Development |
| PostgreSQL | Relational Database |
| Docker | Database Containerization |
| Django ORM | Database Operations |
| DRF Serializers | Request Validation |

---

# 📂 Project Structure

```text
student_api_django/
│
├── manage.py
│
|── settings.py
|── urls.py
|── asgi.py
│── wsgi.py
│
├── students/
│   ├── models.py
│   ├── serializers.py
│   ├── services.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
│
├── requirements.txt
└── README.md
```

---

# 🏗️ System Architecture

```text
Client Request
      ↓
DRF View
      ↓
Serializer Validation
      ↓
Service Layer
      ↓
Django ORM
      ↓
PostgreSQL Database
      ↓
JSON Response
```

---

# 🗄️ Database Design

## Student Table

| Column | Type |
|----------|------|
| id | Integer |
| name | String |
| age | Integer |
| branch | String |

---

## Unique Constraint

Duplicate student records are prevented using a database-level unique constraint.

```python
class Meta:
    constraints = [
        models.UniqueConstraint(
            fields=["name", "age", "branch"],
            name="unique_student"
        )
    ]
```

This ensures:

```text
John | 20 | CSE
```

cannot be inserted more than once.

---

# 📋 API Endpoints

## Create Student

### POST /api/students/

Request:

```json
{
    "name": "John",
    "age": 20,
    "branch": "CSE"
}
```

Response:

```json
{
    "id": 1,
    "name": "John",
    "age": 20,
    "branch": "CSE"
}
```

---

## Get All Students

### GET /api/students/

Response:

```json
[
    {
        "id": 1,
        "name": "John",
        "age": 20,
        "branch": "CSE"
    }
]
```

---

# 🔍 Validation Strategy

## Serializer Validation

Incoming requests are validated using DRF serializers.

Example:

```python
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
```

Validation includes:

- Required fields
- Data type checking
- Request body validation

---

## Database-Level Validation

Unique constraints ensure:

- No duplicate student records
- Consistent database state
- Improved data integrity

---

# 🐳 Docker Setup

## Pull PostgreSQL Image

```bash
docker pull postgres
```

---

## Run PostgreSQL Container

```bash
docker run --name student-postgres \
-e POSTGRES_USER=postgres \
-e POSTGRES_PASSWORD=postgres \
-e POSTGRES_DB=studentdb \
-p 5432:5432 \
-d postgres
```

---

## Verify Running Container

```bash
docker ps
```

Expected:

```text
student-postgres
```

---

# ⚙️ PostgreSQL Configuration

Update `settings.py`:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "studentdb",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
```

---

# 🏃 Running the Project

## Clone Repository

```bash
git clone https://github.com/MeghanaKanchiboina1616/Student-api-Django
```

---

## Navigate to Project

```bash
cd student-management-api
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Create Migrations

```bash
python manage.py makemigrations
```

---

## Apply Migrations

```bash
python manage.py migrate
```

---

## Run Server

```bash
python manage.py runserver
```

Server:

```text
http://127.0.0.1:8000
```

---

# 📡 API Examples

## Create Student

```http
POST /api/students/
Content-Type: application/json

{
    "name": "Meghana",
    "age": 21,
    "branch": "AIML"
}
```

---

## Get Students

```http
GET /api/students/
```

---

# 🔥 Backend Concepts Demonstrated

- Django REST Framework
- PostgreSQL Integration
- Dockerized Database
- REST API Development
- Django ORM
- Service Layer Pattern
- Serializer Validation
- Database Constraints
- CRUD Operations
- Relational Database Design
- Clean Architecture

---

# 🚀 Future Improvements

- Update Student API
- Delete Student API
- Pagination
- Search Students
- JWT Authentication
- Role-Based Access Control (RBAC)
- Swagger/OpenAPI Documentation
- Docker Compose Setup
- CI/CD Pipeline
- PostgreSQL Query Optimization

---

# 📚 Learning Outcomes

This project helped in understanding:

- Building REST APIs using Django REST Framework
- Connecting Django with PostgreSQL
- Running PostgreSQL inside Docker Containers
- Implementing Service Layer Architecture
- Using Serializers for Validation
- Managing Database Constraints
- Designing Relational Database Models
- Following Backend Development Best Practices

---

# 👨‍💻 Author
**Meghana Kanchiboyina**
Developed as a backend engineering project to demonstrate Django REST Framework, PostgreSQL, Docker, Service Layer Architecture, Database Design, and REST API Development best practices.
