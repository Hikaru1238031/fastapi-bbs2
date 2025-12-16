# app/main.py
from fastapi import FastAPI
from app.routers import threads
from starlette.staticfiles import StaticFiles

app = FastAPI(title="BBS API - Step1")

# Threadsルーターを登録
app.include_router(threads.router)

from app.routers import posts  # ← 追加

app.mount(
    "/static", # ブラウザがアクセスするURLパス (例: http://.../static/css/style.css)
    StaticFiles(directory="app/static"), # ← Dockerコンテナ内でのディレクトリ構造
    name="static"
)

app.include_router(threads.router)
app.include_router(posts.router)
app.include_router(posts.threads_router)