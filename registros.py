from sqlalchemy import select
from sqlalchemy.orm import Session
from conexion import engine
from modelos import Estudiante

def registrar_estudiante(nombre: str, correo: str):
    if not nombre or not correo:
        print("Error: Nombre o correo vacío, revise que los datos esten correctos.")
        return
    
    with Session(engine) as session:
        with session.begin():
            stmt = select(Estudiante).where(Estudiante.correo == correo)
            correo_existente = session.scalars(stmt).first()
            
            if correo_existente:
                print("Error: El correo ya se encuentra registrado, revise que los datos esten correctos.")
                return
                
            nuevo_estudiante = Estudiante(nombre=nombre, correo=correo)
            session.add(nuevo_estudiante)
            
        print("El estudiante se guardó exitosamente.")

def listar_estudiantes():
    with Session(engine) as session:
        stmt = select(Estudiante)
        estudiantes = session.scalars(stmt).all()
        if not estudiantes:
            print("No hay estudiantes registrados.")
            return
        
        for e in estudiantes:
            print(f"ID: {e.estudiante_id} | Nombre: {e.nombre} | Correo: {e.correo}")