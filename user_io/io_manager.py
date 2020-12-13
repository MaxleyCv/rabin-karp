import sys

def read_strings(input_file="karp.in"):
    """
    Function to read the string and substring from the file
    :param input_file: file name
    :return: tuple: (string, substring)
    """
    with open(input_file, "r") as INPUT:
        output = INPUT.readlines()
        return tuple([string.rstrip('\n') for string in output])


def write_entries(data_iterable, output_file="karp.out"):
    """
    Function to flush the result to output files
    :param data_iterable: entries list of id's
    :param output_file: output filepath
    :return: none
    """
    with open(output_file, "w") as OUTPUT:
        for entry in data_iterable:
            OUTPUT.write(str(entry) + " ")
