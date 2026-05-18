"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
def _leer_datos():
    with open("files/input/data.csv", "r", encoding="utf-8") as file:
        return [line.strip().split("\t") for line in file if line.strip()]


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    datos = _leer_datos()
    valores = {}

    for fila in datos:
        letra = fila[0]
        valor = int(fila[1])

        if letra not in valores:
            valores[letra] = [valor, valor]
        else:
            if valor > valores[letra][0]:
                valores[letra][0] = valor
            if valor < valores[letra][1]:
                valores[letra][1] = valor

    return [(letra, valores[letra][0], valores[letra][1]) for letra in sorted(valores)]
