from abc import ABC, abstractmethod


class Fingerprint(ABC):
    """
    Abstract interface to implement different fingerprints
    """
    @abstractmethod
    def get_hash(self, string):
        pass

    @abstractmethod
    def iterate_hash(self, previous_hash, next_symbol, previous_symbol, length):
        pass
