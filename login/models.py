from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from database.crmbdd import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
