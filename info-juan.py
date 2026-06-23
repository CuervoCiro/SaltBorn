# info de mi proyecto
nombre_proyecto = "SaltBorn" # nombre de tu proyecto
descripcion = "SaltBorn es un videojuego de plataformas en 2D diseñado para ser tan entretenido como desafiante" # que resuelve
tecnologias = ["React","Django","MySQL","Unity/C#"] # ["React", "Django", "MySQL"]
integrantes = ["Juan Manuel Cuervo Ciro","Juan Carlos Posada","Sair Cardona", "Luis Mateo Arraut"] # ["Nombre1", "Nombre2"]
funcionalidades = ["Login","Registro","seleccion de niveles", "Guardado de progreso","Pefil de Usuario", "Configuración de audio y video"] # ["Login", "Registro"]
def mostrar_info():
  print(f"Proyecto: {nombre_proyecto}")
  print(f"Descripcion: {descripcion}")
  print("Tecnologias:")
  for t in tecnologias:
    print(f" - {t}")
  print("Integrantes:")
  for i in integrantes:
    print(f" - {i}")
mostrar_info()