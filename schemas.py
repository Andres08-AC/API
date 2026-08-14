from pydantic import BaseModel


class UsuarioCreate(BaseModel):
    nombre: str
    apellido: str
    telefono: str
    edad: int


class UsuarioResponse(BaseModel):
    id: int
    nombre: str
    apellido: str
    telefono: str
    edad: int

    class Config:
        from_attributes = True
