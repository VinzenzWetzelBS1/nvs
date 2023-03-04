class Klasse:

    def __init__(self, name):
        self.name = name
        self.raum = None
        self.schueler_list = []
        self.klassenlehrer = None

    def add_schueler(self, schueler):
        schueler.klassen_name = self.name
        self.schueler_list.append(schueler)
