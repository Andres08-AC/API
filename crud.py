from sqlalchemy.orm import Session
from models import Usuario
from schemas import UsuarioCreate


def obtener_usuarios(db: Session):
    return db.query(Usuario).all()


def obtener_usuario(db: Session, usuario_id: int):
    return (
        db.query(Usuario)
        .filter(Usuario.id == usuario_id)
        .first()
    )


def crear_usuario(db: Session, datos: UsuarioCreate):

    nuevo_usuario = Usuario(
        nombre=datos.nombre,
        apellido=datos.apellido,
        telefono=datos.telefono,
        edad=datos.edad
    )

    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)

    return nuevo_usuario


def eliminar_usuario(db: Session, usuario_id: int):

    usuario = obtener_usuario(db, usuario_id)

    if usuario is None:
        return None

    db.delete(usuario)
    db.commit()

    return usuario
