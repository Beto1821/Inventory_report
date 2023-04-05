from .simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, produtcs: list[dict]):
        # Chama o método generate da classe pai
        data = SimpleReport().generate(produtcs)
        # print(data)

        # Obtendo a data de fabricação mais antiga,
        #  a data de validade mais próxima
        # e a empresa com mais produtos
        # a partir do resultado do método generate da classe pai
        oldest_fabrication_date = "".join(data[32:42])
        closest_expiration_date = "".join(data[74:84])
        company_with_most_products = "".join(data[112:121])
        # Obtendo uma lista com o nome das empresas dos produtos
        # e contando a quantidade de produtos de cada empresa com o Counter
        company = [p["nome_da_empresa"] for p in produtcs]
        products_by_company = Counter(company)
        # print(products_by_company)

        #  saida
        report = f"Data de fabricação mais antiga: {oldest_fabrication_date}\n"
        report += f"Data de validade mais próxima: {closest_expiration_date}\n"
        report += f"Empresa com mais produtos: {company_with_most_products}\n"
        report += "Produtos estocados por empresa:\n"
        for company, num_products in products_by_company.items():
            report += f"- {company}: {num_products}\n"
        #   print(f"{company} {num_products}")
        return report
