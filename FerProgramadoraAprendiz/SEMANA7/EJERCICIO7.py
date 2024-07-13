"""Desarrollo de un Programa en Python:
Crea una o varias clases en Python que hagan uso de constructores (__init__) y destructores (__del__).
Asegúrate de que los constructores inicialicen correctamente los atributos del objeto y que los destructores realicen alguna forma de limpieza o cierre de recursos (si es aplicable).
Requisitos Específicos:

El programa debe demostrar claramente cómo se utilizan los constructores y destructores en las clases.
Incluye comentarios en el código que expliquen cómo funcionan estos métodos y en qué situaciones se activan.
Asegúrate de que el código esté bien estructurado y siga las buenas prácticas de programación.
Publicación en GitHub:

Sube el código fuente de tu programa a tu repositorio de GitHub. Asegúrate de que el repositorio sea accesible públicamente para que pueda ser revisado.
Entrega de la Tarea:

Proporciona el enlace de tu repositorio de GitHub a través de la plataforma de entrega de tareas.
Asegúrate de cumplir con la fecha y hora límite para la presentación de la tarea."""
class Miclase:
    def __init__(self):
        """Contructor : se llama automaticamente al crear un objeto"""
        print("Sela credo un objeto de Miclase")
    def __del__(self):
        """Destructor : se llma automaticamene cuando el objeto de mi clase es destruido"""
        print("Sela destruido una objeto de Miclase")
    """Creamos un objeto de la clase Miclase"""
objeto = Miclase()
