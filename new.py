import graphics
import clear
from datetime import date

idCounter = 1    # Laufende ID

def newTask():    
    
    while (True):
        global idCounter
        # Grafik einfügen
        clear.clear()
        graphics.newMenu()
        print("Zurück zum Hauptmenü mit [B]")
        print("")
        
        # Aufgabenbeschreibung & Zurück zum Hauptmenü
        task = input("Wie lautet die neue Aufgabe? (Bitte keine Kommas verwenden!) :/> ").lower()
        if task == "b":
            break
        print("")
        
        # Priorität setzen
        print("Prioritäten setzen:")
        print(" [A]: hohe Priorität")
        print(" [B]: mittlere Priorität")
        print(" [C]: niedrige Prioriät")
        print("")
        while (True):
            prio = input("Welche Priorität soll die Aufgabe erhalten? :/> ").lower()
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
        print("")
        
        # Fälligkeitstermin eingeben
        dueDate = input ("Fälligkeit der Aufgabe? Wähle das Format dd.mm.jjjj   :/> ")
        print("")
        
        # Status setzen und Erstelldatum setzen
        status = False
        heute = str(date.today().strftime("%d.%m.%Y"))
        
        # Aufgabe speichern
        while True:
            save = input("Möchtest du Aufgabe speichern? J/N :/> ").lower()
            print("")
            if save == "j":
                # ID identifizieren und idCounter erhöhen
                try:
                    with open ("daten/tasks.txt", "r", encoding="utf-8") as file:
                        data_str_original = file.readlines()     

                except FileNotFoundError:
                    print("Datei nicht gefunden!")
                
                if len(data_str_original) == 0:
                    idCounter = 1
                else:
                    lastLine = data_str_original[-1].strip()
                    lastLine = lastLine.strip("[]")
                    parts = lastLine.split(",")
                    idCounter = int(parts[0].strip()) + 1                           
                
                # Neuen Datensatz speichern
                data = f"[{idCounter}, {task}, {prio}, {status}, {heute}, {dueDate}]"
                data_str = str(data)
                with open ("daten/tasks.txt", "a", encoding="utf-8") as file:
                    file.write(data_str + "\n")                   
                break
                
            elif save == "n":
                print("*** ⚠️  Aufgabe nicht gespeichert! ***")
                print("")
                break
            else:
                print("*** ⚠️  Eingabe unzulässig! ***")
                print("")
            
        # Weitere Aufgabe hinzufügen (J/N)
        back = "j"
        while True:
            back = input("Möchtest du eine weitere Aufgabe hinzufügen? (J/N) :/>  ")
            if back.lower() == "n":
                break
            elif back.lower() == "j":
                break
            else:
                print("*** ⚠️  Eingabe unzulässig! ***")
                print("")                
        if back == "n":
            break