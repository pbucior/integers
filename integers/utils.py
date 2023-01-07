from integers import exceptions


def read_file(file_name: str):
    try:
        file = open(file_name, "r")
        return file.read()
    except FileNotFoundError:
        print("Plik źródłowy nie istnieje")
        raise


def get_values(p_values: str):
    str_values = p_values.split(";")
    int_values = []
    for i in range(len(str_values)):
        try:
            int_value = int(str_values[i])
            if not 0 <= int_value <= 12:
                raise exceptions.WrongNumber("Liczby muszą być z przedziału 0-12")
            int_values.append(int_value)
        except ValueError:
            print("Wprowadzono błędną wartość")
            raise
    return int_values


def make_pairs(numbers):
    used_indexes = []
    pairs_list = []
    for idx1, value1 in enumerate(numbers):
        for idx2, value2 in enumerate(numbers):
            if idx1 < idx2 and idx1 not in used_indexes and idx2 not in used_indexes and value1 + value2 == 12:
                used_indexes.append(idx1)
                used_indexes.append(idx2)
                if value1 > value2:
                    pairs_list.append([value2, value1])
                else:
                    pairs_list.append([value1, value2])
    return pairs_list


def write_to_file(file_name, values):
    file = open(file_name, "w+")
    for i in range(len(values)):
        file.write(str(values[i]) + "\n")
    file.close()
