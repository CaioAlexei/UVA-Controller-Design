import unittest
import ft


import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        lista,veri,erro=ft.recebendo_arquivo('C:/Users/Caio/kivy_venv/app/Projeto/testes/teste.txt')
        self.assertEqual(lista,['1 2 3 4\n', '4 5 6 \n', '8 9 10 4\n', '11 12 13 \n'])
        self.assertEqual(veri,1)
        self.assertEqual(erro,'sem erro')

if __name__ == '__main__':
    unittest.main()