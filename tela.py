import customtkinter as ctk
from tkinter import messagebox

# Configuração inicial do CustomTkinter
ctk.set_appearance_mode("System")  # Alterna entre "Light", "Dark" ou "System"
ctk.set_default_color_theme("blue")  # Tema de cores: "blue", "green", "dark-blue"

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

# Variáveis globais
indice_pergunta = 0
pontuacao = 0

# Função para verificar a resposta
def verificar_resposta(selecao):
    global indice_pergunta, pontuacao

    if selecao == perguntas[indice_pergunta]["resposta"]:
        pontuacao += 1

    indice_pergunta += 1
    if indice_pergunta < len(perguntas):
        exibir_pergunta()
    else:
        # Mensagem final e encerramento
        messagebox.showinfo("Fim do Quiz", f"Você acertou {pontuacao} de {len(perguntas)} perguntas!")
        janela.quit()

# Função para exibir a pergunta atual
def exibir_pergunta():
    pergunta_atual = perguntas[indice_pergunta]
    pergunta_label.configure(text=pergunta_atual["pergunta"])

    # Atualiza os botões com as opções
    for i, opcao in enumerate(pergunta_atual["opcoes"]):
        botoes_opcoes[i].configure(text=opcao, command=lambda opcao=opcao: verificar_resposta(opcao))

# Configuração da janela principal
janela = ctk.CTk()
janela.title("Quiz Interativo")
janela.geometry("600x400")

# Título da Pergunta
pergunta_label = ctk.CTkLabel(janela, text="", font=("Arial", 16), wraplength=500, justify="center")
pergunta_label.pack(pady=20)

# Botões das Opções
botoes_opcoes = []
for _ in range(4):
    botao = ctk.CTkButton(janela, text="", font=("Arial", 14), width=400, height=40)
    botao.pack(pady=10)
    botoes_opcoes.append(botao)

# Exibe a primeira pergunta
exibir_pergunta()

# Inicia o loop principal
janela.mainloop()
