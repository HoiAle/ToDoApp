# ToDoApp – Konsolenbasierter Aufgabenmanager

## Kurzbeschreibung

Die ToDoApp ist ein einfaches Konsolenprogramm (ohne grafische Oberfläche), mit dem man To-Do-Listen verwalten kann.
Man kann Aufgaben anlegen, bearbeiten, löschen, als erledigt markieren sowie nach Datum, Status oder Priorität sortieren und filtern.
Alle Aufgaben werden in einer Textdatei gespeichert und beim Start automatisch wieder geladen.

## Ziel der Arbeit

Ziel dieses Projekts ist die Entwicklung einer konsolenbasierten Anwendung,
die grundlegende Programmierkonzepte in Python demonstriert.
Dazu gehören der Umgang mit Dateien, die Aufteilung des Programms in mehrere Module
sowie die Verarbeitung und Validierung von Benutzereingaben.

## Funktionen

- Aufgaben erstellen
- Aufgaben bearbeiten
- Aufgaben löschen
- Status ändern (offen / erledigt)
- Aufgaben sortieren (ID, Beschreibung, Priorität, Status, Datum)
- Aufgaben filtern (Status, Priorität, Beschreibung)
- Speicherung in einer `.txt`-Datei
- Fehlerbehandlung bei ungültigen Eingaben

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

## Technischer Aufbau

Das Programm ist in mehrere Python-Dateien aufgeteilt, um den Code übersichtlich
und wartbar zu halten. Jede Datei übernimmt eine klar definierte Aufgabe.

Die zentrale Steuerung erfolgt über die Datei `app.py`.
Diese verarbeitet Benutzereingaben und ruft die entsprechenden Module auf.
Die eigentliche Logik (z. B. Bearbeiten, Löschen, Sortieren) ist klar von der Darstellung getrennt.

### Projektstruktur

ToDoApp/
│
├── app.py              # Startpunkt der Anwendung, Menü- und Programmsteuerung
├── graphics.py         # Konsolen-Ausgabe, Menüs und Tabellen
├── clear.py            # Löscht den Konsolenbildschirm
│
├── new.py              # Neue Aufgaben erstellen
├── edit.py             # Bestehende Aufgaben bearbeiten
├── delete.py           # Aufgaben löschen
├── status.py           # Aufgabenstatus ändern (offen/erledigt)
├── sort.py             # Aufgaben sortieren und speichern
├── filter.py           # Aufgaben filtern (nur Anzeige)
├── load.py             # Aufgaben aus Datei laden und anzeigen
│
├── daten/
│   └── tasks.txt       # Dauerhafte Speicherung der Aufgaben


## Datenhaltung

Die Aufgaben werden in einer Textdatei `daten/tasks.txt` gespeichert.
Jede Aufgabe wird zeilenweise in folgendem Format abgelegt:

```csharp
[ID, Beschreibung, Priorität, Status, Erstelldatum, Fälligkeitsdatum]
```











