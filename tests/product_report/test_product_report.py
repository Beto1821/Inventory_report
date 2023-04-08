from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        12312,
        "MacBook",
        7000,
        "Taiwan",
        "01-08-2022",
        "01-08-2032",
        "a sete chaves"
    )
    expected_awser = (
        "O produto MacBook fabricado em Taiwan por 7000 "
        "com validade até 01-08-2022 precisa ser armazenado "
        "a sete chaves."
    )
    assert str(product) == expected_awser
