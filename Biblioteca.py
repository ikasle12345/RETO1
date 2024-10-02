import math

class EstadisticaDescriptiva:
    """
    Clase para realizar cálculos de estadísticas descriptivas sobre listas de datos numéricos.
    
    Descripción:
    Esta clase ofrece métodos para calcular las principales métricas estadísticas utilizadas en el análisis de datos.
    Entre las métricas que se pueden calcular están la media aritmética, la mediana, los percentiles, la varianza y la desviación típica.
    También proporciona un método para obtener un resumen estadístico completo de un conjunto de datos.

    Funcionalidades:
    - **mediaAritmetica**: Calcula el promedio de una lista de valores.
    - **mediana**: Encuentra el valor que divide el conjunto de datos en dos partes iguales.
    - **percentil**: Obtiene el valor por debajo del cual se encuentra un porcentaje dado de los datos.
    - **varianza**: Mide la dispersión de los valores respecto a la media aritmética.
    - **desviacionTipica**: Calcula la raíz cuadrada de la varianza, indicando qué tan dispersos están los valores respecto a la media.
    - **resumenEstadistico**: Devuelve un diccionario con todas las métricas calculadas.

    Uso:
    Esta clase está diseñada para ser utilizada con listas de valores numéricos. No se recomienda usarla con listas vacías o con valores no numéricos.
    Cada método incluye manejo de excepciones para evitar errores de tipo y de índices.
    """
    def mediaAritmetica(self, datos):
        """
        Calcula la media aritmética de una lista de valores numéricos.
        Definición:
        Tendencia central que se calcula sumando todos los valores de un conjunto de datos y dividiendo 
        la suma total entre el número total de elementos.
        
        Parámetros:
        datos: Lista de números.
        
        Otros datos:
        Se utiliza 'len()' para obtener la longitud de elementos de la lista.
        Se utiliza 'sum()' para obtener la suma total de los elementos de la lista. 
        La excepción 'TypeError' verifica que todos los elementos de la variable datos sean números.
        La excepción 'ZeroDivisionError': verifica si se intenta realizar una división entre cero.
        la excepción 'Exception' se utiliza si ocurre un error genérico.
        Salida:
        Tipo de dato Float.
        """
        if len(datos) == 0:
            return "El dato para la media se ha recibido vacío"
        return sum(datos) / len(datos)

    def mediana(self, datos):
        """
        Calcula la mediana de una lista de valores numéricos.
        Definición:
        Representa el valor central de un conjunto de datos cuando estos están ordenados.
        
        Parámetros:
        datos: Lista de números.
        
        Otros datos:
        Se utiliza 'sorted()'para crear y devolver una nueva lista ordenada.
        Se utiliza 'len()' para obtener la longitud de elementos.
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

    def percentil(self, datos, PercentilDeseado):
        """
        Calcula el percentil deseado de una lista de valores numéricos.
        Definición:
        Es una medida estadística que indica el valor por debajo del cual se encuentra un cierto porcentaje de los datos.
        
        Parámetros:
        datos: Lista de números.
        PercentilDeseado: Tipo de dato Float. Valor del percentil deseado (entre 0 y 100).
        
        Otros datos:
        Se utiliza 'sorted()' para crear y devolver una nueva lista ordenada.
        Se utiliza 'len()' para obtener la longitud de elementos.
        La excepción IndexError comprueba que la variable datos no esté vacía.
        La excepción TypeError verifica que todos los elementos de la variable datos sean números.
        La excepción Exception se utiliza si ocurre un error genérico.
        
        Salida:
        Tipo de dato Float.
        """
        try:
            if not (0 <= PercentilDeseado <= 100):
                print("Error: El percentil deseado debe estar entre 0 y 100.")
                return None
            
            # Ordenar la lista de datos
            datosOrdenados = sorted(datos)
            # Calcular la posición del percentil
            posicionPercentil = (PercentilDeseado / 100) * (len(datosOrdenados) - 1)
            
            # Usar int() en lugar de math.floor para el índice inferior
            indiceInferior = int(posicionPercentil)
            # Usar math.ceil para el índice superior
            indiceSuperior = math.ceil(posicionPercentil)
            
            # Si ambos índices son iguales, significa que estamos en una posición exacta
            if indiceInferior == indiceSuperior:
                return datosOrdenados[indiceInferior]
            else:
                # Interpolar entre los dos valores
                return datosOrdenados[indiceInferior] + (posicionPercentil - indiceInferior) * (datosOrdenados[indiceSuperior] - datosOrdenados[indiceInferior])
        
        except IndexError:
            print("Error: La lista está vacía. No se puede calcular el percentil.")
        except TypeError:
            print("Error: Todos los elementos de la lista deben ser números y el percentil debe ser un número.")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

    def varianza(self, datos):
        """
        Calcula la varianza de una lista de valores numéricos.
        Definición:
        La varianza es una medida que indica qué tan dispersos están los valores de una lista con respecto a su media.
        
        Parámetros:
        datos: Lista de números.
        
        Otros datos:
        Se utiliza 'sum()' para
        se utiliza 'len()' para obtener la longitud de elementos 
        La excepción IndexError comprueba que la variable datos no esté vacía.
        La excepción TypeError verifica que todos los elementos de la variable datos sean números.
        La excepción ZeroDivisionError: verifica si se intenta realizar una división entre cero.
        La excepción Exception se utiliza si ocurre un error genérico.
        
        Salida:
        Tipo de dato Float.
        """
        if len(datos) == 0:
            return None
        media = self.mediaAritmetica(datos)
        sumaCuadrados = sum((num - media) ** 2 for num in datos)
        return sumaCuadrados / len(datos)

    def desviacionTipica(self, datos):
        """
        Calcula la desviación típica de una lista de valores numéricos usando manejo de excepciones.
        Definición:
        La desviación típica es una medida de dispersión que indica qué tan dispersos están los valores con respecto a la media.

        Parámetros:
        datos (list): Lista de números.

        Otros datos:
        math.sqrt() se usa para calcular la raíz cuadrada de la varianza.

        Retorna:
        Tipo de dato Float.
        """

        varianza = self.varianza(datos)
        if varianza is None:
            print("Error: No se puede calcular la desviación típica de una lista vacía o con datos incorrectos.")
            return None
        return math.sqrt(varianza)

    def resumenEstadistico(self, datos):
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
        datos: Lista de números.
        
        Salida:
        Diccionario con el resumen estadístico.
        """

        if len(datos) == 0:
            return None
        return {
            "Media Aritmética": self.mediaAritmetica(datos),
            "Mediana": self.mediana(datos),
            "Mínimo": min(datos),
            "Máximo": max(datos),
            "Percentil 25": self.percentil(datos, 25),
            "Percentil 50": self.percentil(datos, 50),
            "Percentil 75": self.percentil(datos, 75),
            "Varianza": self.varianza(datos),
            "Desviación Típica": self.desviacionTipica(datos)
        }
