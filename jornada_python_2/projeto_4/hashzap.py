#tela inicial:
    #titulo: hashzap
    #botao: iniciar chat
        #clickar no botao:
            #abrir popup/modal
            #titulo: bem vindo
            #caixa de texto para escolher nick
            #botao entrar no chat:
                #sumir popup
                #sumir titulo
                #sumir botao
                    #carregar chat
                    #carregar campo enviar mensagem 
                    #botao enviar
                        #enviar mensagem
                        #limpar caixa de mensagem

#flet
#importar flet
import flet as ft

#criar o main
def main(pagina):

    def enviar_mensagem_tunel(mensagem):
        texto = ft.Text(mensagem)
        chat.controls.append(texto)

        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        nome_usuario = caixa_nome.value
        texto_campo_enviar_mensagem = campo_enviar_mensagem.value
        texto = f'{nome_usuario}: {texto_campo_enviar_mensagem}'
        pagina.pubsub.send_all(texto)
        campo_enviar_mensagem.value = ''

        pagina.update()

    campo_enviar_mensagem = ft.TextField(label='mensagem', on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton('enviar', on_click=enviar_mensagem)
    
    linha_enviar = ft.Row([campo_enviar_mensagem, botao_enviar])
    chat = ft.Column()
    
    def entrar_chat(evento):
        popup.open = False
        pagina.remove(titulo)
        pagina.remove(botao_iniciar)
        pagina.add(chat)
        pagina.add(linha_enviar)

        nome_usuario = caixa_nome.value
        texto_mensagem = f'{nome_usuario} entrou no chat'
        pagina.pubsub.send_all(texto_mensagem)

        pagina.update()

    titulo_popup = ft.Text('bem vindo ao hashzap')
    caixa_nome = ft.TextField(label='escolha seu nick')
    botao_popup = ft.ElevatedButton('entrar no chat', on_click=entrar_chat)

    popup = ft.AlertDialog(title=titulo_popup, content=caixa_nome, actions=[botao_popup])

    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    titulo = ft.Text('Hashzap')
    pagina.add(titulo)
    botao_iniciar = ft.ElevatedButton('iniciar', on_click=abrir_popup)
    pagina.add(botao_iniciar)

#executar main via browser
ft.app(main, view=ft.WEB_BROWSER)

#executar main via app
#ft.app(main) mas precisa da lib mvp instalada
