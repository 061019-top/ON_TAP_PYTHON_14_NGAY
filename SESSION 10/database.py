from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

DB_URL = 'mysql+pymysql://root:minhhaycuoi2006@localhost/library_db'

engine = create_engine(DB_URL)

Base = declarative_base()  

LocalSession = sessionmaker(
    autoflush=False,
    bind=engine,
    expire_on_commit=False
)

def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()