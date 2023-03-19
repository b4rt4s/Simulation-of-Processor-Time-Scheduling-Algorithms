# Program "algorithm_fcfs.py" wykonuje specyficzne dla
# algorytmu FCFS sortowanie czasów, które są następnie przekazywane
# do pliku "create_times.py" w celu wyliczenia pozostałych typów czasów.
# Poprzez funkcję sort_by_arrival_time() sortuje nam zagnieżdżone listy
# odczytane z listy według czasu przybycia procesów.


# Funkcja sortująca dane testowe według czasu przybycia procesów od najkrótszego do najdłuższego.
def sort_by_arrival_time(list_of_times):

    # Sortowanie według czasu przybycia procesów od najkrótszego do najdłuższego.
    # Dokładniej mówiąc sortujemy pierwszy element listy zagnieżdżonej w liście.
    list_of_times.sort(key=lambda x: x[0])

    return list_of_times
