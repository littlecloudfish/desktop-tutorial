

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# from sqlalchemy_media import StoreManager, FileSystemStore
# import functools

#not sure path
# TEMP_PATH = '/tmp/sqlalchemy-media'

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# StoreManager.register(
#     'fs',
#     functools.partial(FileSystemStore, TEMP_PATH, 'http://static.example.org/'),
#     default=True
# )