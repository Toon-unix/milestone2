from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
import asyncpg

app = FastAPI()

DATABASE_URL = os.getenv("DATABASE_URL")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "API is running"}

@app.get("/user")
async def user_endpoint():
    conn = await asyncpg.connect(DATABASE_URL)
    row = await conn.fetchrow("SELECT name FROM users LIMIT 1")
    await conn.close()
    return {"name": row["name"] if row else None}

@app.get("/containerid")
async def container_id():
    container_id = os.getenv("HOSTNAME", "unknown")
    return {"container_id": container_id}