# Evaluación Practica - Unidad 2

## Situación problemática
Una universidad necesita registrar equipos tecnologicos(Notebooks, proyectores, etc) y gestionar sus prestamos a estudiantes.

## Guía para la instalación y Ejecución Local

### 1. Clonar el repositorio
```bash
git clone https://github.com/BenjaVarela/Evaluacion_Practica_Programacion_2.git
cd cd Evaluacion_Practica_Programacion_2

### 2. Crear y activar un entorno virtual
```bash
python -m venv venv
# Luego el siguiente comando, que en Windows es:
source venv/Scripts/activate
```

### 3. Instalar el ORM
```bash
python -m pip install sqlalchemy
```

### 4. Ejecutar el sistema de reservas
```bash
python main.py
```

El sistema cuenta con cinco funcionalidades enumeradas del 0-8. Cada una de ellas con una función única, en las cuales se encuentran:

1. Crear equipo
2. Listar equipos
3. Buscar equipo por ID
4. Actualizar equipo
5. Eliminar equipo
6. Registrar estudiante
7. Listar estudiantes
8. Registrar préstamo
0. Salir
## Pruebas

Para realizar las pruebas, se debe elegir una opción de las disponibles.

# Respuestas y evidencias

## Pregunta 1:

Archivo y función: modelos.py (Clase prestamo)
Código / respuesta:
class Prestamo(Base):
    __tablename__ = "prestamo"
    prestamo_id: Mapped[int] = mapped_column(primary_key=True)
    estudiante_id: Mapped[int] = mapped_column(ForeignKey('estudiante.estudiante_id'), nullable=False)
    equipo_id: Mapped[int] = mapped_column(ForeignKey('equipo.equipo_id'), nullable=False)
    fecha_prestamo: Mapped[str] = mapped_column(nullable=False)
    cantidad: Mapped[int] = mapped_column(nullable=False)
    estado: Mapped[str] = mapped_column(String(20), nullable=False)
    estudiante: Mapped["Estudiante"] = relationship(back_populates="prestamos")
    equipo: Mapped["Equipo"] = relationship(back_populates="prestamos")

Explicación:
estudiante_id: Clave foránea que referencia a estudiante.estudiante_id. Relaciona la transacción de préstamo con la persona que solicita el equipo.equipo_id: Clave foránea que referencia a equipo.equipo_id. Relaciona el préstamo con el dispositivo tecnológico otorgado. Los atributos relationship() con back_populates permiten la navegación bidireccional ORM entre las entidades Estudiante, Prestamo y Equipo, Prestamo.


## Pregunta 2:
Archivo y función: CRUD.py (función crear_equipo )
Código / respuesta:
def crear_equipo(nombre: str, tipo: str, stock_disponible: int):
    if not nombre or not tipo or stock_disponible < 0:
        print("Error: Los datos estan vacíos o el stock es inválido, por favor revise que los datos esten correctos.")
        return
    
    with Session(engine) as session:
        with session.begin():
            nuevo_equipo = Equipo(nombre=nombre, tipo=tipo, stock_disponible=stock_disponible)
            session.add(nuevo_equipo)
        print("El nuevo equipo se guardó correctamente.")
Explicación:

La instrucción session.add(nuevo_equipo) añade el objeto instanciado a la sesión activa del ORM.

La persistencia en la base de datos SQLite se confirma mediante el bloque with session.begin():, el cual ejecuta un commit automático al finalizar el contexto sin errores.

## Pregunta 3:
Archivo y función: CRUD.py, función listar_equipos
Código / respuesta:
def listar_equipos():
    with Session(engine) as session:
        stmt = select(Equipo)
        equipos = session.scalars(stmt).all()
        if not equipos:
            print("No hay equipos registrados en la base de datos.")
            return

        for e in equipos:
            print(f"ID: {e.equipo_id} | Nombre: {e.nombre} | Tipo: {e.tipo} | Stock: {e.stock_disponible}")

Explicación:

Se construye la sentencia ORM stmt = select(Equipo) para consultar la tabla equipo.

El método session.scalars(stmt).all() ejecuta la consulta SQL a través del motor de base de datos y convierte el conjunto de resultados en una lista de objetos de la clase Equipo.

Finalmente, el código verifica mediante if not equipos si la consulta devolvió registros vacíos y, de no ser así, itera sobre cada instancia para mostrar por consola sus atributos (equipo_id, nombre, tipo y stock_disponible).