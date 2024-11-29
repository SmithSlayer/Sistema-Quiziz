Sistema Quizz

1. Objetivo Do Projeto

O programa deve:

. Apresentar uma série de perguntas com múltiplas escolhas (por exemplo, A, B, C, D).
. Permitir que o usuário escolha uma resposta para cada pergunta.
. Avaliar se a resposta está correta.
. Mostrar o desempenho ao usuário.
. Permitir que o usuário crie perguntas é as edite.

2. Expansões e Melhorias

1. Adicionar Níveis de Dificuldade
 Separar perguntas em categorias de "fácil", "médio" e "difícil".
 Permitir que o usuário escolha o nível antes de começar.
2. Pontuação Avançada
 Dar mais pontos para perguntas difíceis e menos para fáceis.
 Mostrar um ranking ou "nível de desempenho" ao final (ex.: iniciante, intermediário, avançado).
3. Tempo para Responder
 Usar a biblioteca time para limitar o tempo de resposta. Se o tempo acabar, considere a resposta como errada.
4. Interface Gráfica
 Utilize Tkinter ou PyQt para criar uma interface mais amigável, com botões para selecionar as respostas.
5. Salvar e Compartilhar Resultados
 Salvar os resultados do quiz em um arquivo de texto ou mostre um resumo ao final para o usuário compartilhar.
6. Criação de Quiz
 Sistema onde o usuário possa criar seus proprios quiz é armazenar-los em um banco de dados

**Planejamento Projeto**

### **Dia 1: Planejamento e Estrutura Inicial**
**Objetivo:**
- Definir o escopo do projeto e montar a base do código.

**Tarefas:**
1. Definir o número de perguntas e criar o banco de dados inicial (lista ou dicionário).
2. Planejar o fluxo do programa:
   - Exibir perguntas.
   - Receber respostas.
   - Avaliar se a resposta está correta.
   - Calcular a pontuação final.
3. Criar a estrutura básica do programa (entrada de perguntas e respostas no terminal).

**Entrega ao final do dia:**
- Um programa básico que exibe perguntas e coleta respostas.

---

### **Dia 2: Lógica de Pontuação e Melhorias**
**Objetivo:**
- Implementar a lógica de pontuação e tornar o código mais robusto.

**Tarefas:**
1. Adicionar lógica para calcular e exibir a pontuação.
2. Implementar validação de entrada do usuário (evitar respostas inválidas como números ou letras fora das opções).
3. Testar o programa para garantir que ele está funcionando corretamente com os dados.

**Entrega ao final do dia:**
- Quiz funcional com pontuação e validação básica.

---

### **Dia 3: Feedback e Aprimoramentos**
**Objetivo:**
- Melhorar a experiência do usuário.

**Tarefas:**
1. Adicionar mensagens personalizadas com base na pontuação (ex.: "Muito bom!" ou "Que tal tentar novamente?").
2. Incluir feedback após cada resposta, indicando se está correta ou não.
3. Organizar o código em funções para melhorar a legibilidade e manutenção.

**Entrega ao final do dia:**
- Um programa que fornece feedback em tempo real e está mais organizado.

---

### **Dia 4: Expansões (Opcional)**
**Objetivo:**
- Adicionar funcionalidades extras.

**Tarefas:**
1. Implementar níveis de dificuldade (fácil, médio, difícil).
2. Adicionar limite de tempo para as respostas (usando a biblioteca `time`).
3. Criar a possibilidade de adicionar mais perguntas automaticamente.

**Entrega ao final do dia:**
- Um quiz com mais funcionalidades e flexibilidade.

---

### **Dia 5: Testes e Refinamento**
**Objetivo:**
- Finalizar o projeto e corrigir problemas.

**Tarefas:**
1. Realizar testes com diferentes tipos de entrada para garantir que o programa é robusto.
2. Refinar o layout do terminal (organizar exibição das perguntas e opções).
3. Criar um arquivo de documentação simples, explicando como o programa funciona.

**Entrega ao final do dia:**
- Um projeto funcional, testado e documentado.

---

### **interface gráfica**

1. **Dia 6:** Estruturar a interface gráfica básica.
2. **Dia 7:** Vincular a lógica do quiz à interface.
3. **Dia 8:** Adicionar funcionalidades extras (botões, cronômetro, feedback visual).
4. **Dia 9:** Testes e refinamento gráfico.