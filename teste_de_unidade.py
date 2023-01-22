# 1 - Bibliotecas
import unittest  # Essa biblioteca será baixada automaticamente pelo PIP

import main


# 2 - Classes (Grupo de definitions)
class MyTestCase(unittest.TestCase):
    # 3 - Métodos e Funções


    def testar_soma_2_numeros(self):
        resultado_esperado = 40
        resultado_obtido = main.somar_2_numeros(13, 27)
        self.assertEqual(resultado_esperado, resultado_obtido)  # add assertion here

    def teste_multiplicar_2_numeros(self):
        resultado_esperado = 40
        resultado_obtido = main.multiplicar_2_numeros(5, 8)
        self.assertEqual(resultado_esperado, resultado_obtido)


if __name__ == '__main__':
    unittest.main()
