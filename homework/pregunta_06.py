"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
def _leer_datos():
    with open("files/input/data.csv", "r", encoding="utf-8") as file:
        return [line.strip().split("\t") for line in file if line.strip()]


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    datos = _leer_datos()
    valores = {}

    for fila in datos:
        elementos = fila[4].split(",")

        for elemento in elementos:
            clave, valor = elemento.split(":")
            valor = int(valor)

            if clave not in valores:
                valores[clave] = [valor, valor]
            else:
                if valor < valores[clave][0]:
                    valores[clave][0] = valor
                if valor > valores[clave][1]:
                    valores[clave][1] = valor

    return [(clave, valores[clave][0], valores[clave][1]) for clave in sorted(valores)]
