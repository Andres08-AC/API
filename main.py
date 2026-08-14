from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from database import Base, engine, get_db
from schemas import UsuarioCreate, UsuarioResponse
import crud


# Crear las tablas si no existen
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="API Usuarios Universitaria",
    version="1.0.0"
)


# CORS para el futuro Frontend React
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
def inicio():
    return "Bienvenido al programa usuarios"


@app.get(
    "/listadeusuarios",
    response_model=list[UsuarioResponse]
)
def obtener_usuarios(db: Session = Depends(get_db)):

    return crud.obtener_usuarios(db)


@app.post(
    "/agregarusuarios",
    response_model=UsuarioResponse,
    status_code=201
)
def agregar_usuario(
    datos: UsuarioCreate,
    db: Session = Depends(get_db)
):

    return crud.crear_usuario(db, datos)


@app.get(
    "/listadeusuarios/{id}",
    response_model=UsuarioResponse
)
def obtener_usuario(
    id: int,
    db: Session = Depends(get_db)
):

    usuario = crud.obtener_usuario(db, id)

    if usuario is None:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )

    return usuario


@app.delete("/eliminarusuario/{id}")
def eliminar_usuario(
    id: int,
    db: Session = Depends(get_db)
):

    usuario = crud.eliminar_usuario(db, id)

    if usuario is None:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )

    return {
        "mensaje": "Usuario eliminado exitosamente"
    }
