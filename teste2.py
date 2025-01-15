from pyswip import Prolog

# Inicializa o Prolog
prolog = Prolog()

# Carrega a base de dados Prolog (chatbot_pgua.pl)
prolog.consult("chatbot_pgua.pl")

# Função para interagir com o usuário e fazer a consulta no Prolog
def chatbot():
    while True:
        # Pergunta ao usuário
        X = input("Pergunte algo: ").strip().lower()
        
        # Se o usuário digitar "sair", o chatbot encerra
        if X == "sair":
            print("Até mais!")
            break

        # Formata a entrada para o Prolog (envelopando com aspas simples)
        X_prolog = f"'{X}'"
        
        # Consulta no Prolog utilizando a base de dados
        resultado = list(prolog.query(f"pergunta_resposta({X_prolog}, Y)"))
        
        # Se houver resposta, exibe a resposta
        if resultado:
            for r in resultado:
                print(f"Resposta: {r['Y']}")
        else:
            print("Desculpe, não entendi sua pergunta.")
    
# Inicia o chatbot
chatbot()
