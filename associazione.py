class Associazione:
    def __init__(self, codice_stand, codice_espositore):
        self.__codice_stand = codice_stand
        self.__codice_espositore = codice_espositore

    @property
    def codice_stand(self):
        return self.__codice_stand

    @property
    def codice_espositore(self):
        return self.__codice_espositore
