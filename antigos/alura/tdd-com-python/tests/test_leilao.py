from unittest import TestCase
from src.leilao.dominio import Usuario, Lance, Leilao
from src.leilao.excecoes import LanceInvalido

class TestLeilao(TestCase):
    def setUp(self):
        self.gui = Usuario('Gui', 100.0)
        self.yuri = Usuario('Yuri', 100.0)
        self.paulo = Usuario('Paulo', 100.0)

        self.lance_do_yuri = Lance(self.yuri, 100.0)
        self.lance_do_gui = Lance(self.gui, 150.0)
        self.lance_do_paulo = Lance(self.paulo, 155.0)

        self.leilao = Leilao('Celular')
        self.leilao.propor(self.lance_do_paulo)
        self.leilao.propor(self.lance_do_gui)
        self.leilao.propor(self.lance_do_yuri)
    
    def test_avalia(self):      
        self.setUp()
        
        menor_valor_esperado = 100.0
        maior_valor_esperado = 155.0
        
        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_avalia2(self):
        gui = Usuario('Gui', 155)
        yuri = Usuario('Yuri', 155)
        paulo = Usuario('Paulo', 155)

        lance_do_paulo = Lance(paulo, 155.0)
        lance_do_gui = Lance(gui, 150.0)
        lance_do_yuri = Lance(yuri, 100.0)

        leilao = Leilao('Celular')
        leilao.propor(lance_do_paulo)
        leilao.propor(lance_do_gui)
        leilao.propor(lance_do_yuri)
        
        menor_valor_esperado = 100.0
        maior_valor_esperado = 155.0
        
        self.assertEqual(menor_valor_esperado, leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, leilao.maior_lance)
    
    def test_avalia3(self):
        gui = Usuario('Gui', 155)
        yuri = Usuario('Yuri', 155)
        paulo = Usuario('Paulo', 155)

        lance_do_paulo = Lance(paulo, 155.0)
        lance_do_yuri = Lance(yuri, 100.0)
        lance_do_gui = Lance(gui, 150.0)

        leilao = Leilao('Celular')
        leilao.propor(lance_do_paulo)
        leilao.propor(lance_do_gui)
        leilao.propor(lance_do_yuri)
        
        menor_valor_esperado = 100.0
        maior_valor_esperado = 155.0
        
        self.assertEqual(menor_valor_esperado, leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, leilao.maior_lance)
    
    def test_nao_deve_permitir_propor_um_lance_em_ordem_decrescente(self):
        with self.assertRaises(LanceInvalido):
            yuri = Usuario('Yuri', 155)
            lance_do_yuri = Lance(yuri, 100.0)

            self.leilao.propor(lance_do_yuri)
            self.leilao.propor(self.lance_do_gui)            
    
    # se o leilão não tiver lances, deve permitir um lance
    def test_se_nao_tiver_lance_deve_permitir_um_lance(self):
        self.leilao.propor(self.lance_do_gui)

        self.assertEqual(1, len(self.leilao.lance))

    # se o último usuário for diferente, deve permitir propor o lance
    def test_se_ultimo_usuario_diferente_deve_permitir_lance(self):
        yuri = Usuario('Yuri', 200)
        lance_do_yuri = Lance(yuri, 200.0)

        self.leilao.propor(self.lance_do_yuri)
        self.leilao.propor(lance_do_yuri)

        quantidade_de_lances_recebidos = len(self.leilao.lance)

        self.assertEqual(2, quantidade_de_lances_recebidos)

    # se o último usuário for o mesmo, não deve permitir propor o lance
    def test_nao_deve_permitir_lance_caso_usuario_seja_o_mesmo(self):
        lance_do_gui_200 = Lance(self.gui, 200.0)
        
        with self.assertRaises(LanceInvalido):
            self.leilao.propor(self.lance_do_gui)
            self.leilao.propor(lance_do_gui_200)
