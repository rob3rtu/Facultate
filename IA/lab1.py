#1
class Nod:
    def __init__(self, informatie, parinte = None):
        self.informatie = informatie
        self.parinte = parinte

    def  __str__(self):
        return str(self.informatie)

    def __repr__(self):
        drum = self.drumRadacina()
        drum_str = "->".join([nod.informatie for nod in drum])
        return f"{self.informatie} ({drum_str})"

    def drumRadacina(self):
        nod = self
        drum = [nod]
        while nod.parinte is not None:
            drum.append(nod.parinte)
            nod = nod.parinte
        return list(reversed(drum))

    def vizitat(self):
        drum = self.drumRadacina()
        return self in drum

class Graf:
    def __init__(self, n, m, listaVecini, start, scop):
        self.n = n
        self.m = m
        self.listaVecini = listaVecini
        self.start = start
        self.scop = scop

    def scopf(self, informatieNod):
        return informatieNod in self.scop

    def succesori(self, nod):
        succesori = []
        for vecin in self.listaVecini[nod.informatie]: 
           succesori.append(vecin)
        return succesori

#2 BFS
NSOL = int(input("Cate solutii vrem? "))

g = Graf(4, 4, [[Nod(2, 1), Nod(1, 0)], [Nod(2, 0)], [Nod(3, 2)], []], Nod(0), [3])


def BFS(graf: Graf):
    coada = [graf.start]
    cnt = 0

    while len(coada) != 0:
        curent = coada.pop(0)
      
        if graf.scopf(curent.informatie):
            print(curent.drumRadacina())
            cnt += 1

            if cnt == NSOL:
                return

        vecini = graf.succesori(curent)

        for vecin in vecini:
            if not vecin.vizitat():
                coada.append(vecin)

    if cnt < NSOL:
        print("Atat s-a putut...", '\n')

BFS(g)