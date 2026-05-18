import flet as ft
from model.model import Model

class Controller:
    def __init__(self, view):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = Model()
        self._ddCodinsValue = None

    def handlePrintCorsiPD(self, e):
        pd = self._view._ddPD.value

        if pd is None:
            self._view.create_alert("Attenzione, selezionare un periodo didattico")
            self._view.update_page()
            return

        if pd == "I":
            pdInt = 1
        else:
            pdInt = 2

        corsiPD = self._model.getCorsiPD(pdInt)

        if len(corsiPD) == 0:
            self._view.txt_result.controls.append(ft.Text(f"Nessun corso trovato per il {pd} periodo didattico"))
            self._view.update_page()
            return

        self._view.txt_result.controls.append(ft.Text(f"Di seguito tutti i corsi del {pd} peridoo didattico"))

        for c in corsiPD:
            self._view.txt_result.controls.append(ft.Text(c))

        self._view.update_page()

    def handlePrintIscrittiCorsiPD(self, e):
        pd = self._view._ddPD.value

        if pd is None:
            self._view.create_alert("Attenzione, selezionare un periodo didattico")
            self._view.update_page()
            return

        if pd == "I":
            pdInt = 1
        else:
            pdInt = 2

        corsi = self._model.getCorsiPDwIscritti(pdInt)

        if len(corsi) == 0:
            self._view.txt_result.controls.append(ft.Text(f"Nessun corso trovato per il {pd} periodo didattico"))
            self._view.update_page()
            return

        self._view.txt_result.controls.append(
            ft.Text(f"Di seguito tutti i corsi del {pd} peridoo didattico con dettaglio iscritti"))

        for c in corsi:
            self._view.txt_result.controls.append(
                ft.Text(f"{c[0]} -- N Iscitti: {c[1]}"))

        self._view.update_page()

    def handlePrintIscrittiCodins(self, e):

        if self._ddCodinsValue is None:
            self._view.create_alert("Per favore selezionare un insegnamento.")
            self._view.update_page()
            return

        studenti = self._model.getStudentiCorso(self._ddCodinsValue.codins)

        if not len(studenti):
            self._view.txt_result.controls.append(ft.Text(
                "Nessuno studente iscritto a questo corso"
            ))
            self._view.update_page()
            return

        self._view.txt_result.controls.append(ft.Text(
            f"Di seguito gli studenti iscritti al corso {self._ddCodinsValue}")
        )

        for s in studenti:
            self._view.txt_result.controls.append(
                ft.Text(s)
            )

        self._view.update_page()

    def handlePrintCDSCodins(self, e):
        pass

    def fillddCodins(self):
        #for cod in self._model.getCodins():
        #    self._view._ddCodIns.options.append(ft.dropdown.Option(cod))
        for corso in self._model.getAllCorsi():
            self._view._ddCodIns.options.append(ft.dropdown.Option(
                key = corso.codins,
                data = corso,
                on_click = self._choiceDDCodins
            ))
            pass

    def _choiceDDCodins(self, e):
        self._ddCodinsValue = e.control.data
        print(self._ddCodinsValue)
