# Perguntas do Quiz
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

# Função para obter uma resposta válida
def obter_resposta_valida():
    while True:
        resposta = input("Digite a letra da sua resposta (A, B, C ou D): ").strip().upper()
        if resposta in ["A", "B", "C", "D"]:
            return resposta  # Retorna a resposta válida
        else:
            print("Resposta inválida! Escolha apenas entre A, B, C ou D.")

# Função principal do Quiz
def quiz_interativo(perguntas):
    print("Bem-vindo ao Quiz!\n")
    pontuacao = 0

    for pergunta in perguntas:
        print(pergunta["pergunta"])
        for opcao in pergunta["opcoes"]:
            print(opcao)
        
        # Chama a função de validação para obter a resposta do usuário
        resposta_usuario = obter_resposta_valida()

        # Verifica se a resposta está correta
        if resposta_usuario == pergunta["resposta"]:
            print("Correto!\n")
            pontuacao += 1
        else:
            print(f"Errado! A resposta certa era {pergunta['resposta']}.\n")

    # Exibe a pontuação final
    print(f"Você acertou {pontuacao} de {len(perguntas)} perguntas!")
    if pontuacao == len(perguntas):
        print("Parabéns! Você acertou tudo!")
    elif pontuacao > len(perguntas) // 2:
        print("Muito bom! Continue assim!")
    else:
        print("Que tal tentar novamente?")

# Executa o Quiz
quiz_interativo(perguntas)
