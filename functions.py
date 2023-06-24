import pandas as pd

import string


# funkcja do wczytanie danych z excela
# i zamiana ich na listę


def read_data_from_excel(file_path):
    df = pd.read_excel(file_path)
    return df.values.tolist()


# funkcja do filtracji danych oraz na poprawne znaki


def filtration(data):
    correct_data = []
    wrong_lines = 0
    correct_lines = 0
    chars = []
    chars.extend(string.ascii_letters)
    chars.extend(" ")

    for data_list in data:
        variable = True
        data_list[0] = str(data_list[0])
        correct_lines+=1
        for element in data_list[0]:
            if element not in chars:
                variable = False
                wrong_lines+=1;
                break
        if variable:
            correct_data.append(data_list)
    
    print(f"Zostalo usunietych {wrong_lines} nieprawidlowych lini kodu")
    print(f"Pozostalo {correct_lines-wrong_lines}")
    return correct_data


# zapis do nowego pliku
# treba podac ścieżke do pliku 
# i liste z poprawnymi danymi


def save_data_to_excel(output_file_path, correct_data):
    output_df = pd.DataFrame(correct_data)
    output_df.to_excel(output_file_path, index=False)

