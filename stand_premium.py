from stand_standard import StandStandard

class StandPremium(StandStandard):
    def __init__(self, codice, superficie, padiglione, prezzo, posizione):
        super().__init__(codice, superficie, padiglione, 0)
        self.__prezzo = prezzo * 1.30
        self.__posizione = posizione

    def __str__(self):
        return f"{super().__str__()} - Posizione: {self.__posizione}"
