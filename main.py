# 18. maddeden sonra yorum satırı eklemeyi bırakıyorum çünkü çok fazla for/if kullanıyorum.
import cards # cards.py başlıklı kağıda bakın
import players # players.py başlıklı kağıda bakın
import methods # methods.py başlıklı kağıda bakın
import sys, random, statistics

class Situations:
    isPlayedBefore = False
    haveCardIndexes = False

class Deck:
    cardsLeft = 108
    haveCards = []

    def getCards():
        Deck.haveCards = []
        AllCards = cards.NoneColor.cards + cards.Red.cards + cards.Yellow.cards + cards.Blue.cards + cards.Green.cards
        # For 2 (6 / 15) //// Çalışma sırasına göre
        # Tüm kartları barındıran, liste tipindeki değişkenin içindeki tüm değerleri döner ve desteye kartları ekler.
        for theCard in AllCards:
            # For 3 (7 / 15):
            # Destede birden fazla olması gereken kartları ekler.
            for _ in range(theCard.amount):
                Deck.haveCards.append(theCard.ID)

        del AllCards

    def dealCards(count):
        # For 5 (10 / 15):
        # Kartları kişi başı 7şer olarak dağıtıyor
        for _ in range(0, count):
            pickNumber = random.randint(0,len(Deck.haveCards)-1)
            GameData.players[0].cards.append(Deck.haveCards[pickNumber])
            Deck.haveCards.pop(pickNumber)

            pickNumber = random.randint(0,len(Deck.haveCards)-1)
            GameData.players[1].cards.append(Deck.haveCards[pickNumber])
            Deck.haveCards.pop(pickNumber)

            pickNumber = random.randint(0,len(Deck.haveCards)-1)
            GameData.players[2].cards.append(Deck.haveCards[pickNumber])
            Deck.haveCards.pop(pickNumber)

            pickNumber = random.randint(0,len(Deck.haveCards)-1)
            GameData.players[3].cards.append(Deck.haveCards[pickNumber])            
            Deck.haveCards.pop(pickNumber)

    def drawCard(player, count):
        for _ in range(count):
            pickNumber = random.randint(0,len(Deck.haveCards)-1)
            player.cards.append(Deck.haveCards[pickNumber])

            if player.name == "Oyuncu":
                print(f"\n 𓏵 Çekilen kart: {GameData.cardIndexes[Deck.haveCards[pickNumber]]}")

            Deck.haveCards.pop(pickNumber)

    def putFirstCard():
        # While bilmemkaç "( – ⌓ – )
        while True:
            pickNumber = random.randint(0,len(Deck.haveCards)-1)
            if Deck.haveCards[pickNumber] == 1 or Deck.haveCards[pickNumber] == 2:
                continue
            GameData.lastCard = Deck.haveCards[pickNumber]
            Deck.haveCards.pop(pickNumber)
            break

    def printLastCard():
        print(f"\n 𓏵 𝐒𝐨𝐧 𝐊𝐚𝐫𝐭:")
        print(f" ୨ৎ {GameData.cardIndexes[GameData.lastCard]}")

    def listCards(player):
        print("✦ . 　⁺ 　 . ✦ . 　⁺ 　 . ✦")
        # For 6 (11 / 15)
        # Oyuncunun tüm kartlarını teker teker indexliyorum
        for i, theCardID in enumerate(player.cards):
            
            print(f"☽ {i}. {GameData.cardIndexes[theCardID]}")
        
        print(     "︶⊹︶︶୨୧︶︶⊹︶")

    def checkthePlayedCard(cardID):
        color = ""
        if len(str(GameData.lastCard)) == 1:
            color = str(GameData.selectedColor)
        elif len(str(GameData.lastCard)) == 2:
            color = str(GameData.lastCard)[0]
        elif len(str(GameData.lastCard)) == 3:
            color = str(GameData.lastCard)[1]

        number = ""
        if len(str(GameData.lastCard)) == 1:
            number = "-"
        elif len(str(GameData.lastCard)) == 2:
            number = str(GameData.lastCard)[1]
        elif len(str(GameData.lastCard)) == 3:
            number = str(GameData.lastCard)[2]

        # If 7 (14 / 15):
        # Kartın numaralı kart mı yoksa aksiyon kartı mı olduğunu kontrol ediyorum.
        if cardID == 0:
            raise("\n Geçersiz kart numarası girdisi, internal value error.")
        elif cardID == 1 or cardID == 2:
            return True
        elif cardID > 0:
            if str(cardID)[0] == color or (len(str(GameData.lastCard)) == 2 and str(cardID)[1] == number):
                return True
        elif cardID < 0:
            if str(cardID)[1] == color or (len(str(GameData.lastCard)) == 3 and str(cardID)[2] == number):
                return True
        else:
            print(f"color = {color}, number = {number}, cardID = {cardID}")
            return False

    def hasPlayableCard(player):
        for i in range(len(player.cards)):
            if Deck.checkthePlayedCard(player.cards[i]) == True:
                return True

        return False

    def playerSelectsColor():
        while True:
            selectedColor = input("\n ─── ･ ｡ﾟ☆: *.☽ .* :☆ﾟ. ─── \n  Yeni rengi seç\n [K] Kırmızı\n [S] Sarı \n [M] Mavi \n [Y] Yeşil\n    ︶⊹︶︶୨୧︶︶⊹︶ \n\n > ")        
            selectedColor = selectedColor.replace(" ","").upper()
            match selectedColor:
                case "K":
                    GameData.selectedColor = 1
                case "S":
                    GameData.selectedColor = 2
                case "M":
                    GameData.selectedColor = 3
                case "Y":
                    GameData.selectedColor = 4
                case _:
                    print("\n 𓏵 Hatalı girdi yaptınız, lütfen K, S, M veya Y yazın.")
                    continue
            break

    def playCard(player):
        # While 2 (12 / 15):
        # Input ile hatalı girdi alınması durumunda doğru girdi alana kadar kullanıcıyı tekrar sorguluyorum
        if Deck.hasPlayableCard(player):
            while True:
                selectedCard = input(f"\nOynayacağınız kartın numarası: ")
                try:
                    selectedCard = int(selectedCard)
                    # If 6 (13 / 15):
                    # Girdinin geçerliliğini kontrol ediyorum
                    if selectedCard in range(0,len(player.cards)):      
                        if Deck.checkthePlayedCard(player.cards[selectedCard]):
                            GameData.lastCard = player.cards[selectedCard]
                            Deck.printLastCard()

                            if (len(str(GameData.lastCard)) == 1 and GameData.lastCard==1) or (len(str(GameData.lastCard)) == 3 and (str(GameData.lastCard)[-1] == "3" or str(GameData.lastCard)[-1] == "1")):
                                GameData.isTurnBlocked=True
                            elif len(str(GameData.lastCard)) == 3 and str(GameData.lastCard)[-1] == "2":
                                p_index = GameData.players.index(player)
                                new_plist = [GameData.players[p_index-i] for i in range(1,5)]
                                GameData.players = new_plist
                                del new_plist
                                GameData.isTurnChanged = True
                                print("\n 𓏵 Tur yönü değişti!")

                            if player.cards[selectedCard]==1 or player.cards[selectedCard]==2:
                                Deck.playerSelectsColor()
                                print(f"\n 𓏵 {player.name}'in seçtiği renk: {GameData.colorIndexes[GameData.selectedColor]}")

                            player.cards.pop(selectedCard)                        
                            break
                        else:
                            print(f"\n Son kart {GameData.cardIndexes[GameData.lastCard]}, senin oynadığın kart {GameData.cardIndexes[player.cards[selectedCard]]}, uyumlu bir kart oyna.")
                            continue
                    else:
                        print("\n 𝐆𝐞𝐜̧𝐞𝐫𝐥𝐢 𝐛𝐢𝐫 𝐬𝐚𝐲ı 𝐠𝐢𝐫𝐢𝐧𝐢𝐳!")
                        continue
                except ValueError:
                    print("\n 𝐒𝐚𝐲ı 𝐠𝐢𝐫𝐢𝐧𝐢𝐳!")
                    continue
        else:
            print("\n 𓏵 Oynanabilir kartınız yok. Kart çekiliyor..")
            Deck.drawCard(player, 1)
            if Deck.hasPlayableCard(player):
                GameData.lastCard = player.cards[-1]
                Deck.printLastCard()

                if (len(str(GameData.lastCard)) == 1 and GameData.lastCard==1) or (len(str(GameData.lastCard)) == 3 and (str(GameData.lastCard)[-1] == "3" or str(GameData.lastCard)[-1] == "1")):
                    GameData.isTurnBlocked=True
                elif len(str(GameData.lastCard)) == 3 and str(GameData.lastCard)[-1] == "2":
                    p_index = GameData.players.index(player)
                    new_plist = [GameData.players[p_index-i] for i in range(1,5)]
                    GameData.players = new_plist
                    del new_plist
                    GameData.isTurnChanged = True
                    print("\n 𓏵 Tur yönü değişti!")

                if player.cards[-1]==1 or player.cards[-1]==2:
                    Deck.playerSelectsColor()
                    print(f"\n 𓏵 {player.name}'in seçtiği renk: {GameData.colorIndexes[GameData.selectedColor]}")

                player.cards.pop(-1)
            else:
                print("\n 𓏵 Hala oynanabilir kart yok! Tur ilerliyor.")


    def isGameContinue():
        # For 6 (17 / 15):
        # Tüm oyuncuların verilerini sırayla çeker
        for i, player in enumerate(GameData.players):
            # If 10 (18 / 15):
            # Kart sayılarını kontrol eder
            if len(player.cards)==0:
                return False
            elif len(player.cards)>0 and i!=3:
                continue
            elif len(player.cards)>0 and i==3:
                return True
                


    def turntheGame():
        while Deck.isGameContinue()==True:
            print(f"\n Destedeki kart sayısı: {len(Deck.haveCards)}")
            for ID in range(4):                
                if GameData.isTurnBlocked==False:
                    if GameData.isTurnChanged==True:
                        GameData.isTurnChanged=False
                        break
                    GameData.players[ID].isThemTurn = True
                    print(f"\n 𓏵 𝗦ı𝗿𝗮 {GameData.players[ID].name}'𝗱𝗮, 𝘀𝗮𝗵𝗶𝗽 𝗼𝗹𝗱𝘂𝗴̆𝘂 𝗸𝗮𝗿𝘁 𝘀𝗮𝘆ı𝘀ı: {len(GameData.players[ID].cards)}")
                    if GameData.players[ID].name == "Oyuncu":
                        Deck.listCards(GameData.players[ID])
                        Deck.playCard(GameData.players[ID])                    
                    else:
                        BotScript.playasBot(GameData.players[ID])
                    GameData.players[ID].isThemTurn = False
                elif GameData.isTurnBlocked==True:
                    GameData.isTurnBlocked=False
                    print(f"\n 𓏵 {GameData.players[ID].name}'ın oynaması {GameData.cardIndexes[GameData.lastCard]} tarafından engellendi.")
                    if len(str(GameData.lastCard)) == 1 and GameData.lastCard==1:
                        print(f"\n 𓏵 {GameData.players[ID].name} 4 kart çekiyor.")
                        Deck.drawCard(GameData.players[ID], 4)
                    elif len(str(GameData.lastCard)) == 3:
                        if str(GameData.lastCard)[-1] == "3":
                            print(f"\n 𓏵 {GameData.players[ID].name} 2 kart çekiyor.")
                            Deck.drawCard(GameData.players[ID], 2)
                        elif str(GameData.lastCard)[-1] == "1":
                            print(f"\n 𓏵 {GameData.players[ID].name} bloklandı.")
                
                if Deck.isGameContinue()==False:
                    break
                input("\n 𓏵 Turu ilerletmek için herhangi bir tuşa basın")
        
        print("\n 𓏵 Oyun bitti.")


class GameData:
    cardIndexes = {}
    players = []
    lastCard = -1
    isTurnBlocked = False
    isTurnChanged = False
    selectedColor = 0
    colorIndexes = {1:"Kırmızı", 2:"Sarı", 3:"Mavi", 4:"Yeşil"}

class BotScript:
    def botPicksColor(player):
        color = ""
        colorList = []
        for card in player.cards:
            if len(str(card))==2:
                color = str(card)[0]
                colorList.append(int(color))
            elif len(str(card))==3:
                color = str(card)[1]
                colorList.append(int(color))
            
        return statistics.mode(colorList)

    def botPlayCard(player, selectedCard):
        GameData.lastCard = player.cards[selectedCard]
        print(f"\n {player.name}'𝗶𝗻 𝗼𝘆𝗻𝗮𝗱ı𝗴̆ı 𝗸𝗮𝗿𝘁: {GameData.cardIndexes[player.cards[selectedCard]]}")
        Deck.printLastCard()

        if (len(str(GameData.lastCard)) == 1 and GameData.lastCard==1) or (len(str(GameData.lastCard)) == 3 and (str(GameData.lastCard)[-1] == "3" or str(GameData.lastCard)[-1] == "1")):
            GameData.isTurnBlocked=True            
        elif len(str(GameData.lastCard)) == 3 and str(GameData.lastCard)[-1] == "2":
            p_index = GameData.players.index(player)
            new_plist = [GameData.players[p_index-i] for i in range(1,5)]
            GameData.players = new_plist
            del new_plist
            GameData.isTurnChanged = True
            print("\n 𓏵 Tur yönü değişti!")

        if player.cards[selectedCard]==1 or player.cards[selectedCard]==2:
            GameData.selectedColor = BotScript.botPicksColor(player)
            print(f"\n 𓏵 {player.name}'in seçtiği renk: {GameData.colorIndexes[GameData.selectedColor]}")
                
        player.cards.pop(selectedCard)

    def playasBot(player):
        for i in range(len(player.cards)):
            if Deck.checkthePlayedCard(player.cards[i]) == True:
                BotScript.botPlayCard(player, i)
                return True
        
        print(f"\n 𓏵 {player.name}'in oynayacak kartı yok, desteden kart çekti.")
        Deck.drawCard(player, 1)
        if Deck.hasPlayableCard(player):
            GameData.lastCard = player.cards[-1]
            print(f"\n {player.name}'𝗶𝗻 𝗼𝘆𝗻𝗮𝗱ı𝗴̆ı 𝗸𝗮𝗿𝘁: {GameData.cardIndexes[player.cards[-1]]}")
            Deck.printLastCard()
            
            if (len(str(GameData.lastCard)) == 1 and GameData.lastCard==1) or (len(str(GameData.lastCard)) == 3 and (str(GameData.lastCard)[-1] == "3" or str(GameData.lastCard)[-1] == "1")):
                GameData.isTurnBlocked=True
            elif len(str(GameData.lastCard)) == 3 and str(GameData.lastCard)[-1] == "2":
                p_index = GameData.players.index(player)
                new_plist = [GameData.players[p_index-i] for i in range(1,5)]
                GameData.players = new_plist
                del new_plist
                GameData.isTurnChanged = True
                print("\n 𓏵 Tur yönü değişti!")

            if player.cards[-1]==1 or player.cards[-1]==2:
                GameData.selectedColor = BotScript.botPicksColor(player)
                print(f"\n 𓏵 {player.name}'in seçtiği renk: {GameData.colorIndexes[GameData.selectedColor]}")

            player.cards.pop(-1)
        else:
            print(f"\n 𓏵 {player.name}'in hala oynanabilir kartı yok! Tur ilerliyor.")

def menu():
    gametext = "1 𓏵 Oyuna Başla" if Situations.isPlayedBefore == False else "1 𓏵 Tekrar Oyna"
    print(f"\n ───── ⋆⋅☆⋅⋆ ─────\n  {gametext}\n  2 𓏵 Çıkış Yap\n꒷꒦︶꒷꒦︶ ๋ ࣭ ⭑꒷꒦")

    # While 1 (1 / 15):
    # 1 ve 2 dışında değer girilene kadar menüden çıkmayı engeller.
    while True:
        secenek = input("𝑺𝒆𝒄̧𝒊𝒏𝒊𝒛: ")
        try:
            secenek = int(secenek)
            # If 1 (2 / 15):
            # Menü seçimini kontrol eder.
            if secenek == 1:                
                break
            elif secenek == 2:
                print("\n𝑶𝒚𝒏𝒂𝒅ı𝒈̆ı𝒏 𝒊𝒄̧𝒊𝒏 𝒕𝒆𝒔̧𝒆𝒌𝒌𝒖̈𝒓𝒍𝒆𝒓! ⋆౨ৎ˚⟡˖ ࣪")
                sys.exit()
                break # Bu satırı debug amaçlı ekledim
            else:
                print("\n𝟏 𝒗𝒆𝒚𝒂 𝟐 𝒅𝒆𝒈̆𝒆𝒓𝒊 𝒈𝒊𝒓𝒊𝒏!")
                continue
        except ValueError:
            print("\n𝟏 𝒗𝒆𝒚𝒂 𝟐 𝒅𝒆𝒈̆𝒆𝒓𝒊 𝒈𝒊𝒓𝒊𝒏!")
            continue
    game()

def game():
    # If 2 (3 / 15):
    # Eğer oyun daha önce oynanmamışsa oyunu tanıtır.
    if Situations.isPlayedBefore==False:
        print("\n              ✦•┈๑⋅⋯⋅⋯⋅⋯⋅⋯ ⋅⋯⋅⋯⋅⋯⋯⋅๑┈•✦\n Oyuna hoşgeldin c: Bu, klasik UNO oyununun aynısı.\n\n 𓏵  Kırmızı, Sarı, Mavi, Yeşil olmak üzere 4 farklı renkten oluşan kartlarımız var.\n 𓏵  Renkli kartlarımız 0-9 arası değerlere sahip olabilir.\n 𓏵  Ayrıca renkli kartlar aksiyon kartı da olabilir. Bu kartlar ile sıradaki kişiye kart çektirebilir, onun bu tur oynamasını engelleyebilir veya tur yönünü değiştirebilirsiniz.\n\n 𓏵  Renkli kartlara isnista olarak 2 tür renksiz kartımız bulunuyor.\n 𓏵  Renksiz kartlar 'Renk Değiştirme' ve '4 kart çektirdikten sonra renk değiştirme' olarak ikiye ayrılıyor.\n\n 𓏵  Sıra size geldiğinde masaya atılan son kart ile ayrı renkte veya aynı rakam/aksiyonda olan bir kart oynamalısınız.\n 𓏵  Ancak renksiz kartları her zaman oynayabilirsiniz.\n\n              ꒷꒦︶꒷꒦︶ ๋ ࣭ ⭑꒷꒦")   

    print("𓈒⠀𓂃⠀⠀˖⠀𓇬⠀˖⠀⠀𓂃⠀𓈒")
    print("✮ Oyun hazırlanıyor..")

    # If 3 (4 / 15):
    # Eğer kartlar daha önce indexlenmemiş ise kartları indexler.
    if Situations.haveCardIndexes==False:
        print("\n✮ Kart bilgisi alınıyor..")
        GameData.cardIndexes = methods.indexCards() # For 1 (5 / 15)
        Situations.haveCardIndexes = True

    print("\n✮ Deste toparlanıyor..")
    Deck.getCards() # For 2 (6 / 15)

    # If 4 (8 / 15):
    # Eğer önceden bir oyun oynanmış ise oyuncuları silip yeniden oluşturur ve masadaki kartı siler.
    if Situations.isPlayedBefore==True:
        GameData.lastCard = -1        
        GameData.players = []

    print("\n✮ Oyuncular oluşturuluyor..")
    # For 4 (9 / 15):
    # Liste halinde 4 sonuç döndüren methodun döndürdüğü değerleri teker teker GameData sınıfındaki oyuncu listesine ekler.
    for thePlayer in players.createPlayers():
        GameData.players.append(thePlayer)

    print("𝑶𝒚𝒖𝒏𝒄𝒖 𝑺𝒂𝒚ı𝒔ı: 4  (1 Oyuncu + 3 Bot)")

    print("\n✮Kartlar dağıtılıyor..")
    Deck.dealCards(7) # For 5 (10 / 15)

    Situations.isPlayedBefore = True

    print("\n\n ┈┈・୨ ✦ ୧・┈┈\n Oyun Başlıyor!\n\n  ｡ﾟ•┈୨♡୧┈• ｡ﾟ")

    Deck.putFirstCard()
    Deck.printLastCard()

    Deck.turntheGame()
    menu()
    


# Çalışmaya Başlama Noktası
if __name__ == "__main__":
    menu()