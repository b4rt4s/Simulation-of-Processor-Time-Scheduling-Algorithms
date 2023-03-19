# W programie "statistics_.py" korzystając z modułu "numpy"
# dokonujemy statystycznych obliczeń takich jak odchylenie
# standardowe, które zapisujemy do pliku wynikowego.

import numpy as np


# Funkcja odczytująca średnie czasy przetwarzania cyklu procesu
# oraz średnie czasy oczekiwania procesu, a następnie obliczająca
# dane statystyczne i zapisująca je do pliku wynikowego w folderze
# "statistics".
def statistics_calculations(name):

    # Odczytujemy pliki wynikowe ze średnią czasów.
    file = open(f"average_times/{name}_average_times.txt")

    # Deklarujemy listę, do której zapisujemy odczytane średnie czasów
    content_list = file.read().split()

    # Deklarujemy puste listy na średnie poszczególnych czasów.
    average_turn_around_times = []
    average_waiting_times = []

    # W pętli for zapisujemy do list nasze średnie czasów.
    for element in range(len(content_list)):

        # Elementy parzyste to średnie cyklu przetwarzania procesu.
        # Elementy nieparzyste to średnia cyklu oczekiwania procesu.
        if element % 2 == 0:
            average_turn_around_times.append(float(content_list[element]))
        else:
            average_waiting_times.append(float(content_list[element]))

    # Tworzymy specjalne listy średnich czasu, aby skorzystać z modułu "numpy".
    statistics_for_turn_around_time = np.array(average_turn_around_times)
    statistics_for_waiting_time = np.array(average_waiting_times)

    # Zapisujemy do pliku wynikowego dane statystyczne na podstawie
    # poszczególnych średnich czasu
    with open(f"statistics/statistics_for_{name}.txt", "w") as file:
        file.write(f"Algorytm FCFS:\n\n"
                   f"Dane statystyczne dla srednich czasow cykli procesow\n"
                   f"Suma: {statistics_for_turn_around_time.sum()}\n"
                   f"Najwieksza: {statistics_for_turn_around_time.max()}\n"
                   f"Najmniejsza: {statistics_for_turn_around_time.min()}\n"
                   f"Srednia: {statistics_for_turn_around_time.mean()}\n"
                   f"Wariancja: {statistics_for_turn_around_time.var()}\n"
                   f"Odch. stand: {statistics_for_turn_around_time.std()}\n\n"
                   f"Dane statystyczne dla srednich czasow oczekiwania procesow\n"
                   f"Suma: {statistics_for_waiting_time.sum()}\n"
                   f"Najwieksza: {statistics_for_waiting_time.max()}\n"
                   f"Najmniejsza: {statistics_for_waiting_time.min()}\n"
                   f"Srednia: {statistics_for_waiting_time.mean()}\n"
                   f"Wariancja: {statistics_for_waiting_time.var()}\n"
                   f"Odch. stand: {statistics_for_waiting_time.std()}\n")
