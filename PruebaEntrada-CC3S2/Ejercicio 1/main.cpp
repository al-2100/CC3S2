#include <stdio.h>
#include <limits.h>
#include <stdlib.h>
#include <time.h>
#include <iostream>

#define MAX_VERTICES 6
#define MAX_ARISTAS 11

struct Vertice {
    int id;
    int distancia;
    struct Vertice* anterior;
};

struct Arista {
    struct Vertice* origen;
    struct Vertice* destino;
    int peso;
};

struct Grafo {
    int numVertices;
    int numAristas;
    struct Vertice vertices[MAX_VERTICES];
    struct Arista aristas[MAX_ARISTAS];
};

// Función para inicializar los vértices
void inicializarVertices(struct Grafo* grafo) {
    for (int i = 0; i < grafo->numVertices; i++) {
        grafo->vertices[i].id = i;
        grafo->vertices[i].distancia = INT_MAX;
        grafo->vertices[i].anterior = NULL;
    }
}

// Función para inicializar las aristas aleatorias
void inicializarAristas(struct Grafo* grafo) {
    srand(time(NULL));

    for (int i = 0; i < grafo->numAristas; i++) {
        int origen = rand() % grafo->numVertices;
        int destino;
        do {
            destino = rand() % grafo->numVertices;
        } while (destino == origen);

        int peso = rand() % 100 + 1;

        grafo->aristas[i].origen = &grafo->vertices[origen];
        grafo->aristas[i].destino = &grafo->vertices[destino];
        grafo->aristas[i].peso = peso;
    }
}

// Función para encontrar el vértice con la distancia mínima no procesado
struct Vertice* encontrarDistanciaMinima(struct Vertice* vertices, int numVertices, int* procesado) {
    int minDistancia = INT_MAX;
    struct Vertice* minVertice = NULL;
    for (int i = 0; i < numVertices; i++) {
        if (!procesado[i] && vertices[i].distancia < minDistancia) {
            minDistancia = vertices[i].distancia;
            minVertice = &vertices[i];
        }
    }
    return minVertice;
}

// Función para imprimir el camino desde el vértice inicial hasta un vértice destino
void imprimirCamino(struct Vertice* vertice) {
    if (vertice->anterior != NULL) {
        imprimirCamino(vertice->anterior);
    }
    printf("%d ", vertice->id);
}

// Función para implementar el algoritmo de Dijkstra
void algoritmoDijkstra(struct Grafo* grafo, struct Vertice* inicial) {
    inicial->distancia = 0;
    int procesado[MAX_VERTICES] = {0};

    for (int i = 0; i < grafo->numVertices; i++) {
        struct Vertice* u = encontrarDistanciaMinima(grafo->vertices, grafo->numVertices, procesado);
        if (u == NULL) break;
        procesado[u->id] = 1;

        for (int j = 0; j < grafo->numAristas; j++) {
            struct Arista* arista = &grafo->aristas[j];
            if (arista->origen == u) {
                struct Vertice* v = arista->destino;
                if (!procesado[v->id] && u->distancia != INT_MAX && u->distancia + arista->peso < v->distancia) {
                    v->distancia = u->distancia + arista->peso;
                    v->anterior = u;
                }
            }
        }
    }

    // Imprimir los resultados
    printf("Distancias y caminos desde el vertice inicial:\n");
    for (int i = 0; i < grafo->numVertices; i++) {
        printf("Vertice %d, Distancia: %d, Camino: ", grafo->vertices[i].id, grafo->vertices[i].distancia);
        imprimirCamino(&grafo->vertices[i]);
        printf("\n");
    }
}

int main() {
    int n, m;

    std::cout<<"Ingrese el numero de vertices: ";
    std::cin>>n;
    std::cout<<"Ingrese el numero de aristas: ";
    std::cin>>m;

    // Crear un grafo aleatorio n vértices y m aristas
    struct Grafo grafo = {n, m};

    // Inicializar los vértices y aristas
    inicializarVertices(&grafo);
    inicializarAristas(&grafo);

    // Ejecutar el algoritmo de Dijkstra desde el vértice 0
    algoritmoDijkstra(&grafo, &grafo.vertices[0]);

    return 0;
}
