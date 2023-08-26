import PySimpleGUI as sg

# region Fonte

fonte = 'Bahnschrift'
fonte_principal = 'Open Sans ExtraBold'
fonte_secundaria = 'Open Sans Medium'

fonte_titulo = (fonte_principal, 16, 'bold')
fonte_frame = (fonte_principal, 7)
fonte_descritivo = (fonte_secundaria, 10,)
fonte_inputs = (fonte_secundaria, 11)
fonte_botao = (fonte_principal, 11, 'bold')

# endregion

# region Paleta de Cores

titulo_campo = '#300138'
cor_titulo = '#4e5d8c'
cor_descritivo = '#919191'
cor_branca = 'white'
cor_texto_inputs = 'gray'

# Cores de destaque
cor_destaque_azul = '#6baee0'

# region Erro

text_color_erro = '#FF0000'
background_color_erro = '#FFD6D6'
button_color_erro = '#FF0000'

# endregion

# region Sucesso

text_color_sucesso = '#008000'
background_color_sucesso = '#D6FFD6'
button_color_sucesso = '#008000'

# endregion

# endregion

#region POPUPS

#region Exibe popup de ERRO

def exibir_popup_erro(texto):
    sg.popup(texto, keep_on_top=True, title="DocBuilder",
             icon="assets/logo/logo-DocBuilder-r.ico", font=(fonte_inputs), text_color=text_color_erro,
             background_color=background_color_erro, button_type=5, no_titlebar=True, relative_location=(0,-150),
                        auto_close = True, auto_close_duration=4, non_blocking=True)

#endregion

#region Exibe popup de SUCESSO
def exibir_popup_sucesso(texto):
    sg.popup(texto, keep_on_top=True, title="DocBuilder",
             icon="assets/logo/logo-DocBuilder-r.ico", font=(fonte_inputs), text_color=text_color_sucesso,
             background_color=background_color_sucesso, button_type=5, no_titlebar=True, relative_location=(0,-300),
                        auto_close = True, auto_close_duration=4, non_blocking=True)

#endregion

#region Exibe popup de SUCESSO
def exibir_popup_termino(texto):
    sg.popup(texto, keep_on_top=True, title="DocBuilder",
             icon="assets/logo/logo-DocBuilder-r.ico", font=(fonte_inputs), text_color='white',
             background_color=cor_destaque_azul, button_type=5, no_titlebar=True, relative_location=(0,-380),
                        auto_close = True, auto_close_duration=4, non_blocking=True)

#endregion

# endregion