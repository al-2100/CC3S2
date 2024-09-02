## Ejercicio 1 - Prueba de entrada

### Descripción
- Commits de la fase de desarrollo:
1. Para el primer commit se importó código pasado en C++ del curso Análisis y Diseño de Algoritmos
2. Para el segundo commit se eliminaron algunos archivos creados por error al iniciar el proyecto
3. Para el tercer commit se modificó main.cpp para pedir aristas y vertices, además de generar los pesos de forma aleatoria.
````cpp
// Función para inicializar las aristas aleatorias
void inicializarAristas(struct Grafo* grafo, bool flag) {
    srand(time(NULL));

    for (int i = 0; i < grafo->numAristas; i++) {
        int origen = rand() % grafo->numVertices; // Vértice origen aleatorio
        int destino, peso;
        do {
            destino = rand() % grafo->numVertices; // Evitar bucles
        } while (destino == origen);
        if (!flag) {
            peso = rand() % 100 + 1; // Peso aleatorio entre 1 y 100
        } else {
            peso = rand() % 200 - 100; // Peso aleatorio entre -100 y 100
        }

        grafo->aristas[i].origen = &grafo->vertices[origen];
        grafo->aristas[i].destino = &grafo->vertices[destino];
        grafo->aristas[i].peso = peso;
    }
}
````
````cpp
//Pedir el numero de vertices y aristas
    std::cout<<"Ingrese el numero de vertices: ";
    std::cin>>n;
    std::cout<<"Ingrese el numero de aristas: ";
    std::cin>>m;
````
4. Para el cuarto commit se creó README.md para la documentación y además se agregaron comentarios donde corresponda.

- Branch grafos-negativos:
1. Se crea la Branch grafos-negativos para permitir la implementación de grafos con aristas negativas.
2. Se hace merge con main branch
3. No hay conflictos al hacer merge con main branch

Queda pendiente que el programa pueda cambiar al algoritmo de Bellman-Ford para grafos con aristas negativas, pues Dijkstra no funciona en esos casos.

Otro punto de mejora sería la implementación de un menú para elegir entre los dos algoritmos. Además se puede implementar la programación orientada a objetos en vez de solo Structs.

Cambios:

````cpp
//Preguntar si se permiten aristas negativas
    std::cout<<"Desea permitir aristas negativas? (1: Si, 0: No): ";
    std::cin>>flag;
````

````cpp
// Función para inicializar las aristas aleatorias
void inicializarAristas(struct Grafo* grafo, bool flag) {
    srand(time(NULL));

    for (int i = 0; i < grafo->numAristas; i++) {
        int origen = rand() % grafo->numVertices; // Vértice origen aleatorio
        int destino, peso;
        do {
            destino = rand() % grafo->numVertices; // Evitar bucles
        } while (destino == origen);
        if (!flag) {
            peso = rand() % 100 + 1; // Peso aleatorio entre 1 y 100
        } else {
            peso = rand() % 200 - 100; // Peso aleatorio entre -100 y 100
        }

        grafo->aristas[i].origen = &grafo->vertices[origen];
        grafo->aristas[i].destino = &grafo->vertices[destino];
        grafo->aristas[i].peso = peso;
    }
}
````