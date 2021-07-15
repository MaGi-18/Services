import threading
import psutil
import time


testliste = []
for i in range(1, 100):
    testliste.append(i)


def controller():
    while len(testliste) != 0:
        if psutil.virtual_memory().percent < 62:
            setEntryInPRTG()
        else:
            print("RAM-Auslastung zu hoch!")

        time.sleep(1)

def setEntryInPRTG():
        """
        Füge den ersten Eintrag aus der Liste über die API in PRTG ein.
        """
        #requests.post(testliste[0])

        """Lösche das soeben eingetragene Element aus der aktuellen Liste"""
        del testliste[0]
        print("Eintrag wurde erstellt!")




controller()


