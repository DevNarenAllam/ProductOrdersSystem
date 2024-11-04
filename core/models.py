from fastapi import FastAPI
from sqlmodel import SQLModel, Field
from core.authentication import get_hashed_pwd
from datetime import date

app = FastAPI()


class UserBase(SQLModel):
    username: str


class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    id: int


# Define the model
class User(SQLModel, table=True):
    __tablename__ = "users"
    __table_args__ = {"mysql_auto_increment": "1001"}

    id: int | None = Field(primary_key=True, default=None)
    name: str = Field(max_length=50)
    email: str = Field(unique=True, max_length=50)
    phone: str | None = Field(default=None, unique=True, max_length=20)
    date_of_birth: date | None = Field(default=None)
    registered_on: date = Field(default_factory=date.today)
    hashed_password: str = Field(
        max_length=100,
        exclude=True,
        repr=False,
    )
    is_active: bool = Field(default=True)


def hash_password(password: str) -> str:
    # Implement your password hashing here
    return "hashed_" + password


@app.post("/users/", response_model=UserRead)
def create_user(user_create: UserCreate):
    hashed_password = hash_password(user_create.password)
    user = User(username=user_create.username, password=hashed_password)
    # Save 'user' to the database
    # ...
    return user  # Returns a UserRead instance without the password


# @app.get("/users/{user_id}", response_model=UserRead)
# def read_user(user_id: int):
#     user = get_user_from_db(user_id)
#     return user  # Password is not included in the response
