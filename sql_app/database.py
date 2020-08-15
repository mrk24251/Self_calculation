from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"postgresql+psycopg2cffi://user:password@host:port/dbname[?key=value&key=value...]
SQLALCHEMY_DATABASE_URL = "postgres://ecotulybegudqp:ffbc23c3e2a96e020abd94c79d7382774ca79e119dffc871ee932184b5a6d47e@ec2-107-22-7-9.compute-1.amazonaws.com:5432/dvvi34oj0bas5"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()