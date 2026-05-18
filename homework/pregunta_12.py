"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
def _leer_datos():
    with open("files/input/data.csv", "r", encoding="utf-8") as file:
        return [line.strip().split("\t") for line in file if line.strip()]
    

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    datos = _leer_datos()
    resultado = {}

    for fila in datos:
        letra = fila[0]
        elementos = fila[4].split(",")

        if letra not in resultado:
            resultado[letra] = 0

        for elemento in elementos:
            valor = int(elemento.split(":")[1])
            resultado[letra] += valor

    return dict(sorted(resultado.items()))
