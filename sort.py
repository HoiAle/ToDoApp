import graphics
import clear
import load


def read_tasks():
    tasks = []

    with open("daten/tasks.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip().strip("[]")        
        parts = line.split(",")

        parts = [p.strip().strip('"').strip("'") for p in parts]
        # *** List comprehension *** 
        # neue_liste = []
        # for p in parts:
        #     p = p.strip()
        #     p = p.strip('"')
        #     p = p.strip("'")
        #     neue_liste.append(p)
        # parts = neue_liste

        idCounter   = parts[0]
        task        = parts[1]
        prio        = parts[2]
        status_raw  = parts[3]
        heute       = parts[4]
        dueDate     = parts[5]

        # Status normalisieren (kompatibel zu load und change)
        sr = status_raw.strip().lower()
        if sr in ("false", "offen"):
            status = "offen"
        elif sr in ("true", "erledigt"):
            status = "erledigt"
        else:
            status = status_raw.strip()

        tasks.append({
            "id": idCounter,
            "task": task,
            "prio": prio,
            "status": status,
            "created": heute,
            "due": dueDate
        })

    return tasks

def write_tasks(tasks):
    lines = []
    for t in tasks:
        line = f"[{t['id']}, {t['task']}, {t['prio']}, {t['status']}, {t['created']}, {t['due']}]\n"
        lines.append(line)

    with open("daten/tasks.txt", "w", encoding="utf-8") as file:
        file.writelines(lines)
        

def prio_key(prio_value):
    prio_value = prio_value.strip().upper()
    mapping = {"A": 1, "B": 2, "C": 3}
    return mapping.get(prio_value, 99)

def status_key(status_value):
    s = status_value.strip().lower()
    mapping = {"offen": 0, "erledigt": 1}
    return mapping.get(s, 99)

def sort():
    while True:
        tasks = read_tasks()
        
        print("Sortieren nach ...")
        print("[1] ... nach Fälligkeitsdatum")
        print("[2] ... nach Erstelldatum")
        print("[3] ... nach Status")
        print("[4] ... nach Priorität")
        print("[5] ... nach Beschreibung")
        print("[6] ... nach ID")
        print("Zurück zum Hauptmenü mit [B]")
        print("")
        eingabe = input("Wie soll sortiert werden? :/> ").lower()
        print("")
    
        if eingabe == "b":
            return

        if eingabe == "1":
            key_func = lambda t: t["due"] or ""
            description = "Fälligkeit"
        elif eingabe == "2":
            key_func = lambda t: t["created"] or ""
            description = "Erstelldatum"
        elif eingabe == "3":
            key_func = lambda t: status_key(t["status"])
            description = "Status"
        elif eingabe == "4":
            key_func = lambda t: prio_key(t["prio"])
            description = "Priorität"
        elif eingabe == "5":
            key_func = lambda t: t["task"].lower()
            description = "Beschreibung"
        elif eingabe == "6":
            key_func = lambda t: int(t["id"]) if str(t["id"]).isdigit() else 999999
            description = "ID"
        else:
            clear.clear()
            graphics.sort()
            graphics.taskOverview()
            load.taskOverview()
            graphics.taskOverviewFinishline()
            print("*** ⚠️  Ungültige Auswahl! Bitte erneut versuchen. ***")
            print("")
            continue

        # Sortieren (aufsteigend)
        tasks.sort(key=key_func)

        # Datei mit neuer Reihenfolge überschreiben
        write_tasks(tasks)

        # UI aktualisieren
        clear.clear()
        graphics.sort()
        graphics.taskOverview()
        load.taskOverview()
        graphics.taskOverviewFinishline()
        print(f"Aufgaben wurden erfolgreich nach {description} sortiert und gespeichert.")
        print("")

        # Weitere Sortierung?
        while True:
            nochmal = input("Möchten Sie eine weitere Sortierung vornehmen? (J/N) :/> ").strip().lower()
            if nochmal.lower() == "n":
                return
            elif nochmal.lower() == "j":
                break
            else:
                clear.clear()
                graphics.sort()
                graphics.taskOverview()
                load.taskOverview()
                graphics.taskOverviewFinishline()
                print("*** ⚠️  Ungültige Auswahl! Bitte erneut versuchen. ***")
                print("")
        