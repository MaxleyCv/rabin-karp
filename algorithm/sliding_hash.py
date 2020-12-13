def get_entries(main_string: str, substring: str, fingerprint) -> list:
    """
    A function to implement sliding hash algorithm
    :param main_string: the parsable string
    :param substring: the substring to find
    :param fingerprint: fingerprint-df type class
    :return: list of positions of found fingerprint-df
    """
    entries = []
    current_substring = main_string[0:len(substring)]
    substring_hash = fingerprint.get_hash(substring)
    current_hash = fingerprint.get_hash(current_substring)
    for ending_position in range(len(substring), len(main_string)):
        current_hash = fingerprint.iterate_hash(current_hash, main_string[ending_position],
                                                main_string[ending_position - len(substring)],
                                                len(substring))
        if substring_hash == current_hash:
            current_substring = main_string[ending_position - len(substring) + 1: ending_position + 1]
            if current_substring == substring:
                entries.append(ending_position - len(substring) + 1)
    return entries