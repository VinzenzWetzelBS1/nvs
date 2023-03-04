from notenCollection import NotenCollection


class Schueler:

    def __init__(self, vorname, nachname, username):
        self.vorname = vorname
        self.nachname = nachname
        self.username = username
        self.noten_collection = NotenCollection()
        self.klassen_name = None
        self.passwort = None

    def benoten(self, note):
        self.noten_collection.noten.append(note)

    def get_klasse(self, klassen):
        for klasse in klassen:
            if klasse.name == self.klassen_name:
                return klasse
        return None
