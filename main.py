from nvsJsonController import NvsJsonController
from schueler import Schueler
from lehrer import Lehrer
from klasse import Klasse
from fach_constants import *

jsonController = NvsJsonController("data.json")
a = jsonController.get_klasse("ITG10B")
schuelerList = jsonController.get_all_schueler()
lehrerList = jsonController.get_all_lehrer()
klassenList = jsonController.get_all_klassen()
a = 2

newSchueler = Schueler("Hallo", "Du", "dasevoli")
jsonController.update_schueler(newSchueler)

a = 2
