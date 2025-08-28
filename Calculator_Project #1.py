#Taschenrechnerprojekt
import time

print("========================================================")
print("    D I G I T A L E R - T A S C H E N R E C H N E R"    )
print("========================================================")
time.sleep(1)
print ()
print ()
print ()


while True:
    try:
        zahl_1= float(input (f"Gib hier eine Zahl ein: --> "))
        time.sleep (0.1)
        print()
        print()
    except ValueError:
        print() 
        print()
        print("Bitte gib ein Wert an!")
        time.sleep (0.5)
        print()
        print()
        break
        
    operator_1= float(input (f"""Gib für den gewünschten Operator die entsprechende Zahl an:
                        1. Addition
                        2. Subtraktion
                        3. Multiplikation
                        4. Division
                        0. Beenden

                        Eingegebene Zahl:  """))
    time.sleep (0.1)
    if operator_1 == 0:
        print (f"Programm beendet.")
        time.sleep (0.5)
        print()
        print()
        break

    try:
        zahl_2= float(input (f"Gib eine Zahl ein: "))
        time.sleep (0.1)
        print()
        print()
    except ValueError:
        print()
        print()
        print (f"Bitte gib ein Wert ein!")
        time.sleep (0.5)
        print()
        break

    if operator_1 == 1:
        ergebnis= zahl_1 + zahl_2
        operator_1 = "+" 
    elif operator_1 == 2:
        ergebnis= zahl_1 - zahl_2
        operator_1 = "-"
    elif operator_1 == 3:
        ergebnis= zahl_1 * zahl_2
        operator_1 = "*"
    elif operator_1 == 4:
        ergebnis= zahl_1 / zahl_2
        operator_1 = ":"
    else:
        print()
        print()
        print ("ungültige Eingabe") 
        time.sleep (0.5)
        break



    ergebnis_dezi= ergebnis
    ergebnis= int(ergebnis)

    print (f"Berechnet wurde", zahl_1, operator_1, zahl_2)
    time.sleep (1)
    print (f"Das Ergebnis ist: {ergebnis} oder in Dezimalzahl: {ergebnis_dezi}")
    print()
    print ()
    time.sleep (0.5)

    frage= input ("Möchtest du eine neue Rechnung durchführen? ")

    if frage.lower () == "ja":
        time.sleep (0.2)
        print() 
        print() 
        continue
    else:
        print() 
        print() 
        print ("Programm beendet")
        print() 
        print() 
        break 