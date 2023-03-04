from note import Note


class NotenCollection:

    def __init__(self, noten=None):
        self.noten = noten

    # TODO: Adding Feature
    def get_notendurchschnitt(self, fach):
        pass

    def add_note(self, fach, wert, gewichtung):
        self.noten.append(Note(fach, wert, gewichtung))
