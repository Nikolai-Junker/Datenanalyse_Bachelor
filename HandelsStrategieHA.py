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

# Autokorrelationsfunktion (ACF) der Log-Returns zur Analyse der Zeitabhängigkeit 
plot_acf(r,title="acf der Log-Returns")
plt.show()
plot_acf(r,title="acf der Log-Returns",zero=False)
plt.show()

# Die folgenden Zeilen erstellen binäre Zeitreihen (True/False), die angeben, ob an einem bestimmten Tag in der Vergangenheit eine positive (für investiert1 und investiert4) oder negative (für investiert2, investiert3, investiert5 und investiert6) Rendite erzielt wurde.
investiert1 = np.append(np.repeat(False,40), r[0:-40]>0)
investiert2 = np.append(np.repeat(False,5), r[0:-5]<0)
investiert3 = np.append(np.repeat(False,2), r[0:-2]<0)
investiert4 = np.append(np.repeat(False,30), r[0:-30]>0)
investiert5 = np.append(np.repeat(False,27), r[0:-27]<0)
investiert6 = np.append(np.repeat(False,18), r[0:-18]<0)

# Die Funktion strategie bestimmt, ob an einem bestimmten Tag in die DAX investiert wird oder nicht. Sie gibt True zurück, wenn alle übergebenen Zeitreihen True sind, sonst False.
def strategie(arr1, arr2, arr3, arr4, arr5, arr6):
    investition = []
    for i in range(0, 8138):
        if((arr1[i]==True)&(arr2[i]==True)&(arr3[i]==True)&(arr4[i]==True)&(arr5[i]==True)&(arr6[i]==True)):
            investition.append(True)
        else:
            investition.append(False)
    return np.asarray(investition)

# Anwendung der Funktion strategie auf die oben erstellten Zeitreihen
investiert=strategie(investiert1,investiert2, investiert3, investiert4, investiert5, investiert6)

# Die folgenden Zeilen berechnen und drucken Statistiken für die mit der LAG 40 erstellte Handelsstrategie
# Die Bedeutung der Statistiken ist im jeweiligen print-Befehl erklärt
# Die verwendete Strategie besteht darin, nur zu investieren, wenn der Return an Tag t-40 positiv war

# Die gleichen Berechnungen und Ausgaben werden dann für die optimierte Handelsstrategie wiederholt
# Die optimierte Strategie besteht darin, nur zu investieren, wenn alle Bedingungen (Renditen an verschiedenen Tagen in der Vergangenheit) erfüllt sind.
