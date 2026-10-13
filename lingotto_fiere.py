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

                    if type(campi[4]) is int: # siamo davanti a uno stand con prese elettriche aggiuntive
                        num_prese = int(campi[4])
                        new_stand = StandPreseElettriche(codice, superficie, padiglione, prezzo, num_prese)

                    elif (type(campi[4]) is str) and (len(campi[4]) > 0): # siamo davanti a uno stand premium
                        posizione = campi[4]
                        new_stand = StandPremium(codice, superficie, padiglione, prezzo, posizione)

                    else:
                        new_stand = StandStandard(codice, superficie, padiglione, prezzo)

                    self.__lista_stand.append(new_stand)

            infile.close()
        except FileNotFoundError:
            raise FileNotFoundError

    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        stand_esiste = False
        espositore_esiste = False
        stand_disponibile = True

        for s in self.__lista_stand:
            if s.codice == codice_stand:
                stand_esiste = True
                break

        for e in self.__lista_espositori:
            if e.codice == codice_espositore:
                espositore_esiste = True
                break

        for a in self.__associazioni:
            if a.codice_stand == codice_stand and a.codice_espositore == codice_espositore:
                stand_disponibile = False
            elif a.codice_espositore == codice_espositore:
                stand_disponibile = False
            elif a.codice_stand == codice_stand:
                stand_disponibile = False

        if stand_esiste and espositore_esiste and stand_disponibile:
            pass
            # TODO


    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        # TODO

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        # TODO
