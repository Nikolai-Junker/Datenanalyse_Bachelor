import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.graphics.tsaplots import plot_acf

# Laden der DAX-Daten aus einer Excel-Datei
DAX = pd.read_excel("DAX_lange_Reihe_bis_31.03.2020.xlsx")

# Erstellen einer Zeitreihe mit den Schlusskursen und den zugehörigen Daten
y = pd.Series(data = np.array(DAX["Close"]), index = np.array(DAX["Date"]))

# Ignorieren von Daten vor dem offiziellen Start des DAX am 01.01.1988
y = y["01.01.1988":]

# Entfernen von Tagen, an denen der DAX-Schlusskurs gleich dem Vortag ist (angenommen, diese sind Feiertage)
y = y[y.shift(1)!=y]

# Umwandeln der DAX-Schlusskurse in den Logarithmus 
x = np.log(y)

# Berechnen der Log-Returns (Änderungen des Logarithmus)
r = np.diff(x)

# Erzeugung von Autokorrelationsplots der Log-Returns zur Untersuchung ihrer zeitlichen Abhängigkeiten
plot_acf(r,title="acf der Log-Returns")
plt.show()
plot_acf(r,title="acf der Log-Returns",zero=False)
plt.show()

# Die folgenden Zeilen erstellen binäre Zeitreihen (True/False), die angeben, ob an einem bestimmten Tag in der Vergangenheit eine positive (für investiert1 und investiert4) oder negative (für investiert2, investiert3, investiert5 und investiert6) Rendite erzielt wurde.
investiert1 = np.append(np.repeat(False,40), r[0:-40]>0)  # prüft, ob der Return vor 40 Tagen positiv war
investiert2 = np.append(np.repeat(False,5), r[0:-5]<0)  # prüft, ob der Return vor 5 Tagen negativ war
investiert3 = np.append(np.repeat(False,2), r[0:-2]<0)  # prüft, ob der Return vor 2 Tagen negativ war
investiert4 = np.append(np.repeat(False,30), r[0:-30]>0)  # prüft, ob der Return vor 30 Tagen positiv war
investiert5 = np.append(np.repeat(False,27), r[0:-27]<0)  # prüft, ob der Return vor 27 Tagen negativ war
investiert6 = np.append(np.repeat(False,18), r[0:-18]<0)  # prüft, ob der Return vor 18 Tagen negativ war

# Die Funktion "strategie" generiert eine binäre Sequenz, die anzeigt, wann alle übergebenen Zeitreihen "True" sind, was impliziert, dass alle Investitionsbedingungen erfüllt sind.
def strategie(arr1, arr2, arr3, arr4, arr5, arr6):
    investition = []
    for i in range(0, 8138):
        if((arr1[i]==True)&(arr2[i]==True)&(arr3[i]==True)&(arr4[i]==True)&(arr5[i]==True)&(arr6[i]==True)):
            investition.append(True)
        else:
            investition.append(False)
    return np.asarray(investition)

# Anwendung der Strategiefunktion auf die erstellten Zeitreihen
investiert=strategie(investiert1,investiert2, investiert3, investiert4, investiert5, investiert6)

# Ausgabe der Ergebnisse für die erste Handelsstrategie (nur auf Basis von 'investiert1' entschieden)
print("LAG 40 Handelsstrategie:")
print("Investiert an", np.sum(investiert1), "Tagen")
print("Anteil am gesamten Zeitraum:",np.sum(investiert1)/(len(r )))
print("Durchschnitt Log-Returns an investierten Tagen:", np.mean(r[investiert1]))
print("Durchschnitt Log-Returns aller Tage:", np.mean(r))
print("Was würden aus 1000 Euro bei dauerhaften Investment?", 1000*np.exp(sum(r)))
print("Was würden aus 1000 Euro mit dieser Strategie?", 1000*np.exp(sum(r[investiert1])))
print("Bei Log-Return von 0.0001 (ca. 2,5% p.a)) an nicht investierten Tagen:", 1000*np.exp(sum(r[investiert1])+(len(r)-np.sum(investiert1))*0.0001))
print("Anzahl Transaktionen:", np.sum(investiert1[:-1] != investiert1[1:]))
print("Bei Log-Return von 0.0001 (ca. 2,5% p.a) an nicht investierten Tagen"+" und 0,1% Transaktionskosten:",1000*np.exp(sum(r[investiert1])+(len(r)-np.sum(investiert1))*0.0001-np.sum(investiert1[:-1] != investiert1[1:])*0.001))

# Ausgabe der Ergebnisse für die optimierte Handelsstrategie (entscheidet auf Basis aller 'investiert'-Arrays)
print("\n")
print("Optimierte Handelsstrategie:")
print("Investiert an", np.sum(investiert), "Tagen")
print("Anteil am gesamten Zeitraum:",np.sum(investiert)/(len(r )))
print("Durchschnitt Log-Returns an investierten Tagen:", np.mean(r[investiert]))
print("Durchschnitt Log-Returns aller Tage:", np.mean(r))
print("Was würden aus 1000 Euro bei dauerhaften Investment?", 1000*np.exp(sum(r)))
print("Was würden aus 1000 Euro bei dieser Strategie?", 1000*np.exp(sum(r[investiert])))
print("Bei Log-Return von 0.0001 (ca. 2,5% p.a)) an nicht investierten Tagen:", 1000*np.exp(sum(r[investiert])+(len(r)-np.sum(investiert))*0.0001))
print("Anzahl Transaktionen:", np.sum(investiert[:-1] != investiert[1:]))
print("Bei Log-Return von 0.0001 (ca. 2,5% p.a) an nicht investierten Tagen"+" und 0,1% Transaktionskosten:",1000*np.exp(sum(r[investiert])+(len(r)-np.sum(investiert))*0.0001-np.sum(investiert[:-1] != investiert[1:])*0.001))
