# ToDoApp – Konsolenbasierter Aufgabenmanager

Ein modular aufgebauter Aufgabenlisten-Manager in Python zur Verwaltung von To-Dos über die Konsole.  
Die Anwendung ermöglicht das Erstellen, Bearbeiten, Löschen, Sortieren und Filtern von Aufgaben mit persistenter Speicherung in einer Textdatei.

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
- Persistente Speicherung in einer `.txt`-Datei
- Fehlerbehandlung bei ungültigen Eingaben

## Installation und Nutzung

### 1. Voraussetzungen

- Python **3.x**
- Terminal / Konsole
- Keine externen Libraries erforderlich

### 2. Projekt starten

```bash
python app.py






ToDo-App/
├── app.py          # Einstiegspunkt
├── graphics.py     # Menü und Programmsteuerung
├── new.py          # Aufgabe erstellen
├── edit.py         # Aufgabe bearbeiten
├── delete.py       # Aufgabe löschen
├── status.py       # Status ändern
├── sort.py         # Aufgaben sortieren
├── filter.py       # Aufgaben filtern
├── load.py         # Laden und Speichern
├── clear.py        # Bildschirm leeren
├── daten/
│   └── tasks.txt   # Aufgaben-Speicher
├── ascii/
│   └── startbildschirm.txt
└── ToDoApp.bat     # Startdatei (Windows)


