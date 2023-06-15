import numpy as np
from scipy import stats
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.neural_network import MLPRegressor

# Funktion zur Durchführung der Z-Transformation, welche die Daten standardisiert
def zTransformation(x):
    return((x-np.mean(x))/np.std(x,ddof=1))

# Einlesen der CSV-Datei, die Daten zur VW-Aktie enthält
data = pd.read_csv("VOW3.DE.Daten.csv")

# Reinigung der Daten durch Entfernen von Reihen mit fehlenden oder gleichbleibenden Werten im Volume, Close und Adj Close
data = data[data["Volume"].shift(1) != data["Volume"]]
data = data[data["Volume"] != 0]
data = data[data["Volume"].notna()]
data = data[data["Close"].shift(1) != data["Close"]]
data = data[data["Close"] != 0]
data = data[data["Close"].notna()]
data = data[data["Adj Close"].shift(1) != data["Adj Close"]]
data = data[data["Adj Close"] != 0]
data = data[data["Adj Close"].notna()]

# Entfernen von Ausreißern im Volume basierend auf dem Z-Score
z = np.abs(stats.zscore(data.Volume))
data = data[(z < 3)]

# Standardisierung des Volume und Adj Close durch Z-Transformation
data["Volume"] = zTransformation(data["Volume"])
data["Adj Close"] = zTransformation(data["Adj Close"])

# Logarithmische Transformation des Close zur Reduzierung des Einflusses von Ausreißern
# Und anschließende Standardisierung
data["logVW"] = np.log(np.array(data["Close"]))
data["logClose"] = np.append(np.NaN, zTransformation(np.diff(data["logVW"])))

# Verschieben des Volumes um verschiedene Zeitfenster zur späteren Nutzung als Input-Features
data["shift1"] = data["Volume"].shift(1)
data["shift2"] = data["Volume"].shift(2)
data["shift3"] = data["Volume"].shift(3)
data["shift4"] = data["Volume"].shift(4)
data["shift5"] = data["Volume"].shift(5)

# Aufteilen der Daten in Trainings- und Testsets (80% Trainingsdaten, 20% Testdaten)
dataTrain = data[data["Date"] <= "2016-08-31"]
dataTest = data[data["Date"] >= "2016-09-01"]

# Festlegen der Eingabemerkmale und des Ziels für das Training
xTrain = dataTrain[["shift5","shift4","shift3","shift2","shift1", "logClose", "Adj Close"]]
xTrain = xTrain[5:]
yTrain = dataTrain["Volume"]
yTrain = yTrain[5:]

# Festlegen der Eingabemerkmale und des Ziels für den Test
xTest = dataTest[["shift5","shift4","shift3","shift2","shift1", "logClose", "Adj Close"]]
xTest = xTest[5:]
yTest = dataTest["Volume"]
yTest = yTest[5:]

# Trainieren eines Gradient Boosting Regressors und Ausgabe der Trainings- und Test-Genauigkeiten
print("GradientBoost")
GB = GradientBoostingRegressor(max_depth=5, min_samples_split=150, min_samples_leaf=30, learning_rate=0.09)
GB.fit(X=xTrain, y=yTrain)
print("Training:", GB.score(X=xTrain,y=yTrain))
print("Test:", GB.score(X=xTest,y=yTest))

# Trainieren eines Neuronalen Netzwerks und Ausgabe der Trainings- und Test-Genauigkeiten
print("\nNeuronales Netz")
NN = MLPRegressor(max_iter=500)
NN.fit(X=xTrain, y=yTrain)
print("Training:", NN.score(X=xTrain,y=yTrain))
print("Test:", NN.score(X=xTest,y=yTest))
