from src.leilao.dominio import Usuario, Lance, Leilao
import pytest

@pytest.fixture
def vini():
    return Usuario('Vini', 100.0)

@pytest.fixture
def leilao():
    return Leilao('Celular')

def test_deve_subtrair_valor_da_carteira_do_usuario_quando_propuser_lance(vini, leilao):
    vini.propor_lance(leilao, 50.0)

    assert vini.carteira == 50.0
