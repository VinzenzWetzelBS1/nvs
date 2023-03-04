import json
import os
from klasse import Klasse
from lehrer import Lehrer
from schueler import Schueler
from notenCollection import NotenCollection
from note import Note


class NvsJsonController:

    def __init__(self, file_name):
        self.file_name = file_name
        if os.stat(file_name).st_size == 0:
            # File is empty
            self.loaded_object = {
                "schueler": [],
                "lehrer": [],
                "klassen": []
            }
            self.save_object_to_file()
        else:
            f = open(file_name)
            self.loaded_object = json.load(f)

    def save_object_to_file(self):
        try:
            f = open(self.file_name, "w")
            json_str = json.dumps(self.loaded_object, default=lambda o: o.__dict__)
            f.write(json_str)
            f.close()
        except Exception:
            print("Error: Speichern des Json Objekts fehlgeschlagen")

    def update_schueler(self, schueler):
        for i in range(len(self.loaded_object["schueler"])):
            if self.loaded_object["schueler"][i]["username"] == schueler.username:
                self.loaded_object["schueler"][i] = schueler
                self.save_object_to_file()
                return
        self.loaded_object["schueler"].append(schueler)
        self.save_object_to_file()

    def update_lehrer(self, lehrer):
        for i in range(len(self.loaded_object["lehrer"])):
            if self.loaded_object["lehrer"][i]["username"] == lehrer.username:
                self.loaded_object["lehrer"][i] = lehrer
                self.save_object_to_file()
                return
        self.loaded_object["lehrer"].append(lehrer)
        self.save_object_to_file()

    def update_klasse(self, klasse):
        for i in range(len(self.loaded_object["klassen"])):
            if self.loaded_object["klassen"][i]["name"] == klasse.name:
                self.loaded_object["klassen"][i] = klasse
                self.save_object_to_file()
                return
        self.loaded_object["klassen"].append(klasse)
        self.save_object_to_file()

    def get_schueler(self, username):
        try:
            item = next(x for x in self.loaded_object["schueler"] if x["username"] == username)
            schueler = Schueler(item["vorname"], item["nachname"], item["username"])
            # Noten müssen von Dict in Klasse: "Note" umgewandelt werden
            noten = []
            for note in item['noten_collection']['noten']:
                noten.append(Note(note['fach'], note['wert'], note['gewichtung']))
            schueler.noten_collection = NotenCollection()
            schueler.noten_collection.noten = noten
            schueler.klassen_name = item["klassen_name"]
            schueler.passwort = item["passwort"]
            return schueler
        except Exception:
            return None

    def get_klasse(self, name):
        try:
            item = next(x for x in self.loaded_object["klassen"] if x["name"] == name)
            if not item:
                return None
            klasse = Klasse(item["name"])
            klasse.raum = item["raum"]

            schueler_list = []
            for schueler in item["schueler_list"]:
                new_schueler = Schueler(schueler["vorname"], schueler["nachname"], schueler["username"])
                new_schueler.klassen_name = item["klassen_name"]
                # Noten müssen von Dict in Klasse: "Note" umgewandelt werden
                noten = []
                for note in schueler['noten_collection']['noten']:
                    noten.append(Note(note['fach'], note['wert'], note['gewichtung']))
                new_schueler.noten_collection = NotenCollection()
                new_schueler.noten_collection.noten = noten
                schueler_list.append(new_schueler)
            klasse.schueler_list = schueler_list

            if item["klassenlehrer"]:
                klasse.klassenlehrer = Lehrer(item["klassenlehrer"]["vorname"], item["klassenlehrer"]["nachname"],
                                              item["klassenlehrer"]["username"])
            return klasse

        except Exception:
            return None

    def get_lehrer(self, username):
        try:
            item = next(x for x in self.loaded_object["lehrer"] if x["username"] == username)
            new_lehrer = Lehrer(item["vorname"], item["nachname"], item["username"])
            new_lehrer.passwort = item["passwort"]
            return new_lehrer
        except Exception:
            return None

    def get_all_schueler(self):
        schueler_list = []
        for item in self.loaded_object["schueler"]:
            new_schueler = Schueler(item["vorname"], item["nachname"], item["username"])
            new_schueler.passwort = item["passwort"]
            new_schueler.klassen_name = item["klassen_name"]
            noten = []
            for note in item["noten_collection"]["noten"]:
                noten.append(Note(note['fach'], note['wert'], note['gewichtung']))
            new_schueler.noten_collection = NotenCollection()
            new_schueler.noten_collection.noten = noten
            schueler_list.append(new_schueler)
        return schueler_list

    def get_all_lehrer(self):
        lehrer_list = []
        for item in self.loaded_object["lehrer"]:
            new_lehrer = Lehrer(item["vorname"], item["nachname"], item["username"])
            new_lehrer.passwort = item["passwort"]
            lehrer_list.append(new_lehrer)
        return lehrer_list

    def get_all_klassen(self):
        klassen_list = []
        for item in self.loaded_object["klassen"]:
            new_klasse = Klasse(item["name"])
            new_klasse.raum = item["raum"]
            klassen_list.append(new_klasse)
            if item["klassenlehrer"]:
                new_klasse.klassenlehrer = Lehrer(item["klassenlehrer"]["vorname"], item["klassenlehrer"]["nachname"], item["klassenlehrer"]["username"])

            schueler_list = []
            for schueler in item["schueler_list"]:
                new_schueler = Schueler(schueler["vorname"], schueler["nachname"], schueler["username"])
                new_schueler.klassen_name = schueler["klassen_name"]
                # Noten müssen von Dict in Klasse: "Note" umgewandelt werden
                noten = []
                for note in schueler['noten_collection']['noten']:
                    noten.append(Note(note['fach'], note['wert'], note['gewichtung']))
                new_schueler.noten_collection = NotenCollection()
                new_schueler.noten_collection.noten = noten
                schueler_list.append(new_schueler)
            new_klasse.schueler_list = schueler_list
        return klassen_list
