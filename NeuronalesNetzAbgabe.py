import numpy 

# Sigmoid-Funktion für die Aktivierungsfunktion des neuronalen Netzwerks
def sigmoidFunction(x):
    return 1.0/(1.0+numpy.exp(-x))

class neuralNetwork:
    # Initialisierung des Netzwerks
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        # Anzahl der Knoten in jeder Schicht setzen
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes

        # Initialisierung der Gewichtsmatrizen für die Schichten 
        # mit zufälligen normalverteilten Werten
        self.wih = numpy.random.normal(0.0, pow(self.inodes, -0.5), (self.hnodes, self.inodes))
        self.who = numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.onodes, self.hnodes))

        # Lernrate setzen
        self.lr = learningrate

        # Festlegen der Aktivierungsfunktion (Sigmoid-Funktion)
        self.activation_function = lambda x: sigmoidFunction(x)

    # Training des neuronalen Netzwerks
    def train(self, inputs_list, targets_list):
        # Input- und Target-Listen in zweidimensionale Arrays umwandeln
        inputs = numpy.array(inputs_list, ndmin=2).T
        targets = numpy.array(targets_list, ndmin=2).T

        # Berechnung der Signale in die versteckte Schicht und deren Ausgänge
        hidden_inputs = numpy.dot(self.wih, inputs)
        hidden_outputs = self.activation_function(hidden_inputs)

        # Berechnung der Signale in die Ausgabeschicht und deren Ausgänge
        final_inputs = numpy.dot(self.who, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)

        # Berechnung der Output- und versteckten Fehlers
        output_errors = targets - final_outputs
        hidden_errors = numpy.dot(self.who.T, output_errors) 

        # Aktualisierung der Gewichte zwischen der versteckten und Ausgabeschicht
        self.who += self.lr * numpy.dot((output_errors * final_outputs * (1.0 - final_outputs)), numpy.transpose(hidden_outputs))

        # Aktualisierung der Gewichte zwischen der Eingabe- und versteckten Schicht
        self.wih += self.lr * numpy.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)), numpy.transpose(inputs))
        
    # Abfrage des neuronalen Netzwerks
    def query(self, inputs_list):
        # Umwandlung der Input-Liste in ein zweidimensionales Array
        inputs = numpy.array(inputs_list, ndmin=2).T

        # Berechnung der Signale in die versteckte Schicht und deren Ausgänge
        hidden_inputs = numpy.dot(self.wih, inputs)
        hidden_outputs = self.activation_function(hidden_inputs)

        # Berechnung der Signale in die Ausgabeschicht und deren Ausgänge
        final_inputs = numpy.dot(self.who, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)

        # Rückgabe der Ausgänge
        return final_outputs
    
# Festlegung der Parameter des neuronalen Netzwerks
input_nodes = 784
hidden_nodes = 200
output_nodes = 10
learning_rate = 0.01

# Erzeugung der Netzwerkinstanz
n = neuralNetwork(input_nodes,hidden_nodes,output_nodes, learning_rate)

# Laden der Trainingsdaten
training_data_file = open("mnist_train.csv", 'r')
training_data_list = training_data_file.readlines()
training_data_file.close()

# Festlegung der Anzahl der Trainingsepochen
epochs = 5

# Training des neuronalen Netzwerks über mehrere Epochen
for e in range(epochs):
    for record in training_data_list:
        all_values = record.split(',')
        inputs = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
        targets = numpy.zeros(output_nodes) + 0.01
        targets[int(all_values[0])] = 0.99
        n.train(inputs, targets)

# Laden der Testdaten
test_data_file = open("mnist_test.csv", 'r')
test_data_list = test_data_file.readlines()
test_data_file.close()

# Initialisierung der Scorecard für die Testergebnisse
scorecard = []

# Testen des neuronalen Netzwerks und Sammeln der Ergebnisse
for record in test_data_list:
    all_values = record.split(',')
    correct_label = int(all_values[0])
    inputs = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
    outputs = n.query(inputs)
    label = numpy.argmax(outputs)
    
    # Prüfen, ob die Netzwerkvorhersage korrekt war, und das Ergebnis zur Scorecard hinzufügen
    if (label == correct_label):
        scorecard.append(1)
    else:
        scorecard.append(0)

# Umwandlung der Scorecard in ein Array und Berechnung der Leistung
scorecard_array = numpy.asarray(scorecard)
print ("performance = ", scorecard_array.sum() / scorecard_array.size)
