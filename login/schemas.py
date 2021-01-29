from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    username: str


class UserAuth(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True


class UserAuthenticate(UserAuth):
    hashed_password: str


class Token(BaseModel):
    access_token: str
    token_type: str
    username: str
    user_sede: int
    user_cargo: int
    user_group: int


class TokenData(BaseModel):
    username: str = None


class User_Cargo(BaseModel):
    id: int
    user_id: int
    cargo_id: int


class User_Group(BaseModel):
    id: int
    user_id: int
    group_id: int


class User_Data(BaseModel):
    user_id: int
    firts_name: str
    last_name: str
    identity_number: str
    sede_id: int
