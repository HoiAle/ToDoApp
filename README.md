# ToDoApp – Konsolenbasierter Aufgabenmanager

Ein modular aufgebauter Aufgabenlisten-Manager in Python zur Verwaltung von To-Dos über die Konsole.  
Die Anwendung ermöglicht das Erstellen, Bearbeiten, Löschen, Sortieren und Filtern von Aufgaben mit Speicherung in einer Textdatei.

## Hintergrund

Die ToDoApp ist eine textbasierte Anwendung ohne grafische Oberfläche.  
Der Fokus liegt auf einfacher Bedienung, klarer Menüführung und robuster Verarbeitung von Benutzereingaben.  
Alle Aufgaben werden dauerhaft in einer Textdatei gespeichert und beim Start automatisch geladen.

## Funktionen

- Aufgaben erstellen
- Aufgaben bearbeiten
- Aufgaben löschen
- Status ändern (offen / erledigt)
- Aufgaben sortieren (ID, Beschreibung, Priorität, Status, Datum)
- Aufgaben filtern (Status, Priorität, Beschreibung)
- Speicherung in einer `.txt`-Datei
- Fehlerbehandlung bei ungültigen Eingaben

## Technischer Aufbau

Die Anwendung ist modular aufgebaut.
Jede Hauptfunktionalität ist in einem eigenen Python-Modul implementiert. Dadurch wird der Code:
- übersichtlich
- wartbar
- leicht erweiterbar

Die zentrale Steuerung erfolgt über die Datei `app.py`.
Diese verarbeitet Benutzereingaben und ruft die entsprechenden Module auf.
Die eigentliche Logik (z. B. Bearbeiten, Löschen, Sortieren) ist klar von der Darstellung getrennt.

## Datenhaltung


## Datenhaltung

Die Aufgaben werden in einer Textdatei `daten/tasks.txt` gespeichert.
Jede Aufgabe wird zeilenweise in folgendem Format abgelegt:

```csharp
[ID, Beschreibung, Priorität, Status, Erstelldatum, Fälligkeitsdatum]
```

## Installation und Nutzung

### Voraussetzungen

- Python **3.x**
- Terminal / Konsole
- Keine externen Libraries erforderlich

### Projekt starten

```bash
python app.py
```

### Nutzung

Nach dem Start erscheint ein nummeriertes Konsolenmenü.
Die gewünschten Aktionen werden durch Eingabe der entsprechenden Zahl ausgewählt.
Die Bedienung erfolgt vollständig über Tastatureingaben.


## Projektstruktur

- `app.py` – Startpunkt der Anwendung
- `graphics.py` – Menü/Anzeige und Programmsteuerung
- `new.py` – Aufgabe erstellen
- `edit.py` – Aufgabe bearbeiten
- `delete.py` – Aufgabe löschen
- `status.py` – Status ändern
- `sort.py` – Aufgaben sortieren
- `filter.py` – Aufgaben filtern (nur Anzeige)
- `load.py` – Laden/Speichern
- `daten/tasks.txt` – dauerhafte Speicherung







