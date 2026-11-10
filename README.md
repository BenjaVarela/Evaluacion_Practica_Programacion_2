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