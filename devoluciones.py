from sqlalchemy import select
from sqlalchemy.orm import Session
from conexion import engine
from modelos import Equipo, Estudiante, Prestamo

def registrar_prestamo(estudiante_id: int, equipo_id: int, fecha: str, cantidad: int):
    if cantidad <= 0 or not fecha:
        print("Error: La cantidad debe ser mayor a cero y la fecha es obligatoria, revise que los datos esten correctos.")
        return
    
    with Session(engine) as session:
        with session.begin():
            estudiante = session.get(Estudiante, estudiante_id)
            if not estudiante:
                print("Error: El estudiante no existe, revise que los datos esten correctos.")
                return
            
            equipo = session.get(Equipo, equipo_id)
            if not equipo:
                print("Error: El equipo no existe, revise que los datos esten correctos.")
                return
            
            if equipo.stock_disponible < cantidad:
                print(f"Error: Stock insuficiente. Stock actual disponible: {equipo.stock_disponible}, revise que los datos esten correctos.")
                return
            
            equipo.stock_disponible -= cantidad
            
            nuevo_prestamo = Prestamo(
                estudiante_id=estudiante_id,
                equipo_id=equipo_id,
                fecha_prestamo=fecha,
                cantidad=cantidad,
                estado="ACTIVO"
            )
            session.add(nuevo_prestamo)
            
        print("El préstamo se registró exitosamente y se descontó el stock del equipo.")