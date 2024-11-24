from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://username:password@localhost/db_name"  # Substituir amb les teves dades de connexió

# Crear el motor de connexió
engine = create_engine(DATABASE_URL)

# Crear la sessió
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base per a les taules
Base = declarative_base()