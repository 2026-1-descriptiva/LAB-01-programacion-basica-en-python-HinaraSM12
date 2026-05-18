"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
def _leer_datos():
    with open("files/input/data.csv", "r", encoding="utf-8") as file:
        return [line.strip().split("\t") for line in file if line.strip()]

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    datos = _leer_datos()
    suma = {}

    for fila in datos:
        letra = fila[0]
        valor = int(fila[1])
        suma[letra] = suma.get(letra, 0) + valor

    return sorted(suma.items())
