import flet as ft

from database.dao import DAO


class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model

    def ottieni_ruoli(self):
        ruoli=DAO.get_authorship()
        return ruoli

    def handle_crea_grafo(self, e):
        try:
            ruolo=self._view.dd_ruolo.value

            self._model.build_graph(ruolo)
            self._view.list_risultato.controls.append(ft.Text(f"{self._model.G.number_of_nodes()}"))
            self._view.list_risultato.controls.append(ft.Text(f"{self._model.G.number_of_edges()}"))
            self._view.btn_classifica.disabled = True

            for n in self._model.G.nodes():
                nome=self._model.G.node[n].name

                self._view.dd_iniziale.options.append(ft.dropdown.Option(key=str(n), text=str(nome)))

            self._view._page.update()
        except:
            self._view.show_alert("inserire un ruolo")

    def handle_classifica(self, e):

        for a, p in self._model.classifica:
            nome=self._model._map_nodi[a].name

            self._view.list_risultato.controls.append(ft.Text(f"{nome} {p}"))
            self._view._page.update()
