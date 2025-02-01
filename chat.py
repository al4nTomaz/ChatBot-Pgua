from pyswip import Prolog

# Função para responder perguntas sobre Paranaguá
def responder_pergunta(pergunta):
    prolog = Prolog()

    # Carregar o arquivo Prolog (chatbot_pgua.pl)
    prolog.consult("chatbot_pgua.pl")

    # Consultando a resposta para a pergunta do usuário
    resposta = list(prolog.query(f"responder_pergunta('{pergunta}', X)"))

    # Verificando se a consulta retornou resultados
    if resposta:
        return resposta[0]['X']
    else:
        return "Desculpe, não entendi sua pergunta."

# Exemplo de uso:
if __name__ == "__main__":
    while True:
        pergunta = input("Pergunte algo sobre Paranaguá (ou digite 'sair' para encerrar): ").lower()
        if pergunta == "sair":
            print("Até mais!")
            break
        else:
            resposta = responder_pergunta(pergunta)
            print(resposta)
