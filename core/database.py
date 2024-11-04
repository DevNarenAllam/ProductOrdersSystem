from sqlmodel import SQLModel, create_engine

from core.authentication import get_hashed_pwd
from core.models import User
from core.config import MYSQL_URL

# Create a SQLite database in memory
engine = create_engine(MYSQL_URL, echo=True)


# Create the table
try:
    SQLModel.metadata.create_all(engine)
    print("Table created successfully.")
except Exception as e:
    print(f"Error: {e}")

    # class Config:
    #     sa_table_args = {"extend_existing": True}
