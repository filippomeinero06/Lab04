from stand_standard import StandStandard

class StandPreseElettriche(StandStandard):
    def __init__(self, codice, superficie, padiglione, prezzo, num_prese):
        new_prezzo = prezzo * (1 + 0.07 * num_prese)
        super().__init__(codice, superficie, padiglione, new_prezzo)
        self.__num_prese = num_prese

    def __str__(self):
        return f"{super().__str__()} - Prese aggiuntive: {self.__num_prese}"



