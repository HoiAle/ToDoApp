import clear

def startbildschirm():
    try:
        with open("ascii/startbildschirm.txt", "r", encoding="utf-8") as file:
            ascii = file.read()
            print(ascii)
            print("")
    except FileNotFoundError:
        print("ASCII art file not found.")
        
    abbrechen = input("***** Weiter mit EINGABE-Taste ***** ")
    if abbrechen.strip().lower() == "donald trump":
        clear.clear()
        try:
            with open("ascii/idiot.txt", "r", encoding="utf-8") as file:
                ascii2 = file.read()
                print(ascii2)
                print("")
        except FileNotFoundError:
            print("ASCII art file not found.")
        exit()
    
def mainMenu():
    print("======================================================================================================")
    print("|                          \033[1;91mW I L L K O M M E N  B E I  D E R  T O D O  A P P\033[0m                         |")
    print("======================================================================================================")
    print("")
    
def navigation():
    print("[1]: Aufgabe hinzufügen")
    print("[2]: Aufgabe bearbeiten")
    print("[3]: Aufgabe löschen")
    print("[4]: Aufgabenstatus ändern")
    print("[5]: Augaben sortieren")
    print("[6]: Aufgaben filtern")
    print("[0]: Programm beenden")
    print("")
    
def newMenu():
    print("======================================================================================================")
    print("|                              \033[1;91mN E U E  A U F G A B E H I N Z U F Ü G E N\033[0m                            |")
    print("======================================================================================================")
    print("")

def taskOverview():
    print("\033[1;91m| ID    | Aufgabenbeschreibung                   | Priorität | Status    | Datum       | Fälligkeit  |\033[0m")
    print("======================================================================================================")
    
def taskOverviewFinishline():
    print("======================================================================================================")
    print("")

def edit():
    print("======================================================================================================")
    print("|                              \033[1;91mA U F G A B E  B E A R B E I T E N        \033[0m                            |")
    print("======================================================================================================")
    print("")

def delete():
    print("======================================================================================================")
    print("|                              \033[1;91mA U F G A B E   L Ö S C H E N             \033[0m                            |")
    print("======================================================================================================")
    print("")

def status():
    print("======================================================================================================")
    print("|                              \033[1;91mS T A T U S   Ä N D E R N                 \033[0m                            |")
    print("======================================================================================================")
    print("")

def sort():
    print("======================================================================================================")
    print("|                              \033[1;91mA U F G A B E  S O R T I E R E N          \033[0m                            |")
    print("======================================================================================================")
    print("")

def filtering():
    print("======================================================================================================")
    print("|                              \033[1;91mA U F G A B E  F I L T E R N              \033[0m                            |")
    print("======================================================================================================")
    print("")