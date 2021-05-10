from abc import ABC


class AbstractReader(ABC):
    def read(self, file_path):
        raise NotImplementedError
