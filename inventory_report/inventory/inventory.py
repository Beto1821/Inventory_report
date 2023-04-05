from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv


class Inventory:
    @staticmethod
    def import_data(file_path: str, report_type: str):
        # Ler arquivo CSV e armazenar dados em uma lista de dicionários
        products = []
        with open(file_path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                products.append(row)

        # Gerar relatório correspondente ao tipo informado
        if report_type == 'simples':
            return SimpleReport.generate(products)
        elif report_type == 'completo':
            return CompleteReport.generate(products)
        else:
            raise ValueError('Tipo de relatório inválido')
