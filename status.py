import clear
import graphics
import load

def change():
    while True:
        # Token
        idFound = False

        print("Zurück zum Hauptmenü mit [B]")
        print("")
        findID = input("Zu welcher Aufgabe [ID] möchtest du den Status ändern? :/> ").lower()
        print("")

        if findID == "b":
            return
        
        if not findID.isdigit():
            clear.clear()
            graphics.status()
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
            status_raw      = parts[3].strip().lower()  
            heute           = parts[4]
            dueDate         = parts[5]

            # Umwandlung bool in String
            if status_raw in ("false", "offen"):
                status = "offen"
            elif status_raw in ("true", "erledigt"):
                status = "erledigt"
            else:
                status = status_raw

            if idCounter == findID:
                idFound = True
                if status == "offen":
                    status = "erledigt"
                elif status == "erledigt":
                    while True:
                        wirklich = input("Sind sie sicher, dass Sie die Aufgabe wieder als OFFEN kennzeichnen möchten? (J/N) :/> ")
                        if wirklich == "j":
                            status = "offen"
                        elif wirklich == "n":
                            break
                        else:
                            print("")
                            print("*** ⚠️  Eingabe unzulässig! ***")
                        break

            # Neuen Datensatz wieder zusammenstellen
            data = f"[{idCounter}, {task}, {prio}, {status}, {heute}, {dueDate}]\n"
            lines[i] = data                             

        if not idFound:
            clear.clear()
            graphics.status()
            graphics.taskOverview()
            load.taskOverview()
            graphics.taskOverviewFinishline()
            print("*** ⚠️  ID existiert nicht! ***")
            print("")
            continue

        with open("daten/tasks.txt", "w", encoding="utf-8") as file:
            file.writelines(lines)

        clear.clear()
        graphics.status()
        graphics.taskOverview()
        load.taskOverview()
        graphics.taskOverviewFinishline()
