import pytest
import csv
import main

lista_para_multiplicar = [
    (2, 3, 6),
    (0, 4, 0),
    (-5, -3, 15),
    (8, 1000, 8000),
    (7, '', ''),
    (9, ' ', '         '),
    (10, 'a', 'aaaaaaaaaa')
]


@pytest.mark.parametrize('numero1, numero2, resultado_esperado', lista_para_multiplicar)
def teste_multiplicar_2_numeros(numero1, numero2, resultado_esperado):
    # Configura - virá da lista

    # Executa
    resultado_obtido = main.multiplicar_2_numeros(numero1, numero2)

    # Valida
    assert resultado_obtido == resultado_esperado


def ler_dados_csv():
    dados_csv = []  # criamos uma lista vazia
    nome_arquivo = 'vendors/massa_dividir_2_numeros.csv'
    try:
        with open(nome_arquivo, newline='') as arquivo_csv:
            campos = csv.reader(arquivo_csv, delimiter=';')
            next(campos)
            for linha in campos:
                dados_csv.append(linha)

        return dados_csv
    except FileNotFoundError:
        print(f'Arquivo não encontrado: {nome_arquivo}')
    except Exception as fail:
        print(f'Falha não prevista: {fail}')


lista_para_dividir = [
    (8, 4, 2),
    (9, 3, 3),
    (9, 2, 4.5),
    (8, 0, 'divisao por zero')
]



@pytest.mark.parametrize('id, numero1, numero2, resultado_esperado, tipo_teste', ler_dados_csv())
def teste_dividir_2_numeros(id, numero1, numero2, resultado_esperado, tipo_teste):
    # Configura
    # Valores vem da lista

    # Executa
    resultado_obtido = main.dividir_2_numeros(float(numero1), float(numero2))
    print(ler_dados_csv())
    # Valida
    if tipo_teste == 'positivo':
        assert float(resultado_esperado) == resultado_obtido
    else:
        assert resultado_esperado == resultado_obtido
