import graphics
import load
import clear

def deleteTask():
    # Abfrage welche Zeile bearbeitet werden soll
    while True:     
        # Tokens
        idFound = False
        token = False

        print("Zurück zum Hauptmenü mit [B]")
        print("")
        findCounter = input("Welche Aufgabe soll gelöscht werden? Gebe dazu die entsprechende [ID] ein :/> ").lower()
        print("")
        if findCounter == "b":
            return  
        
        if not findCounter.isdigit():
            clear.clear()
            graphics.delete()
            graphics.taskOverview()
            load.taskOverview()
            graphics.taskOverviewFinishline()
            print("*** ⚠️  Ungültige Eingabe! Bitte eine numerische ID eingeben. ***")
            print("")
            continue

        try:
            with open ("daten/tasks.txt", "r", encoding="utf-8") as file:
                lines = file.readlines()
        except FileNotFoundError:
            print("Datei konnte nicht gefunden werden!")

        for i, line in enumerate(lines):
            line = line.strip().strip("[]")
            parts = line.split(",")

            # Anführungszeichen löschen
            parts = [p.strip().strip('"').strip("'") for p in parts]
            
            # Teile der Zeile jeweils in eine Variable
            idCounter       = parts[0]

            if idCounter == findCounter:
                idFound = True

                while True:
                    abfrage = input(f"Sind Sie sicher das Sie die ID {idCounter} löschen möchten? (J/N) :/> ").lower()
                    if abfrage == "j":
                        del lines[i]

                        # IDs durchzählen
                        neue_lines = []
                        for idx, line in enumerate(lines, start=1):
                            line_clean = line.strip().strip("[]")
                            parts = [p.strip().strip('"').strip("'") for p in line_clean.split(",")]

                            # ID überschreiben
                            parts[0] = str(idx)
                            neue_lines.append(f"[{', '.join(parts)}]\n")
                        with open("daten/tasks.txt", "w", encoding="utf-8") as file:
                            file.writelines(neue_lines)
                        clear.clear()
                        graphics.delete()
                        graphics.taskOverview()
                        load.taskOverview()
                        graphics.taskOverviewFinishline()
                        print("*** Aufgabe wurde gelöscht! ***")
                        print("")
                        break

                    elif abfrage == "n":
                        clear.clear()
                        graphics.delete()
                        graphics.taskOverview()
                        load.taskOverview()
                        graphics.taskOverviewFinishline()
                        print("*** ⚠️  Löschen abgebrochen ***")
                        print("")
                        token = True
                        break
                    else:
                        print("*** ⚠️  Eingabe unzulässig! ***")
                        print("")                
                break

        if not idFound:
            clear.clear()
            graphics.delete()
            graphics.taskOverview()
            load.taskOverview()
            graphics.taskOverviewFinishline()
            print("*** ⚠️  ID existiert nicht! ***")
            print("")
            continue
        
        while True:
            if token:
                break
            back = input("Möchtest du noch eine Aufgabe löschen? (J/N) :/> ").lower()
            print("")
            if back == "n":
                return
            elif back == "j":
                # Zur nächsten Runde der while True-Schleife
                break
            else:
                print("*** ⚠️  Eingabe unzulässig! ***")
                print("")     
                