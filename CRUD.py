from sqlalchemy import select
from sqlalchemy.orm import Session
from conexion import engine
from modelos import Equipo, Prestamo

def crear_equipo(nombre: str, tipo: str, stock_disponible: int):
    if not nombre or not tipo or stock_disponible < 0:
        print("Error: Los datos estan vacíos o el stock es inválido, por favor revise que los datos esten correctos.")
        return
    
    with Session(engine) as session:
        with session.begin():
            nuevo_equipo = Equipo(nombre=nombre, tipo=tipo, stock_disponible=stock_disponible)
            session.add(nuevo_equipo)
        print("El nuevo equipo se guardó correctamente.")

def listar_equipos():
    with Session(engine) as session:
        stmt = select(Equipo)
        equipos = session.scalars(stmt).all()
        if not equipos:
            print("No hay equipos registrados en la base de datos.")
            return

        for e in equipos:
            print(f"ID: {e.equipo_id} | Nombre: {e.nombre} | Tipo: {e.tipo} | Stock: {e.stock_disponible}")

def buscar_equipo_por_id(equipo_id: int):
    with Session(engine) as session:
        equipo = session.get(Equipo, equipo_id)
        if not equipo:
            print("Error: El equipo no fue encontrado, por favor revise que los datos esten correctos.")
            return
        
        print(f"ID: {equipo.equipo_id} | Nombre: {equipo.nombre} | Tipo: {equipo.tipo} | Stock: {equipo.stock_disponible}")

def actualizar_equipo(equipo_id: int, nombre: str, tipo: str, stock_disponible: int):
    if not nombre or not tipo or stock_disponible < 0:
        print("Error: Los datos estan vacíos o el stock es inválido, por favor revise que los datos esten correctos.")
        return
    
    with Session(engine) as session:
        with session.begin():
            equipo = session.get(Equipo, equipo_id)
            if not equipo:
                print("Error: El equipo a actualizar no existe, por favor revise que los datos esten correctos.")
                return
            
            equipo.nombre = nombre
            equipo.tipo = tipo
            equipo.stock_disponible = stock_disponible
        print("La actualización del equipo se guardó correctamente.")

def eliminar_equipos(equipo_id: int):
    with Session(engine) as session:
        with session.begin():
            equipo = session.get(Equipo, equipo_id)
            if not equipo:
                print("Error: El equipo que desea eliminar no existe, por favor revise que los datos esten correctos.")
                return

            stmt = select(Prestamo).where(Prestamo.equipo_id == equipo_id)
            prestamos_asociados = session.scalars(stmt).first()

            if prestamos_asociados:
                print("Error: No se podrá eliminar el equipo ya que este tiene un prestamo asociado. Por favor revise que los datos esten correctos.")
                return

            session.delete(equipo)
            print("El equipo seleccionado se eliminó correctamente de la base de datos.")