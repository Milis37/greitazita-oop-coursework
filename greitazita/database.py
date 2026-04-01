from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .config import DATABASE_URL
from .models import Base

class DatabaseManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.engine = create_engine(DATABASE_URL, echo=False)
            Base.metadata.create_all(cls._instance.engine)
            cls._instance.Session = sessionmaker(bind=cls._instance.engine)
        return cls._instance

    def get_session(self):
        return self._instance.Session()
