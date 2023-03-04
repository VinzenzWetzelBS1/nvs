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

new_klasse = Klasse("ITG10B")
new_klasse.add_schueler(schuelerList[0])
new_klasse.raum = 23
new_klasse.klassenlehrer = lehrerList[0]
jsonController.update_klasse(new_klasse)
a = 2
