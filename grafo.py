from collections import deque

class Grafo:
    def __init__(self, es_dirigido=False):
        self.es_dirigido = es_dirigido
        self.vertices = {}

    def agregar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = []

    def agregar_arista(self, u, v, peso=1):
        if u not in self.vertices:
            self.agregar_vertice(u)
        if v not in self.vertices:
            self.agregar_vertice(v)
        self.vertices[u].append((v, peso))
        if not self.es_dirigido:
            self.vertices[v].append((u, peso))

    def obtener_vecinos(self, vertice):
        return [vecino for vecino, _ in self.vertices.get(vertice, [])]

    def existe_arista(self, u, v):
        return any(vecino == v for vecino, _ in self.vertices.get(u, []))

    def bfs(self, inicio):
        visitados = set()
        cola = deque([inicio])
        resultado = []

        while cola:
            actual = cola.popleft()
            if actual not in visitados:
                visitados.add(actual)
                resultado.append(actual)
                for vecino in self.obtener_vecinos(actual):
                    if vecino not in visitados:
                        cola.append(vecino)
        return resultado

    def dfs(self, inicio):
        visitados = set()
        resultado = []

        def dfs_rec(v):
            visitados.add(v)
            resultado.append(v)
            for vecino in self.obtener_vecinos(v):
                if vecino not in visitados:
                    dfs_rec(vecino)

        if inicio in self.vertices:
            dfs_rec(inicio)
        return resultado

    def es_conexo(self):
        if not self.vertices:
            return True
        inicio = next(iter(self.vertices))
        return len(self.bfs(inicio)) == len(self.vertices)

    def encontrar_camino(self, inicio, fin):
        if inicio not in self.vertices or fin not in self.vertices:
            return []

        from collections import deque
        visitados = set()
        cola = deque([inicio])
        padre = {inicio: None}

        while cola:
            actual = cola.popleft()
            if actual == fin:
                break
            for vecino in self.obtener_vecinos(actual):
                if vecino not in visitados and vecino not in cola:
                    padre[vecino] = actual
                    cola.append(vecino)
            visitados.add(actual)

        # reconstruir camino si se encontró
        if fin not in padre:
            return []

        camino = []
        actual = fin
        while actual is not None:
            camino.append(actual)
            actual = padre[actual]
        camino.reverse()
        return camino