import re
import json
import os

def replace_variables_in_latex(latex_text, variables):
    # Utilizamos una expresión regular para encontrar los comandos "\variable{x}"
    pattern_var = r"\\var\{([^}]+)\}"
    pattern_varlist = r"\\varlist\{([^}]+)\}"
    
    def replace_variable(match):
        # Función para reemplazar los comandos de variable con su valor correspondiente
        var_name = match.group(1)
        
        if var_name in variables:
            print("Sí encontró:",var_name)
            return str(variables[var_name])
        else:
            print("No ncontró:",var_name)
            return match.group(0)  # Mantenemos el comando original si no se encuentra la variable
    def replace_variable_list(match):
        def list2lista(lista):
            respuesta = "\\begin{tabular}{cp{11cm}}"
            for elemento in lista:
                respuesta += "\n  \\textbullet & "+elemento+" \\\\"
            return respuesta + "\n\\end{tabular} \\\\"
    
        # Función para reemplazar los comandos de variable con su valor correspondiente
        var_name = match.group(1)
        
        if var_name in variables:
            print("Sí encontró:",var_name)
            return str(list2lista(variables[var_name]))
        else:
            print("No ncontró:",var_name)
            return match.group(0)  # Mantenemos el comando original si no se encuentra la variable

    # Aplicamos la función de reemplazo a cada coincidencia encontrada en el texto LaTeX
    result = re.sub(pattern_var, replace_variable, latex_text)
    result = re.sub(pattern_varlist, replace_variable_list, result)
    return result

# Ejemplo de uso:
if __name__ == "__main__":
    listdir=os.listdir("syllabi_json")
    print(listdir)
    # Archivo LaTeX de ejemplo
    with open('plantilla.tex', 'r',  encoding="utf-8") as file:
        latex_text = file.read()

    for arch in listdir:
        # Cargamos las variables desde el archivo JSON
        with open("syllabi_json/"+arch, 'r',  encoding="utf-8") as json_file:
            variables = json.load(json_file)


        # Realizar el reemplazo de las variables
        result_latex = replace_variables_in_latex(latex_text, variables)

        # Guardar el resultado en otro archivo
        with open("syllabi_tex/"+arch[:-4]+".tex", 'w',  encoding="utf-8") as file:
            file.write(result_latex)

        print("Reemplazo de variables completado.")
