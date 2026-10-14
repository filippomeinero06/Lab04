class StandStandard:
    def __init__(self, codice, superficie, padiglione, prezzo):
        self.__codice = codice
        self.__superficie = superficie
        self.__padiglione = padiglione
        self.__prezzo = prezzo
        self.__codice_espositore = None

    @property
    def codice(self):
        return self.__codice

    @property
    def codice_espositore(self):
        return self.__codice_espositore

    @codice_espositore.setter
    def codice_espositore(self, codice_espositore):
        self.__codice_espositore = codice_espositore

    def __eq__(self, other):
        return self.__codice_espositore == other.__codice_espositore

    def __str__(self):
        if self.__codice_espositore is None:
            return f"{self.__codice}: {self.__superficie} mq - Padiglione {self.__padiglione} - Prezzo {self.__prezzo}€ - Disponibile"
        else:
            return f"{self.__codice}: {self.__superficie} mq - Padiglione {self.__padiglione} - Prezzo {self.__prezzo}€ - Occupato"


    def __lt__(self, other):
        return self.__prezzo < other.__prezzo
