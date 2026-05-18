"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
def _leer_datos():
    with open("files/input/data.csv", "r", encoding="utf-8") as file:
        return [line.strip().split("\t") for line in file if line.strip()]
    

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    datos = _leer_datos()
    conteo = {}

    for fila in datos:
        elementos = fila[4].split(",")

        for elemento in elementos:
            clave = elemento.split(":")[0]
            conteo[clave] = conteo.get(clave, 0) + 1

    return dict(sorted(conteo.items()))
