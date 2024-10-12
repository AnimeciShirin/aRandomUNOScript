class Players:
    def __init__(self, ID:int=-1, name:str="", cardCount:int=-1, cards=None, themTurn:bool=False):
        self.ID = ID
        self.name = name
        self.cardCount = cardCount
        self.cards = cards if cards is not None else [] # Buradaki bugfix için ChatGPT kullandım
        self.themTurn = themTurn

def createPlayers():
    p1 = Players(0, "Oyuncu", 0)
    b1 = Players(1, "Bot-1", 0)
    b2 = Players(2, "Bot-2", 0)
    b3 = Players(3, "Bot-3", 0)

    return [p1, b1, b2, b3]