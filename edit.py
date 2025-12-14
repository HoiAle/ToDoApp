import graphics
import load
import clear

def findCounter():
    while True:
        # Tokens
        idFound = False
        token = False

        print("Zurück zum Hauptmenü mit [B]")
        print("")
        findID = input("Welche Aufgabe [ID] soll bearbeitet werden? :/> ").lower()
        print("")
        
        if findID == "b":
            return
        
        if not findID.isdigit():
            clear.clear()
            graphics.edit()
            graphics.taskOverview()
            load.taskOverview()
            graphics.taskOverviewFinishline()
            print("*** ⚠️  Ungültige Eingabe! Bitte nur eine Ziffer angeben ***")
            print("")
            continue
        
        # Datei in Variable einlesen
        try:
            with open ("daten/tasks.txt", "r", encoding="utf-8") as file:
                lines = file.readlines()
        except FileNotFoundError:
            print("Datei konnte nicht gefunden werden!")

        # Zeile für Zeile einlesen und segmentieren
        for i, line in enumerate(lines):
            line = line.strip().strip("[]")
            parts = line.split(",")
        
            # Teile der Zeile jeweils in eine Variable
            idCounter       = parts[0]
            task            = parts[1]
            prio            = parts[2]
            status_raw      = parts[3]
            heute           = parts[4]
            dueDate         = parts[5]

            # Umwandlung bool in String
            if status_raw.lower() == "false":
                status = "offen"
            elif status_raw.lower() == "true":
                status = "erledigt"
            else:
                status = status_raw    # fallback
            
            if idCounter == findID:               
                idFound = True          # Anpassung Token-Status
                
                while True:
                    print("[1] Aufgabenbeschreibung bearbeiten")
                    print("[2] Priorität wechseln")
                    print("[3] Fälligkeitsdatum bearbeiten")
                    print("[B] Abbrechen")
                    print("")
                    edit = input("Was soll bearbeitet werden? :/> ").lower()

                    if edit == "1":
                        task = input("Wie lautet die neue Aufgabenbeschreibung? :/> ")
                        break
                    elif edit == "2":
                        while True:
                            prio = input("Wie lautet die neue Priorität? :/> ").lower()
                            if prio == "a":
                                break
                            elif prio == "b":
                                break
                            elif prio == "c":                                
                                break
                            else:
                                print("")
                                print("*** ⚠️  Eingabe unzulässig! ***")
                                print("Bitte [A], [B] oder [C] eingeben ***")
                                print("")
                        break
                    elif edit == "3":
                        dueDate = input("Wie lautet das neue Fälligkeitsdatum :/> ")
                        break
                    elif edit == "b":
                        token = True
                        break
            
                if token:
                    break

                # Neuen Datensatz wieder zusammenstellen
                data = f"[{idCounter}, {task}, {prio}, {status}, {heute}, {dueDate}]\n"
                lines[i] = data            

                with open("daten/tasks.txt", "w", encoding="utf-8") as file:
                    file.writelines(lines)
                
                break

            if token:
                    break
        
        # Wenn ID nicht gefunden wurde Fehlermeldung und Schleife beenden
        if not idFound:
            clear.clear()
            graphics.edit()
            graphics.taskOverview()
            load.taskOverview()
            graphics.taskOverviewFinishline()
            print("*** ⚠️  ID existiert nicht! ***")
            print("")
            continue

        while True:
            back = input("Möchtest noch etwas verändern? (J/N) :/>  ").lower()
            print("")
            if back == "n":
                return
            elif back == "j":
                clear.clear()
                graphics.edit()
                graphics.taskOverview()
                load.taskOverview()
                graphics.taskOverviewFinishline()
                break
            else:
                print("*** ⚠️  Eingabe unzulässig! ***")
                print("")               
        
        # 1. Abfrage welche ID bearbeitet werden soll
        # 1.1 wenn "B": zurück zum Hauptmenü
        # 1.2 wenn ID nicht gefunden: Fehlermeldung un zurück zu 1.
        # 1.3 wenn ID gefunden: gehe zu 2.
        # 2. Anzeige welche Bearbeitungsmöglichkeiten zur Verfügung stehen
        # 3. Es muss eine Bearbeitungsmöglichkeit ausgewählt werden
        # 4. Die neuen Eingabe muss in der entsprechenden Variable gespeichert werden
        # 5. Abfrage, ob noch etwas bearbeitet werden soll. 
        # 5.1 wenn nein: zurück zum Hauptmenü.
        # 5.2 wenn ja: zurück zur ID-Abfrage bzw. 1.
