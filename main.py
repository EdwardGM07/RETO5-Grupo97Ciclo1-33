import json

def contar_cantidad_cursos(lista_cursos)->int:
  cantidad_cursos=0
  for curso in lista_cursos:
    if curso["nombre"]=="FP":
      cantidad_cursos+=1
  return cantidad_cursos

def contar_cantidad_cursos_buscado(lista_cursos, curso_buscado)->int:
  cantidad_cursos=0
  for curso in lista_cursos:
    if curso["nombre"]==curso_buscado:
      cantidad_cursos+=1
  return cantidad_cursos

def contar_cantidad_cursos_profesor(lista_cursos,cedula_profesor)->int:
  cantidad_cursos=0
  for curso in lista_cursos:
    profe_curso=curso["profesor"]
    if profe_curso["cedula"]==cedula_profesor:
      cantidad_cursos+=1

  return cantidad_cursos

def calcular_matriculados(lista_cursos)->int:
  total_matriculados=0
  for curso in lista_cursos:
    if curso["nombre"]=="FP":
      total_matriculados+=len(curso["estudiantes"])
  return total_matriculados

def calcular_notas_finales(lista_cursos):
  for curso in lista_cursos:
    for estudiante in curso["estudiantes"]:
      lista_notas=estudiante["notas"]
      estudiante["nota_final"]=lista_notas[0]*0.3+lista_notas[1]*0.35+lista_notas[2]*0.35
      print("El estudiante ",estudiante["nombre"],"en el curso",curso["nombre"], "obtuvo la nota ", estudiante["nota_final"])



 
with open('informacion.txt', 'r') as file:
    texto = file.read().replace('\n', '')
#print(texto)

lista_cursos = json.loads(texto)
#######reto1
cantidad_cursos_programacion=contar_cantidad_cursos(lista_cursos)
print ("la cantidad de profes de programacion es ",cantidad_cursos_programacion)
#######reto2
curso_quesebusca="IN"
cantidad_curso_buscado=contar_cantidad_cursos_buscado(lista_cursos, curso_quesebusca)
print("la cantidad de cursos para",curso_quesebusca,"es",cantidad_curso_buscado)
#######reto3
cedula_profe=123
cantidad_curso_profesor=contar_cantidad_cursos_profesor(lista_cursos,cedula_profe)
print("el total de profesor con cedula ",cedula_profe,"es",cantidad_curso_profesor)
#######reto4
cantidad_estudiantes_programacion=calcular_matriculados(lista_cursos)
print("Cantidad de estudiantes matriculados en programacion son: ",cantidad_estudiantes_programacion)
#######reto 5
calcular_notas_finales(lista_cursos)
