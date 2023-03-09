# informatii despre un nod din arborele de parcurgere (nu nod din graful initial)
class NodParcurgere:
    def __init__(self, info, g=0, h=0, parinte=None):
        self.info = info  # eticheta nodului, de exemplu: 0,1,2...
        self.parinte = parinte  # parintele din arborele de parcurgere
        self.h = h
        self.g = g
        self.f = g + h

    def drumRadacina(self):
        l = []
        nod = self
        while nod:
            l.insert(0, nod)
            nod = nod.parinte
        return l


    def vizitat(self): #verifică dacă nodul a fost vizitat (informatia lui e in propriul istoric)
        nodDrum = self.parinte
        while nodDrum:
            if (self.info == nodDrum.info):
                return True
            nodDrum = nodDrum.parinte

        return False

    def __str__(self):
        return str(self.info)
    def __repr__(self):
        sir = str(self.info) + "("
        drum = self.drumRadacina()
        sir += ("->").join([str(n.info) for n in drum])
        sir += ")"
        return sir


class Graph:  # graful problemei

    def __init__(self, matrice, start, scopuri, lista_h):
        self.matrice = matrice
        self.nrNoduri = len(matrice)
        self.start = start  # informatia nodului de start
        self.scopuri = scopuri  # lista cu informatiile nodurilor scop
        self.lista_h = lista_h


    # va genera succesorii sub forma de noduri in arborele de parcurgere
    def succesori(self, nodCurent):
        listaSuccesori = []
        for i in range(self.nrNoduri):
            if self.matrice[nodCurent.info][i] != 0:
                nodNou = NodParcurgere(info=i, g=nodCurent.g + self.matrice[nodCurent.info][i], h=self.estimeaza_h(i), parinte=nodCurent)
                if not nodNou.vizitat():
                    listaSuccesori.append(nodNou)
        return listaSuccesori

    def scop(self, infoNod):
        return infoNod in self.scopuri

    def estimeaza_h(self, nod):
        return self.lista_h[nod]



##############################################################################################
#                                 Initializare problema                                      #
##############################################################################################

m = [
    [0, 3, 5, 10, 0, 0, 100],
    [0, 0, 0, 4, 0, 0, 0],
    [0, 0, 0, 4, 9, 3, 0],
    [0, 3, 0, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 4, 0, 5],
    [0, 0, 3, 0, 0, 0, 0]
]

start = 0
scopuri = [4, 6]
lista_h = [0, 1, 6, 2, 0, 3, 0]
gr = Graph(m, start, scopuri, lista_h)

def bin_search(listaNoduri, nodDeInserat, ls, ld):
    mij = (ls + ld) // 2
    if mij >= len(listaNoduri):
        return mij
    if mij < 0:
        return 0
    if ls == ld:
        if listaNoduri[ls].f < nodDeInserat.f:
            return ls + 1
        elif listaNoduri[ls].f > nodDeInserat.f:
            return ls
        elif listaNoduri[ls].f == nodDeInserat.f:
            if listaNoduri[ls].g == nodDeInserat.g:
                return ls
            elif listaNoduri[ls].g > nodDeInserat.g:
                return ls + 1
            else:
                return ls

    if listaNoduri[mij].f == nodDeInserat.f:
        if listaNoduri[mij].g == nodDeInserat.g:
            return mij
        elif listaNoduri[mij].g > nodDeInserat.g:
            return bin_search(listaNoduri, nodDeInserat, mij + 1, ld)
        else:
            return bin_search(listaNoduri, nodDeInserat, ls, mij)
    elif listaNoduri[mij].f > nodDeInserat.f:
        return bin_search(listaNoduri, nodDeInserat, ls, mij)
    else:
        return bin_search(listaNoduri, nodDeInserat, mij + 1, ld)


def aStarSolMultiple(gr, nrSolutiiCautate=1):
    # in coada vom avea doar noduri de tip NodParcurgere (nodurile din arborele de parcurgere)
    c = [NodParcurgere(gr.start, 0, gr.estimeaza_h(gr.start))]

    while len(c) > 0:
        #print("Coada actuala: " + str(c))
        #input()
        nodCurent = c.pop(0)

        if gr.scop(nodCurent.info):
            print("Solutie:")
            drum = nodCurent.drumRadacina()
            print(("->").join([str(n.info) for n in drum]))
            print("Cost " + str(nodCurent.g))
            print("\n----------------\n")
            #input()
            nrSolutiiCautate -= 1
            if nrSolutiiCautate == 0:
                return
        # [2, 5, 7, 8, 10, 14]
        for s in gr.succesori(nodCurent):
            indice = bin_search(c, s, 0, len(c) - 1)
            if indice == len(c):
                c.append(s)
            else:
                c.insert(indice, s)


#### algoritm BF
# presupunem ca vrem mai multe solutii (un numar fix) prin urmare vom folosi o variabilă numită nrSolutiiCautate
# daca vrem doar o solutie, renuntam la variabila nrSolutiiCautate
# si doar oprim algoritmul la afisarea primei solutii

def breadth_first(gr, nrSolutiiCautate=1):
    # in coada vom avea doar noduri de tip NodParcurgere (nodurile din arborele de parcurgere)
    c = [NodParcurgere(gr.start)]

    while len(c) > 0:
        #print("Coada actuala: " + str(c))
        #input()
        nodCurent = c.pop(0)

        if gr.scop(nodCurent.info):
            print("Solutie:")
            drum = nodCurent.drumRadacina()
            print(("->").join([str(n.info) for n in drum]))
            print("\n----------------\n")
            #input()
            nrSolutiiCautate -= 1
            if nrSolutiiCautate == 0:
                return
        c+=gr.succesori(nodCurent)


def depth_first(gr, nrSolutiiCautate=1):
    # vom simula o stiva prin relatia de parinte a nodului curent
    df(NodParcurgere(gr.start), nrSolutiiCautate)


def df(nodCurent, nrSolutiiCautate):
    if nrSolutiiCautate <= 0:  # testul acesta s-ar valida doar daca in apelul initial avem df(start,if nrSolutiiCautate=0)
        return nrSolutiiCautate
    #print("Stiva actuala: " + repr(nodCurent.drumRadacina()))
    #input()
    if gr.scop(nodCurent.info):
        print("Solutie: ", end="")
        drum = nodCurent.drumRadacina()
        print(("->").join([str(n.info) for n in drum]))
        print("\n----------------\n")
        #input()
        nrSolutiiCautate -= 1
        if nrSolutiiCautate == 0:
            return nrSolutiiCautate
    lSuccesori = gr.succesori(nodCurent)
    for sc in lSuccesori:
        if nrSolutiiCautate != 0:
            nrSolutiiCautate = df(sc, nrSolutiiCautate)

    return nrSolutiiCautate


# df(a)->df(b)->df(c)->df(f)
#############################################


def df_nerecursiv(nrSolutiiCautate):
    stiva = [NodParcurgere(gr.start)]
    #consider varful stivei in dreapta
    while stiva: #cat timp stiva nevida
        nodCurent=stiva.pop() #sterg varful
        if gr.scop(nodCurent.info):
            print("Solutie:")
            drum = nodCurent.drumRadacina()
            print(("->").join([str(n.info) for n in drum]))
            print("\n----------------\n")
            #input()
            nrSolutiiCautate -= 1
            if nrSolutiiCautate == 0:
                return
        stiva += gr.succesori(nodCurent)[::-1] #adaug in varf succesoii in ordine inversa deoarece vreau sa expandez primul succesor generat si trebuie sa il pun in varf


aStarSolMultiple(gr, nrSolutiiCautate=2)