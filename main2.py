class Lehrer:
    def __init__(self, vorname, nachname, unterrichtsfaecher):
        self.vorname = vorname
        self.nachname = nachname
        self.unterrichtsfaecher = unterrichtsfaecher

    def benoten(self, schueler, fach, note):
        if fach not in schueler.noten or fach not in self.unterrichtsfaecher:
            return
        else:
            schueler.noten[fach].append(note)

class Schueler:
    noten = {
        "deutsch": [],
        "mathe": []
    }

    def __init__(self, vorname, nachname):
        self.vorname = vorname
        self.nachname = nachname

    def notendurchschnitt(self, fach):
        if fach not in self.noten:
            return -1
        else:
            abs_wert = 0
            anzahl_noten = len(self.noten[fach])
            for i in self.noten[fach]:
                abs_wert += i
            if anzahl_noten == 0 or abs_wert == 0:
                return -1
            else:
                return abs_wert / anzahl_noten

class Zeugnis:

    def __init__(self, schulname):
        self.schulname = schulname

    def erstelleZeugnis(self, schueler):
        print(f"Der Schüler {schueler.vorname} {schueler.nachname} hat die Noten in folgenden Fächern erreicht:")
        print(f"Deutsch: {round(schueler.notendurchschnitt('deutsch'))}")
        print(f"Mathe: {round(schueler.notendurchschnitt('mathe'))}")
        print(f"Erreicht wurde dies in der Schule: {self.schulname}")

class Schule:
    def __init__(self, Schulname):
        self.schulname = Schulname
        self.schuelerliste = []
        self.lehrerliste = []
    def neu_lehrer(self, lehrer):
        self.lehrerliste.append(lehrer)
    def neu_schueler(self, schueler):
        self.schuelerliste.append(schueler)
    def schueler_ausgeben(self):
        for schueler in range(len(self.schuelerliste)):
            print(self.schuelerliste[schueler].vorname, self.schuelerliste[schueler].nachname)
    def lehrer_ausgeben(self):
        for lehrer in range(len(self.lehrerliste)):
            print(self.lehrerliste[lehrer].vorname, self.lehrerliste[lehrer].nachname)
baumschule = Schule("Baumschule")
def dialog():
    svorname = ""
    snachname = ""
    lvorname = ""
    lnachname = ""
    lunterrichtsfächer = ""
    print("Schüler:")
    baumschule.schueler_ausgeben()
    print("Lehrer:")
    baumschule.lehrer_ausgeben()
    print("was möchten sie tun?")
    print("1:Schüler erstellen")
    print("2:Lehrer erstellen")
    print("3:Noten vergeben")
    print("4:Zeugnis erstellen")
    try :
        eingabe = input(">")
    except :
        exit()
    if eingabe == "1" :
        svorname = input("vorname: ")
        snachname = input("nachname: ")
        baumschule.neu_schueler(Schueler(svorname, snachname))
    if eingabe == "2" :
        lvorname = input("vorname: ")
        lnachname = input("nachname: ")
        lunterrichtsfächer = input("unterrichtsfächer: ")
        unterrichtsfächerliste = lunterrichtsfächer.split(",")
        baumschule.neu_lehrer(Lehrer(lvorname, lnachname, unterrichtsfächerliste))
while True:
    dialog()