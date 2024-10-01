import math

def mediaAritmetica(datos):
    """
    Calcula la media aritmética de una lista de valores numéricos.
    Definición:
    Tendencia central que se calcula sumando todos los valores de un conjunto de datos y dividiendo 
    la suma total entre el número total de elementos.
    
    Parámetros:
    datos (list): Es una Lista de números.
    
    Otros datos:
    Se utiliza 'len()' para obtener la longitud de elementos de la lista.
    Se utiliza 'sum()' para obtener la suma total de los elementos de la lista. 
    La excepción TypeError verifica que todos los elementos de la variable datos sean números.
    La excepción ZeroDivisionError: verifica si se intenta realizar una división entre cero.
    
    Salida:
    Tipo de dato Float.
    """
    try:
        return sum(datos) / len(datos)
    except ZeroDivisionError:
        print("Error: No se puede calcular la media de una lista vacía.")
    except TypeError:
        print("Error: La lista debe contener solo números.")

def mediana(datos):
    """
    Calcula la mediana de una lista de valores numéricos.
    
    Definición:
    Representa el valor central de un conjunto de datos cuando estos están ordenados.
    
    Parámetros:
    datos(list): Lista de números.
    se utiliza 'len()' para obtener la longitud de elementos.
    
    Otros datos:
    Se utiliza 'sorted()'para crear y devolver una nueva lista ordenada.
    Se utiliza 'len()' para obtener la longitud de elementos 
    La excepción IndexError comprueba que la variable datos no esté vacía.
    La excepción TypeError verifica que todos los elementos de la variable datos sean números.
    La excepción Exception se utiliza si ocurre un error genérico.
    
    Salida:
    Tipo de dato Float.
    """
    try:
        datosOrdenados = sorted(datos)
        num = len(datosOrdenados)
        mitad = num // 2

        if num % 2 != 0:
            return datosOrdenados[mitad]
        else:
            return (datosOrdenados[mitad - 1] + datosOrdenados[mitad]) / 2

    except IndexError:
        print("Error: La lista está vacía. No se puede calcular la mediana.")
    except TypeError:
        print("Error: Todos los elementos de la lista deben ser números.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


def percentil(datos, PercentilDeseado):
    """
    Calcula el percentil deseado de una lista de valores numéricos.
    
    Definición:
    Es una medida estadística que indica el valor por debajo del cual se encuentra un cierto porcentaje de los datos.
    
    Parámetros:
    datos (list): Lista de números.
    PercentilDeseado (float): Valor del percentil deseado (entre 0 y 100).
    
    Otros datos:
    math.floor()
    math.ceil()
    Se utiliza 'sorted()'para crear y devolver una nueva lista ordenada.
    se utiliza 'len()' para obtener la longitud de elementos 
    La excepción IndexError comprueba que la variable datos no esté vacía.
    La excepción TypeError verifica que todos los elementos de la variable datos sean números.
    La excepción Exception se utiliza si ocurre un error genérico.
    
    Salida:
    float: El valor del percentil deseado en la lista, o None si ocurre un error.
    """
    try:
        if not (0 <= PercentilDeseado <= 100):
            print("Error: El percentil deseado debe estar entre 0 y 100.")
            return None
        datosOrdenados= sorted(datos)
        posicionPercentil= (PercentilDeseado / 100) * (len(datosOrdenados) - 1)
        indiceInferior= math.floor(posicionPercentil)
        indiceSuperior= math.ceil(posicionPercentil)
        if indiceInferior == indiceSuperior:
            return datosOrdenados[int(posicionPercentil)]
        else:
            return datosOrdenados[indiceInferior] + (posicionPercentil - indiceInferior) * (datosOrdenados[indiceSuperior] - datosOrdenados[indiceInferior])
    except IndexError:
        print("Error: La lista está vacía. No se puede calcular el percentil.")
    except TypeError:
        print("Error: Todos los elementos de la lista deben ser números y el percentil debe ser un número.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

def varianza(datos):
    """
    Calcula la varianza de una lista de valores numéricos usando manejo de excepciones.
    
    Definición:
    La varianza es una medida que indica qué tan dispersos están los valores de una lista con respecto a su media.
    
    Parámetros:
    datos (list): Lista de números.
    
    Otros datos:
    Se utiliza 'sum()' para
    se utiliza 'len()' para obtener la longitud de elementos 
    La excepción IndexError comprueba que la variable datos no esté vacía.
    La excepción TypeError verifica que todos los elementos de la variable datos sean números.
    La excepción ZeroDivisionError: verifica si se intenta realizar una división entre cero.
    La excepción Exception se utiliza si ocurre un error genérico.
    
    Salida:
    float: La varianza de la lista, o None si ocurre un error.
    """
    try:
        media = mediaAritmetica(datos)
        sumaCuadrados = sum((num - media) ** 2 for num in datos)
        return sumaCuadrados / len(datos)
    except IndexError:
        print("Error: La lista está vacía. No se puede calcular la varianza.")
    except TypeError:
        print("Error: Todos los elementos de la lista deben ser números.")
    except ZeroDivisionError:
        print("Error: La lista está vacía. No se puede calcular la varianza.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

def desviacionTipica(datos):
    """
    Calcula la desviación típica de una lista de valores numéricos usando manejo de excepciones.
    
    Definición:
    La desviación típica es una medida de dispersión que indica qué tan dispersos están los valores con respecto a la media.
    
    Parámetros:
    datos (list): Lista de números.
    
    Otros datos:
    math.sqrt() se usa para calcular la raíz cuadrada de la varianza.
    
    Retorna:
    float: La desviación típica de la lista, o None si ocurre un error.
    """
    try:
        varianza = varianza(datos)
        if varianza is None:
            print("Error: No se puede calcular la desviación típica de una lista vacía o con datos incorrectos.")
        return math.sqrt(varianza)
    except TypeError:
        print("Error: Todos los elementos de la lista deben ser números.")
    except ValueError:
        print("Error: No se puede calcular la raíz cuadrada de un valor negativo.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

def resumenEstadistico(datos):
    """
    Calcula un resumen estadístico de una lista de valores numéricos.  
    -> Media aritmética
    -> Mediana
    -> Mínimo
    -> Máximo
    -> Percentiles 25, 50 y 75
    -> Varianza
    -> Desviación típica
    
    Parámetros:
    datos (list): Lista de números.
    
    Otros datos: 
    
    
    Salida:
    dict: Diccionario con el resumen estadístico.
    """
    if len(datos) == 0:
        return None
    else:
        resumen = {
            "Media Aritmética": mediaAritmetica(datos),
            "Mediana": mediana(datos),
            "Mínimo": min(datos),
            "Máximo": max(datos),
            "Percentil 25": percentil(datos, 25),
            "Percentil 50": percentil(datos, 50),
            "Percentil 75": percentil(datos, 75),
            "Varianza": varianza(datos),
            "Desviación Típica": desviacionTipica(datos)
        }
    
    return resumen