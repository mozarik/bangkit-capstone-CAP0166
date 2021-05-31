import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

''' DATABASE CONNECTION '''
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:@localhost:3306/db_watcher"
# SQLALCHEMY_DATABASE_URL = os.environ.get('DB_CONN')

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
