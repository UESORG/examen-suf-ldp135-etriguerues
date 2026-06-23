import json


# =====================================================================
# 1. MÓDULO DE PERSISTENCIA Y VALIDACIÓN DE ÓRDENES
# =====================================================================
def importar_y_validar_orden(json_orden):
    """
    Decodifica una cadena JSON a diccionario, aplica cláusulas de guarda
    y captura excepciones de tiempo de ejecución de manera segura.
    """
    try:
        orden = json.loads(json_orden)

        # Cláusulas de guarda estructurales
        if "items" not in orden or "total" not in orden:
            raise KeyError("Estructura de datos incompleta: faltan llaves obligatorias.")

        # Validación semántica comercial
        if orden["total"] <= 0:
            raise ValueError("El monto total de la orden no puede ser menor o igual a cero.")

        return orden
    except (json.JSONDecodeError, KeyError, ValueError) as error:
        print(f"[M1][ERROR] Validación fallida: {error}")
        return None


# =====================================================================
# 2. MÓDULO DE HISTORIAL (ESTRUCTURA LIFO)
# =====================================================================
def gestionar_historial_carrito(historial_pila, accion, item=None):
    """
    Modifica una lista por referencia emulando una Pila (Stack).
    Soporta operaciones LIFO de inserción y extracción.
    """
    if accion == "AGREGAR" and item is not None:
        historial_pila.append(item)
        return historial_pila

    elif accion == "DESHACER":
        if not historial_pila:  # Control de subdesbordamiento de pila
            return None
        return historial_pila.pop()

    return historial_pila


# =====================================================================
# 3. MÓDULO DE LOGÍSTICA DE BODEGA (MATRICES)
# =====================================================================
def escanear_estanteria_bodega(matriz_bodega, fila_centro, col_centro):
    """
    Analiza un entorno de 3x3 en una matriz bidimensional con
    mecanismos de prevención de desbordamientos de índice.
    """
    filas = len(matriz_bodega)
    columnas = len(matriz_bodega[0]) if filas > 0 else 0
    items_encontrados = 0

    # Delimitación dinámica de rangos respetando los bordes de la matriz
    rango_filas_inicio = max(0, fila_centro - 1)
    rango_filas_fin = min(filas, fila_centro + 2)

    rango_cols_inicio = max(0, col_centro - 1)
    rango_cols_fin = min(columnas, col_centro + 2)

    for i in range(rango_filas_inicio, rango_filas_fin):
        for j in range(rango_cols_inicio, rango_cols_fin):
            if matriz_bodega[i][j] == 1:
                items_encontrados += 1

    return items_encontrados


# =====================================================================
# 4. MÓDULO DE FIDELIZACIÓN (ESTRUCTURAS JERÁRQUICAS Y RECURSIVIDAD)
# =====================================================================
def calcular_descuento_cascada(nodo_descuento):
    """
    Navega un árbol binario de decisión de cupones mediante recursividad,
    administrando correctamente la pila de ejecución.
    """
    # Caso Base: Nodo hoja encontrado con el beneficio final
    if "porcentaje_final" in nodo_descuento:
        return nodo_descuento["porcentaje_final"]

    # Caso Inductivo: Selección de caminos condicionales
    if nodo_descuento.get("cliente_frecuente") is True:
        return calcular_descuento_cascada(nodo_descuento["derecha"])
    else:
        return calcular_descuento_cascada(nodo_descuento["izquierda"])


# =====================================================================
# 5. MÓDULO DE ORDENAMIENTO EFICIENTE (ALGORITMIA DRY)
# =====================================================================
def ordenar_productos_quicksort(lista_items):
    """
    Ordena una lista de diccionarios por la clave 'precio' de menor a mayor.
    Complejidad temporal promedio: O(N log N).
    """
    if len(lista_items) <= 1:
        return lista_items

    # Selección de pivote en el punto medio de la colección
    pivote = lista_items[len(lista_items) // 2]["precio"]

    # Listas por comprensión (Abstracción DRY)
    menores = [producto for producto in lista_items if producto["precio"] < pivote]
    iguales = [producto for producto in lista_items if producto["precio"] == pivote]
    mayores = [producto for producto in lista_items if producto["precio"] > pivote]

    return ordenar_productos_quicksort(menores) + iguales + ordenar_productos_quicksort(mayores)


# =====================================================================
# 6. MÓDULO DE BÚSQUEDA DE CATÁLOGO (BÚSQUEDA BINARIA)
# =====================================================================
def buscar_precio_binario(lista_ordenada, precio_buscado):
    """
    Busca un precio objetivo en una lista ordenada usando división y conquista.
    Complejidad temporal: O(log N). Retorna el índice o -1 si no existe.
    """
    inicio = 0
    fin = len(lista_ordenada) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        precio_actual = lista_ordenada[medio]["precio"]

        if precio_actual == precio_buscado:
            return medio
        elif precio_actual < precio_buscado:
            inicio = medio + 1  # Descarte de la mitad izquierda
        else:
            fin = medio - 1  # Descarte de la mitad derecha

    return -1