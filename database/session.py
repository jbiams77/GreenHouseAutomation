from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import database.db_globals as db

class SingletonSession:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SingletonSession, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        self.engine = create_engine(db.BASE_DATABASE_URL, echo=True)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

# global singleton session instance
db_session = SingletonSession().session
