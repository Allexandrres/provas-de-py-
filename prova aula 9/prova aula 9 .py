import ft

def main(page: ft.Page):
    # Lista para armazenar as tarefas
    tarefas = []

    # Função para adicionar uma tarefa
    def adicionar_tarefa(e):
        if campo_tarefa.value.strip():  # Verifica se o campo não está vazio
            tarefas.append(campo_tarefa.value)
            lista_tarefas.controls.append(ft.Text(campo_tarefa.value))
            campo_tarefa.value = ""  # Limpa o campo de entrada
            lista_tarefas.update()  # Atualiza a lista exibida
            campo_tarefa.focus()  # Foca novamente no campo de entrada

    # Campo de entrada para o nome da tarefa
    campo_tarefa = ft.TextField(
        label="Digite uma tarefa",
        hint_text="Exemplo: Comprar pão",
        expand=True,
    )

    # Botão para adicionar a tarefa
    botao_adicionar = ft.ElevatedButton(
        text="Adicionar Tarefa",
        on_click=adicionar_tarefa,
    )

    # Lista de tarefas exibida na tela
    lista_tarefas = ft.Column()

    # Layout da aplicação
    page.add(
        ft.Row([campo_tarefa, botao_adicionar]),
        lista_tarefas,
    )

# Executa a aplicação
ft.app(target=main)