import db_globals as db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



# Database connection
engine = create_engine(db.BASE_DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# Create tables
db.Base.metadata.create_all(engine)

# Commit changes and close session
session.commit()
session.close()
