# Datenanalyse_Bachelor
Ein Auszug aus älteren Datenanalyse Projekten während meines Bachelorstudiums

## Monte Carlo Simulation für Knock-Out-Optionen

Das Python-Skript **BewertungAktienKnockoutSimulation** verwendet die Monte Carlo Simulation, um den erwarteten Preis einer Knock-Out-Option zu ermitteln.

### Funktionsweise

Das Skript simuliert die Preisbewegungen einer Aktie über eine bestimmte Laufzeit mit gegebenen Marktparametern wie dem risikolosen Zinssatz und der Volatilität. Es führt 100.000 Simulationen durch und berechnet für jeden Tag den kumulierten Aktienpreis.

Eine Knock-Out-Schwelle ist definiert, und das Skript bestimmt, in welchen Simulationen der Aktienpreis unter diese Schwelle fällt ("Knock-Out"). In diesen Fällen wird die Option wertlos.

Für Simulationen ohne Knock-Out wird die Auszahlung am Ende der Laufzeit berechnet. Diese entspricht der Differenz zwischen dem Endpreis der Aktie und dem Ausübungspreis, falls diese Differenz positiv ist, und Null sonst. Die Auszahlungen werden dann auf den heutigen Wert abgezinst, um den erwarteten Preis der Option zu erhalten.

Schließlich berechnet das Skript den Preis der Option ohne Knock-Out nach dem Black-Scholes-Modell und gibt beide Preise aus.

### Nutzung

Das Skript kann ausgeführt werden, ohne dass Parameter übergeben werden müssen. Die notwendigen Marktparameter und Optionseigenschaften sind im Skript hardcodiert und können dort angepasst werden.
