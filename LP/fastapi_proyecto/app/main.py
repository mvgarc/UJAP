from fastapi import FastAPI
from app.database import engine, Base
from app.routers import usuarios

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Usuarios",
    description="API construida con FastAPI + PostgreSQL",
    version="1.0.0"
)

app.include_router(usuarios.router)

@app.get("/")
def inicio():
    return {"mensaje": "API funcionando correctamente"}
