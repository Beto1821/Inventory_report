from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.complete_report import CompleteReport

from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @staticmethod
    def import_data(file_path: str, type: str):
        if file_path.endswith(".csv"):
            data = CsvImporter.import_data(file_path)
        elif file_path.endswith(".json"):
            data = JsonImporter.import_data(file_path)
        else:
            data = XmlImporter.import_data(file_path)

        if type == "simples":
            return SimpleReport.generate(data)
        else:
            return CompleteReport.generate(data)
