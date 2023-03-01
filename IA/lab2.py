class Nod:
    def __init__(self, informatie, parinte=None):
        self.informatie = informatie
        self.parinte = parinte
    
    def drumRadacina(self):
        drum = [self]
        nod = self
        while nod.parinte is not None:
            drum.append(nod.parinte)
            nod = nod.parinte
        drum.reverse()
        return drum
    
    def vizitat(self):
        return self.informatie in self.drumRadacina()
    
    def __repr__(self):
        return f"{self.informatie} ({'->'.join([nod.informatie for nod in self.drumRadacina()])})"
    
    def __str__(self):
        return str(self.informatie)

class Graf:
    def __init__(self, noduri, muchii, start, scopuri):
        self.noduri = noduri
        self.muchii = muchii
        self.start = start
        self.scopuri = scopuri
        
    def scop(self, informatie):
        # return informatie in self.scopuri
        return informatie[0] == 0 and informatie[1] == 0
    
    
    def succesori(self, nod):
        if nod.informatie[2]==1: #mal stang(initial)
            NCmal_curent = nod.informatie[0]
            NMmal_curent = nod.informatie[1]
            NCmal_opus = n - NCmal_curent

            return (NCmal_opus, NMmal_curent, 0)    
        else:
            return (nod.informatie[0], nod.informatie[1], 1) 

    def bfs(self):
        gasite = []
        coada = [Nod(self.start)]
        while coada and len(gasite) < NSOL:
            nod_curent = coada.pop(0)
            if self.scop(nod_curent.informatie):
                gasite.append(nod_curent)
            else:
                succesorii = self.succesori(nod_curent)
                for succesor in succesorii:
                    if not succesor.vizitat():
                        coada.append(succesor)
        return gasite
    
    def dfs_not_rec(self):
        stiva = [Nod(self.start)]
        solutii = []
        while stiva:
            nodCurent = stiva.pop()
            if self.scop(nodCurent.informatie):
                solutii.append(nodCurent)
                if len(solutii) == NSOL:
                    return solutii
            stiva.extend(self.succesori(nodCurent))
        return solutii

    def dfs_rec(self, nod, solutii, NSOL):
        if self.scop(nod.informatie):
            solutii.append(nod)
            NSOL -= 1
            if NSOL == 0:
                return
        
        for succesor in self.succesori(nod):
            if not succesor.vizitat():
                self.dfs_rec(succesor, solutii, NSOL)

                if NSOL == 0:
                    return
                
#1
file = open("input.txt", "r")

n = int(file.readline())
m = int(file.readline())

stareInit = (n, n, 1)
