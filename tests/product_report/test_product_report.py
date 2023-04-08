from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        "1",
        "farinha",
        50,
        "Farinini",
        "01-05-2021",
        "02-06-2023",
        "ao abrigo de luz"
    )
    expected_awser = (
        "O produto farinha fabricado em Farinini por 50 "
        "com validade até 01-05-2021 precisa ser armazenado "
        "ao abrigo de luz."
    )
    assert str(product) == expected_awser
