#math.ceil y sqr
import math

def media_aritmetica(datos):
    """
    Calcula la media aritmética de una lista de valores numéricos.
    
    Parámetros:
    datos (list): Lista de números.
    
    Salida:
    float: La media aritmética de la lista.
    """
    return sum(datos) / len(datos) if len(datos) > 0 else None

def mediana(datos):
    """
    Calcula la mediana de una lista de valores numéricos.
    
    Parámetros:
    datos (list): Lista de números.
    
    Salida:
    float: La mediana de la lista.
    """
    n = len(datos)
    if n == 0:
        return None
    datosOrdenados = sorted(datos)
    mitad = n // 2
    
    if n % 2 != 0:
        return datosOrdenados[mitad]
    else:
        return (datosOrdenados[mitad - 1] + datosOrdenados[mitad]) / 2

def percentiles(datos, PercentilDeseado):
    """
    Calcula el percentil deseado de una lista de valores numéricos.
    
    Parámetros:
    datos (list): Lista de números.
    percentil_deseado (float): Valor del percentil deseado (entre 0 y 100).
    
    Retorna:
    float: El valor del percentil deseado en la lista.
    """
    if not (0 <= PercentilDeseado <= 100):
        return None
    n = len(datos)
    if n == 0:
        return None
    datos_ordenados = sorted(datos)
    k = (PercentilDeseado / 100) * (n - 1)
    f = math.floor(k)
    c = math.ceil(k)
    
    if f == c:
        return datos_ordenados[int(k)]
    else:
        return datos_ordenados[f] + (k - f) * (datos_ordenados[c] - datos_ordenados[f]) 

def varianza(datos):
    """
    Calcula la varianza de una lista de valores numéricos.
    
    Parámetros:
    datos (list): Lista de números.
    
    Retorna:
    float: La varianza de la lista.
    """
    n = len(datos)
    if n == 0:
        return None
    media = media_aritmetica(datos)
    sumaCuadrados = sum((x - media) ** 2 for x in datos)
    return sumaCuadrados / n

def desviacionTipica(datos):
    """
    Calcula la desviación típica de una lista de valores numéricos.
    
    Parámetros:
    datos (list): Lista de números.
    
    Retorna:
    float: La desviación típica de la lista.
    """
    varianza = varianza(datos)
    return math.sqrt(varianza) if varianza is not None else None

def resumenEstadistico(datos):
    """
    Calcula un resumen estadístico de una lista de valores numéricos.
    
    El resumen incluye:
    - Media aritmética
    - Mediana
    - Mínimo
    - Máximo
    - Percentiles 25, 50 y 75
    - Varianza
    - Desviación típica
    
    Parámetros:
    datos (list): Lista de números.
    
    Retorna:
    dict: Diccionario con el resumen estadístico.
    """
    if len(datos) == 0:
        return None
    
    resumen = {
        "Media Aritmética": media_aritmetica(datos),
        "Mediana": mediana(datos),
        "Mínimo": min(datos),
        "Máximo": max(datos),
        "Percentil 25": percentil(datos, 25),
        "Percentil 50": percentil(datos, 50),
        "Percentil 75": percentil(datos, 75),
        "Varianza": varianza(datos),
        "Desviación Típica": desviacion_tipica(datos)
    }
    
    return resumen