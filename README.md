# 🚀 Full-Stack Authentication System

A complete, secure user registration and login system built from scratch. This project demonstrates the fundamental concepts of full-stack development, including REST API creation, secure password management, and seamless client-server communication.

## ✨ Features

* **User Registration:** Securely register new users with duplicate username validation.
* **User Authentication:** Login functionality with secure credential verification.
* **Password Hashing:** Passwords are never stored in plaintext. They are securely hashed and salted using the `bcrypt` library.
* **RESTful API:** Clean communication between the frontend and backend using asynchronous JavaScript (Fetch API) and JSON.
* **Robust Error Handling:** Returns appropriate HTTP status codes (e.g., 400 Bad Request, 401 Unauthorized, 500 Internal Server Error) and displays user-friendly error messages on the frontend.
* **Environment Security:** Database credentials and secrets are safely managed using `.env` variables, keeping sensitive data out of the source code.
* **Client-Side Validation:** Ensures password confirmation matches before sending requests to the server, reducing unnecessary API calls.

## 🛠️ Tech Stack

**Frontend:**
* HTML5 / CSS3
* Vanilla JavaScript (ES6+ async/await, Fetch API)

**Backend:**
* Python 3
* FastAPI (Web framework for building APIs)
* Uvicorn (ASGI web server implementation)
* Bcrypt (Password hashing)

**Database:**
* PostgreSQL (Relational Database)
* Psycopg2 (PostgreSQL database adapter for Python)

## ⚙️ Local Setup & Installation

Follow these steps to run the project locally on your machine.

### 1. Prerequisites
Ensure you have the following installed:
* Python 3.x
* PostgreSQL
* A local development server (e.g., VS Code "Live Server" extension)

### 2. Database Configuration
1. Open pgAdmin or your PostgreSQL terminal.
2. Create a new database named `demo`.
3. Open the Query Tool for the `demo` database and execute the following SQL to create the users table:

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);
```

### 3. Backend Setup
Clone the repository and install the required Python dependencies:

```bash
git clone [https://github.com/Vosikas/Fullstack-auth.git](https://github.com/Vosikas/Fullstack-auth.git)
cd Fullstack-auth
pip install fastapi uvicorn psycopg2 bcrypt pydantic python-dotenv
```

### 4. Environment Variables
In the root directory of the project, create a file named `.env` and add your local PostgreSQL credentials:

```env
DB_HOST=localhost
DB_NAME=demo
DB_USER=postgres
DB_PASSWORD=your_super_secret_password
DB_PORT=5432
```
*(Note: The `.env` file is included in `.gitignore` and will not be pushed to version control).*

### 5. Running the Application

**Start the Backend API:**
Open your terminal in the project directory and run the Uvicorn server:
```bash
uvicorn main:app --reload
```
The API will start running at `http://127.0.0.1:8000`.

**Start the Frontend:**
Open the `register.html` or `login.html` file using a local web server (like the Live Server extension in VS Code) to bypass CORS restrictions during local development.

## 📡 API Endpoints

| Method | Endpoint | Description | Request Body (JSON) |
| :--- | :--- | :--- | :--- |
| `POST` | `/register` | Registers a new user | `{"username": "...", "password": "..."}` |
| `POST` | `/login` | Authenticates a user | `{"username": "...", "password": "..."}` |

## 💡 Future Enhancements
- [ ] Implement JSON Web Tokens (JWT) for persistent user sessions.
- [ ] Add password strength validation (regex) on the frontend.
- [ ] Create a protected dashboard route accessible only to authenticated users.
