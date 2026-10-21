from ascii_barchart.io import load_rows  # CSV-Funktion importieren
from ascii_barchart.analysis import average_value1_by_type  # Auswertungsfunktion importieren

rows = load_rows("data/points.csv")  # CSV-Datei einlesen
averages = average_value1_by_type(rows)  # Mittelwerte berechnen

for point_type, average in averages:  # Ergebnisse durchgehen
    print(point_type, average)  # Typ und Mittelwert ausgeben