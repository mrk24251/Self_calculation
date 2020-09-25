from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = os.environ['DATABASE_URL']

# postgresql+psycopg2://punish:punish@127.0.0.1:5432
# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"postgresql+psycopg2cffi://user:password@host:port/dbname[?key=value&key=value...]
SQLALCHEMY_DATABASE_URL = "postgres://dyzcgcqupktivs:0d8126207f1c2023eb85f74a833cd8abf4b44a8cc316c16719e093332b7a0e69@ec2-3-218-112-22.compute-1.amazonaws.com:5432/d3jgfifnf1nfr2"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
