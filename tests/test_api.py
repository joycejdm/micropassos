from src.api import obter_frase_motivacional


def test_obter_frase_motivacional_retorno():
    """
    Testa se a função de API retorna uma string contendo
    o ícone de formatação esperado.
    """
    resultado = obter_frase_motivacional()

    assert isinstance(resultado, str)
    assert "💡" in resultado