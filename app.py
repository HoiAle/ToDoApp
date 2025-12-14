# Imports
import sort
import graphics
import clear
import new
import load
import edit
import delete
import status
import filter

# Startbildschirm
clear.clear()
graphics.startbildschirm()


# Hauptprogramm
while (True):
    # Bildschirm löschen
    clear.clear()
    
    # Aufgabenübersicht einfügen
    graphics.mainMenu()
    graphics.taskOverview()
    load.taskOverview()
    graphics.taskOverviewFinishline()
    graphics.navigation()
    
    # Abfrage was getan werden soll
    eingabe = input("Was möchtest du tun? :/> ")
    
    # Neue Aufgabe hinzufügen
    if (eingabe=="1"):
        clear.clear()
        new.newTask()

    # Aufgabe bearbeiten
    if (eingabe == "2"):
        clear.clear()
        graphics.edit()
        graphics.taskOverview()
        load.taskOverview()
        graphics.taskOverviewFinishline()
        edit.findCounter()

    # Aufgabe löschen
    if (eingabe == "3"):
        clear.clear()
        graphics.delete()
        graphics.taskOverview()
        load.taskOverview()
        graphics.taskOverviewFinishline()
        delete.deleteTask()

    # Status ändern
    if (eingabe == "4"):
        clear.clear()
        graphics.status()
        graphics.taskOverview()
        load.taskOverview()
        graphics.taskOverviewFinishline()
        status.change()

    if (eingabe == "5"):
        clear.clear()
        graphics.sort()
        graphics.taskOverview()
        load.taskOverview()
        graphics.taskOverviewFinishline()
        sort.sort()

    if (eingabe == "6"):
        clear.clear()
        graphics.filtering()
        graphics.taskOverview()
        load.taskOverview()
        graphics.taskOverviewFinishline()
        filter.filtern()

    if (eingabe=="0"):
        break
