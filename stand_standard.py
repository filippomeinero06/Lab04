class StandStandard:
    def __init__(self, codice, superficie, padiglione, prezzo):
        self.__codice = codice
        self.__superficie = superficie
        self.__padiglione = padiglione
        self.__prezzo = prezzo
        self.__codice_espositore = None     # attributo che contiene il codice dell'espositore a cui lo stand è associato (un po' come se fosse la chiave esterna per una tabella di un DB)

    @property
    def codice(self):
        return self.__codice

    @property
    def codice_espositore(self):
        return self.__codice_espositore

    @property
    def prezzo(self):
        return self.__prezzo

    @prezzo.setter
    def prezzo(self, prezzo):
        self.__prezzo = prezzo

    @codice_espositore.setter
    def codice_espositore(self, codice_espositore):
        self.__codice_espositore = codice_espositore

    def __eq__(self, other):
        if self.__codice_espositore == other.codice:
            return True
        else:
            return False

    def __str__(self):
        if self.__codice_espositore is None:
            return f"{self.__codice}: {self.__superficie} mq - Padiglione {self.__padiglione} - Prezzo {self.__prezzo:.2f}€ - Disponibile"
        else:
            return f"{self.__codice}: {self.__superficie} mq - Padiglione {self.__padiglione} - Prezzo {self.__prezzo:.2f}€ - Occupato"


    def __lt__(self, other):
        if self.__prezzo < other.prezzo:
            return True
        else:
            return False

