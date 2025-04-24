from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Exemplo de URL de conexão:
# postgresql://usuario:senha@localhost:5432/nome_do_banco

DATABASE_URL = "postgresql://postgres:root@127.0.0.1:5432/"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
