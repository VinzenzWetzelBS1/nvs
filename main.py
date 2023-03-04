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

new_schueler = Schueler("Vinzenz", "Wetzel", "dasevoli")
new_schueler.klassen_name = "ITG10B"
jsonController.update_schueler(new_schueler)

new_klasse = Klasse("ITG10B")
new_klasse.raum = 23
new_klasse.add_schueler(new_schueler)
jsonController.update_klasse(new_klasse)

a = schuelerList[0].get_klasse(klassenList)
b = schuelerList[1].get_klasse(klassenList)

a = 2
