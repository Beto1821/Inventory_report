# Importe o módulo ABC para definir classes abstratas e métodos abstratos
from abc import ABC, abstractmethod


class Importer(ABC):
    # Defina um método estático abstrato chamado import_data
    #  que deve ser implementado por subclasses concretas de Importer
    @staticmethod
    @abstractmethod
    def import_data(file_path: str) -> list:
        # O método import_data deve ler os dados
        #  de um arquivo no caminho 'file_path'
        # e retorná-los como uma lista. Como este é um método abstrato,
        #  essa implementação deve ser feita por qualquer
        # classe que herda de Importer
        pass  # Placeholder statement for abstract method,
        # it should be implemented in the concrete subclasses.
