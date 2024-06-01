
class Grafo:
    def __init__(self):
        self.grafo = {}
        self.n = None
        self.m = None

    def mostrar_grafo(self):
        print("\nVetor de Adjacência: ")
        for v in self.grafo:
            print(f"{v}: ", end="")
            for k in self.grafo[v]:
                print(f"{k} ", end="")
            print()

    def gerar_digrafo(self, lines):
        self.n = int(lines[0].split()[0])
        self.m = int(lines[0].split()[1])
        for v in range(self.n):
            self.grafo[v] = []
        i = 1
        while i <= self.m:
            u = int(lines[i].split()[0])
            v = int(lines[i].split()[1])
            p = int(lines[i].split()[2])
            self.grafo[u].append((v, p))
            i += 1

    def dijkstra(self, raiz):
        def menor_vertice():
            menor = d.index(max(d))
            for k in self.grafo.keys():
                if aberto[k] and d[k] < d[menor]:
                    menor = k
            return menor

        d = [9999 for _ in range(self.n)]
        pai = [-1 for _ in range(self.n)]
        aberto = [True for _ in range(self.n)]
        d[raiz], pai[raiz] = 0, raiz
        while True in aberto:
            menor = menor_vertice()
            aberto[menor] = False
            for tupla in self.grafo[menor]:
                # Verifique se tupla[0] está dentro do intervalo de índices válidos para d
                if tupla[0] < len(d) and d[tupla[0]] > d[menor] + tupla[1]:
                    d[tupla[0]] = d[menor] + tupla[1]
                    pai[tupla[0]] = menor
        caminho = []
        for i in range(self.n):
            caminho.append((d[i], pai[i]))
        return caminho


def main():
    grafo = Grafo()
    lines = list()
    with open('dijkstra_digrafo.txt', 'r') as file:
        lines = [line.strip() for line in file if line.strip()]
        file.close()
    grafo.gerar_digrafo(lines)
    grafo.mostrar_grafo()
    raiz = int(input("Informe a raiz...: "))
    if raiz in grafo.grafo.keys():
        caminho = grafo.dijkstra(raiz)
        print("===================")
        print(f"Caminho com raiz {raiz}: ")
        for i, tupla in enumerate(caminho):
            print(f"({tupla[1]},{i}): {tupla[0]}")


if __name__ == "__main__":
    main()