# Program "main.py" zarządza procesem całej symulacji.
# Krótko mówiąc, łączy ze sobą wszystkie pliki w jedną całość.

# Importowanie modułów plików projektu.
import test_data_create
import test_data_read
import algorithm_fcfs
import algorithm_sjf
import create_times
import write_times
import calculations
import statistics_

# Importowanie modułu "os", który pozwala m.in. na usuwanie pliku.
import os

# Lista ścieżek do plików, które chcemy usuwać przy każdym nowym załadowaniu
# programu "main.py"
list_of_paths = ["test_data/data_for_process_scheduling_solver.txt", "average_times/fcfs_average_times.txt",
                 "average_times/sjf_average_times.txt", "average_times/sjf_average_times.txt",
                 "average_times/sjf_average_times.txt", "standard_deviation_times/fcfs_standard_deviation_times.txt",
                 "standard_deviation_times/sjf_standard_deviation_times.txt"]

# Usuwanie plików przy każdym nowym załadowaniu programu "main.py".
for path in list_of_paths:
    if os.path.isfile(path):
        os.unlink(path)

# Przeprowadzenie 20 symulacji planowania czasu procesora dla zamkniętej
# puli zadań.
for i in range(1, 21):
    # Utworzenie danych potrzebnych do wykonania pojedynczej symulacji.
    test_data_create.create_data(i)

    # Odczyt i sortowanie czasów przybycia i wykonywania procesów według odpowiednich algorytmów.
    read_and_sort_times1 = algorithm_fcfs.sort_by_arrival_time(test_data_read.read_data(i))
    read_and_sort_times2 = algorithm_sjf.sort_by_arrival_and_burst_time(test_data_read.read_data(i))

    # Stworzenie listy czasów wyjścia, cykli przetwarzania oraz oczekiwania procesów.
    create_times1 = create_times.create_list_of_times(read_and_sort_times1)
    create_times2 = create_times.create_list_of_times(read_and_sort_times2)

    # Zapis do pliku wyników uzyskanych czasów dla obu algorytmów.
    write_times.writing_to_file(create_times1, 'fcfs', i)
    write_times.writing_to_file(create_times2, 'sjf', i)

    # Odczyt czasów cykli przetwarzania oraz oczekiwania procesów,
    # obliczenie ich średnich, odchyleń standardowych oraz zapis wyników do odpowiednich plików.
    calculations.writing_to_file(calculations.average_time('fcfs', i), 'fcfs', 'average')
    calculations.writing_to_file(calculations.average_time('sjf', i), 'sjf', 'average')
    calculations.writing_to_file(calculations.standard_deviation('fcfs', i), 'fcfs', 'standard_deviation')
    calculations.writing_to_file(calculations.standard_deviation('sjf', i), 'sjf', 'standard_deviation')

# Stworzenie danych statystycznych na bazie średnich czasów dla obu algorytmów.
statistics_.statistics_calculations('fcfs')
statistics_.statistics_calculations('sjf')
