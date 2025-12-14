import clear
import graphics
import load
from sort import read_tasks   # ← wichtig: read_tasks() wiederverwenden


def _print_task_row(t):
    """Eine Task-Zeile im selben Layout wie load.taskOverview() ausgeben."""
    print(
        f"| {str(t['id']).ljust(6)}"
        f"| {str(t['task'])[:38].ljust(38)} "
        f"| {str(t['prio']).ljust(10)}"
        f"| {str(t['status']).ljust(10)}"
        f"| {str(t['created']).ljust(11)} "
        f"| {str(t['due']).ljust(11)} |"
    )


def filtern():
    """
    Zeigt gefilterte Aufgaben (Status, Priorität oder Beschreibung),
    OHNE die Datei zu verändern.
    """
    while True:
        tasks = read_tasks()

        if not tasks:
            clear.clear()
            graphics.status()
            graphics.taskOverview()
            graphics.taskOverviewFinishline()
            print("*** Es sind keine Aufgaben vorhanden oder die Datei existiert nicht. ***")
            print("")
            return

        print("Filtern nach ...")
        print("[1] ... nach Status (offen / erledigt)")
        print("[2] ... nach Priorität (A–C)")
        print("[3] ... nach Beschreibung (Teilstring)")
        print("Zurück zum Hauptmenü mit [B]")
        print("")
        eingabe = input("Wie soll gefiltert werden? :/> ").strip().lower()
        print("")

        if eingabe == "b":
            return

        filtered = []
        beschreibung = ""

        # ------------------------------
        # Filter 1: Status
        # ------------------------------
        if eingabe == "1":
            status_input = input("Filter-Status (offen/erledigt) :/> ").strip().lower()
            print("")

            for t in tasks:
                if t["status"].strip().lower() == status_input:
                    filtered.append(t)

            beschreibung = f"Status = {status_input}"

        # ------------------------------
        # Filter 2: Priorität
        # ------------------------------
        elif eingabe == "2":
            prio_input = input("Filter-Priorität (A-C) :/> ").strip().upper()
            print("")

            for t in tasks:
                if str(t["prio"]).strip().upper() == prio_input:
                    filtered.append(t)

            beschreibung = f"Priorität = {prio_input}"

        # ------------------------------
        # Filter 3: Beschreibung enthält ...
        # ------------------------------
        elif eingabe == "3":
            text_input = input("Suchtext in der Beschreibung :/> ").strip().lower()
            print("")

            for t in tasks:
                if text_input in str(t["task"]).lower():
                    filtered.append(t)

            beschreibung = f'Beschreibung enthält "{text_input}"'

        else:
            clear.clear()
            graphics.filtering()
            graphics.taskOverview()
            graphics.taskOverviewFinishline()
            print("*** ⚠️  Ungültige Auswahl! Bitte erneut versuchen. ***")
            print("")
            continue

        # ------------------------------
        # Gefilterte Ansicht anzeigen
        # ------------------------------
        clear.clear()
        graphics.status()
        graphics.taskOverview()

        if not filtered:
            print(f"*** Keine Aufgaben gefunden für Filter: {beschreibung}. ***")
        else:
            for t in filtered:
                _print_task_row(t)

        graphics.taskOverviewFinishline()
        print(f"(Temporäre Ansicht – gefiltert nach: {beschreibung})")
        print("")

        # Noch einmal filtern?
        while True: 
            nochmal = input("Weitere Filterung vornehmen? (J/N) :/> ").strip().lower() 
            if nochmal.lower() == "n": 
                return
            elif nochmal.lower() =="j": 
                clear.clear()
                break 
            else: 
                clear.clear() 
                graphics.filtering() 
                graphics.taskOverview() 
                graphics.taskOverviewFinishline() 
                print("*** ⚠️ Ungültige Auswahl! Bitte erneut versuchen. ***") 
                print("")