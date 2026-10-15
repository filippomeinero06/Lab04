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
        self.__associazioni = [] # lista di oggetti di tipo Associazione

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
                campi = line.strip().split(",")

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
                        try:
                            num_prese = int(campi[4])
                            new_prezzo = prezzo * (1 + 0.07 * num_prese)
                            new_stand = StandPreseElettriche(codice, superficie, padiglione, new_prezzo, num_prese)
                        except ValueError:
                            posizione = campi[4]
                            new_prezzo = prezzo * 1.30
                            new_stand = StandPremium(codice, superficie, padiglione, new_prezzo, posizione)
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

        for s in self.__lista_stand:
            if s.codice == codice_stand:
                stand = s
                stand_esiste = True
                if s.codice_espositore is None:
                    stand_disponibile = True
            if s.codice_espositore == codice_espositore:
                espositore_libero = False

        for e in self.__lista_espositori:
            if e.codice == codice_espositore:
                espositore_esiste = True
                break



        if stand_esiste:
            if espositore_esiste:
                if stand_disponibile:
                    if espositore_libero:
                        stand.codice_espositore = codice_espositore
                    else:
                        raise Exception(f"L'espositore {codice_espositore} è già in uno stand")
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

            for s in self.__lista_stand:
                if s == e: # vuol dire che l'espositore è associato a quello stand
                    print(f" | {s.__str__()}", end="")
                    break
            print()

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        stand_ordinati = []

        for s in self.__lista_stand:
            posizione = 0
            while posizione < len(stand_ordinati) and stand_ordinati[posizione] < s:
                posizione += 1
            stand_ordinati.insert(posizione, s)

        return stand_ordinati
