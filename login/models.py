from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database.crmbdd import Base
from crm.models import Cargo, Sede


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50))
    email = Column(String(50))
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    rcarga = relationship("Rcarga")
    user_cargo = relationship("User_Cargo", back_populates="users")
    user_data = relationship("User_Data", back_populates="users")
    user_group = relationship("User_Group", back_populates="users")


class Grupo(Base):
    __tablename__ = "grupo"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(30))

    user_group = relationship("User_Group", back_populates="grupo")


class User_Data(Base):
    __tablename__ = "user_data"

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    firts_name = Column(String(50))
    last_name = Column(String(50))
    identity_number = Column(String(50))
    sede_id = Column(Integer, ForeignKey("sede.id"))

    users = relationship("User", back_populates="user_data")


class User_Cargo(Base):
    __tablename__ = "user_cargo"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    cargo_id = Column(Integer, ForeignKey("cargo.id"))

    users = relationship("User", back_populates="user_cargo")


class User_Group(Base):
    __tablename__ = "user_group"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    grupo_id = Column(Integer, ForeignKey("grupo.id"))

    users = relationship("User", back_populates="user_group")
    grupo = relationship("Grupo", back_populates="user_group")
