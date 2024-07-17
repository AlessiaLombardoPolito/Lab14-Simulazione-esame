import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_graph(self, e):
        self._view.txt_result.controls.clear()
        self._model.buildGraph()
        numNodi, numArchi = self._model.getDetailsGraph()
        self._view.txt_result.controls.append(ft.Text(f"Il grafo ha {numNodi} nodi e {numArchi} archi"))
        pesomin, pesomax = self._model.getPesoMax_min()
        self._view.txt_result.controls.append(ft.Text(f"Il peso minore è {pesomin} e il peso maggiore è {pesomax}"))
        self._view._page.update()

    def handle_countedges(self, e):


        valore = self._view.txt_name.value
        try :
            intd = float(valore)

        except ValueError:
            self._view.txt_result.controls.append(ft.Text(f"Il numero inserito non è un valore numerico"))
            self._view._page.update()

            return

        if (self._model.controllaSoglia(intd)):
            archiMinori, archiMaggiori = self._model.contaArchi(intd)
            self._view.txt_result.controls.append(ft.Text(f"Il numero di archi con peso minore della soglia è  {archiMinori}"))
            self._view.txt_result.controls.append(ft.Text(f"Il numero di archi con peso maggiore della soglia è  {archiMaggiori}"))
            self._view._page.update()

        else:
            self._view.txt_result.controls.append(ft.Text(f"Il valore inserito {valore} non è nel range consentito"))
            self._view._page.update()

    def handle_search(self, e):
        valore = self._view.txt_name.value
        try:
            intd = float(valore)

        except ValueError:
            self._view.txt_result.controls.append(ft.Text(f"Il numero inserito non è un valore numerico"))
            self._view._page.update()

            return
        if (self._model.controllaSoglia(intd)):
            percorso = self._model.cercaPercorso(intd)
            for p in percorso:
                self._view.txt_result.controls.append(ft.Text(f"{p}"))
        self._view._page.update()

