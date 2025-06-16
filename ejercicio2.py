from grafo import Grafo

def ejecutar_ejercicio2():
    print("===== Ejercicio 2: Recorridos (BFS y DFS) =====")
    grafo = Grafo()
    for v in ['A', 'B', 'C', 'D', 'E', 'F']:  # F es desconexo
        grafo.agregar_vertice(v)
    for u, v in [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E')]:
        grafo.agregar_arista(u, v)

    print("BFS desde A:", grafo.bfs('A'))
    print("DFS desde A:", grafo.dfs('A'))
    print()