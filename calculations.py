# Program "calculations.py" odczytuje pliki wynikowe zawierające
# pięć typów czasów, z których wybiera czasy przetwarzania cyklów
# procesów oraz czasy oczekiwania procesów. Następnie program oblicza
# średnią wspomnianych wcześniej czasów i zapisuje je do plików wynikowych.

# Importujemy z modułu statistics (Uwaga! Nie ze statistics_.py/)
# funkcję pozwalającą obliczyć odchylenie standardowe.
import statistics


# Program odczytujący czasy z plików wynikowych.
def read_results_of_time(name, i):

    # Otworzenie pliku z wynikami danego algorytmu.
    with open(f"{name}_results_of_times/{name}_results_of_times{i}.txt") as file:

        # Umieszczenie w zmiennej "lines" listy, której elementami są
        # pięcioelementowe listy zagnieżdżone.
        lines = [line.split() for line in file]

        # Utworzenie pustej listy, w której umieścimy czasy przetwarzania cyklu procesów
        # oraz czasy oczekiwania procesów.
        list_of_results = []

        # Zapis danych testowych do pustej listy, której elementami są dwuelementowe
        # listy zagnieżdżone liczb całkowitych.
        # Lista zagnieżdżona w liście "lines" wygląda następująco:
        # 1. liczba: czasy przybycia procesów,
        # 2. liczba: czasy wykonywania procesów,
        # 3. liczba: czasy wyjścia procesów,
        # 4. liczba: czasy cykli przetwarzania procesów,
        # 5. liczba: czasy oczekiwania procesów.
        for element in lines:
            list_of_results.append([int(element[3]), int(element[4])])

    return list_of_results


# Funkcja zwracająca średnie czasów:
# 1. średnia czasu oczekiwania procesu,
# 2. średnia czasu cyklu przetwarzania procesu.
def average_time(name, i):

    # Deklaracja zmiennych do sumowania czasów.
    sum_of_turn_around_time = 0
    sum_of_waiting_time = 0

    # Deklaracja zmiennej, w której zapisujemy listę czasów.
    times = read_results_of_time(name, i)

    # Sumowanie czasów.
    for time in times:
        sum_of_turn_around_time += time[0]
        sum_of_waiting_time += time[1]

    # Deklaracja listy, w której umieścimy średnie czasów.
    average_times = []

    # Obliczanie średnich czasów.
    average_turn_around_time = sum_of_turn_around_time / len(times)
    average_waiting_time = sum_of_waiting_time / len(times)

    # Dodanie średnich czasów do listy.
    average_times.append([average_turn_around_time, average_waiting_time])

    return average_times


# Funkcja zwracająca odchylenie standardowe czasów:
# 1. odchylenie standardowe czasu oczekiwania procesu,
# 2. odchylenie standardowe cyklu przetwarzania procesu.
def standard_deviation(name, i):

    # Deklaracja zmiennej, w której zapisujemy listę czasów.
    times = read_results_of_time(name, i)

    # Tworzymy dwie nowe listy, w których umieścimy poszczególne
    # czasy cykli przetwarzania procesów i czasy oczekiwania.
    list_of_turn_around_times = []
    list_of_waiting_times = []

    # Dodanie czasów do list
    for time in times:
        list_of_turn_around_times.append(time[0])
        list_of_waiting_times.append(time[1])

    # Deklaracja listy, w której umieścimy odchylenia standardowe czasów.
    standard_deviation_times = []

    # Obliczanie odchyleń standardowych czasów.
    standard_deviation_turn_around_time = statistics.stdev(list_of_turn_around_times)
    standard_deviation_waiting_time = statistics.stdev(list_of_waiting_times)

    # Dodanie odchyleń standardowych czasów do listy.
    standard_deviation_times.append([standard_deviation_turn_around_time, standard_deviation_waiting_time])

    return standard_deviation_times


# Funkcja zapisująca średnie czasów lub odchylenia standardowe do plików wynikowych
# w folderze "average_times", lub "standard_deviation_times".
def writing_to_file(list_of_average_times, name, name2):

    # Utworzenie pliku tekstowego, do którego zapiszemy średnie/odchylenia standardowe
    # czasów wygenerowane przez dany algorytm.
    # 1. Średnia/Odchylenie standardowe czasu oczekiwania procesu.
    # 2. Średnia/Odchylenie standardowe czasu cyklu przetwarzania procesu.
    with open(f"{name2}_times/{name}_{name2}_times.txt", "a") as file:
        for line in list_of_average_times:
            file.write(f"{line[0]} {line[1]}\n")
