import pytest
from carrito_pro import (
    importar_y_validar_orden,
    gestionar_historial_carrito,
    escanear_estanteria_bodega,
    calcular_descuento_cascada,
    ordenar_productos_quicksort,
    buscar_precio_binario
)

def test_m1_json_y_excepciones():
    orden_correcta = '{"id_orden": 8812, "items": 3, "total": 149.99}'
    res = importar_y_validar_orden(orden_correcta)
    assert res is not None
    assert res["id_orden"] == 8812
    assert importar_y_validar_orden('{"id_orden": 1, "items": 1, "total": -5.0}') is None
    assert importar_y_validar_orden('{"id_orden": 2, "total": 40.0}') is None

def test_m2_pila_referencia():
    historial = ["PROD_A", "PROD_B"]
    gestionar_historial_carrito(historial, "AGREGAR", "PROD_C")
    assert len(historial) == 3
    assert historial[-1] == "PROD_C"
    deshecho = gestionar_historial_carrito(historial, "DESHACER")
    assert deshecho == "PROD_C"
    assert len(historial) == 2

def test_m3_matriz_bodega():
    bodega = [[0, 1, 0], [1, 1, 0], [0, 0, 0]]
    assert escanear_estanteria_bodega(bodega, 1, 1) == 3
    assert escanear_estanteria_bodega(bodega, 0, 2) == 2

def test_m4_arbol_recursivo():
    arbol_cupones = {
        "cliente_frecuente": False,
        "izquierda": {
            "cliente_frecuente": True,
            "derecha": {"porcentaje_final": 15},
            "izquierda": {"porcentaje_final": 5}
        },
        "derecha": {"porcentaje_final": 30}
    }
    assert calcular_descuento_cascada(arbol_cupones) == 15

def test_m5_eficiencia_quicksort_y_binaria():
    items = [
        {"nombre": "A", "precio": 45.0},
        {"nombre": "B", "precio": 15.5},
        {"nombre": "C", "precio": 189.99}
    ]
    ordenados = ordenar_productos_quicksort(items)
    assert ordenados[0]["precio"] == 15.5
    assert buscar_precio_binario(ordenados, 45.0) == 1
    assert buscar_precio_binario(ordenados, 99.9) == -1