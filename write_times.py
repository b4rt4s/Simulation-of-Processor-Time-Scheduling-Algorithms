# Program "write_times.py" dla danego zestawu danych zapisuje je
# w pliku "{name}_results_of_times/{name}_results_of_times{i}.txt",
# gdzie {name} oznacza nazwę algorytmu SJF lub FCFS, a {i} to numer
# od 1 do 20. Dokładniej mówiąc, zapisuje dane w 100 linijkach, gdzie
# każda z nich zawiera 5 liczb:
# 1. liczba: czas przybycia procesów,
# 2. liczba: czas wykonywania procesów,
# 3. liczba: czas wyjścia procesów,
# 4. liczba: czas cykli przetwarzania procesów,
# 5. liczba: czas oczekiwania procesów.

# Funkcja zapisująca wyniki czasów do plików.
def writing_to_file(list_of_times, name, i):

    # Utworzenie pliku tekstowego w odpowiednim folderze, do którego zapiszemy
    # czasy wygenerowane przez podany algorytm.
    with open(f"{name}_results_of_times/{name}_results_of_times{i}.txt", "w") as file:

        # Do pliku zapisujemy 100 linii zawierających 5 liczb oddzielonych spacjami.
        for line in list_of_times:
            file.write(f"{line[0]} {line[1]} {line[2]} {line[3]} {line[4]}\n")
