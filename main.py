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


def getDialogAntwort():
    try:
        print("1. Lehrer anlegen")
        print("2. Schüler anlegen")
        print("3. Schüler benoten")
        print("4. Zeugnis erstellen")
        antwort = int(input("Wählen Sie eine Option: "))
        return antwort
    except Exception:
        print("Error bei Eingabe.")
        return -1

schueler1 = Schueler("Vinzenz", "Wetzel")
lehrer1 = Lehrer("Markus", "Scherg", ["deutsch", "mathe"])
zeugnis = Zeugnis("Berufsschule 1 Bayreuth")

lehrer1.benoten(schueler1, "deutsch", 2)
lehrer1.benoten(schueler1, "deutsch", 1)
lehrer1.benoten(schueler1, "deutsch", 3)
lehrer1.benoten(schueler1, "deutsch", 3)
lehrer1.benoten(schueler1, "mathe", 2)
lehrer1.benoten(schueler1, "mathe", 1)
lehrer1.benoten(schueler1, "mathe", 1)
lehrer1.benoten(schueler1, "mathe", 5)

dialogAntwort = -1
while dialogAntwort > 4 or dialogAntwort <= 0:
    dialogAntwort = getDialogAntwort()

match dialogAntwort:
    case 1:
        pass
    case 2:
        pass
    case 3:
        pass
    case 4:
        zeugnis.erstelleZeugnis(schueler1)








