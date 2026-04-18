from sqlalchemy.orm import Session
from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioCreate

def obtener_todos(db: Session):
    return db.query(Usuario).all()

def obtener_por_id(db: Session, usuario_id: int):
    return db.query(Usuario).filter(Usuario.id == usuario_id).first()

def obtener_por_email(db: Session, email: str):
    return db.query(Usuario).filter(Usuario.email == email).first()

def crear(db: Session, datos: UsuarioCreate):
    nuevo = Usuario(nombre=datos.nombre, email=datos.email)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def actualizar(db: Session, usuario_id: int, datos: UsuarioCreate):
    usuario = obtener_por_id(db, usuario_id)
    if not usuario:
        return None
    usuario.nombre = datos.nombre
    usuario.email = datos.email
    db.commit()
    db.refresh(usuario)
    return usuario

def eliminar(db: Session, usuario_id: int):
    usuario = obtener_por_id(db, usuario_id)
    if not usuario:
        return None
    db.delete(usuario)
    db.commit()
    return usuario
def creacion_google(db: Session, usuario_id:int):
    return usuario