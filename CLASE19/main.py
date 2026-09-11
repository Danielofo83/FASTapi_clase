from sqlmodel import SQLModel, create_engine, Session
from fastapi import FastAPI
from contextlib import asynccontextmanager

engine = create_engine("postgresql+psycopg2://postgres:secret_password@localhost:5432/empresa_db")

@async contextmanager

async def create_db_and_tables(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    print("Database and tables created successfully.")
    yield
    
    app = FastAPI()
    lifespan=create_db_and_tables(app)
    app = FastAPI(lifespan=lifespan)
