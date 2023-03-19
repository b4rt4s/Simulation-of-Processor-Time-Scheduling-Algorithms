# Program "test_data_create.py" tworzy dane testowe w postaci czasów
# przybycia i czasów wykonania procesów, które będą wykorzystane przez
# programy implementujące działanie algorytmów przydziału czasu procesora
# do wykonania symulacji. Dane zapisywane są do folderu "test_data".

# Moduł random potrzebny do generowania pseudolosowych danych.
import random


# Funkcja tworząca dane testowe do projektu.
# Do metody przekazujemy nr pliku, który jest częścią
# nazwy pliku, do którego będą zapisywane dane testowe.
def create_data(number_of_file):

    # Deklaracja pustych list, w których umieścimy wygenerowane dane.
    list1 = []
    list2 = []

    # Utworzenie pliku tekstowego, w którym umieścimy wygenerowane dane testowe.
    # Zmienna "number_of_file" przekazywana do funkcji jako argument jest
    # zadeklarowana w pliku głównym main i oznacza numer dopisywany do nazwy pliku,
    # który tworzymy. Plik testowy jest zapisywany w folderze "test_data".
    with open(f"test_data/test_data{number_of_file}.txt", "w") as file:

        # Losujemy 100 par liczb, które zostaną umieszczone w pliku.
        for line in range(1, 101):

            # Pierwsza wylosowana liczba z zakresu od 0 do 25 to czas przybycia procesu.
            num1 = random.randint(0, 25)

            # Druga wylosowana liczba z zakresu od 1 do 25 to czas wykonania procesu.
            num2 = random.randint(1, 25)

            # Dodajemy wylosowane czasy do odpowiednich list.
            list1.append(num1)
            list2.append(num2)

            # Zapisujemy wylosowane czasy do pliku tekstowego.
            # Każda linia zawiera 2 liczby.
            # Pierwsza liczba to czas przybycia procesu.
            # Druga liczba to czas wykonania procesu.
            file.write(f"{num1} {num2}\n")

    # Utworzenie pliku tekstowego w folderze "test_data" o nazwie "data_for_process_scheduling_solver.txt",
    # do którego dopisujemy wygenerowane dane w następującej postaci:
    # - pierwsza linia: czasy przybycia oddzielone spacjami,
    # - druga linia: czasy wykonania oddzielone spacjami,
    # - trzecia linia: znak nowej linii,
    # - kolejne linie: powtórzenie powyższych linii dla kolejnych danych, które pochodzą z pozostałych x plików.
    # Używam tego pliku do kopiowania wygenerowanych danych do kalkulatora online,
    # który potwierdza mi czy symulacja wykonała się prawidłowo.
    with open("test_data/data_for_process_scheduling_solver.txt", "a") as file:
        for line in list1:
            file.write(f"{line}, ")

        file.write("\n")

        for line in list2:
            file.write(f"{line}, ")

        file.write("\n\n")
