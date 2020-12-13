from fingerprint import *
from fingerprint.fingerprint import Fingerprint


class HornerSchema(Fingerprint):
    """
    Class fot implementation of horner schema
    """
    def __init__(self, multiplier=10, mod=997):
        self.mod = mod
        self.multiplier = multiplier

    def get_hash(self, string):
        """
        Function to initialize hash through schema
        :param string: string to hash
        :return: hash
        """
        hash = 0
        for position in range(len(string)):
            hash += ord(string[position]) * self.multiplier ** (len(string) - position - 1)
        return hash % self.mod

    def iterate_hash(self, previous_hash, next_symbol, previous_symbol, length):
        """
        Function to slide a hash: we delete first symbol and add the last
        :param previous_hash: hash of previous substring
        :param next_symbol: next symbol to add
        :param previous_symbol: first symbol to pop from a substring
        :param length: length of substring
        :return: new hash of slided substring
        """
        return ((previous_hash - ord(previous_symbol) * self.multiplier ** (length - 1)) * self.multiplier +
                ord(next_symbol)) % self.mod
