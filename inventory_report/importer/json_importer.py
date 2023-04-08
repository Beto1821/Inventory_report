# Importe a classe abstrata Importer, que JsonImporter herdará
from inventory_report.importer.importer import Importer

# Importe o módulo json para manipulação de arquivos JSON
import json


# Crie uma classe chamada JsonImporter que herda de Importer
class JsonImporter(Importer):
    # Defina um método estático chamado import_data
    #  que recebe um caminho de arquivo como entrada e retorna uma lista
    @staticmethod
    def import_data(filename: str) -> list:
        # Verifique se o arquivo é um arquivo JSON
        if filename.endswith(".json"):
            # Se for um arquivo JSON, abra o arquivo
            #  no modo leitura e carregue os dados usando o módulo json
            with open(filename, "r") as file:
                data = json.load(file)
                # Retorne os dados carregados
                return data
        # Se o arquivo não for JSON, levante um erro
        else:
            raise ValueError("Arquivo inválido")
