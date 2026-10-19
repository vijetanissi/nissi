import os
import psycopg2
import uvicorn
from fastapi import FastAPI

app = FastAPI()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "postgres")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", "password")

@app.get("/")
def home():
    return {"message": "Hello! My app is running successfully on OpenShift!"}

@app.get("/db-check")
def db_check():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            connect_timeout=5
        )
        conn.close()
        return {"database": "Connected successfully to AWS RDS PostgreSQL!"}
    except Exception as e:
        return {"database": "Connection failed", "error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
