perguntas = [
    {
        "pergunta": "Qual é a capital do Brasil?",
        "opcoes": ["A) Rio de Janeiro", "B) Brasília", "C) São Paulo", "D) Salvador"],
        "resposta": "B"
    },
    {
        "pergunta": "Quem escreveu 'Dom Casmurro'?",
        "opcoes": ["A) Machado de Assis", "B) Clarice Lispector", "C) José de Alencar", "D) Monteiro Lobato"],
        "resposta": "A"
    },
    {
        "pergunta": "Quanto é 7 x 8?",
        "opcoes": ["A) 54", "B) 56", "C) 58", "D) 60"],
        "resposta": "B"
    }
]

def quiz_interativo(perguntas):
    print("Bem-vindo ao Quiz!\n")
    pontuacao = 0

    for pergunta in perguntas:
        print(pergunta["pergunta"])
        for opcao in pergunta["opcoes"]:
            print(opcao)
        resposta = input("Digite a letra da sua resposta: ").strip().upper()

        if resposta == pergunta["resposta"]:
            print("Correto!\n")
            pontuacao += 1
        else:
            print(f"Errado! A resposta certa era {pergunta['resposta']}.\n")

    print(f"Você acertou {pontuacao} de {len(perguntas)} perguntas!")
    if pontuacao == len(perguntas):
        print("Parabéns! Você acertou tudo!")
    elif pontuacao > len(perguntas) // 2:
        print("Muito bom! Continue assim!")
    else:
        print("Que tal tentar novamente?")

# Chamando o Quiz
quiz_interativo(perguntas)
