# FastAPI RESTful App

A simple **FastAPI** project with **MySQL**, following **RESTful API principles** to manage resources using CRUD operations (Create, Read, Update, Delete).

## 🚀 Features
- FastAPI for high-performance APIs
- MySQL database integration
- SQLAlchemy for ORM
- Pydantic for data validation
- RESTful API structure

## 🛠 Tech Stack
- **FastAPI** (Backend Framework)
- **MySQL** (Database)
- **SQLAlchemy** (ORM for database interaction)
- **Pydantic** (Data validation)
- **Uvicorn** (ASGI server for running FastAPI)

## 📌 Installation & Setup

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/Bhumigor/Fastapi-Restful-App.git
cd Fastapi-Restful-App
```

### 2️⃣ Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables
Create a `.env` file and add your database configuration:
```sh
DATABASE_URL=mysql+pymysql://username:password@localhost/db_name
```

### 5️⃣ Start the FastAPI Server
```sh
uvicorn main:app --reload
```

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|---------|-------------|
| **GET** | `/items/` | Get all items |
| **GET** | `/items/{item_id}` | Get item by ID |
| **POST** | `/items/` | Create a new item |
| **PUT** | `/items/{item_id}` | Update an existing item |
| **DELETE** | `/items/{item_id}` | Delete an item |

📌 **Visit API Docs:** Open **`http://127.0.0.1:8000/docs`** in your browser for interactive API documentation.

## 🛠 Project Structure
```sh
Fastapi-Restful-App/
│── main.py           # FastAPI application entry point
│── models.py         # Database models using SQLAlchemy
│── routes.py         # API endpoints
│── schemas.py        # Pydantic models for validation
│── database.py       # Database connection setup
│── config.py         # Configuration settings
│── requirements.txt  # Project dependencies
│── .env              # Environment variables (ignored in Git)
```

## 📌 Contributing
Feel free to fork, create issues, and submit PRs! 🚀

---
💡 **Happy Coding!** 😊
