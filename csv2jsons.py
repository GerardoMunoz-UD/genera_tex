# Programa que crea a partir de los CSV un json con la información de los Syllabus
import csv
import json


# syllabus_dic={
    # "Espacio Académico" : "Producción y Comprensión de Textos",
    # "Código del Espacio" : "5",
    # "Número de Créditos" : "2",
    # "Área de Formación" : "Administrativa y Socio-Humanística",
    # "Horas Trabajo Directo" : "4",
    # "Horas Trabajo Colaborativo" : "0",
    # "Horas Trabajo Autónomo" : "2",
    # "Obligatorio" : "",
    # "Básico" : "",
    # "Complementario" : "",
    # "Electivo" : "",
    # "IntrísecoIntríseco" : "",
    # "Extrínseco" : "",
    # "Teórico" : "",
    # "Teórico-Práctico" : "",
    # "Práctico" : "",
    # "Asistido por TICs" : "",
# {
    # "Clase magistral" : "",
    # "Seminario" : "",
    # "Seminario-Taller" : "",
    # "Taller" : "",
    # "Prácticas" : "",
    # "Proyectos con tutoría" : "",
    # "Conocimientos previos del curso" : "Gramática española, ortografía, lexicografía básica.",
    # "Prerrequisitos" : "",
    # "Es prerrequisito de" : "",
    # "Habilidades y Resultados de Aprendizaje" : {
        # "Col_1a":{
            # "col2a":{
                # "col3a":[
                    # "col4a",
                    # "col4b"                
                # ],
                # "col3c":[
                    # "col4c",
                    # "col4d",                
                    # "col4e"                
                # ],
                # "col3f":[
                    # "col4f"
                # ]
            # },
            # "col2g":{
                # "col3g":[
                    # "col4g",
                    # "col4h"                
                # ],
                # "col3i":[
                    # "col4i",
                    # "col4j"                
                # ]
           # }
        # },
        # "Col_1k":{
            # "col2k":{
                # "col3k":[
                    # "col4k",
                    # "col4l"                
                # ],
                # "col3m":[
                    # "col4m",
                    # "col4n",                
                    # "col4o"                
                # ]
            # },
            # "col2p":{
                # "col3p":[
                    # "col4p",
                    # "col4q"                
                # ],
                # "col3r":[
                    # "col4r",
                    # "col4s",                
                    # "col4t"                
                # ]
           # }
        # }
    # },
    # "Contenidos y Unidades Temáticas" : [
        # "Contenido 1",
        # "Contenido 2",
        # "...",
        # "Contenido n"
    # ],
    # "Enfoque de Aprendizaje y Enseñanza" : "",
    # "Plan de Evaluaciones" : "",
    # "Resultados de Aprendizaje a ser evaluados" : [
        # "Resultado 1",
        # "Resultado 2",
        # "...",
        # "Resultado n",
    # ],
    # "Materiales de Estudio" : {
        # "[1]":"Álvaro Andrés Hamburguer Fernández, {\\it Escribir para objetivar el saber: Cómo producir artículos, libros, reseñas, textos y ensayos}. Segunda Edición, Bogotá, D.C., Universidad de La Salle, 2017.",
        # "[2]":"William Ángel Salazar Pulido, {\\it Alta Redacción: Informes científicos, académicos, técnicos y administrativos}. Novena Edición, NET Educativa, Bogotá, D.C., 2009.",
        # "[3]":"Rodrigo de Castro Korgi, {\\it El universo \\LaTeX}. Segunda Edición, Bogotá: Universidad Nacional de Colombia, 2003.",
        # "[4]":"Hilary Glasman-Deal, {\\it Science Research Writing: For Non-Native Speakers of English}. Imperial College Press, London, 2010.",
        # "[5]":"Estanislao Zuleta, {\\it Elogio de la dificultad y Otros ensayos}. Quinta Edición, Fundación Estanislao Zuleta, Cali, 2001.",
        # "[6]":"Estanislao Zuleta, {\\it Arte y Filosofía}. Segunda Edición, Hombre Nuevo Editores, Fundación Estanislao Zuleta, Medellín, 2001.",
        # "[7]":"Academias de la Lengua Española, {\\it Ortografía de la Lengua Española}. Editorial Espasa Calpe, S.A., Madrid, 1999",
        # "[8]":"William Ospina, {\\it La lámpara maravillosa: Cuatro ensayos sobre la educación y un elogio de la lectura}. Random House Mondadori, S.A.S., Bogotá, 2013.",
        # "[9]":"Peter Watson, {\\it Convergencias: El orden subyacente en el corazón de la ciencia}. Editorial Planeta S.A., Bogotá, 2017.",
        # "[10]":"Nils J. Nilsson, {\\it Para una comprensión de las creencias}. Fondo de Cultura Económica, México, 2019."
    # }
   
# }        

def leer_archivo_csv(nombre_archivo_csv):
    datos = []
    with open('plantilla.json', 'r', encoding='utf-8') as json_file:
        plantilla_json = json.load(json_file)
    with open(nombre_archivo_csv, newline='', encoding='utf-8') as csvfile:
        lector_csv = csv.reader(csvfile, delimiter=";")
        cabeceras = next(lector_csv)  # Leer la primera fila como cabeceras
        print("cabeceras:",cabeceras)
        print()
        print("plantilla_json:",set(plantilla_json.keys()))
        print()
        print("Repetidos->",set(cabeceras) & set(plantilla_json.keys()))
        for fila in lector_csv:
            #print()
            var1=dict(zip(cabeceras, fila))
            #print("Repetidos->",set(var1.keys()) & set(plantilla_json.keys()))
            var= var1 | plantilla_json
            nombre_archivo_json=("syllabi_json/"+var["Semestre"]+"_"+var["Código del Espacio"]+"_"+var["Espacio Académico"]+".json").replace(" ","_")
            #print(nombre_archivo_json)
            with open(nombre_archivo_json, 'w', encoding='utf-8') as archivo_json:
                json.dump(var, archivo_json, ensure_ascii=False, indent=4, separators=(',', ': '))        
        

# Ejemplo de uso:
if __name__ == "__main__":
    nombre_archivo_csv = "MallaCurricular.csv"
    datos_leidos = leer_archivo_csv(nombre_archivo_csv)
