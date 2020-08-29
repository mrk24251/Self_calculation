from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# postgresql+psycopg2://punish:punish@127.0.0.1:5432
# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"postgresql+psycopg2cffi://user:password@host:port/dbname[?key=value&key=value...]

SQLALCHEMY_DATABASE_URL = "postgres://edivuszmtozaer:5cd123b632aceca4937d0a3cebf94efff795f6ac831819a8f5e70d619b4c4c11@ec2-34-238-26-109.compute-1.amazonaws.com:5432/ddl7hva590ggcq"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
