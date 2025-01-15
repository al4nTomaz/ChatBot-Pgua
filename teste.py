from pyswip import Prolog

prolog = Prolog()

prolog.consult("chatbot_pgua.pl")
# consulta = list(prolog.query("pergunta_resposta(X)"))
consulta = list(prolog.query("regra(X)"))

for resultado in consulta:
    print(resultado["X"])

X = input("pergunta? ")

# print()
# X = X.replace(" ", "")
print(len(X))

for valor in prolog.query("pergunta_resposta("+ X +", Y)"):
    print(X, " pergunta_resposta ", valor["Y"])