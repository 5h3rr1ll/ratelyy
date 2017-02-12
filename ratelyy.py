#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Begrüßung
def Welcome():

    print("Hallo, ich bin ratelyy, dein Persönlicher Einkaufsassistent.")
    print("Ich helfe Dir dabei schnell zu erknenn, ob ein Produkt zu Dir passt")
    print("oder nicht!")
    print("Um dir zukünftig schnell sagen zu können, ob es ein Produkt zu Dir")
    print("passt, müsstest Du mir kurz ein paar Fragen beantworten")

#Namen des User erfragen
def UserData():
    print("Wie darf ich Dich nennen? ")
    UserName = input()

    while len(UserName) < 0:
        UserName = input("Dein Name sollte min. einen Buchstaben haben!")

    #Ethik, wichtig für zukünftige Produktempfehlungen
    Ethik = input("Ist dir ethische Handel bei Unternehmen wichtig? J/N ")

    while len(Ethik) < 0:
        Ethik = input("Du hast nichts eingegeben! J oder N ? ")
    if Ethik in ["Ja", "ja", "J", "j"]:
        print("Super!")
        Ethik = True
    else:
        print("Okay")
        Ethik = False

    Kinderarbeit = input("Ist Dir wichtig dass keine Kinderarbeit ? J/N ")

    while len(Kinderarbeit) < 0:
        Kinderarbeit = input("Du hast nichts eingegeben! (J)a oder (N)ein ? ")
    if Kinderarbeit in ["Ja", "ja", "J", "j"]:
        print("Super!")
        Kinderarbeit = True
    else:
        print("Okay")
        Kinderarbeit = False

        return Ethik, Kinderarbeit

    # def Produkt():
    #     return True
    #
    # if Produkt == True:
    #     print("Jap!")

#Einkaufsliste
def EinkaufsListe():
    Liste = {}

    Item = input("Was brauchst du? ")
    Anzahl = int(input("Wieviel?"))

    if Item not in Liste:
        Liste[Item] = Anzahl

    print("Du hast jetzt folgendes in deiner Einkaufslist")
    print(Liste)

# class Produkt(object):
#     def __init__(self, pname, ean):
#         self.pname = pname
#         self.ean = ean
#
Welcome()
UserData()
EinkaufsListe()
