# Proyecto de Grafos en Python (POO)

Este proyecto implementa una estructura de **grafo** en Python utilizando **Programación Orientada a Objetos (POO)**. Está dividido en tres ejercicios principales:

1. Construcción y operaciones básicas de grafos.
2. Recorridos: BFS y DFS.
3. Conectividad y búsqueda de rutas.

## Estructura del Proyecto

```
📁 grafo-proyecto/
├── grafo.py             # Clase principal Grafo con todos los métodos
├── ejercicio1.py        # Construcción del grafo y operaciones básicas
├── ejercicio2.py        # Recorridos BFS y DFS
├── ejercicio3.py        # Conectividad y caminos
├── main.py              # Archivo principal que ejecuta los ejercicios
└── README.md            # Documentación del proyecto
```

---

## 1. Clase Grafo (`grafo.py`)

La clase `Grafo` permite crear grafos dirigidos o no dirigidos y soporta aristas ponderadas.

### Métodos principales

- `__init__(es_dirigido=False)`: Inicializa el grafo. Usa un diccionario para representar los vértices y sus vecinos.
- `agregar_vertice(vertice)`: Añade un vértice al grafo si no existe.
- `agregar_arista(u, v, peso=1)`: Conecta los vértices `u` y `v`. Agrega automáticamente los vértices si no existen.
- `obtener_vecinos(vertice)`: Devuelve la lista de vecinos de un vértice.
- `existe_arista(u, v)`: Verifica si hay una arista entre `u` y `v`.
- `bfs(inicio)`: Implementa **búsqueda en amplitud (BFS)** desde un vértice inicial.
- `dfs(inicio)`: Implementa **búsqueda en profundidad (DFS)** desde un vértice inicial.
- `es_conexo()`: Verifica si el grafo no dirigido es conexo.
- `encontrar_camino(inicio, fin)`: Encuentra un camino entre dos vértices usando BFS y reconstrucción de ruta.

---

## 2. Ejercicio 1 - Operaciones Básicas (`ejercicio1.py`)

- Se crea una instancia de grafo **no dirigido**.
- Se agregan vértices y aristas.
- Se imprime la lista de vecinos de varios vértices.
- Se verifica la existencia de aristas.
- También se crea un **grafo dirigido** con diferentes aristas.

---

## 3. Ejercicio 2 - Recorridos (`ejercicio2.py`)

- Se ejecuta un **recorrido BFS** desde el vértice `'A'`.
- Se ejecuta un **recorrido DFS** desde `'A'`.
- Se agrega un vértice desconectado `'F'` para probar casos no conectados.

---

## 4. Ejercicio 3 - Conectividad y Caminos (`ejercicio3.py`)

- Se verifica si el grafo es **conexo**.
- Se encuentra un camino entre `'A'` y `'E'`.
- También se prueba encontrar un camino a un vértice inexistente para validar errores.

---

## 5. Uso del programa (`main.py`)

El archivo `main.py` importa y ejecuta los tres ejercicios en orden:

```bash
python main.py
```

Muestra por consola los resultados de todos los métodos implementados en la clase `Grafo`.

---

## Requisitos

- Python 3.7 o superior

---

## Ejemplo de salida esperada

```text
===== Ejercicio 1: Construcción y operaciones básicas =====
Vecinos de A: ['B', 'C']
Vecinos de D: ['B', 'C', 'E']
Vecinos de F: []
¿Existe arista A-C? True
¿Existe arista A-D? False

===== Ejercicio 2: Recorridos BFS y DFS =====
BFS desde A: ['A', 'B', 'C', 'D', 'E']
DFS desde A: ['A', 'B', 'D', 'C', 'E']

===== Ejercicio 3: Conectividad y Caminos =====
¿Grafo es conexo? False
Camino de A a E: ['A', 'B', 'D', 'E']
Camino de A a G: []
```

---

## Licencia

Este proyecto es de uso educativo. Puedes modificarlo libremente para aprender o ampliar la funcionalidad de grafos.
