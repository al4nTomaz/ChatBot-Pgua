# Dicionário com as perguntas e respostas
respostas = {
    'qual é a cidade mais antiga do Paraná?': 'A cidade mais antiga do Paraná é Paranaguá.',
    'qual é a principal cidade do litoral paranaense': 'A principal cidade do litoral paranaense é Paranaguá.',
    'qual é o principal porto do Paraná?': 'O principal porto do Paraná é o Porto de Paranaguá.',
    'qual é a origem do nome Paranaguá?': 'O nome Paranaguá tem origem Tupi-Guarani e significa "grande mar redondo" ou "enseada do mar".',
    'qual é a data de fundação de Paranaguá?': 'Paranaguá foi fundada em 1526.',
    'quais são os principais eventos históricos ocorridos em Paranaguá?': 'Paranaguá foi palco de importantes eventos históricos, como a Guerra dos Cabanos e a passagem de tropas durante a Guerra do Paraguai.',
    'quais são as principais manifestações culturais de Paranaguá?': 'Paranaguá possui um rico patrimônio cultural, com destaque para a Festa de Nossa Senhora do Rosário, a Folia de Reis e a culinária caiçara.',
    'quais são os principais pontos turísticos históricos de Paranaguá?': 'Entre os principais pontos turísticos históricos de Paranaguá estão a Igreja de Nossa Senhora do Rosário, o Forte dos Palmares e o Museu Municipal.',
    'qual é a localização geográfica de Paranaguá?': 'Paranaguá está localizada na região litorânea do Paraná, a aproximadamente 60 km ao sul da capital Curitiba.',
    'quais são os principais rios que banham Paranaguá?': 'Os principais rios que banham Paranaguá são o Nhundiaquara e o Itiberê.',
    'qual é o clima predominante em Paranaguá?': 'O clima predominante em Paranaguá é subtropical úmido, com verões quentes e chuvosos e invernos amenos.',
    'quais são as principais praias de Paranaguá?': 'As principais praias de Paranaguá são a Praia de Pontal do Paraná e a Praia de Caiobá.',
    'quais são as principais atividades econômicas de Paranaguá?': 'As principais atividades econômicas de Paranaguá são o porto, a indústria e o turismo.',
    'qual a importância do Porto de Paranaguá para a economia do estado?': 'O Porto de Paranaguá é o principal porto do Paraná e um dos mais importantes do Brasil, sendo responsável por grande parte das exportações do estado.',
    'quais são os principais atrativos turísticos de Paranaguá?': 'Além dos pontos históricos, Paranaguá oferece diversos atrativos turísticos, como trilhas ecológicas, observação de aves e turismo náutico.'
}

def chatbot():
    print("Olá! Eu sou o ChatBot de Paranaguá. Pergunte-me sobre a cidade!")
    print("Digite 'sair' para encerrar a conversa.")
    
    while True:
        pergunta = input("Você: ").strip().lower()
        
        if pergunta == 'sair':
            print("ChatBot: Até logo! Se precisar de mais informações, estarei aqui.")
            break
        
        # Resposta do chatbot
        resposta = respostas.get(pergunta, "Desculpe, não tenho uma resposta para essa pergunta. Tente outra!")
        print(f"ChatBot: {resposta}")

# Iniciar o chatbot
chatbot()
