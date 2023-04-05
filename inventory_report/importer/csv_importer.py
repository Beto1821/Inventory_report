from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @staticmethod
    def import_data(file_path: str) -> list:
        if file_path.endswith(".csv"):
            with open(file_path) as csvfile:
                reader = csv.DictReader(csvfile)
                products = [row for row in reader]
                return products
        else:
            raise ValueError("Formato de arquivo inválido")
