import xml.etree.ElementTree as ET
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(file_path: str) -> list:
        if file_path.endswith(".xml"):
            products = []
            tree = ET.parse(file_path)
            root = tree.getroot()
            for product in root:
                product_dict = {}
                for attribute in product:
                    product_dict[attribute.tag] = attribute.text
                products.append(product_dict)
            return products
        else:
            raise ValueError("Arquivo inválido")
