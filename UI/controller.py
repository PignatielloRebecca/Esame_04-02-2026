import flet as ft

from database.dao import DAO


class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model

    def handle_popola_dropdown(self):

        for o in DAO.get_authorship():
            pass


    def handle_crea_grafo(self, e):
        pass

    def handle_classifica(self, e):
        pass