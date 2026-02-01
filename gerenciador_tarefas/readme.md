# 📋 Gerenciador de Tarefas CLI

Um sistema simples e eficiente de lista de tarefas (To-Do List) executado diretamente no terminal. Desenvolvido em Python, o projeto foca na interatividade, utilizando cores para facilitar a leitura e sons para feedback das ações.

## 🚀 Funcionalidades

- **Adicionar Tarefas:** Insira novas pendências na lista.
- **Concluir Tarefas:** Marque tarefas como feitas (o sistema valida se já foi concluída).
- **Remover Tarefas:** Exclua itens da lista definitivamente.
- **Visualização:** Listagem clara com status (Pendente/Concluído).
- **Persistência de Dados:** As tarefas são salvas automaticamente em um arquivo `tarefas.json`, mantendo seus dados salvos mesmo após fechar o programa.
- **Feedback Visual e Sonoro:** Uso da biblioteca `colorama` para interface colorida e `chime` para sons de sucesso ou erro.

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **JSON:** Para armazenamento local dos dados.
- **Colorama:** Para estilização de texto no terminal.
- **Chime:** Para notificações sonoras.
- **OS/Time:** Para manipulação do sistema e controle de fluxo.

## 📦 Como executar

1. Clone o repositório.
2. Instale as dependências necessárias:
   ```bash
   pip install colorama chime
