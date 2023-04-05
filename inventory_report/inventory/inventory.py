from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json


class Inventory:
    @staticmethod
    def import_data(file_path: str, report_type: str):
        # Ler arquivo CSV ou JSON e armazenar dados em uma lista de dicionários
        if file_path.endswith(".csv"):
            with open(file_path) as csvfile:
                reader = csv.DictReader(csvfile)
                products = [row for row in reader]
        elif file_path.endswith(".json"):
            with open(file_path) as jsonfile:
                products = json.load(jsonfile)
        else:
            raise ValueError("Formato de arquivo inválido")
        # Gerar relatório correspondente ao tipo informado
        if report_type == "simples":
            return SimpleReport.generate(products)
        elif report_type == "completo":
            return CompleteReport.generate(products)
        else:
            raise ValueError("Tipo de relatório inválido")
