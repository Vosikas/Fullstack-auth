from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import psycopg2
import bcrypt

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_credentials=True, 
    allow_headers=["*"]
)

class User(BaseModel):
    username: str
    password: str

@app.post("/register")
def register(user: User):
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="demo",
            user="postgres",
            password="YOUR_PASSWORD_HERE", 
            port='5432'
        )
        cursor = conn.cursor()
        
        hased_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
        hased_password = hased_password.decode('utf-8')
        
        query = "INSERT INTO users (username,password) VALUES (%s,%s)"
        cursor.execute(query, (user.username, hased_password))
        conn.commit()
        
    except psycopg2.IntegrityError:
        if 'conn' in locals():
            conn.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists")
        
    finally:
       
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()
            
    return {"message": "Successful!"}

@app.post("/login")
def login(user: User):
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="demo",
            user="postgres",
            password="YOUR_PASSWORD_HERE", 
            port='5432'
        )
        cursor = conn.cursor()
        
        query = "SELECT password FROM users WHERE username = %s"
        cursor.execute(query, (user.username,))
        result = cursor.fetchone()
        
        if result is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Wrong username or password")
            
        stored_password = result[0]
        
        if not bcrypt.checkpw(user.password.encode('utf-8'), stored_password.encode('utf-8')):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Wrong username or password")
            
    except psycopg2.Error:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Database error")
        
    finally:
        
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()
            
    return {"message": "Successful login!"}