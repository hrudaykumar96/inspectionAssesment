# 🚗 Vehicle Damage Inspection Backend

A Django REST API for managing vehicle damage inspections with JWT authentication.

---

## ⚙️ Requirements

- Python 3.8+
- MySQL (or compatible DB like MariaDB)
- `pip` and `virtualenv`

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/hrudaykumar96/inspectionAssesment
cd vehicle-inspection-backend
```

---

### 2. Create a Virtual Environment

```bash
python -m venv ven
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Create `.env` File

Create a `.env` file in the root directory with your database and secret settings:

```env
DB_NAME=your_db_name
DB_USER=your_mysql_user
DB_PASSWORD=your_mysql_password
DB_HOST=localhost
DB_PORT=3306

SECRET_KEY=your_django_secret_key
DEBUG=True
```

---

### 5. Set Up the Database

Create your MySQL database manually:

```sql
CREATE DATABASE your_db_name;
```

---

### 6. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 7. (Optional) Create a Superuser

```bash
python manage.py createsuperuser
```

---

### 8. Run the Development Server

```bash
python manage.py runserver
```

Server will be available at:  
👉 `http://127.0.0.1:8000/`

---

## 📡 API Endpoints & How to Test

### 1. User Authentication

| Method | URL                                   | Description            | Payload / Notes                                  |
|--------|-------------------------------------|------------------------|-------------------------------------------------|
| POST   | `http://127.0.0.1:8000/signup/`    | Register a new user    | JSON: `{ "username": "...", "password": "..." }` |
| POST   | `http://127.0.0.1:8000/login/`     | Obtain JWT tokens      | JSON: `{ "username": "...", "password": "..." }` |
| POST   | `http://127.0.0.1:8000/refresh/`   | Refresh JWT access token | JSON: `{ "refresh": "<refresh_token>" }`         |

---

### 2. Inspections (Authenticated routes)

> **Include JWT token in the header:**

```
Authorization: Bearer <your_access_token>
```

| Method | URL                                         | Description                    | Payload / Notes                                       |
|--------|---------------------------------------------|-------------------------------|-----------------------------------------------------|
| GET    | `http://127.0.0.1:8000/inspections/`       | List inspections for the user; filter with query param `status` (optional) | Example: `http://127.0.0.1:8000/inspections/?status=pending` |
| POST   | `http://127.0.0.1:8000/inspections/`       | Create a new inspection        | JSON example:<br> `{ "vehicle_number": "DL01AB1234", "damage_report": "Broken tail light", "image_url": "https://example.com/image.jpg" }` |
| GET    | `http://127.0.0.1:8000/inspection/id/<id>/`   | Get details of a specific inspection (owned by user) | -                                                   |
| GET    | `http://127.0.0.1:8000/inspection/status/<id>/`   | Get details of a specific inspection by status | -                                                   |
| PATCH  | `http://127.0.0.1:8000/inspection/id/<id>/`   | Update status (`reviewed` or `completed`) | JSON example: `{ "status": "reviewed" }`             |
| DELETE | `http://127.0.0.1:8000/inspection/id/<id>/`   | Delete an inspection (owned by user) | -                                               |

---

## Example cURL Requests

**Login**

```bash
curl -X POST http://127.0.0.1:8000/login/ \
-H "Content-Type: application/json" \
-d '{"username":"youruser", "password":"yourpass"}'
```

**Get Inspections with optional status filter**

```bash
curl -X GET "http://127.0.0.1:8000/inspections/?status=pending" \
-H "Authorization: Bearer <your_access_token>"
```

**Create a New Inspection**

```bash
curl -X POST http://127.0.0.1:8000/inspections/ \
-H "Authorization: Bearer <your_access_token>" \
-H "Content-Type: application/json" \
-d '{"vehicle_number":"DL01AB1234","damage_report":"Broken tail light","image_url":"https://example.com/image.jpg"}'
```

---

✅ You’re now ready to test the API with Postman, cURL, or any REST client!
