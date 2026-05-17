from src.api import obter_frase_motivacional

def test_obter_frase_motivacional_retorno():
    """
    Testa se a função de API retorna uma string contendo 
    o ícone de formatação esperado, garantindo que o fluxo não quebra.
    """
    resultado = obter_frase_motivacional()
    
    # Valida se o retorno é realmente um texto (string)
    assert isinstance(resultado, str)
    
    # Valida se o texto contém o emoji de lâmpada que definimos na formatação
    assert "💡" in resultado