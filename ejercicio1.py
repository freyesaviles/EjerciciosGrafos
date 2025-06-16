from grafo import Grafo

def ejecutar_ejercicio1():
    print("===== Ejercicio 1: Operaciones Básicas =====")
    grafo = Grafo()
    for v in ['A', 'B', 'C', 'D', 'E']:
        grafo.agregar_vertice(v)

    for u, v in [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E')]:
        grafo.agregar_arista(u, v)

    print("Vecinos de A:", grafo.obtener_vecinos('A'))
    print("Vecinos de D:", grafo.obtener_vecinos('D'))
    print("Vecinos de F:", grafo.obtener_vecinos('F'))  # No existe

    print("¿Existe arista A-C?", grafo.existe_arista('A', 'C'))
    print("¿Existe arista A-D?", grafo.existe_arista('A', 'D'))

    print("\nGrafo Dirigido:")
    g_dirigido = Grafo(es_dirigido=True)
    for u, v in [('X', 'Y'), ('Y', 'Z'), ('X', 'Z')]:
        g_dirigido.agregar_arista(u, v)

    print("Vecinos de X:", g_dirigido.obtener_vecinos('X'))
    print("Vecinos de Y:", g_dirigido.obtener_vecinos('Y'))
    print()