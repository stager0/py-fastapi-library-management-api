from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "sqlite:///./py-fastapi-library-management-api.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True, future=True)

SessionLocal = sessionmaker(expire_on_commit=False, bind=engine, future=True)

def get_db() -> SessionLocal:
    session = SessionLocal()

    try:
        yield session
    finally:
        session.close()