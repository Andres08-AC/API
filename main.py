from fastapi import FastAPI

app = FastAPI()

usuarios = [
    {
        "id": 1,
        "nombre": "marisol",
        "apelldio": "con un ojo el mar y el otro el sol",
        "telefono": "3208456871",
        "edad": 30
    },
    {
        "id": 2,
        "nombre": "pelusa",
        "apelldio": "valero",
        "telefono": "3203575215",
        "edad": 27
    },
    
]

@app.get("/")
def inicio():
    return "Bienvendio al programa usuarios"

@app.get("listadeusuarios")
def obtener_usuaruos():
    return usuarios

@app.post("/agregarusuarios")
def agregar_usuarios(
    nombre: str,
    apellido: str,
    telefono: str,
    edad: int
):
    nuevo_id = len(usuarios) + 1

    nuevo_usuarios = {
        "id": nuevo_id,
        "nombre": nombre,
        "apellido": apellido,
        "telefono": telefono,
        "edad": edad
    }
    usuarios.append(nuevo_usuarios)

    return {
        "mensaje": "nuevo usuario agregado",
        "usuario": nuevo_usuarios
    }

@app.get("/listadeusuarios/{id}")
def obtener_usuario(id: int):
    for usuario in usuarios:
        if usuario["id"] == id:
            return usuario

    return {
        "mensaje": "usuario no encontrado"
    }

@app.delete("/eliminarusuario/{id}")
def eliminar_usuario(id: int):
    for usuario in usuarios:
        if usuario["id"] == id:
            usuarios.remove(usuario)

            return {
                "mensaje": "usuario eliminado exitosamente",
                "usuario": usuario
            }

    return {
        "mensaje": "usuario no encontrado"
    }