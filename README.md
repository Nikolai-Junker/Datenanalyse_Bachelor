# Datenanalyse_Bachelor
Ein Auszug aus älteren Datenanalyse Projekten während meines Bachelorstudiums

## Monte Carlo Simulation für Knock-Out-Optionen

Das Python-Skript **BewertungAktienKnockoutSimulationOpt.py** verwendet die Monte Carlo Simulation, um den erwarteten Preis einer Knock-Out-Option zu ermitteln.

### Funktionsweise

Das Skript simuliert die Preisbewegungen einer Aktie über eine bestimmte Laufzeit mit gegebenen Marktparametern wie dem risikolosen Zinssatz und der Volatilität. Es führt 100.000 Simulationen durch und berechnet für jeden Tag den kumulierten Aktienpreis.

Eine Knock-Out-Schwelle ist definiert, und das Skript bestimmt, in welchen Simulationen der Aktienpreis unter diese Schwelle fällt ("Knock-Out"). In diesen Fällen wird die Option wertlos.

Für Simulationen ohne Knock-Out wird die Auszahlung am Ende der Laufzeit berechnet. Diese entspricht der Differenz zwischen dem Endpreis der Aktie und dem Ausübungspreis, falls diese Differenz positiv ist, und Null sonst. Die Auszahlungen werden dann auf den heutigen Wert abgezinst, um den erwarteten Preis der Option zu erhalten.

Schließlich berechnet das Skript den Preis der Option ohne Knock-Out nach dem Black-Scholes-Modell und gibt beide Preise aus.

### Nutzung

Das Skript kann ausgeführt werden, ohne dass Parameter übergeben werden müssen. Die notwendigen Marktparameter und Optionseigenschaften sind im Skript hardcodiert und können dort angepasst werden.

## DAX Handelsstrategie Analyse

Das Python-Skript **HandelsStrategieHA** analysiert historische DAX-Daten und implementiert mehrere Handelsstrategien, um deren Leistung zu bewerten.

### Funktionsweise

1. Zunächst werden die benötigten Bibliotheken importiert und die historischen DAX-Daten aus einer Excel-Datei geladen. Die Daten umfassen den Schlusskurs (`Close`) und das Datum (`Date`) jedes Handelstags.

2. Die Datenreihe wird so angepasst, dass sie ab dem offiziellen Startdatum des DAX, dem 1. Januar 1988, beginnt. Alle Tage, an denen der DAX-Wert identisch zum Vortag ist (was auf einen Feiertag hindeuten könnte), werden entfernt.

3. Der natürliche Logarithmus des DAX-Wertes wird berechnet, um die normalisierten Preisänderungen (logarithmierten Returns) zu ermitteln.

4. Die Autokorrelation der logarithmierten Returns wird geplottet, um eine visuelle Analyse der Daten zu ermöglichen.

5. Auf Basis der logarithmierten Returns werden mehrere Handelsstrategien implementiert. Dabei handelt es sich um einfache technische Handelsregeln, die auf der Beobachtung von vergangenen Preisbewegungen basieren. 

6. Jede Strategie entscheidet, ob an einem bestimmten Tag investiert wird oder nicht. Die Entscheidungen der einzelnen Strategien werden zu einer optimierten Gesamtstrategie kombiniert.

7. Schließlich werden für jede Strategie verschiedene Kennzahlen ausgegeben, wie z. B. die Anzahl der Handelstage, der durchschnittliche logarithmierte Return an Handelstagen und der Endwert einer hypothetischen Investition von 1.000 Euro. 

### Anforderungen

Zur Ausführung dieses Skripts sind folgende Python-Bibliotheken erforderlich:

- numpy
- matplotlib
- pandas
- statsmodels

Außerdem muss eine Excel-Datei mit historischen DAX-Daten verfügbar sein. Diese Datei muss die Spalten `Close` (für den Schlusskurs) und `Date` (für das Datum) enthalten.

### Nutzung

Es sollte sichergestellt werden, dass alle benötigten Bibliotheken installiert wurden und die DAX-Daten in der gleichen Verzeichnisebene wie das Skript vorliegen. Anschließend kann das Skript einfach ausgeführt werden. Die Ergebnisse der Handelsstrategien werden in der Konsole ausgegeben.
Die Handelsstrategien können angepasst oder erweitert werden, indem Sie weitere Bedingungen für das Array `investiert` definieren und diese in die Funktion `strategie()` einfügen.

### Ausgabe

Die Ausgabe des Skripts enthält Informationen zur Leistung jeder Handelsstrategie, wie z.B. die Anzahl der Tage, an denen investiert wurde, den durchschnittlichen logarithmierten Return an diesen Tagen und den hypothetischen Endwert einer ursprünglichen Investition von 1.000 Euro. Zusätzlich werden potenzielle Transaktionskosten berücksichtigt.

## Einfaches neuronales Netzwerk zur Handschriften-Erkennung

Das Python-Skript **NeuronalesNetzAbgabe** implementiert ein einfaches künstliches neuronales Netzwerk zur Klassifizierung von Bildern aus dem MNIST-Datensatz von handschriftlichen Ziffern. 

### Code-Struktur

#### Sigmoid-Funktion

Die Sigmoid-Funktion wird als Aktivierungsfunktion für die Neuronen im Netzwerk verwendet. Sie wandelt die Eingaben der Neuronen (gewichtete Summe der Inputs) in Werte zwischen 0 und 1 um.

#### Neuronales Netzwerk-Klasse

Die Hauptklasse in diesem Skript ist die `neuralNetwork`-Klasse. Sie stellt das neuronale Netzwerk dar und enthält Methoden zum Trainieren (`train`) und Abfragen (`query`) des Netzwerks. 

#### Netzwerk-Initialisierung

Die Netzwerk-Initialisierung erfolgt im Konstruktor der `neuralNetwork`-Klasse. Hier werden die Anzahl der Knoten in jeder Schicht (Eingabe-, versteckte, Ausgabe-Schicht), die Gewichtsmatrizen zwischen den Schichten und die Lernrate festgelegt. 

#### Netzwerk-Training

Das Training des Netzwerks erfolgt durch die Methode `train`. Sie nimmt eine Liste von Inputs und eine Liste von erwarteten Outputs (Targets) entgegen. Sie berechnet dann die Ausgaben des Netzwerks für die gegebenen Eingaben und aktualisiert die Gewichtsmatrizen basierend auf den Fehlern der Netzwerkausgaben im Vergleich zu den erwarteten Ausgaben.

#### Netzwerk-Abfrage

Die Abfrage des Netzwerks erfolgt durch die Methode `query`. Sie nimmt eine Liste von Inputs entgegen und liefert die Ausgaben des Netzwerks für diese Inputs.

#### Training und Testing des Netzwerks

Nachdem das Netzwerk erstellt wurde, wird es auf der Grundlage eines Teils des MNIST-Datensatzes trainiert. Dann wird es mit einem anderen Teil des Datensatzes getestet, und die Leistung des Netzwerks wird anhand der Übereinstimmung zwischen den Netzwerkausgaben und den tatsächlichen Labels der Testdaten bewertet.

## Aktienvolumenvorhersage für die VW-Aktie

Das Skript **VW-Volumen-Prognose-Abgabe** verwendet Maschinelles Lernen, um das Volumen der VW-Aktie vorherzusagen. Es nutzt sowohl ein Gradient Boosting Modell als auch ein Neuronales Netzwerk (MLP Regressor) für die Vorhersage.

### Funktionsweise des Skripts

1. **Datenimport und -bereinigung**: Das Skript beginnt mit dem Importieren der Daten aus einer CSV-Datei und führt dann mehrere Reinigungsschritte durch. Die Reinigung umfasst das Entfernen von Zeilen mit fehlenden oder gleichen Volumen-, Close- und Adj Close-Werten. Zudem werden Ausreißer auf Grundlage des Z-Scores identifiziert und entfernt.

2. **Daten-Transformation**: Danach werden die 'Volume' und 'Adj Close' Daten durch eine Z-Transformation standardisiert. Der Close-Wert wird logarithmiert und ebenfalls standardisiert, um den Einfluss von Ausreißern zu reduzieren.

3. **Feature Engineering**: Anschließend werden neue Merkmale erstellt, indem das Volumen für verschiedene Zeitfenster verschoben wird.

4. **Aufteilen der Daten**: Die Daten werden in ein Trainings- und ein Testset aufgeteilt. Das Trainingsset enthält alle Daten bis zum 31.08.2016, während das Testset alle Daten ab dem 01.09.2016 enthält.

5. **Modelltraining und -auswertung**: Schließlich werden zwei Modelle, ein Gradient Boosting Regressor und ein Neuronales Netzwerk, trainiert und evaluiert. Die Genauigkeit der Modelle wird auf den Trainings- und Testdaten berechnet und ausgegeben.

### Verwendete Modelle

1. **Gradient Boosting Regressor**: Dieses Modell ist eine Art von Ensemble-Lernmethode, die mehrere schwache Vorhersagemodelle in ein einziges starkes Modell kombiniert. In diesem Fall wird das Modell mit einer maximalen Tiefe von 5, einer Mindestanzahl von 150 Samples für einen Split und 30 Samples für ein Blatt sowie einer Lernrate von 0,09 trainiert.

2. **MLP Regressor**: MLP steht für "Multilayer Perceptron", eine Art von neuronalem Netzwerk. In diesem Fall wird das MLP auf den gleichen Daten trainiert wie der Gradient Boosting Regressor. Die maximale Anzahl von Iterationen für das MLP ist auf 500 eingestellt.
