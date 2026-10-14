# backend/main.py

from fastapi import FastAPI
from .routers import papers

app = FastAPI(title="MedLearn MVP")

app.include_router(papers.router)
