import tkinter as tk
from tkinter import messagebox

# Banco de perguntas
perguntas = [
    {
        "pergunta": "Qual é a capital do Brasil?",
        "opcoes": ["Rio de Janeiro", "Brasília", "São Paulo", "Salvador"],
        "resposta": "Brasília"
    },
    {
        "pergunta": "Quem escreveu 'Dom Casmurro'?",
        "opcoes": ["Machado de Assis", "Clarice Lispector", "José de Alencar", "Monteiro Lobato"],
        "resposta": "Machado de Assis"
    },
    {
        "pergunta": "Quanto é 7 x 8?",
        "opcoes": ["54", "56", "58", "60"],
        "resposta": "56"
    }
]

# Variáveis globais para controlar o progresso do quiz
indice_pergunta = 0
pontuacao = 0

# Função para verificar a resposta
def verificar_resposta(selecao):
    global indice_pergunta, pontuacao

    # Verifica se a resposta está correta
    if selecao == perguntas[indice_pergunta]["resposta"]:
        pontuacao += 1

    # Passa para a próxima pergunta ou encerra o quiz
    indice_pergunta += 1
    if indice_pergunta < len(perguntas):
        exibir_pergunta()
    else:
        # Mostra a pontuação final
        messagebox.showinfo("Fim do Quiz", f"Você acertou {pontuacao} de {len(perguntas)} perguntas!")
        janela.destroy()  # Fecha a janela após o quiz

# Função para exibir a pergunta atual
def exibir_pergunta():
    pergunta_atual = perguntas[indice_pergunta]
    pergunta_label.config(text=pergunta_atual["pergunta"])

    # Atualiza os botões com as opções
    for i, opcao in enumerate(pergunta_atual["opcoes"]):
        botoes_opcoes[i].config(text=opcao, command=lambda opcao=opcao: verificar_resposta(opcao))

# Criação da janela principal
janela = tk.Tk()
janela.title("Quiz Interativo")
janela.geometry("500x300")

# Rótulo para exibir a pergunta
pergunta_label = tk.Label(janela, text="", font=("Arial", 14), wraplength=400, justify="center")
pergunta_label.pack(pady=20)

# Botões para as opções
botoes_opcoes = []
for _ in range(4):  # Cria 4 botões, um para cada opção
    botao = tk.Button(janela, text="", font=("Arial", 12), width=30)
    botao.pack(pady=5)
    botoes_opcoes.append(botao)

# Exibe a primeira pergunta
exibir_pergunta()

# Inicia o loop principal
janela.mainloop()
