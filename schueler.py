from notenCollection import NotenCollection


class Schueler:

    def __init__(self, vorname, nachname, username, noten_collection=NotenCollection(), klassen_name=None, passwort=None):
        self.vorname = vorname
        self.nachname = nachname
        self.username = username
        self.noten_collection = noten_collection
        self.klassen_name = klassen_name
        self.passwort = passwort

    def change_klassen_name(self, name):
        self.klassen_name = name

    def benoten(self, note):
        self.noten_collection.noten.append(note)
