
class NodParcurgere:
    def __init__(self, info, g = 0, h = 0, parinte=None):
        self.info = info  # eticheta nodului, de exemplu: 0,1,2...
        self.parinte = parinte  # parintele din arborele de parcurgere
        self.g = g
        self.h = h
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

    def __init__(self, matrice, lista_h, start, scopuri):
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
                nodNou = NodParcurgere(info=i, g=nodCurent.g+self.matrice[nodCurent.info][i], h=self.estimeaza_h(i), parinte=nodCurent)
                if not nodNou.vizitat():
                    listaSuccesori.append(nodNou)
        return listaSuccesori

    def scop(self, infoNod):
        return infoNod in self.scopuri;

    def estimeaza_h(self, nod):
        return self.lista_h[nod]


m = [    
    [0, 3, 5, 10, 0, 0, 100],    
    [0, 0, 0, 4, 0, 0, 0],    
    [0, 0, 0, 4, 9, 3, 0],    
    [0, 3, 0, 0, 2, 0, 0],    
    [0, 0, 0, 0, 0, 0, 0],    
    [0, 0, 0, 0, 4, 0, 5],    
    [0, 0, 3, 0, 0, 0, 0],
]

start = 0
scopuri = [4, 6]
lista_h = [0, 1, 6, 2, 0, 3, 0]
gr = Graph(m, lista_h, start, scopuri)

def binSearch(listaNoduri, nodDeInsert, st, dr):
    mij = (st + dr) // 2

    if mij >= len(listaNoduri):
        return mij
    
    if mij < 0:
        return 0

    if st == dr:
        if listaNoduri[st].f < nodDeInsert.f:
            return dr + 1
        elif listaNoduri[st].f > nodDeInsert.f:
            return dr
        elif listaNoduri[dr].f == nodDeInsert.f:
            if listaNoduri[dr].g == nodDeInsert.g:
                return dr
        elif listaNoduri[dr].g > nodDeInsert.g:
                return dr + 1
        else:
            return dr - 1

    if listaNoduri[mij].f == nodDeInsert.f:
        if listaNoduri[mij].g == nodDeInsert.g:
            return mij
        elif listaNoduri[mij].g > nodDeInsert.g:
            return binSearch(listaNoduri, nodDeInsert, mij + 1, dr)
        else:
            return binSearch(listaNoduri, nodDeInsert, st, mij)
    elif listaNoduri[mij].f > nodDeInsert.f:
        return binSearch(listaNoduri, nodDeInsert, st, mij)
    else:
        return binSearch(listaNoduri, nodDeInsert, mij + 1, dr)



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
            print("Cost "+str(nodCurent.f))
            print("\n----------------\n")
            #input()
            nrSolutiiCautate -= 1
            if nrSolutiiCautate == 0:
                return
            
        for s in gr.succesori(nodCurent):
            indice = binSearch(c, s, 0, len(c) - 1)
            if indice == len(c):
                c.append(s)
            else:
                c.append(indice, s)

        c+=gr.succesori(nodCurent)

aStarSolMultiple(gr, nrSolutiiCautate=4)