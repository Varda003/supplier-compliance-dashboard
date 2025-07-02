from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # <--- add this import
from routers import supplier

app = FastAPI()

# Add CORS middleware to allow React frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React default origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(supplier.router)

@app.get("/")
def root():
    return {"message": "Supplier Compliance Dashboard API is running."}
