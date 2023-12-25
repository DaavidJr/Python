
#USO DE IF Y AND

print("Programa becas")
distancia_alumno= int(input("ingrese distancia de la escuela"))
sueldo_familia= int(input("ingrese sueldo familia"))
numero_hermanos= int(input("ingrese cantidad de hermanos"))

if distancia_alumno>40 and sueldo_familia<=200000 and numero_hermanos>2:
    print("Te ganaste la beca")
else: print("No te ganaste la beca")

#USO DE IN PARA ELEGIR COSAS LOWER TRANSFORMAR EN MINISCULAS, UPPER TRANSFORMA EN MAYUSCULA
print("Seleccion de asignaturas año 2023")
print("Ingrese su asignatura  a elegir: informatica - redes - mecanica")

opcion= input("Ingresa la asignatura")
asignatura=opcion.lower()
if asignatura in ("informatica", " redes" , "mecanica"):
    print("asignatura ingresada correctamente")
else:
    print("Asignatura no valida")

        
  




