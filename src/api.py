import requests

def obter_frase_motivacional():
    """
    Consome a API pública do Advice Slip (Conselhos) - É mais rápida e estável.
    Retorna a frase formatada ou uma frase padrão em caso de erro.
    """
    url = "https://api.adviceslip.com/advice"
    
    try:
        # Passar um User-Agent ajuda a evitar que a API bloqueie o script
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        
        response = requests.get(url, headers=headers, timeout=5)
        
        if response.status_code == 200:
            dados = response.json()
            # A estrutura dessa API é diferente, pegamos o 'advice' dentro de 'slip'
            frase = dados['slip']['advice']
            return f'\n💡 "{frase}"\n'
        else:
            return f"\n💡 Continue em frente! Um MicroPasso de cada vez. (Status: {response.status_code})\n"
            
    except requests.exceptions.RequestException as e:
        # Imprime o erro real no terminal só para você debugar, se quiser
        # print(f"Erro de conexão: {e}")
        return "\n💡 Bora pra cima! O importante é dar o primeiro passo.\n"

if __name__ == "__main__":
    print(obter_frase_motivacional())