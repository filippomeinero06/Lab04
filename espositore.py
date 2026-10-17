class Espositore:
    def __init__(self, codice, nome, cognome):
        self.__codice = codice
        self.__nome = nome
        self.__cognome = cognome

    @property
    def codice(self):
        return self.__codice

    def __str__(self):
        return f"{self.__codice}: {self.__nome} - {self.__cognome}"

