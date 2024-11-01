import pandas as pd

# Wczytanie pierwszego pliku Excela i pobranie etykiet z pierwszej kolumny
def get_labels_from_first_file(file_path):
    df = pd.read_excel(file_path, usecols=[0], header=None)  # Wczytujemy tylko pierwszą kolumnę bez nagłówka
    labels = df[0].dropna().unique()  # Pobieramy unikalne, niepuste wartości jako etykiety
    print("Etykiety pobrane z pierwszego pliku Excel:", labels)  # Wyświetlamy etykiety dla diagnostyki
    return set(labels)  # Zwracamy jako zestaw (set), aby szybciej sprawdzać obecność etykiet

# Filtracja kolumn w pliku CSV na podstawie etykiet
def filter_columns_in_csv(input_file, labels_set, output_file):
    # Używamy delimiter=";" i quotechar='"', aby poprawnie rozdzielić kolumny
    df = pd.read_csv(input_file, delimiter=";", quotechar='"', on_bad_lines="skip")  
    print("Kolumny w drugim pliku CSV:", df.columns.tolist())  # Wyświetlamy kolumny dla diagnostyki
    filtered_df = df[df.columns[df.columns.isin(labels_set)]]  # Zachowujemy tylko kolumny, których etykiety są w zbiorze
    print("Kolumny po filtrowaniu:", filtered_df.columns.tolist())  # Wyświetlamy kolumny po filtrowaniu
    filtered_df.to_excel(output_file, index=False)  # Zapisujemy przefiltrowany plik do nowego pliku Excel

# Ścieżki do plików
first_file_path = r"D:\studia\analiza_danych\ela_analysis\data\graduates-major-dictionary.xlsx"
second_file_path = r"D:\studia\analiza_danych\ela_analysis\graduates-major-data.csv"
output_file_path = r"D:\studia\analiza_danych\ela_analysis\graduates-major-data_filtered.xlsx"

# Proces
labels_set = get_labels_from_first_file(first_file_path)
filter_columns_in_csv(second_file_path, labels_set, output_file_path)

print(f"Nowy przefiltrowany plik został zapisany jako {output_file_path}")
