from datetime import datetime


class SimpleReport:
    @staticmethod
    def generate(products):
        # Calcula a data de fabricação mais antiga
        oldest_date = min(
            [
                datetime.strptime(p["data_de_fabricacao"], "%Y-%m-%d")
                for p in products
            ]
        )
        oldest_date = datetime.strftime(oldest_date, "%Y-%m-%d")

        # Calcula a data de validade mais próxima
        today = datetime.today().date()
        closest_date = min(
            [
                datetime.strptime(p["data_de_validade"], "%Y-%m-%d").date()
                for p in products
                if datetime.strptime(p["data_de_validade"], "%Y-%m-%d").date()
                >= today
            ]
        )
        closest_date = datetime.strftime(closest_date, "%Y-%m-%d")

        # Calcula a empresa com mais produtos
        companies = {}
        for p in products:
            if p["nome_da_empresa"] in companies:
                companies[p["nome_da_empresa"]] += 1
            else:
                companies[p["nome_da_empresa"]] = 1
        most_products_company = max(companies, key=companies.get)

        # Retorna o relatório
        report = f"Data de fabricação mais antiga: {oldest_date}\n"
        report += f"Data de validade mais próxima: {closest_date}\n"
        report += f"Empresa com mais produtos: {most_products_company}"
        return report
