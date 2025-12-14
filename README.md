ToDoApp – Konsolenbasierter Aufgabenmanager

Ein modular aufgebauter Aufgabenlisten-Manager in Python zur Verwaltung von To-Dos über die Konsole.
Die Anwendung ermöglicht das Erstellen, Bearbeiten, Löschen, Sortieren und Filtern von Aufgaben mit persistenter Speicherung in einer Textdatei.

Overview

Die ToDoApp ist eine textbasierte Anwendung ohne grafische Benutzeroberfläche.
Der Fokus liegt auf einfacher Bedienung, klarer Menüführung und robuster Verarbeitung von Benutzereingaben.
Alle Aufgaben werden dauerhaft in einer Textdatei gespeichert und beim Start automatisch geladen.

Features

Aufgaben erstellen

Aufgaben bearbeiten

Aufgaben löschen

Status ändern (offen / erledigt)

Aufgaben sortieren (ID, Beschreibung, Priorität, Status, Datum)

Aufgaben filtern (Status, Priorität, Beschreibung)

Persistente Speicherung in einer .txt-Datei

Fehlerbehandlung bei ungültigen Eingaben

Installation and Usage
Voraussetzungen

Python 3.x

Terminal / Konsole

Keine externen Bibliotheken erforderlich

Programm starten

Starte die Anwendung mit:

python app.py

Bedienung

Nach dem Start erscheint ein textbasiertes Hauptmenü.
Die Navigation erfolgt über nummerierte Eingaben:

[1] Aufgabe hinzufügen

[2] Aufgabe bearbeiten

[3] Aufgabe löschen

[4] Aufgabenstatus ändern

[5] Aufgaben sortieren

[6] Aufgaben filtern

[0] Programm beenden

Alle Eingaben werden validiert. Ungültige Eingaben führen nicht zum Absturz.

Program Flow

Start über app.py

Anzeige des Hauptmenüs

Auswahl einer Funktion

Verarbeitung im jeweiligen Modul

Rückkehr ins Hauptmenü

Speicherung der Daten in daten/tasks.txt

Filtern erfolgt temporär und verändert die Datei nicht.
Sortieren überschreibt die Datei mit der neuen Reihenfolge.

Project Structure

ToDoApp
├── app.py – Einstiegspunkt und Hauptprogrammschleife
├── graphics.py – Konsolenausgabe und Menüführung
├── new.py – Neue Aufgaben erstellen
├── edit.py – Aufgaben bearbeiten
├── delete.py – Aufgaben löschen
├── status.py – Aufgabenstatus ändern
├── sort.py – Aufgaben sortieren
├── filter.py – Aufgaben filtern (temporär)
├── load.py – Laden und Anzeigen der Aufgaben
├── clear.py – Bildschirm leeren
└── daten
  └── tasks.txt – Persistente Datenspeicherung

Data Model

Jede Aufgabe besteht aus:

ID

Beschreibung

Priorität (A, B, C)

Status (offen / erledigt)

Erstellungsdatum

Fälligkeitsdatum

Die Daten werden zeilenweise in einer Textdatei gespeichert.
