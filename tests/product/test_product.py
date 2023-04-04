from inventory_report.inventory.product import Product


def test_cria_produto():
    # informações tiradas de item id 9 de :
    # /Users/adalbertoramosribeiro/Desktop/Trybe/Projetos/turma-23/sd-023-b-inventory-report/inventory_report/data/inventory.json
    id = 9
    nome_do_produto = "eucalyptus globulus"
    nome_da_empresa = "Target Corporation"
    data_de_fabricacao = "2020-09-06"
    data_de_validade = "2024-05-01"
    numero_de_serie = "GT74 LHWJ FCXL JNQT ZCXM 4761 GWSP"
    instrucoes_de_armazenamento = "instrucao 9"

    produto = Product(id, nome_do_produto, nome_da_empresa, data_de_fabricacao, data_de_validade, numero_de_serie, instrucoes_de_armazenamento)

    assert produto.id == id
    assert produto.nome_do_produto == nome_do_produto
    assert produto.nome_da_empresa == nome_da_empresa
    assert produto.data_de_fabricacao == data_de_fabricacao
    assert produto.data_de_validade == data_de_validade
    assert produto.numero_de_serie == numero_de_serie
    assert produto.instrucoes_de_armazenamento == instrucoes_de_armazenamento
