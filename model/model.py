import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._diGraph = nx.DiGraph()
        self._allChromosomes = DAO.getAllChromosomes()
        self._edges = DAO.getAllEdges()
        self._allGenes = DAO.getAllGenes()
        self.idMap = {}
        self._valMin = 0
        self._valMax = 0
        self._listaPesi = []


    def loadGenes(self):
        self._allGenes = DAO.getAllGenes()
        self.idMap = {}
        for g in self._allGenes:
            self.idMap[g.GeneID] = g.Chromosome

    def buildGraph(self):
        self._diGraph.clear()
        lista = []
        for chromosome in self._allChromosomes:
            lista.append(chromosome)
        self._diGraph.add_nodes_from(lista)
        self.loadGenes()


        for edge in self._edges:
            v1 = edge[0]
            v2 = edge[1]
            peso = edge[2]
            nodoP = self.idMap[v1]
            nodoA = self.idMap[v2]
            if (nodoP, nodoA) in self._diGraph.edges:
                self._diGraph[nodoP][nodoA]["weight"] += peso
            else:
                self._diGraph.add_edge(nodoP,nodoA, weight = peso)



    def getDetailsGraph(self):
        return self._diGraph.number_of_nodes(), self._diGraph.number_of_edges()

    def getPesoMax_min(self):
        self._listaPesi = []
        listaArchi= self._allChromosomes
        for i in listaArchi:
            for j in listaArchi:
                if (i,j) in self._diGraph.edges:
                    self._listaPesi.append(self._diGraph[i][j]["weight"])

        self._listaPesi.sort()
        self._valMin = self._listaPesi[0]
        self._valMax = self._listaPesi[-1]
        return self._listaPesi[0], self._listaPesi[-1]


    def controllaSoglia(self, d):
        if d>= self._valMin and d<= self._valMax:
            return True
        else: return False


    def contaArchi(self,d):
        archiMaggiori = 0
        archiMinori = 0
        for peso in self._listaPesi:
            if peso>=d:
                archiMaggiori += 1
            else:
                archiMinori += 1
        return archiMinori, archiMaggiori



    def cercaPercorso(self, valore):
        pass

    def ricorsione(self, parziale):
        pass
