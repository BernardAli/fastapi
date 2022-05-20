from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLACHEMY_DATABASE_URL = 'postgresql://<username>:<password>@<ip-address/hostname>/<databasename>'

SQLACHEMY_DATABASE_URL = 'postgresql://postgres:Matt6:33@localhost/fastapi'
engine = create_engine(SQLACHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()