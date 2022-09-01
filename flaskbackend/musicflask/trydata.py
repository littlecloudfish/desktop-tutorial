from database import Base, SessionLocal,engine
from models import User, Music
from sqlalchemy import select

Base.metadata.create_all(engine)
Session = SessionLocal

with Session() as session:
    spongebob = User(
        username="spongebob",
        fullname="Spongebob Squarepants",
        postmusics=[Music(name="crimanal")],
    )
    sandy = User(
        username="sandy",
        fullname="Sandy Cheeks",
        postmusics=[
            Music(name="dangerous"),
            Music(name="crimanal"),
        ],
    )
    patrick = User(username="patrick", fullname="Patrick Star")
    session.add_all([spongebob, sandy, patrick])
    session.commit()


stmt = select(User).where(User.username.in_(["spongebob", "sandy"]))

for user in session.scalars(stmt):
    print(user)
