import mimetypes
from sqlalchemy import Column, Integer, String, ForeignKey,DateTime, Float, Text,TypeDecorator,Unicode
from sqlalchemy.types import Date
from sqlalchemy.orm import  relationship
from sqlalchemy.sql import func
from database import Base
import datetime
# user_login package
from flask_login import UserMixin  
#sqlalchemy media
from sqlalchemy_media import File, MagicAnalyzer, ContentTypeValidator
from sqlalchemy_media.constants import MB, KB
import json

from hmac import compare_digest


class DictMixIn:
    def to_dict(self):
        return {
            column.name: getattr(self, column.name)
            if not isinstance(
                getattr(self, column.name), (datetime.datetime, datetime.date)
            )
            else getattr(self, column.name).isoformat()
            for column in self.__table__.columns
        }
#sqlalchemy media
class CV(File):
    __pre_processors__ = [
        MagicAnalyzer(),
        ContentTypeValidator(['application/pdf', 'image/jpeg'])
    ]
    __max_length__ = 16*MB
    __min_length__ = 10*KB

class Json(TypeDecorator):
    impl = Unicode

    def process_bind_param(self, value, engine):
        return json.dumps(value)

    def process_result_value(self, value, engine):
        if value is None:
            return None
        return json.loads(value)

# class Record(Base, DictMixIn):
#     __tablename__ = "Records"

#     id = Column(Integer, primary_key=True, index=True)
#     date = Column(Date)
#     country = Column(String, index=True)
#     cases = Column(Integer)
#     deaths = Column(Integer)
#     recoveries = Column(Integer)

class User(Base,DictMixIn,UserMixin):
    __tablename__ = "user_account"
    id = Column(Integer, primary_key=True)
    username = Column(String(30))
    email = Column(String(30))
    image_file = Column(String(20))
    password = Column(String(60))
    create_date = Column(DateTime(timezone=True), nullable=False,server_default=func.now())
    fullname = Column(String)
    postmusics = relationship(
        "Music", back_populates="user", cascade="all, delete-orphan"
    )
    makescore = relationship(  
        "Score", back_populates="user", cascade="all, delete-orphan"
    )
    profileimg = relationship("Img", back_populates="user")
    makefeedback = relationship(  
        "Music_Feedback", back_populates="user", cascade="all, delete-orphan"
    )
# change for file
    cv = Column(CV.as_mutable(Json))


    def check_password(self, password):
        #return compare_digest(password, "password")
        return password == self.password
    def __repr__(self):
        return f"User(id={self.id!r}, name={self.username!r}, fullname={self.fullname!r})"

class Music(Base,DictMixIn):
    __tablename__ = "music"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    music_address = Column(String, nullable=False,server_default="/DEMOMUSIC/crimanal.mp3")
    # cover_address = Column(String, nullable=False,server_default="/demopicture/example.png")
    post_date = Column(DateTime(timezone=True), nullable=False,server_default=func.now())
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)
    user = relationship("User", back_populates="postmusics")
    musicscore = relationship("Score", back_populates="music",cascade = "all, delete-orphan")
    coverimg = relationship("Img", back_populates="music")
    musicfeedback = relationship("Music_Feedback", back_populates="music",cascade = "all, delete-orphan")

    def __repr__(self):
        return f"Address(id={self.id!r}, name={self.name!r},user={self.user!r})"

class Score(Base,DictMixIn):
    __tablename__="scores"
    id = Column(Integer, primary_key=True)
    grade = Column(Float,nullable=False)
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)
    user = relationship("User", back_populates="makescore")
    music_id = Column(Integer, ForeignKey("music.id"), nullable=False)
    music = relationship("Music", back_populates="musicscore")

class Img(Base,DictMixIn):
    __tablename__="imagetable"
    id = Column(Integer, primary_key=True)
    img = Column(Text, unique=True, nullable = False)
    name = Column(String(350), nullable=False)
    mimetype = Column(Text, nullable=False)
    music_id = Column(Integer, ForeignKey("music.id"))
    music = relationship("Music", back_populates="coverimg")
    user_id = Column(Integer, ForeignKey("user_account.id"))
    user = relationship("User", back_populates="profileimg")

class Music_Feedback(Base,DictMixIn):
    __tablename__="music_feedback"
    id = Column(Integer, primary_key=True)
    feedbackcomment = Column(String(650),nullable=False)
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)
    user = relationship("User", back_populates="makefeedback")
    music_id = Column(Integer, ForeignKey("music.id"), nullable=False)
    music = relationship("Music", back_populates="musicfeedback")

