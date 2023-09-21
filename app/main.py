# app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers import order_controller
from database import engine, Base

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(order_controller.router)

# Create tables in the database
Base.metadata.create_all(bind=engine)
