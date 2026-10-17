from espositore import Espositore
from stand_standard import StandStandard
from stand_prese_elettriche import StandPreseElettriche
from stand_premium import StandPremium

class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self.__nome = nome
        self.__lista_stand = [] # lista di oggetti di tipo Stand
        self.__lista_espositori = [] # lista di oggetti di tipo Espositore

    """Aggiungere setter e getter se necessari"""
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome


    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        try:
            infile = open(file_path, "r")

            for line in infile:
                line = line.strip()
                if not line:  # salta le eventuali righe vuote
                    continue
                campi = line.split(",")

                codice = campi[0]
                if codice[:2] == "ES": # siamo davanti ad un espositore
                    nome = campi[1]
                    cognome = campi[2]

                    new_espositore = Espositore(codice, nome, cognome)

                    self.__lista_espositori.append(new_espositore)

                else: # siamo davanti a uno stand
                    superficie = int(campi[1])
                    padiglione = int(campi[2])
                    prezzo = float(campi[3])

                    if len(campi) > 4: # se c'è un valore di numero di prese o di posizione (se lo stand è speciale)
                        try:    # provo a trasformare in intero il valore che c'è in più in campi[4], se va a buon
                                # fine è uno stand con prese elettriche aggiuntive, se si solleva l'eccezione ValueError
                                # allora il valore non è un intero e di conseguenza sarà una stringa e quindi uno stand premium
                            num_prese = int(campi[4])
                            new_stand = StandPreseElettriche(codice, superficie, padiglione, prezzo, num_prese)
                        except ValueError:
                            posizione = campi[4]
                            new_stand = StandPremium(codice, superficie, padiglione, prezzo, posizione)
                    else:
                        new_stand = StandStandard(codice, superficie, padiglione, prezzo)

                    self.__lista_stand.append(new_stand)

            infile.close()
        except FileNotFoundError:
            raise

    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        stand_esiste = False
        espositore_esiste = False
        stand_disponibile = False
        espositore_libero = True

        stand = None # variabile usata nel for per salvarmi lo stand da associare all'espositore (inizializzata a None solo perché altrimenti era presente un warning alla riga 92)

        for s in self.__lista_stand:
            if s.codice == codice_stand: # se il codice combacia ho trovato lo stand da associare
                stand = s # mi memorizzo lo stand da associare
                stand_esiste = True
                if s.codice_espositore is None: # se quello stand da associare ha l'attributo codice_espositore ancora a None vuol dire che è libero
                    stand_disponibile = True
            if s.codice_espositore == codice_espositore: # se tra gli stand ne trovo uno che ha già associato l'espositore in questione, quell'espositore non può essere associato ad un altro stand
                espositore_libero = False

        for e in self.__lista_espositori:
            if e.codice == codice_espositore:
                espositore_esiste = True
                break

        if stand_esiste:
            if espositore_esiste:
                if stand_disponibile:
                    if espositore_libero:
                        stand.codice_espositore = codice_espositore # se tutte le condizioni sono soddisfatte avviene l'associazione tra lo stand e l'espositore
                    else:
                        raise Exception(f"L'espositore {codice_espositore} è già associato ad un altro stand")
                else:
                    raise Exception(f"Lo stand {codice_stand} è già occupato")
            else:
                raise Exception(f"L'espositore {codice_espositore} non esiste")
        else:
            raise Exception(f"Lo stand {codice_stand} non esiste")


    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        for e in self.__lista_espositori:
            print(e.__str__(), end="")

            for s in self.__lista_stand: # per ogni espositore scorro tutti gli stand per vedere se ce ne uno associato a quell'espositore
                if s == e: # vuol dire che l'espositore è associato a quello stand
                    print(f" | {s.__str__()}", end="")
                    break
            print()

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        stand_ordinati = []

        for s in self.__lista_stand:
            posizione = 0
            while posizione < len(stand_ordinati) and stand_ordinati[posizione] < s: # finché non arrivo alla fine della lista e finché lo stand nella posizione in cui mi trovo nella lista ha un prezzo minore dello stand in questione (quello del ciclo for) continuo a scorrere in avanti (a incrementare la posizione di 1)
                posizione += 1
            # quando trovo uno stand con un prezzo maggiore dello stand in questione, aggiungo lo stand in questione nella lista, nella posizione precedente allo stand che aveva il prezzo maggiore
            stand_ordinati.insert(posizione, s)

        return stand_ordinati
