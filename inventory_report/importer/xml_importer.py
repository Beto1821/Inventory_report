# Importe o módulo ElementTree do XML
# e a classe abstrata Importer, que XmlImporter herdará
import xml.etree.ElementTree as ET
from inventory_report.importer.importer import Importer


# Crie uma classe chamada XmlImporter que herda de Importer
class XmlImporter(Importer):
    # Defina um método estático chamado import_data
    #  que recebe um caminho de arquivo como entrada e retorna uma lista
    @staticmethod
    def import_data(file_path: str) -> list:
        # Verifique se o arquivo é um arquivo XML
        if file_path.endswith(".xml"):
            # Se for um arquivo XML,
            #  crie uma lista vazia para armazenar os produtos
            products = []
            # Analise o arquivo XML usando o módulo ElementTree
            tree = ET.parse(file_path)
            # Obtenha a raiz do arquivo XML
            root = tree.getroot()
            # Itere sobre todos os produtos no arquivo XML
            for product in root:
                # Crie um dicionário vazio
                #  para armazenar os atributos do produto
                product_dict = {}
                # Itere sobre todos os atributos
                #  do produto e adicione-os ao dicionário
                for attribute in product:
                    product_dict[attribute.tag] = attribute.text
                # Adicione o dicionário de atributos do produto
                #  à lista de produtos
                products.append(product_dict)
            # Retorne a lista de produtos
            return products
        # Se o arquivo não for XML, levante um erro
        else:
            raise ValueError("Arquivo inválido")
