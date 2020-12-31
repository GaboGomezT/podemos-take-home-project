from sqlalchemy import create_engine
from dotenv import load_dotenv
from os import getenv

load_dotenv()

user = getenv("PODEMOS_DB_USER")
password = getenv("PODEMOS_DB_PASS")
db_url = getenv("PODEMOS_DB_URL")
db_uri = f"mysql+pymysql://{user}:{password}@{db_url}:3306"
print(f"\033[1m\033[92mdb_uri -> \033[94m{ db_uri }\033[0m")
engine = create_engine(db_uri)

with engine.connect() as con:
    print("hello world")
    rs = con.execute('SELECT * FROM podemos_eval.Grupos')

    for row in rs:
        print(row)