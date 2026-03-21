from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Modelo de usuario
class Usuario(BaseModel):
    id: int
    nombre: str
    email: str

# Base de datos simulada
usuarios = [
    {"id": 1, "nombre": "Ana", "email": "ana@email.com"},
    {"id": 2, "nombre": "Luis", "email": "luis@email.com"}
]

# GET todos los usuarios
@app.get("/usuarios")
def obtener_usuarios():
    return usuarios

# GET usuario por id
@app.get("/usuarios/{id}")
def obtener_usuario(id: int):
    for usuario in usuarios:
        if usuario["id"] == id:
            return usuario
    return {"error": "Usuario no encontrado"}

# POST crear usuario
@app.post("/usuarios")
def crear_usuario(usuario: Usuario):
    usuarios.append(usuario.dict())
    return {"mensaje": "Usuario creado"}

# PUT actualizar usuario
@app.put("/usuarios/{id}")
def actualizar_usuario(id: int, usuario_actualizado: Usuario):
    for usuario in usuarios:
        if usuario["id"] == id:
            usuario["nombre"] = usuario_actualizado.nombre
            usuario["email"] = usuario_actualizado.email
            return {"mensaje": "Usuario actualizado"}
    return {"error": "Usuario no encontrado"}

# DELETE eliminar usuario
@app.delete("/usuarios/{id}")
def eliminar_usuario(id: int):
    for usuario in usuarios:
        if usuario["id"] == id:
            usuarios.remove(usuario)
            return {"mensaje": "Usuario eliminado"}
    return {"error": "Usuario no encontrado"}