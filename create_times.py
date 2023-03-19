# Program "create_times.py" dla danego zestawu danych oblicza
# czasy wyjścia, cyklu przetwarzania oraz oczekiwania procesów.
# Dane te zwracane są w formie listy zawierającej zagnieżdżone
# listy pięcioelementowe i wykorzystywane dalej przez program
# "write_times.py", który zapisuje je do pliku wynikowego.

# Funkcja implementująca ogólną część symulacji algorytmu planowania
# czasu procesora FCFS oraz SJF. Funkcja tworzy nam listy
# czasów wyjścia, cykli przetwarzania oraz oczekiwania procesów.
def create_list_of_times(list_of_data):
    # Przypisujemy do zmiennej "test_data" nasze dane testowe,
    # które zostały posortowane w pliku "algorithm_fcfs.py" lub
    # "algorithm_sjf.py".
    test_data = list_of_data

    # Tworzymy listę czasów wyjścia procesów, czyli czasów,
    # w których proces opuszcza procesor po całkowitym jego wykonaniu.
    exit_time = []

    # Tworzymy listę czasów cykli przetwarzania procesów,
    # czyli czasów różnicy między czasem wyjścia procesu i czasem jego przybycia.
    turn_around_time = []

    # Tworzymy listę czasów oczekiwania procesów.
    waiting_time = []

    # Tworzymy listę składająca się z 5 indeksów:
    # 1. indeks: czasy przybycia procesów,
    # 2. indeks: czasy wykonywania procesów,
    # 3. indeks: czasy wyjścia procesów,
    # 4. indeks: czasy cykli przetwarzania procesów,
    # 5. indeks: czasy oczekiwania procesów.
    times = []

    # W pętli for przemieszczamy się po liście składającej się
    # z zagnieżdżonych list, których elementami są
    # czasy przybycia i wykonywania procesów.
    for element in range(len(test_data)):

        # Dodawanie czasów wyjścia procesów do listy.
        if element == 0:

            # Pierwszy czas wyjścia jest równy sumie czasu przybycia i czasu wykonywania procesu.
            # Proces ten musi mieć najniższy czas przybycia ze wszystkich procesów.
            exit_time.append(test_data[element][0] + test_data[element][1])
        else:

            # Pozostałe czasy są równe sumie czasu wyjścia bieżącego procesu
            # i czasu wykonywania procesu, który był następny w kolejce.
            exit_time.append(exit_time[element - 1] + test_data[element][1])

        # Dodawanie czasów cykli przetwarzania procesów do listy.
        # Jest to różnica czasu wyjścia procesu i czasu przybycia procesu.
        turn_around_time.append(exit_time[element] - test_data[element][0])

        # Dodawanie czasów oczekiwania procesów do listy.
        if element == 0:

            # Pierwszy czas oczekiwania jest zawsze równy zero, ponieważ
            # pierwszy proces nie oczekuje na wykonanie, lecz przetwarza
            # się od razu.
            waiting_time.append(0)
        else:

            # Pozostałe czasy oczekiwania są równe różnicy czasu przetwarzania cyklu procesu
            # i czasu wykonywania procesu.
            waiting_time.append(turn_around_time[element] - test_data[element][1])

        # Dodawanie wszystkich typów czasów do jednej listy.
        # 1. indeks: czasy przybycia procesów,
        # 2. indeks: czasy wykonywania procesów,
        # 3. indeks: czasy wyjścia procesów,
        # 4. indeks: czasy cykli przetwarzania procesów,
        # 5. indeks: czasy oczekiwania procesów.
        times.append([test_data[element][0], test_data[element][1],
                      exit_time[element], turn_around_time[element],
                      waiting_time[element]])

    return times
