# Importe a classe abstrata Importer, que CsvImporter herdará
from inventory_report.importer.importer import Importer

# Importe o módulo csv para manipulação de arquivos CSV
import csv


# Crie uma classe chamada CsvImporter que herda de Importer
class CsvImporter(Importer):
    # Defina um método estático chamado import_data
    #  que recebe um caminho de arquivo como entrada e retorna uma lista
    @staticmethod
    def import_data(file_path: str) -> list:
        # Verifique se o arquivo é um arquivo CSV
        if file_path.endswith(".csv"):
            # Se for um arquivo CSV, abra o arquivo no modo leitura
            #  e crie um objeto reader do módulo csv
            with open(file_path) as csvfile:
                reader = csv.DictReader(csvfile)
                # Crie uma lista de dicionários
                #  para armazenar cada linha do arquivo CSV como um dicionário
                products = [row for row in reader]
                # Retorne a lista de dicionários
                return products
        # Se o arquivo não for CSV, levante um erro
        else:
            raise ValueError("Arquivo inválido")
