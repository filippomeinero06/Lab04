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


