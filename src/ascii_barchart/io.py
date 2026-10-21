import csv  # CSV-Dateien einlesen
import os  # Prüfen, ob eine Datei existiert


def load_rows(csv_path):  # Funktion zum Einlesen der CSV-Datei
    if not os.path.isfile(csv_path):  # Prüfen, ob die Datei existiert
        raise FileNotFoundError(csv_path)  # Fehlermeldung, falls sie fehlt

    rows = []  # Leere Liste für die Daten erstellen

    with open(csv_path, newline="", encoding="utf-8") as file:  # Datei öffnen
        reader = csv.DictReader(file)  # CSV anhand der Spaltennamen lesen

        for row in reader:  # Jede Zeile einzeln durchgehen
            rows.append((  # Werte als Tupel in die Liste einfügen
                row["type"],  # Typ speichern, z. B. A
                float(row["value1"]),  # value1 in eine Zahl umwandeln
                float(row["value2"])  # value2 in eine Zahl umwandeln
            ))

    return rows  # Alle eingelesenen Daten zurückgeben