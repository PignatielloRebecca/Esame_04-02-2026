import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        self.G = nx.DiGraph()
        self.artists = []
        self._map_nodi={}

    def load_map_nodi(self, ruolo):
        for o in DAO.get_all_artista(ruolo):
            self._map_nodi[o.artist_id] = o
        return self._map_nodi

    def build_graph(self, role: str):
        lista_nodi=[]

        for id in self.load_map_nodi(role).keys():
            lista_nodi.append(id)
        self.G.add_nodes_from(lista_nodi)

        connesioni=DAO.get_all_connessioni(role)

        for a1, a2, peso in connesioni:
            self.G.add_edge(a1, a2, weight=peso)

        return self.G


    def classifica(self, nodo_iniziale):

        lista_artista=[]

        for vicino in self.G.neighbors(nodo_iniziale):
            somma=0
            for arco_out in self.G.out_edges(vicino, data=True):
                somma+=arco_out[2]['weight']
            for arco_in in self.G.in_edges(vicino, data=True):
                somma-=arco_in[2]['weight']

                lista_artista.append((vicino, somma))
        return lista_artista
