# Program "test_data_read.py" odczytuje dane testowe w postaci czasów
# przybycia i czasów wykonania procesów, które będą wykorzystane przez
# programy implementujące działanie algorytmów przydziału czasu procesora
# do wykonania symulacji.

# Funkcja "read_data" to funkcja odczytująca dane testowe z plików tekstowych.
# Do funkcji przekazujemy nr pliku, który jest częścią nazwy pliku,
# z którego będą odczytywane dane testowe.
def read_data(number_of_file):

    # Otworzenie pliku z danymi testowymi znajdującego się w folderze "test_data".
    with open(f"test_data/test_data{number_of_file}.txt") as file:

        # Umieszczenie w zmiennej "lines" listy, której elementami są
        # dwuelementowe listy zagnieżdżone. Pierwszy element to czas przybycia
        # procesu, a drugi element to czas wykonywania procesu.
        lines = [line.split() for line in file]

        # Utworzenie pustej listy, w której umieścimy listy dwuelementowe składające
        # się z wyżej wymienionych czasów.
        list_of_test_data = []

        # Zapis danych testowych do pustej listy, której elementami
        # są zagnieżdżone dwuelementowe listy.
        # Pierwsza liczba to czas przybycia procesu.
        # Druga liczba to czas wykonywania procesu.
        # Konwertujemy wartości czasów na typ całkowity.
        for element in lines:
            list_of_test_data.append([int(element[0]), int(element[1])])

    return list_of_test_data
