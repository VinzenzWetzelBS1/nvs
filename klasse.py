class Klasse:

    def __init__(self, name, raum=0, schueler_list=None, klassenlehrer=None):
        self.name = name
        self.raum = raum
        self.schueler_list = schueler_list
        self.klassenlehrer = klassenlehrer

    def set_raum(self, name):
        self.raum = name

    def set_klassenlehrer(self, lehrer):
        self.klassenlehrer = lehrer

    def add_schueler(self, schueler):
        schueler.klassen_name = self.name
        self.schueler_list.append(schueler)
