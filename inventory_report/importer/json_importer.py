from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @staticmethod
    def import_data(filename: str) -> list:
        if filename.endswith('.json'):
            with open(filename, 'r') as file:
                data = json.load(file)
                return data
        else:
            raise ValueError("Arquivo inválido")
