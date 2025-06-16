# ejercicio3.py

from grafo import Grafo

def ejecutar_ejercicio3():
    print("===== Ejercicio 3: Conectividad y Caminos =====")
    # 1. Creamos el grafo y agregamos vértices
    grafo = Grafo()
    for v in ['A', 'B', 'C', 'D', 'E', 'F']:  # F queda desconectado
        grafo.agregar_vertice(v)

    # 2. Agregamos las aristas
    aristas = [
        ('A', 'B'),
        ('A', 'C'),
        ('B', 'D'),
        ('C', 'D'),
        ('D', 'E'),
    ]
    for u, v in aristas:
        grafo.agregar_arista(u, v)

    # 3. Probamos es_conexo y encontrar_camino
    print("¿Grafo es conexo?", grafo.es_conexo())
    print("Camino de A a E:", grafo.encontrar_camino('A', 'E'))
    print("Camino de A a G:", grafo.encontrar_camino('A', 'G'))  # G no existe
    print()  # línea en blanco para separar salidas

if __name__ == "__main__":
    ejecutar_ejercicio3()