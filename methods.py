import cards

def indexCards():
    cardIndexes = {}
    AllCards = cards.NoneColor.cards + cards.Red.cards + cards.Yellow.cards + cards.Blue.cards + cards.Green.cards

    # For 1 (5 / 15):
    # Tüm kartları barındıran, liste tipindeki değişkenin içindeki tüm değerleri döner ve (ID, isim) şeklinde bir sözlük oluşturur.
    for theCard in AllCards:
        cardIndexes[theCard.ID] = theCard.name

    del AllCards
    return cardIndexes