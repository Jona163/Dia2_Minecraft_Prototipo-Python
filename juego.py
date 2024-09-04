"""
Autor: [Jonathan Hernandez]
Fecha: [02/09/24]
Descripción: [Prototipo basico minecraft]
"""
# Importación de librería de Ursina y del controlador en primera persona
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

# Crear una instancia de la aplicación de Ursina
app = Ursina()

# Clase Voxel, que representa un bloque en el mundo
class Voxel(Button):
    def __init__(self, position=(0, 0, 0)):
        # Llamada al constructor de la clase Button, para crear un bloque interactivo
        super().__init__(
            parent=scene,              # El padre es la escena 3D
            position=position,          # Posición del bloque en el mundo
            model='cube',               # El modelo 3D es un cubo
            origin_y=0.5,               # Ajustar el origen del cubo en el eje Y
            texture='grass',            # Textura del bloque (en este caso, césped)
            color=color.rgb(255, 255, 255),  # Color del bloque (blanco)
            highlight_color=color.lime, # Color resaltado al pasar el ratón sobre el bloque
        )

    # Detecta la entrada del teclado o ratón
    def input(self, key):
        # Si el ratón está sobre el bloque
        if self.hovered:
            # Si se presiona el botón izquierdo del ratón, crea un nuevo bloque adyacente
            if key == "left mouse down":
                voxel = Voxel(position=self.position + mouse.normal)
            # Si se presiona el botón derecho del ratón, destruye el bloque
            if key == "right mouse down":
                destroy(self)

# Tamaño del "chunk" (bloque de terreno generado)
chunkSize = 16
# Crear una cuadrícula de bloques en el plano XZ
for z in range(chunkSize):
    for x in range(chunkSize):
        voxel = Voxel(position=(x, 0, z))  # Crear bloques en la posición (x, 0, z)

# Añadir un controlador de primera persona para mover al jugador
player = FirstPersonController()

# Iniciar la aplicación
app.run()
