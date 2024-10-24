import unittest
from src.belly import Belly

class TestBelly(unittest.TestCase):

    def setUp(self):
        self.belly = Belly()

    def test_comer_muchos_pepinos_y_grunir(self):
        self.belly.comer(42)
        self.belly.esperar(2)
        self.assertTrue(self.belly.esta_gruñendo(), "El estómago debería gruñir después de comer 42 pepinos y esperar 2 horas.")

    def test_comer_pocos_pepinos_y_no_grunir(self):
        self.belly.comer(10)
        self.belly.esperar(2)
        self.assertFalse(self.belly.esta_gruñendo(), "El estómago no debería gruñir después de comer solo 10 pepinos.")

    def test_comer_pepinos_esperar_menos_de_una_hora(self):
        self.belly.comer(50)
        self.belly.esperar(0.5)
        self.assertFalse(self.belly.esta_gruñendo(), "El estómago no debería gruñir si solo se espera media hora.")

    def test_comer_pepinos_y_esperar_en_minutos(self):
        self.belly.comer(30)
        self.belly.esperar(1.5)  # 90 minutos
        self.assertTrue(self.belly.esta_gruñendo(), "El estómago debería gruñir después de 90 minutos y 30 pepinos.")

    def test_comer_una_cantidad_no_valida_de_pepinos(self):
        with self.assertRaises(ValueError):
            self.belly.comer(150)  # Exceso de pepinos

    def test_comer_cero_pepinos(self):
        with self.assertRaises(ValueError):
            self.belly.comer(0)

    def test_comer_pepinos_negativos(self):
        with self.assertRaises(ValueError):
            self.belly.comer(-5)

    def test_comer_un_monton_de_pepinos(self):
        self.belly.comer(25)  # Simula "un montón"
        self.belly.esperar(3)
        self.assertTrue(self.belly.esta_gruñendo(), "El estómago debería gruñir después de comer 'un montón' de pepinos y esperar 3 horas.")

if __name__ == '__main__':
    unittest.main()
