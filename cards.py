class Card:
    def __init__(self, name:str="", ID:int=-1, amount:int=1):
        self.name = name
        self.ID = ID
        self.amount = amount

    def __str__(self):
        return self.name

# Renksiz
class NoneColor:
    NCD = Card("[] +4 Kart", 1, 4)
    NCC = Card("[] Renk Değiştirme", 2, 4)

    cards = [NCD, NCC]

# Kırmızı
class Red:
    R0 = Card("[K] 0", 10, 1)
    R1 = Card("[K] 1", 11, 2)
    R2 = Card("[K] 2", 12, 2)
    R3 = Card("[K] 3", 13, 2)
    R4 = Card("[K] 4", 14, 2)
    R5 = Card("[K] 5", 15, 2)
    R6 = Card("[K] 6", 16, 2)
    R7 = Card("[K] 7", 17, 2)
    R8 = Card("[K] 8", 18, 2)
    R9 = Card("[K] 9", 19, 2)
    RB = Card("[K] Bloklama", -11, 2)
    RR = Card("[K] Yön Değiştirme", -12, 2)
    RD = Card("[K] +2 Kart", -13, 2)

    cards = [R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, RB, RR, RD]

# Sarı
class Yellow:
    Y0 = Card("[S] 0", 20, 1)
    Y1 = Card("[S] 1", 21, 2)
    Y2 = Card("[S] 2", 22, 2)
    Y3 = Card("[S] 3", 23, 2)
    Y4 = Card("[S] 4", 24, 2)
    Y5 = Card("[S] 5", 25, 2)
    Y6 = Card("[S] 6", 26, 2)
    Y7 = Card("[S] 7", 27, 2)
    Y8 = Card("[S] 8", 28, 2)
    Y9 = Card("[S] 9", 29, 2)
    YB = Card("[S] Bloklama", -21, 2)
    YR = Card("[S] Yön Değiştirme", -22, 2)
    YD = Card("[S] +2 Kart", -23, 2)

    cards = [Y0, Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8, Y9, YB, YR, YD]

# Mavi
class Blue:
    B0 = Card("[M] 0", 30, 1)
    B1 = Card("[M] 1", 31, 2)
    B2 = Card("[M] 2", 32, 2)
    B3 = Card("[M] 3", 33, 2)
    B4 = Card("[M] 4", 34, 2)
    B5 = Card("[M] 5", 35, 2)
    B6 = Card("[M] 6", 36, 2)
    B7 = Card("[M] 7", 37, 2)
    B8 = Card("[M] 8", 38, 2)
    B9 = Card("[M] 9", 39, 2)
    BB = Card("[M] Bloklama", -31, 2)
    BR = Card("[M] Yön Değiştirme", -32, 2)
    BD = Card("[M] +2 Kart", -33, 2)

    cards = [B0, B1, B2, B3, B4, B5, B6, B7, B8, B9, BB, BR, BD]

# Yeşil
class Green:
    G0 = Card("[Y] 0", 40, 1)
    G1 = Card("[Y] 1", 41, 2)
    G2 = Card("[Y] 2", 42, 2)
    G3 = Card("[Y] 3", 43, 2)
    G4 = Card("[Y] 4", 44, 2)
    G5 = Card("[Y] 5", 45, 2)
    G6 = Card("[Y] 6", 46, 2)
    G7 = Card("[Y] 7", 47, 2)
    G8 = Card("[Y] 8", 48, 2)
    G9 = Card("[Y] 9", 49, 2)
    GB = Card("[Y] Bloklama", -41, 2)
    GR = Card("[Y] Yön Değiştirme", -42, 2)
    GD = Card("[Y] +2 Kart", -43, 2)

    cards = [G0, G1, G2, G3, G4, G5, G6, G7, G8, G9, GB, GR, GD]