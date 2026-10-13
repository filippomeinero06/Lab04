from stand_standard import StandStandard

class StandPreseElettriche(StandStandard):
    def __init__(self, codice, superficie, padiglione, prezzo, num_prese):
        super().__init__(codice, superficie, padiglione, 0)
        self.__prezzo = prezzo * (1 + 0.07 * num_prese)
        self.__num_prese = num_prese



