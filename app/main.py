# app/main.py
from fastapi import FastAPI
from app.routers import threads

app = FastAPI(title="BBS API - Step1")

# Threadsルーターを登録
app.include_router(threads.router)

from app.routers import posts  # ← 追加

app.include_router(threads.router)
app.include_router(posts.router)
app.include_router(posts.threads_router)