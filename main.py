import user_io.io_manager as io_manager
import fingerprint.horner_schema as horner
from fingerprint.fingerprint import *
import algorithm.sliding_hash as algo

if __name__ == '__main__':
    string, substring = io_manager.read_strings("user_io/karp.in")
    horner_fingerprint = horner.HornerSchema()
    entries = algo.get_entries(string, substring, horner_fingerprint)
    io_manager.write_entries(entries, output_file="user_io/karp.out")
