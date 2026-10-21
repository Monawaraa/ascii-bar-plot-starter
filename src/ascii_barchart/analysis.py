def average_value1_by_type(rows):  # Mittelwert für jeden Typ berechnen
    sums = {}  # Summe von value1 für jeden Typ speichern
    counts = {}  # Anzahl der Werte für jeden Typ speichern

    for point_type, value1, _value2 in rows:  # Alle Daten durchgehen
        sums[point_type] = sums.get(point_type, 0.0) + value1  # Werte addieren
        counts[point_type] = counts.get(point_type, 0) + 1  # Anzahl erhöhen

    result = []  # Leere Liste für die Ergebnisse erstellen

    for point_type in sorted(sums):  # Typen alphabetisch durchgehen
        average = sums[point_type] / counts[point_type]  # Mittelwert berechnen
        result.append((point_type, round(average, 2)))  # Typ und Mittelwert speichern

    return result  # Ergebnisse zurückgeben
