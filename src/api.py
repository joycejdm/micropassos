import requests


def obter_frase_motivacional():
    """
    Consome a API pública do Advice Slip (Conselhos).
    Retorna a frase formatada ou uma frase padrão em caso de erro.
    """
    url = "https://api.adviceslip.com/advice"

    try:
        # Passar um User-Agent ajuda a evitar bloqueios
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        headers = {"User-Agent": user_agent}

        response = requests.get(url, headers=headers, timeout=5)

        if response.status_code == 200:
            dados = response.json()
            frase = dados['slip']['advice']
            return f'\n💡 "{frase}"\n'
        else:
            status = response.status_code
            return f"\n💡 Continue em frente! (Status: {status})\n"

    except requests.exceptions.RequestException:
        return "\n💡 Bora pra cima! O importante é dar o primeiro passo.\n"


if __name__ == "__main__":
    print(obter_frase_motivacional())
