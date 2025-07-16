import tkinter as tk

class Abaco:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Abaco Digitale")
        self.root.config(bg="#1E1E1E")
        self.root.geometry("800x650")

        # Nuovi nomi colonne e barre
        self.barre = {"1": 0, "U^1": 0, "U^2": 0, "U^3": 0, "U^4": 0, "U^5": 0, "U^6": 0, "U^7": 0, "U^8": 0, "U^9": 0}
        self.keys = list(self.barre.keys())

        # I valori vengono aggiornati in base alla base selezionata
        self.valori = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]
        self.valore_decimale = sum(self.barre[k] * v for k, v in zip(self.keys, self.valori))
        self.valore_binario = bin(self.valore_decimale)[2:]
        self.valore_esadecimale = hex(self.valore_decimale)[2:].upper()

        self.title()
        # crea il frame orizzontale sopra l'abaco
        self.frame_top = tk.Frame(self.root, bg="#1E1E1E")
        self.frame_top.pack(side=tk.TOP, fill=tk.X, padx=10, pady=1)

        self.seleziona_base()
        self.conta()
        self.vista_abaco()

    def title(self):
        self.frame_title = tk.Frame(self.root, bg="#1E1E1E")
        self.frame_title.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

        self.descrizione = tk.Label(self.frame_title, font=('Helvetica', 12), bg="#1E1E1E", fg="white",
                                    text=("- Utilizza i pulsanti per scegliere la base numerica tra binario (2), decimale (10) e esadecimale (16).\n"
                                        + "- Premi sulla base delle colonne per aumentare di 1 il conteggio di quella colonna.\n"
                                        + "- Sotto l'Abaco viene visualizzato il numero rispettivamente in binario, decimale ed esadecimale."))
        self.descrizione.pack()

    def cambia_base(self, base):
        self.base_corrente = base
        if base == 2:
            self.num_righe = 1
            base_valori = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
        elif base == 16:
            self.num_righe = 15
            base_valori = [1, 16, 256, 4096, 65536, 1048576, 16777216, 268435456, 4294967296, 68719476736]
        else:
            self.num_righe = 9
            base_valori = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]

        self.valori = base_valori
        nuovo_barre = {}
        resto = self.valore_decimale
        for k, v in reversed(list(zip(self.keys, base_valori))):
            nuovo_barre[k], resto = divmod(resto, v)
        self.barre = {k: nuovo_barre.get(k, 0) for k in self.keys}

        self.frame_abaco.destroy()
        self.vista_abaco()

    def seleziona_base(self):
        self.frame_select = tk.Frame(self.frame_top, bg="#1E1E1E")
        self.frame_select.pack(side=tk.RIGHT, padx=10, pady=1)

        self.base_numerica = [2, 10, 16]
        self.base_corrente = 10
        
        self.label_base = tk.Label(self.frame_select, text="Seleziona la base:", font=('Helvetica', 14, 'bold'), bg="#1E1E1E", fg="white")
        self.label_base.pack(side=tk.TOP)

        self.btn_binario = tk.Button(self.frame_select, text="2", width=3, font=('Helvetica', 16, 'bold'), bg="#333333", fg="white", relief="raised",
                                    command=lambda: self.cambia_base(2))
        self.btn_binario.pack(side=tk.LEFT, padx=10, pady=10)

        self.btn_decimale = tk.Button(self.frame_select, text="10", width=3, font=('Helvetica', 16, 'bold'), bg="#333333", fg="white", relief="raised",
                                      command=lambda: self.cambia_base(10))
        self.btn_decimale.pack(side=tk.LEFT, padx=10, pady=10)

        self.btn_esadecimale = tk.Button(self.frame_select, text="16", width=3, font=('Helvetica', 16, 'bold'), bg="#333333", fg="white", relief="raised",
                                         command=lambda: self.cambia_base(16))
        self.btn_esadecimale.pack(side=tk.LEFT, padx=10, pady=10)

        self.frame_reset = tk.Frame(self.frame_select, bg="#1E1E1E")
        self.frame_reset.pack(side=tk.LEFT, padx=20)

        self.btn_reset = tk.Button(self.frame_reset, text="Clear", width=6, font=('Helvetica', 14, 'bold'), bg="#FF4444", fg="white", relief="raised",
                                   command=self.reset_abaco)
        self.btn_reset.pack(padx=5, pady=5)

        if self.base_corrente == 2:
            self.num_righe = 1
        elif self.base_corrente == 16:
            self.num_righe = 15
        else:
            self.num_righe = 9

    def conta(self):
        if hasattr(self, "frame_counter"):
            self.frame_counter.destroy()
        self.frame_counter = tk.Frame(self.frame_top, bg="#1E1E1E")
        self.frame_counter.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=10, anchor="n")

        tk.Label(self.frame_counter, text=f"Decimale: {self.valore_decimale}", font=('Helvetica', 16), bg="#1E1E1E", fg="white").pack(anchor="center")
        tk.Label(self.frame_counter, text=f"Binario: {self.valore_binario}", font=('Helvetica', 16), bg="#1E1E1E", fg="white").pack(anchor="center")
        tk.Label(self.frame_counter, text=f"Esadecimale: {self.valore_esadecimale}", font=('Helvetica', 16), bg="#1E1E1E", fg="white").pack(anchor="center")

    def vista_abaco(self):
        self.frame_abaco = tk.Frame(self.root, bg="#1E1E1E", relief="solid", width=300, height=500)
        self.frame_abaco.pack(side=tk.TOP, padx=10, pady=10, anchor="center")  # rimosso fill=tk.BOTH, expand=True
        self.frame_abaco.pack_propagate(False)
        
        self.sfera_labels = {}

        max_height = 60

        for col in range(len(self.keys)):
            self.frame_abaco.grid_columnconfigure(col, weight=1)
        for row in range(self.num_righe + 2):
            self.frame_abaco.grid_rowconfigure(row, weight=0)

        # Creo gli spazi per le sfere
        for col, key in enumerate(self.keys):
            self.sfera_labels[key] = []
            for row in range(self.num_righe):
                spazio = tk.Frame(self.frame_abaco, width=10, height=max_height, border=2, bg="#636363", relief="solid")
                spazio.grid(row=row+1, column=col, sticky="nsew")
                spazio.grid_propagate(False)

                sfera = tk.Label(spazio, text= "", bg="#636363")
                sfera.pack(expand=True, fill=tk.BOTH)
                self.sfera_labels[key].append(sfera)

        # Aggiungo la base delle colonne con le rispettive labels
        for col, key in enumerate(self.keys):
            btn_base = tk.Button(self.frame_abaco, text=key, width=5, font=('Helvetica', 16, 'bold'), bg="#444", bd=2, relief="solid",
                                command=lambda k=key: self.aggiungi(k))
            btn_base.grid(row= self.num_righe+1 , column=col, sticky="nsew")
            btn_base.grid_propagate(False)

        self.aggiorna_sfere()

    def aggiungi(self, colonna):
        idx = self.keys.index(colonna)
        max_righe = self.num_righe
        # Aggiungi una sfera nella colonna
        if self.barre[colonna] < max_righe:
            self.barre[colonna] += 1
        else:
            self.barre[colonna] = 0
            # Se non è l'ultima colonna, aggiungi a quella a destra
            if idx < len(self.keys) - 1:
                self.aggiungi(self.keys[idx + 1])
        self.aggiorna_sfere()

    def aggiorna_sfere(self):
        self.valore_decimale = sum(self.barre[k] * v for k, v in zip(self.keys, self.valori))
        self.valore_binario = bin(self.valore_decimale)[2:]
        self.valore_esadecimale = hex(self.valore_decimale)[2:].upper()

        self.colori_colonne = {
            "1": "#FFFFFF",
            "U^1": "#00BFFF",
            "U^2": "#32CD32",
            "U^3": "#EDFF27",
            "U^4": "#FF8400",
            "U^5": "#FF0000",
            "U^6": "#FF0084",
            "U^7": "#9A00C5",
            "U^8": "#1500D5",
            "U^9": "#232323"
        } 

        for key in self.keys:
            n = self.barre[key]
            tot = len(self.sfera_labels[key])
            colore = self.colori_colonne.get(key, "#FFFFFF")

            for i, sfera in enumerate(self.sfera_labels[key]):
                if i >= tot - n:
                    sfera.config(text="", bg= colore)
                else:
                    sfera.config(text="", bg="#636363")
        
        self.conta()

    def reset_abaco(self):
        # Azzera tutte le colonne e aggiorna la vista
        self.barre = {k: 0 for k in self.keys}
        self.aggiorna_sfere()

if __name__ == "__main__":
    Abaco().root.mainloop()