import fach_constants
from nvsJsonController import NvsJsonController
from schueler import Schueler
from lehrer import Lehrer
from klasse import Klasse
from fach_constants import Fach
from note import Note

jsonController = NvsJsonController("data.json")
a = jsonController.get_klasse("ITG10B")
schuelerList = jsonController.get_all_schueler()
lehrerList = jsonController.get_all_lehrer()
klassenList = jsonController.get_all_klassen()

new_schueler = Schueler("Leon", "Anders", "LeAn1")
new_schueler.benoten(Note(Fach.MATHE, 2, 1.0))
jsonController.update_schueler(new_schueler)

a = 2
