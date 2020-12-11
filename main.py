from fastapi import FastAPI
import uvicorn
from login import login
from rcarga import rcarga
from crm import crm
from fastapi.middleware.cors import CORSMiddleware
from database.crmbdd import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(login.router)
app.include_router(rcarga.router)
app.include_router(crm.router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
