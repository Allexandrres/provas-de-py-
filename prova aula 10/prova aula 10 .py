import flet as ft  

def main(page: ft.Page):
    # Função chamada ao enviar o formulário
    def enviar_formulario(e):
        if campo_nome.value.strip() and campo_email.value.strip() and campo_mensagem.value.strip():
            # Exibe uma mensagem de confirmação
            mensagem_confirmacao.value = (
                f"Obrigado, {campo_nome.value.strip()}! Seu formulário foi enviado com sucesso."
            )
            mensagem_confirmacao.color = "green"
            
            # Limpa os campos do formulário
            campo_nome.value = ""
            campo_email.value = ""
            campo_mensagem.value = ""
        else:
            # Exibe uma mensagem de erro
            mensagem_confirmacao.value = "Por favor, preencha todos os campos antes de enviar."
            mensagem_confirmacao.color = "red"
        
        page.update()  # Atualiza a interface para refletir as mudanças

    # Criação dos componentes da interface
    campo_nome = ft.TextField(label="Nome", width=400)
    campo_email = ft.TextField(label="Email", width=400)
    campo_mensagem = ft.TextField(label="Mensagem", multiline=True, width=400, height=100)
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_formulario)
    mensagem_confirmacao = ft.Text("")  # Área para exibir mensagens de confirmação ou erro

    # Adiciona os componentes à página
    page.add(
        ft.Column(
            [
                ft.Text("Formulário de Contato", size=20, weight="bold"),
                campo_nome,
                campo_email,
                campo_mensagem,
                botao_enviar,
                mensagem_confirmacao,
            ],
            alignment="center",
            horizontal_alignment="center",
        )
    )

# Executa a aplicação
if __name__ == "__main__":
    ft.app(target=main)
