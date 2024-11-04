from core.database import engine
from core.models import User
from sqlmodel import Session, select
from core.authentication import get_hashed_pwd
from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.post("/users/", response_model=User)
def add_user(user: User):
    try:
        with Session(engine) as session:
            user.hashed_password = get_hashed_pwd(user.hashed_password)
            session.add(user)
            session.commit()
            session.refresh(user)
            return user

    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=400, detail="User could not be created")


# user = User(
#     name="John Doe",
#     email="john@example.com",
#     hashed_password="Python#123",
#     phone="1234567890",
#     date_of_birth="1990-01-01",
#     is_active=True,
# )

# add_user(user)
