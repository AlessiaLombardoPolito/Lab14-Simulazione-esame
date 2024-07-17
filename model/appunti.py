"""per accedere al valore di un DD
        forma = self._view.ddshape.value


per accedere ad un text
        dTOTtxt = self._view._txtInSoglia.value


per riempire un dd
        for year in anni:
            self._view.ddyear.options.append(ft.dropdown.Option(f"{year}"))


per riempire la listview
        self._view.txt_result.controls.append(ft.Text(f"Soglia inserita non valida. Inserire un intero. "))


per pulire la listview
            self._view._txt_result.controls.clear()


per pulire il grafo
        self._grafo.clear()


per controllare il dato inserito
       try:
            dTOT = int(dTOTtxt)
       except ValueError:
            warnings.warn("Soglia not integer.")
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text(f"Soglia inserita non valida. Inserire un intero. "))
            return


       try:
            intd = float(valore)

       except ValueError:
            self._view.txt_result.controls.append(ft.Text(f"Il numero inserito non è un valore numerico"))
            self._view._page.update()

            """