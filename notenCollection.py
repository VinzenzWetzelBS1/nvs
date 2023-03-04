from note import Note


class NotenCollection:

    def __init__(self):
        self.noten = []

    # TODO: Adding Feature
    def get_notendurchschnitt(self, fach):
        # TODO
        pass

    def get_all_noten(self, fach):
        # TODO
        pass

    def add_note(self, fach, wert, gewichtung):
        self.noten.append(Note(fach, wert, gewichtung))

    def remove_note(self, fach, wert, gewichtung):
        # TODO
        pass
