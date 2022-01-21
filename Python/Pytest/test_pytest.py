from codigo.jogo import brincadeira
from pytest import mark

"""
O teste é formado por 3 etapas(gwt - aaa):

Given - Dado
When - Quando
Then - Então

ou

- Arrange
- Act
- Assert


instalar pytest: pip install pytest

executar: pytest arquivo.py

IMPORTANTE: Se o problema não for  AssertionError, o problema está na estrutura do código

Se o retorno do teste for um ponto: teste.py/ .  <-- Teste Ok

tag -x para o codigo quando ocorrer o erro
tag --pdb abre debugger
tag -v detalha o teste
tag -s mostra as saidas no console
--junit xml report.xml - gera um arquivo com o resultado

Mark(Marcações):
from pytest import mark
@mark.nomedatag

tags embutidas:
@mark.skip
@mark.skipif
@mark.xfail
@mark.usefixture
@mark.parametrize

pytest -m 'nomedatag' 
ou 
pytest -m 'not nomedatag'(pra nao rodar os testes q contem a tag)

ao executar colocar o nome da tag, o pytest só executara as tags informadas
"""

def test_quando_brincadeira_receber_1_entao_deve_retornar_1():
    entrada = 1 #given
    esperado = 1 #given
    resultado = brincadeira(entrada) #when

    assert resultado == esperado #then

def test_quando_brincadeira_receber_3_entao_deve_retornar_queijo():
    assert brincadeira(3)=='queijo'

@mark.goiabada
def test_quando_brincadeira_receber_5_entao_deve_retornar_goiabada():
    assert brincadeira(5) == 'goiabada'

@mark.goiabada
def test_quando_brincadeira_receber_10_entao_deve_retornar_goiabada():
    assert brincadeira(10) == 'goiabada'

