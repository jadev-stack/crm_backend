from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database.crmbdd import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50))
    email = Column(String(50))
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    rcarga = relationship("Rcarga")
