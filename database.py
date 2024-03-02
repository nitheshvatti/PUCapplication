from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

database_url = "mssql+pyodbc://yeshwanth:Infinity%403104@pucserver.database.windows.net/PUCDB?driver=ODBC+Driver+17+for+SQL+Server"

engine = create_engine(database_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# conn = engine.connect()

Base = declarative_base()
