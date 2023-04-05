from datetime import datetime


class SimpleReport:
    @staticmethod
    def generate(products: list[dict]):
        # Calcula a data de fabricação mais antiga
        oldest_date = min([p["data_de_fabricacao"] for p in products])

        # Calcula a data de validade mais próxima
        today = datetime.today().date()
        closest_date = min(
            [
                p["data_de_validade"]
                for p in products
                if datetime.strptime(p["data_de_validade"], "%Y-%m-%d").date()
                >= today
            ]
        )

        # Calcula a empresa com mais produtos
        companies = {}
        for p in products:
            if p["nome_da_empresa"] in companies:
                companies[p["nome_da_empresa"]] += 1
            else:
                companies[p["nome_da_empresa"]] = 1
        # função max =>
        # https://cienciaprogramada.com.br/2022/04/funcao-max-em-python
        most_products_company = max(companies, key=companies.get)

        # Retorna o relatório
        report = f"Data de fabricação mais antiga: {oldest_date}\n"
        report += f"Data de validade mais próxima: {closest_date}\n"
        report += f"Empresa com mais produtos: {most_products_company}"
        return report
