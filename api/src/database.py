from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
rom dotenv import load_dotenv
from os import getenv

load_dotenv()
    
user = getenv("DB_USER")
password = getenv("DB_PASS")
db_url = getenv("DB_URL")

engine = create_engine(f"mysql+pymysql://{user}:{password}@{db_url}:3306", convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import yourapplication.models
    Base.metadata.create_all(bind=engine)