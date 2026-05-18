"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
def _leer_datos():
    with open("files/input/data.csv", "r", encoding="utf-8") as file:
        return [line.strip().split("\t") for line in file if line.strip()]

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    datos = _leer_datos()
    return sum(int(fila[1]) for fila in datos)
