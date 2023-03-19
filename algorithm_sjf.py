# Program "algorithm_sjf.py" wykonuje specyficzne dla
# algorytmu SJF sortowanie czasów, które są następnie przekazywane
# do pliku "create_times.py" w celu wyliczenia pozostałych typów czasów.
# Poprzez funkcję sort_by_arrival_and_burst_time() sortuje nam
# zagnieżdżone listy odczytane z listy najpierw według czasu przybycia procesów,
# a następnie według czasów wykonywania się procesów.

# Funkcja sortująca dane testowe według czasu przybycia procesów
# od najkrótszego do najdłuższego, a następnie według czasu wykonywania
# procesów od najkrótszego do najdłuższego i w drugiej kolejności według
# czasów przybycia procesów od najkrótszego do najdłuższego.
def sort_by_arrival_and_burst_time(list_of_times):

    # Lista, w której umieszczamy posortowane czasy.
    sorted_times = []

    # Sortowanie według czasów przybycia procesów,
    # aby wyłapać proces, który zaczyna się
    # od najkrótszego czasu przybycia.
    list_of_times.sort(key=lambda x: (x[0], x[1]))

    # Deklaracja zmiennej, która będzie zliczać łączny czas
    # wyjściowy procesów. Przypisujemy jej na początku sumę
    # równą czasowi przybycia procesu oraz czasu wykonywania procesu.
    # Warto zaznaczyć, że proces ten jest pierwszym procesem.
    # Przy tym drugim indeksy mają następujące znaczenie:
    # - indeks zero oznacza wybór pierwszej listy zagnieżdżonej,
    # - indeks jeden oznacza wybór drugiego elementu listy zagnieżdżonej,
    # którym jest czas wykonywania procesu.
    exit_timer = list_of_times[0][0] + list_of_times[0][1]

    # Dodajemy do listy jako wyjątek proces o najniższym czasie
    # przybycia. Dzieje się tak, ponieważ pierwszy proces musi
    # mieć zawsze najniższy czas.
    sorted_times.append(list_of_times[0])

    # Usuwamy proces nr 1 z listy, którą odczytujemy, aby
    # w drugim sortowaniu wziąć pod uwagę tylko elementy
    # niedodane jeszcze do listy "sorted_times".
    del list_of_times[0]

    # Sortujemy listę według czasów wykonywania procesów od najniższego
    # do najwyższego, a w drugiej kolejności według czasów przybycia procesów
    # również od najniższego do najwyższego.
    list_of_times.sort(key=lambda x: (x[1], x[0]))

    # Pętla while wykonująca się do momentu, w którym lista przez nas odczytywana
    # nie zostanie całkowicie wyczyszczona z elementów, które usuwamy po dodaniu
    # ich do nowej posortowanej listy.
    while list_of_times:

        # Przechodzimy po kolei przez wszystkie elementy listy.
        for element in range(len(list_of_times)):

            # Sprawdzam, czy czas przybycia procesu, który ma się wykonać,
            # jest mniejszy lub równy czasowi wyjścia minionego procesu.
            if exit_timer >= list_of_times[element][0]:

                # Jeżeli warunek jest spełniony, to dodajemy proces na listę.
                sorted_times.append(list_of_times[element])

                # Następnie dodajemy czas wykonania procesu do czasu wyjścia procesów.
                exit_timer += list_of_times[element][1]

                # Usuwamy proces z listy, ponieważ został on dodany na posortowaną listę.
                del list_of_times[element]

                break

    return sorted_times
