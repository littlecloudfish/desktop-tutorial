from database import Base, SessionLocal,engine
from models import Score, User, Music
from sqlalchemy import select

Base.metadata.create_all(engine)
Session = SessionLocal

# with Session() as session:
#     numberone = Score(grade = 3.6,user_id=1,music_id=2)
#     session.add(numberone)
#     session.commit()
# stmt = select(Score)
# for ss in session.scalars(stmt):
#     print(ss)
# with Session() as session:
#     spongebob = User(
#         username="spongebob",
#         fullname="Spongebob Squarepants",
#         postmusics=[Music(name="crimanal")],
#     )
#     sandy = User(
#         username="sandy",
#         fullname="Sandy Cheeks",
#         postmusics=[
#             Music(name="dangerous"),
#             Music(name="crimanal"),
#         ],
#     )
#     patrick = User(username="patrick", fullname="Patrick Star")
#     session.add_all([spongebob, sandy, patrick])
#     session.commit()

# stmt = select(User).where(User.username.in_(["spongebob", "sandy"]))

# for user in session.scalars(stmt):
#     print(user)
select(Music).where(name="test")