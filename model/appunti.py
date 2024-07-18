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


componente connessa di un grafo non orientato:
    def getConnessa(self, v0int):
        v0 = self._idMap[v0int]

        #slz 1 : successori di v0 in dfs
        successors = nx.dfs_successors(self._grafo, v0) #restituisce dizionario dei successori in una dfs
        allSuccessors = []
        for v in successors.values():
            allSuccessors.extend(v)


        #slz 2 : predecessori di v0 in dfs
        predecessors = nx.dfs_predecessors(self._grafo, v0)


        #slz 3 : conto i nodi dell'albero di visita del dfs
        albero = nx.dfs_tree(self._grafo, v0)

        #slz4 : node_connected_components
        connComp = nx.node_connected_component(self._grafo, v0)

        #il 3 e il 4 contengono anche il nodo di partenza, mentre il 2 e l'1 non lo contengono





eventi on action
self._ddAnno = ft.Dropdown(label="Anno", width=200, alignment=ft.alignment.top_left,
                                   on_change=self._controller.handleDDYearSelection)
       # nella consegna c'è
        # scritto intercettando l’evento onAction, quindi in questo menù scriviamo on_change che cambia risultato
        # ogni volta che cambio il contenuto della tendina, ed essendo un evento nel
        # controller poi mettiamo la e




Alla pressione del bottone “Test Connessione”:
• verificare se è possibile raggiungere l’aeroporto di arrivo a partire da quello di partenza;
• stampare un possibile percorso (se esiste) tra i due aeroporti.

    def esistePercorso(self,v0,v1):
        connessa = nx.node_connected_component(self._grafo, v0)
        if v1 in connessa:
            return True
        else:
            return False



Permettere all’utente di selezionare,
dall’apposita tendina, un album a1 tra quelli
presenti nel grafo. Alla pressione del bottone
“Analisi Componente”, si stampino:
• la dimensione della componente connessa a cui appartiene a1;
• la durata complessiva (in minuti) di tutti gli album appartenenti alla componente connessa di a1.

    def getConnessaDetails(self, v0):
        conn = nx.node_connected_component(self._graph, v0)
        durataTOT = 0
        for album in conn:
            durataTOT += toMinutes(album.totD)

        return len(conn), durataTOT"""

