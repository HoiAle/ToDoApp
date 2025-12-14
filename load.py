import new 

def taskOverview():   
    # tasks.txt lesen und in Variable speichern
    try:
        with open("ToDoApp/daten/tasks.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Datei nicht gefunden")

    # jede Zeile lesen, separieren und in Variablen speichern
    for line in lines:
        line = line.strip()
        line = line.strip("[]")
        parts = line.split(",")

        # Anführungszeichen löschen
        parts = [p.strip().strip('"').strip("'") for p in parts]
        
        # Teile der Zeile jeweils in eine Variable
        idCounter       = parts[0]
        task            = parts[1]
        prio            = parts[2]
        status_raw      = parts[3]
        heute           = parts[4]
        dueDate         = parts[5]

        # Umwandlung boolschen Status in "offen" oder "erledigt"
        if status_raw.lower() == "false":
            status = "offen"
        elif status_raw.lower() == "true":
            status = "erledigt"
        else:
            status = status_raw    # fallback

        # Ausgabe der Aufgabenzeile
        print(f"| {idCounter.ljust(6)}| {task[:38].ljust(38)} | {prio.ljust(10)}| {status.ljust(10)}| {heute.ljust(11)} | {dueDate.ljust(11)} |")