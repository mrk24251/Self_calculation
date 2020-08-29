from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import psycopg2

# postgresql+psycopg2://punish:punish@127.0.0.1:5432
# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"postgresql+psycopg2cffi://user:password@host:port/dbname[?key=value&key=value...]
SQLALCHEMY_DATABASE_URL = os.environ.get('DATABASE_URL')

engine = psycopg2.connect(SQLALCHEMY_DATABASE_URL, sslmode='require')

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
