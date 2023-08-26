# Autor: Gustavo Rosas
# GitHub: https://github.com/GustavoRosas-Dev/fastdoc
# Data: 2023-06-11

# region IMPORTS

from PySimpleGUI import popup
import customtkinter as ctk
from PIL import ImageTk, Image  # Necessário p/ exibir o logo no App
import json  # Necessário p/ fazer CRUD em arquivos JSON
import ctypes  # Necessário p/ mudar o ícone na barra de tarefas do windows
from popups import exibir_popup_sucesso, exibir_popup_erro, exibir_popup_termino
import random
import os # Acessar e manipular pastas do Windows
import pandas as pd # P/ manipular dataframes
import functools # Para embrulhar defs


#region Imports necessários para preencher modelos_documentos
from docx import Document
from docx2pdf import convert  # pip install docx2pdf
from datetime import datetime
#endregion

# endregion

# region VARIÁVEIS
logo_ico = "resources/images/logo.ico"
logo_dark = "resources/images/FastDoc-Dark-Mode.png"
logo_light = "resources/images/FastDoc-Light-Mode.png"
# endregion

# region APARÊNCIA

# region Cores Sucesso

text_color_sucesso = '#008000'
background_color_sucesso = '#D6FFD6'
foreground_color_sucesso = '#C1EFC1'
button_color_sucesso = '#008000'
button_hover_color_sucesso = '#006300'

# endregion

# region Cores Cinza

cor_cinza_claro_botao = '#979da2'
cor_cinza_escuro_botao = '#4b4f51'

# endregion

# region Cores Azuis
cor_azul_claro = "#1F7FC9"
cor_azul_escuro = "#0864AA"

# endregion

# endregion

# region LISTAS
extensao_documento_list = ['Extensão*', 'PDF', 'DOCX', 'Ambos']

prazos_list = ['Prazo', '7 dias', '15 dias', '30 dias', '45 dias', '60 dias', '90 dias', '120 dias', '180 dias',
               '1 ano']

frases_termino = ['Ta-dah! Missão cumprida!', 'Check! Tarefa concluída.', 'Voilà, trabalho terminado!',
                  'Bam! Documento preenchido com êxito!', 'Tcharan! Terminado com sucesso.',
                  'Ding dong! Tarefa realizada com excelência.', 'Trabalho finalizado, oh grande mestre!']

frases_exemplos_detalhes = ['Item (ex: Etapa - Estudo preliminar)', 'Item (ex: Etapa - Anteprojeto)', 'Item (ex:  '
    'Etapa - Projeto Executivo)', 'Item (ex: Etapa - Definição do programa)', 'Item (ex: Etapa - Levantamento de necessidades)',
    'Item (ex: Etapa - Análise de viabilidade)', 'Item (ex: Etapa - Desenvolvimento conceitual)',
    'Item (ex: Etapa - Elaboração do projeto executivo)', 'Item (ex: Etapa - Detalhamento técnico)',
    'Item (ex: Etapa - Orçamento e planejamento)', 'Item (ex: Etapa - Análise de impacto ambiental)',
    'Item (ex: Etapa - Aprovação de órgãos competentes)', 'Item (ex: Etapa - Acompanhamento da construção)']

frases_popup_iniciar = [
    "Preparando a documentação.\nDeixe-me fazer todo o trabalho chato enquanto você toma um café!",
    "Iniciando o preenchimento.\nEm breve você terá seus modelos_documentos prontos, sem estresse!",
    "Trabalhando duro.\nPorque eu me importo com a sua tranquilidade!",
    "Documentos em progresso.\nApenas relaxe e deixe-me cuidar de tudo para você!",
    "Garantindo sua paz de espírito.\nEstou cuidando de todos os detalhes!",
    "Documentos? Desafio aceito!",
    "Aguarde um pouquinho.\n Estou dando vida aos seus modelos_documentos!",
    "Preparando tudo para você.\nRelaxe e deixe-me cuidar da documentação!",
    "Preenchimento em andamento.\nEm breve, seus modelos_documentos estarão prontos!",
    "O preenchimento perfeito está em curso.\nConfie em mim para cuidar de tudo!",
    "Documentos em processo de criação.\nSua tranquilidade é a minha prioridade!",
]

nacionalidade_list = ['Nacionalidade', 'Brasileiro(a)', 'Alemão(a)', 'Americano(a)', 'Argentino(a)', 'Australiano(a)',
                      'Boliviano(a)',
                      'Canadense(a)', 'Chileno(a)', 'Chinês(a)', 'Colombiano(a)', 'Coreano(a)', 'Equatoriano(a)',
                      'Espanhol(a)', 'Francês(a)', 'Indiano(a)', 'Italiano(a)', 'Japonês(a)', 'Mexicano(a)',
                      'Neozelandês(a)', 'Paraguaio(a)', 'Peruano(a)', 'Português(a)', 'Sul-africano(a)', 'Uruguaio(a)',
                      'Venezuelano(a)']

nacionalidade_masculino_list = ['Brasileiro', 'Alemão', 'Americano', 'Argentino', 'Australiano', 'Boliviano',
                                'Canadense', 'Chileno', 'Chinês', 'Colombiano', 'Coreano', 'Equatoriano', 'Espanhol',
                                'Francês', 'Indiano', 'Italiano', 'Japonês', 'Mexicano', 'Neozelandês', 'Paraguaio',
                                'Peruano', 'Português', 'Sul-africano', 'Uruguaio', 'Venezuelano']

nacionalidade_feminino_list = ['Brasileira', 'Alemã', 'Americana', 'Argentina', 'Australiana', 'Boliviana',
                               'Canadense', 'Chilena', 'Chinesa', 'Colombiana', 'Coreana', 'Equatoriana', 'Espanhola',
                               'Francesa', 'Indiana', 'Italiana', 'Japonesa', 'Mexicana', 'Neozelandesa', 'Paraguaia',
                               'Peruana', 'Portuguesa', 'Sul-africana', 'Uruguaia', 'Venezuelana']

complemento_list = ['Complemento', 'Andar', 'Sala', 'Conjunto']

estado_civil_feminino_list = ['Solteira', 'Casada', 'Separada', 'Divorciada', 'Viúva']
estado_civil_masculino_list = ['Solteiro', 'Casado', 'Separado', 'Divorciado', 'Viúvo']
estado_civil_generico_list = ['Estado civil', 'Solteiro(a)', 'Casado(a)', 'Separado(a)', 'Divorciado(a)', 'Viúvo(a)']

profissao_feminino_list = ['Arquiteta', 'Engenheira', 'Designer de interiores']
profissao_masculino_list = ['Arquiteto', 'Engenheiro', 'Designer de interiores']
profissao_generico_list = ['Profissão', 'Arquiteto(a)', 'Engenheiro(a)', 'Designer de interiores']

cau_crea_list = ['CAU', 'CREA']

condicoes_de_pagamento_list = ['À vista', 'Pix', 'Parcelado', 'Cartão de crédito', 'Boleto']
numero_de_parcelas_list = ['Parcelas', '1x','2x','3x','4x','5x','6x','7x','8x','9x','10x','11x','12x']
porcentagem_ENTRADA_list = ['Entrada', '5%', '10%', '15%', '20%', '25%', '30%', '35%', '40%', '45%', '50%', '55%',
                           '60%', '65%', '70%', '75%', '80%', '85%', '90%', '95%', '100%']
porcentagem_QUITACAO_list = ['Quitação', '5%', '10%', '15%', '20%', '25%', '30%', '35%', '40%', '45%', '50%', '55%',
                           '60%', '65%', '70%', '75%', '80%', '85%', '90%', '95%', '100%']


# endregion

#region DECORADORES
def controlador_login(funcao):
    @functools.wraps(funcao)
    def func_que_roda_funcao():
        print('************* Embrulhando a função no decorador *************\n')

        # region A FAZER: Ativar tela de login + verificações, aqui
        print('Abrindo a tela de login...\n')
        TelaDeLogin.mainloop() # Abre a tela de login

        user_logged = False # Usuário deslogado (por padrão)

        # A FAZER: Criar lógica que muda o user logged para True SE o usuário se logar

        # endregion
        if user_logged: # Se o usuário estiver logado
            funcao() # Abra o App

        print('\n************* Fechando o embrulho *************')

    return func_que_roda_funcao
#endregion

#region CLASSES

#region TELA DE LOGIN
class TelaDeLogin(ctk.CTk):
    def __init__(self):

        self.login_salvo = False

        super().__init__()

        #region CONFIG. Window
        self.title("FastDoc")
        self.geometry("250x300")
        self.minsize(width=250, height=300)
        self.iconbitmap(logo_ico)

        #region FAZ A JANELA DE LOGIN SURGIR NO CENTRO DA TELA
        self.update_idletasks()

        width = 250
        height = 300
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")
        self.minsize(width, height)
        #endregion

        self.attributes("-topmost", True)  # Faz a janela ficar sempre por cima (Keep on Top)
        #endregion

        #region (Text) Fazer Login
        self.texto = ctk.CTkLabel(self, text="Fazer Login")
        self.texto.pack(padx=10, pady=10)
        # endregion

        # region (Entry) E-mail
        self.email = ctk.CTkEntry(self, placeholder_text="Seu e-mail")
        self.email.pack(padx=10, pady=10)
        # endregion

        # region (Entry) chave_de_acesso
        self.chave_de_acesso = ctk.CTkEntry(self, placeholder_text="Chave de acesso", show="*")
        self.chave_de_acesso.pack(padx=10, pady=10)
        # endregion

        # region (CheckBox) Lembrar Login
        self.checkbox = ctk.CTkCheckBox(self, text="Lembrar Login", command=self.lembrar_login)
        self.checkbox.pack(padx=10, pady=10)
        # endregion

        # region  (Button) Login
        self.botao = ctk.CTkButton(self, text="Login", command=self.click_login)
        self.botao.pack(padx=10, pady=10)
        # endregion

        self.carregar_dados()

    def lembrar_login(self):
        if self.login_salvo == False:
            self.login_salvo = True
            print('Salvar login.')
            return True
        else:
            self.login_salvo = False
            print('Não salvar login.')
            return False

    def carregar_dados(self):
        try:
            with open("user_setting_janela_login.json", "r") as file:
                data = json.load(file)

                email_value = data.get("email", "")
                self.email.delete(0, "end")
                self.email.insert(0, email_value)

                chave_de_acesso_value = data.get("chave_de_acesso", "")
                self.chave_de_acesso.delete(0, "end")
                self.chave_de_acesso.insert(0, chave_de_acesso_value)

                checkbox_value = data.get("checkbox", "")


        except FileNotFoundError:
            pass

    def click_login(self):
        print("Fazer Login")

        email_value = self.email.get()
        chave_de_acesso_value = self.chave_de_acesso.get()
        checkbox_value = self.checkbox.get()
        if checkbox_value == 1:
            checkbox_value = True
        else:
            checkbox_value = False

        data = {"email": email_value, "chave_de_acesso": chave_de_acesso_value, "checkbox": checkbox_value}

        with open("user_setting_janela_login.json", "w") as file:
            json.dump(data, file)

        #region A FAZER: (GET) login e senha e verifica na APi se eles existem no banco de dados.

        #region A FAZER: Se o usuário ou a chave de acesso NÃO forem válidos, exiba um popup de erro/ encerre o
        # programa.


TelaDeLogin = TelaDeLogin()

#endregion

# region APP
class FastDocApp(ctk.CTk):

    def __init__(self):

        # region CONFIG - NECESSÁRIA para que o Windows 11 exiba o ícone do App na barra de tarefas
        # Defina o AppUserModelID para o seu aplicativo
        myappid = 'GustavoRosas.FastDoc.v1'  # Substitua com uma string única

        # Define o AppUserModelID do processo atual
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        # endregion

        super().__init__()

        # region CONFIG - Define o Modo (Dark, Light, System) + o Tema dos botões

        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        # endregion

        # region CONFIG - dimensões da janela, o titulo e o icone, "Keep On Top".

        self.minsize(width=550, height=550)
        self.geometry("550x400")
        self.maxsize(width=800, height=550)
        self.title("FastDoc")
        self.iconbitmap(logo_ico)

        self.attributes("-topmost", True)  # Faz a janela ficar sempre por cima (Keep on Top)

        self.sidebar_ELEMENTS_profissional_PF_visible = False

        # endregion

        # region inicia as defs (widgets e carrega as informações o usuário salvas no user settings)

        self.create_widgets()
        self.load_data()
        self.change_appearance_mode('Dark')

        # endregion

    # region UI - CRIAR A JANELA AQUI ██████████████████████████████████████████████████████

    def create_widgets(self):

        # ███ ESQUERDA ███
        # region PAINEL LATERAL

        # region (SIDEBAR ESQ.) Barra lateral Esquerda (sidebar_esq)
        self.sidebar_esq = ctk.CTkFrame(self, width=100, corner_radius=8)
        self.sidebar_esq.grid(row=0, column=0, sticky="nsw", padx=10, pady=10, rowspan=2)
        # endregion

        # region PROGRESS BAR ----------- uso: self.progressbar_1.set(novo_valor)  # Atualize a barra de progresso

        progress_bar_size = 80

        self.slider_progressbar_frame = ctk.CTkFrame(self.sidebar_esq, fg_color="transparent",
                                                     width=progress_bar_size, bg_color='transparent')
        self.slider_progressbar_frame.pack(fill="both", padx=3, pady=0)

        self.progressbar_1 = ctk.CTkProgressBar(self.slider_progressbar_frame, mode="determinate",
                                                width=progress_bar_size, fg_color=cor_cinza_claro_botao,
                                                progress_color=cor_azul_claro)
        self.progressbar_1.pack(fill="both", padx=10, pady=10)
        self.progressbar_1.set(0)  # Valor inicial da barra de progresso (0%)

        # endregion

        # region (inside SIDEBAR ESQ.) (BOTÃO) Profissional

        self.profissional_button = ctk.CTkButton(self.sidebar_esq, text="Profissional", command=self.btn_Profissional,
                                                 fg_color=cor_azul_claro, hover_color=cor_azul_escuro)
        self.profissional_button.pack(pady=10, padx=10)

        # endregion

        # region (inside SIDEBAR ESQ.) (BOTÃO) Cliente

        self.cliente_button = ctk.CTkButton(self.sidebar_esq, text="Cliente", command=self.btn_Cliente,
                                            fg_color=cor_cinza_claro_botao, hover_color=cor_cinza_escuro_botao)
        self.cliente_button.pack(pady=10, padx=10)

        # endregion

        # region (inside SIDEBAR ESQ.) (BOTÃO) Documentos

        self.documentos_button = ctk.CTkButton(self.sidebar_esq, text="Documentos",
                                               command=self.btn_Documentos, fg_color=cor_cinza_claro_botao,
                                               hover_color=cor_cinza_escuro_botao)
        self.documentos_button.pack(pady=10, padx=10)

        # endregion

        # region (inside SIDEBAR ESQ.) (SIDEBAR) Organização: Escolha o tema (texto + dropdown)

        self.sidebar_tema = ctk.CTkFrame(self.sidebar_esq, width=80, corner_radius=8, fg_color="transparent",
                                         bg_color='transparent',)
        self.sidebar_tema.pack(side="bottom", padx=0, pady=0)

        # endregion

        # region (inside SIDEBAR ESQ.) (LABEL) Texto 'TEMA'

        self.appearance_mode_label = ctk.CTkLabel(self.sidebar_tema, text="Escolha o tema:", anchor='w')
        self.appearance_mode_label.pack(padx=10, pady=0)

        # endregion

        # region (inside SIDEBAR ESQ.) (DROPDOWN) Tema

        self.appearance_mode_optionmenu = ctk.CTkOptionMenu(self.sidebar_tema, values=["Dark", "Light", "System"],
                                                            command=self.change_appearance_mode)
        self.appearance_mode_optionmenu.pack(padx=10, pady=10)

        # endregion

        # endregion

        #region (CREATE) ███ DIREITA 1º (MÚLTIPLOS SIDEBARS) ███

        # region (TAB VIEW 1) (CREATE) PROFISSIONAL (OK)

        def tab_view_1():
            self.tabview1 = ctk.CTkTabview(self, width=250, segmented_button_selected_color=cor_azul_claro,
                                           segmented_button_unselected_hover_color=cor_cinza_escuro_botao,
                                           segmented_button_selected_hover_color=cor_azul_escuro)
            self.tabview1.grid(row=0, column=1, sticky="nsew", padx=10, pady=5)

            # region (Tab) Pessoa Física (OK)
            self.tabview1.add("Pessoa Física")

            # region (inside Tab "Pessoa Física") (INPUT) Nome Completo

            self.nome_completo_profissional = ctk.CTkEntry(self.tabview1.tab("Pessoa Física"),
                                                           placeholder_text="Nome Completo*")
            self.nome_completo_profissional.pack(padx=10, pady=5, fill="x")

            # endregion

            # region (inside "Tab Pessoa Física") (INPUT) E-mail

            self.email_profissional = ctk.CTkEntry(self.tabview1.tab("Pessoa Física"), placeholder_text='Seu e-mail')
            self.email_profissional.pack(padx=10, pady=5, fill="x")

            # endregion

            # region (inside Tab "Pessoa Física") (INPUT) Número do CPF

            self.numero_cpf_profissional = ctk.CTkEntry(self.tabview1.tab("Pessoa Física"), placeholder_text="CPF")
            self.numero_cpf_profissional.pack(padx=10, pady=5, fill="x")

            # endregion

            #region (inside Tab "Pessoa Física") (FRAME) Nacionalidades + Estado Civil

            # region FRAME
            self.frame_nacionalidade_estado_civil_profissional = ctk.CTkFrame(self.tabview1.tab("Pessoa Física"),
                                                              fg_color="transparent")
            self.frame_nacionalidade_estado_civil_profissional.pack(padx=0, pady=0, fill='x', anchor='n')
            # endregion

            # region (DROPDOWN) Nacionalidades

            self.nacionalidade_profissional = ctk.CTkComboBox(self.frame_nacionalidade_estado_civil_profissional,
                                                              values=nacionalidade_list, width=170)
            self.nacionalidade_profissional.pack(side='left', padx=10, pady=5, fill="x", expand=True)

            # endregion

            # region (DROPDOWN) ESTADO CIVIL

            self.estado_civil_profissional = ctk.CTkComboBox(self.frame_nacionalidade_estado_civil_profissional,
                                                             values=estado_civil_generico_list)
            self.estado_civil_profissional.pack(side='left', padx=10, pady=5, fill="x", expand=True)

            # endregion

            #endregion

            #region (inside Tab "Pessoa Física") (FRAME) Profissão + Número de Registro

            # region FRAME
            self.frame_profissoa_numero_do_registro = ctk.CTkFrame(self.tabview1.tab("Pessoa Física"),
                                                                 fg_color="transparent")
            self.frame_profissoa_numero_do_registro.pack(padx=0, pady=0, fill='x', anchor='n')
            # endregion

            # region (DROPDOWN) Profissão

            self.profissao_profissional = ctk.CTkComboBox(self.frame_profissoa_numero_do_registro,
                                                          values=profissao_generico_list, width=170)
            self.profissao_profissional.pack(side='left', padx=10, pady=5, fill="x", anchor='n', expand=True)

            # endregion

            # region (INPUT) Número do Registro (CAU/CREA)

            self.numero_registro_cau_crea = ctk.CTkEntry(self.frame_profissoa_numero_do_registro, placeholder_text="CAU/"
                                                                                                              "CREA")
            self.numero_registro_cau_crea.pack(side='left', padx=10, pady=5, fill="x", expand=True)

            # endregion

            #endregion

            # region (inside Tab "Pessoa Física") (FRAME) Endereço: CEP (api via cep) + Número + Complemento

            #region FRAME
            self.tabFrame_Endereco_profissional = ctk.CTkFrame(self.tabview1.tab("Pessoa Física"),
                                                              fg_color="transparent")
            self.tabFrame_Endereco_profissional.pack(padx=0, pady=0, fill='x', anchor='n')
            #endregion

            #region CEP
            self.cep_profissional = ctk.CTkEntry(self.tabFrame_Endereco_profissional, placeholder_text="CEP", width=70)
            self.cep_profissional.pack(side="left", padx=10, pady=5)
            #endregion

            #region Número
            self.numero_endereco_profissional = ctk.CTkEntry(self.tabFrame_Endereco_profissional, placeholder_text="Número",
                                                             width=60)
            self.numero_endereco_profissional.pack(side="left", padx=1, pady=5)
            #endregion

            #region Complemento
            self.complemento_endereco_profissional = ctk.CTkEntry(self.tabFrame_Endereco_profissional,
                                                                  placeholder_text="Complemento", width=270)
            self.complemento_endereco_profissional.pack(side="left", padx=10, pady=5, expand=True, fill='x')
            #endregion

            # endregion

            #region  (inside FRAME Tab "Pessoa Física") (SUPERFRAME 6X1) LOGRADOURO + NUMERO + BAIRRO + CIDADE + UF

            # region Frame
            self.frame_logradouro_numero_bairro_cidade_uf_profissional = ctk.CTkFrame(self.tabview1.tab("Pessoa Física"),
                                                                      fg_color="transparent")
            self.frame_logradouro_numero_bairro_cidade_uf_profissional.pack(padx=0, pady=0, fill="x", anchor='n')
            # endregion

            # region (Input) Logradouro
            self.logradouro_profissional = ctk.CTkEntry(self.frame_logradouro_numero_bairro_cidade_uf_profissional,
                                                       placeholder_text="Logradouro")
            self.logradouro_profissional.pack(padx=10, pady=5, expand=True,
                                             fill="x")  # after, -anchor, -before, -expand, -fill, -in, -ipadx, -ipady, -padx, -pady, or -side
            # endregion

            # region (inside FRAME Profissional) (FRAME) Bairro/ Cidade/ UF

            # region (inside FRAME Profissional) Frame
            self.tabFrame_Bairro_Cidade_UF_profissional = ctk.CTkFrame(
                self.frame_logradouro_numero_bairro_cidade_uf_profissional,
                                                                      fg_color="transparent")
            self.tabFrame_Bairro_Cidade_UF_profissional.pack(padx=0, pady=0, fill="x", anchor='n')
            # endregion

            # region (inside FRAME Profissional) (Input) Bairro
            self.bairro_endereco_profissional = ctk.CTkEntry(self.tabFrame_Bairro_Cidade_UF_profissional,
                                                            placeholder_text="Bairro")
            self.bairro_endereco_profissional.pack(side="left", padx=10, pady=5, expand=True, fill="x")
            # endregion

            # region (inside FRAME Profissional) (Input) Cidade
            self.cidade_endereco_profissional = ctk.CTkEntry(self.tabFrame_Bairro_Cidade_UF_profissional,
                                                            placeholder_text="Cidade", width=80)
            self.cidade_endereco_profissional.pack(side="left", padx=1, pady=5, expand=True, fill="x")
            # endregion

            # region (inside FRAME Profissional) (Input) UF
            self.uf_endereco_profissional = ctk.CTkEntry(self.tabFrame_Bairro_Cidade_UF_profissional,
                                                        placeholder_text="UF", width=60)
            self.uf_endereco_profissional.pack(side="left", padx=10, pady=5, fill="x")
            # endregion

            # endregion

            #endregion

            # Adicione outros elementos da aba Pessoa Física conforme necessário

            # endregion

            # region (Tab) Pessoa Jurídica (OK)

            self.tabview1.add("Pessoa Jurídica")

            # region (inside Tab "Pessoa Jurídica") (INPUT) CNPJ

            self.cnpj_empresarial = ctk.CTkEntry(self.tabview1.tab("Pessoa Jurídica"),
                                                 placeholder_text="CNPJ")
            self.cnpj_empresarial.pack(padx=10, pady=5, fill="x", anchor='n')

            # endregion

            # region (inside Tab "Pessoa Jurídica") (AUTO/INPUT) Razão Social

            self.razao_social_empresarial = ctk.CTkEntry(self.tabview1.tab("Pessoa Jurídica"),
                                                         placeholder_text="Razão Social")
            self.razao_social_empresarial.pack(padx=10, pady=5, fill="x", anchor='n')

            # endregion

            # region (inside Tab "Pessoa Jurídica") (AUTO/INPUT) Nome Fantasia

            self.nome_fantasia_empresarial = ctk.CTkEntry(self.tabview1.tab("Pessoa Jurídica"),
                                                          placeholder_text="Nome Fantasia")
            self.nome_fantasia_empresarial.pack(padx=10, pady=5, fill="x", anchor='n')

            # endregion

            # region (inside Tab "Pessoa Juridica") (FRAME) Logradouro + Número

            # region Frame
            self.tabFrame_Logradouro_Numero_empresarial = ctk.CTkFrame(self.tabview1.tab("Pessoa Jurídica"),
                                                                       fg_color="transparent")
            self.tabFrame_Logradouro_Numero_empresarial.pack(padx=0, pady=0, fill="x", anchor='n')
            # endregion

            # region (Input) Logradouro
            self.logradouro_empresarial = ctk.CTkEntry(self.tabFrame_Logradouro_Numero_empresarial,
                                                       placeholder_text="Logradouro")
            self.logradouro_empresarial.pack(side="left", padx=10, pady=5, expand=True, fill="x") #after, -anchor, -before, -expand, -fill, -in, -ipadx, -ipady, -padx, -pady, or -side
            # endregion

            # region (Input) Numero
            self.numero_endereco_empresarial = ctk.CTkEntry(self.tabFrame_Logradouro_Numero_empresarial,
                                                            placeholder_text="Número",
                                                            width=60)
            self.numero_endereco_empresarial.pack(side="left", padx=10, pady=5)
            # endregion

            # endregion

            # region (inside Tab "Pessoa Juridica") (Input) Detalhes
            self.detalhes_endereco_empresarial = ctk.CTkEntry(self.tabview1.tab("Pessoa Jurídica"),
                                                              placeholder_text="Detalhes")
            self.detalhes_endereco_empresarial.pack(padx=10, pady=5, fill="x", anchor='n')
            # endregion

            # region (inside Tab "Pessoa Juridica") (FRAME) Bairro/ Cidade/ UF

            # region Frame
            self.tabFrame_Bairro_Cidade_UF_empresarial = ctk.CTkFrame(self.tabview1.tab("Pessoa Jurídica"),
                                                                      fg_color="transparent")
            self.tabFrame_Bairro_Cidade_UF_empresarial.pack(padx=0, pady=0, fill="x", anchor='n')
            # endregion

            # region (Input) Bairro
            self.bairro_endereco_empresarial = ctk.CTkEntry(self.tabFrame_Bairro_Cidade_UF_empresarial,
                                                            placeholder_text="Bairro")
            self.bairro_endereco_empresarial.pack(side="left", padx=10, pady=5, expand=True, fill="x")
            # endregion

            # region (Input) Cidade
            self.cidade_endereco_empresarial = ctk.CTkEntry(self.tabFrame_Bairro_Cidade_UF_empresarial,
                                                            placeholder_text="Cidade", width=80)
            self.cidade_endereco_empresarial.pack(side="left", padx=1, pady=5, expand=True, fill="x")
            # endregion

            # region (Input) UF
            self.uf_endereco_empresarial = ctk.CTkEntry(self.tabFrame_Bairro_Cidade_UF_empresarial,
                                                        placeholder_text="UF", width=60)
            self.uf_endereco_empresarial.pack(side="left", padx=10, pady=5, fill="x")
            # endregion

            # endregion

            # region (inside Tab "Pessoa Jurídica") (AUTO/INPUT) E-mail

            self.email_empresarial = ctk.CTkEntry(self.tabview1.tab("Pessoa Jurídica"),
                                                  placeholder_text="E-mail empresarial")
            self.email_empresarial.pack(padx=10, pady=5, fill="x", anchor='n')

            # endregion

            # region (inside Tab "Pessoa Jurídica") (AUTO/INPUT) DDD + Telefone

            self.telefone_empresarial = ctk.CTkEntry(self.tabview1.tab("Pessoa Jurídica"),
                                                     placeholder_text="DDD + Telefone empresarial")
            self.telefone_empresarial.pack(padx=10, pady=5, fill="x", anchor='n')

            # endregion

            # Adicione outros elementos da aba Pessoa Jurídica conforme necessário

            return self.tabview1

            # endregion

        # endregion

        # region (TAB VIEW 2) (CREATE) CLIENTE

        def tab_view_2():
            self.tabview2 = ctk.CTkTabview(self, width=250, segmented_button_selected_color=cor_azul_claro,
                                           segmented_button_unselected_hover_color=cor_cinza_escuro_botao,
                                           segmented_button_selected_hover_color=cor_azul_escuro)
            self.tabview2.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

            # region (Tab) Informações de contato
            self.tabview2.add("Info. contato")

            #region (SWITCHER) Alternador entre PF e PJ
            self.switcher_cliente_PF_PJ = ctk.CTkSwitch(self.tabview2.tab("Info. contato"), text='Pessoa Física',
                                                        width=100, height=10, command=self.switcher_cliente_PF_PJ,
                                                        progress_color=cor_azul_claro, fg_color=cor_azul_escuro)
            self.switcher_cliente_PF_PJ.pack(pady=10)
            #endregion

            #region (Tab) Info. contato

            #region (controlled by SWITCHER) Frame CLIENTE PF
            self.switcher_frame_cliente_PF = ctk.CTkFrame(self.tabview2.tab("Info. contato"), width=100,
                                                          corner_radius=8, fg_color='transparent')
            self.switcher_frame_cliente_PF.pack(expand=True, fill='both')

            # region (inside FRAME Cliente PF) (INPUT) Nome Completo

            self.nome_completo_cliente = ctk.CTkEntry(self.switcher_frame_cliente_PF,
                                                      placeholder_text="Nome completo*")
            self.nome_completo_cliente.pack(padx=10, pady=5, fill="x")

            # endregion

            # region (inside FRAME Cliente PF) (INPUT) E-mail

            self.email_cliente = ctk.CTkEntry(self.switcher_frame_cliente_PF, placeholder_text="E-mail")
            self.email_cliente.pack(padx=10, pady=5, fill="x")

            # endregion

            # region (inside FRAME Cliente PJ) (AUTO/INPUT) DDD + Telefone

            self.telefone_cliente_PF = ctk.CTkEntry(self.switcher_frame_cliente_PF,
                                                     placeholder_text="DDD + Telefone")
            self.telefone_cliente_PF.pack(padx=10, pady=5, fill="x", anchor='n')

            # endregion

            # region (inside FRAME Cliente PF) (FRAME) Nacionalidades + Estado Civil + Profissão
            self.frame_nacionalidades_estado_civil_profissao = ctk.CTkFrame(self.switcher_frame_cliente_PF,
                                                                  fg_color="transparent")
            self.frame_nacionalidades_estado_civil_profissao.pack(padx=0, pady=0, fill="x", anchor='n')

            # region (inside FRAME nacionalidades_estado_civil_profissao) (DROPDOWN) Nacionalidades

            self.nacionalidade_cliente = ctk.CTkComboBox(self.frame_nacionalidades_estado_civil_profissao,
                                                         values=nacionalidade_list, width=120)
            self.nacionalidade_cliente.pack(side='left', padx=10, pady=5, fill="x", expand=True)

            # endregion

            # region (inside FRAME nacionalidades_estado_civil_profissao) (DROPDOWN) ESTADO CIVIL

            self.estado_civil_cliente = ctk.CTkComboBox(self.frame_nacionalidades_estado_civil_profissao,
                                                        values=estado_civil_generico_list, width=105)
            self.estado_civil_cliente.pack(side='left', padx=0, pady=5, fill="x", expand=True)

            # endregion

            # region (inside FRAME nacionalidades_estado_civil_profissao) (INPUT) Profissão

            self.profissao_cliente = ctk.CTkEntry(self.frame_nacionalidades_estado_civil_profissao,
                                                     placeholder_text="Profissão")
            self.profissao_cliente.pack(side='left', padx=10, pady=5, fill="x", expand=True)

            # endregion

            #endregion

            #region (inside FRAME Cliente PF) (FRAME) CPF + Rede Social
            self.frame_cpf_e_rede_social = ctk.CTkFrame(self.switcher_frame_cliente_PF, fg_color="transparent")
            self.frame_cpf_e_rede_social.pack(padx=0, pady=0, fill="x", anchor='n')

            # region (inside FRAME Cliente PF) (INPUT) Número do CPF

            self.cpf_cliente = ctk.CTkEntry(self.frame_cpf_e_rede_social, placeholder_text="Número do CPF", width=110)
            self.cpf_cliente.pack(side='left', padx=10, pady=5, fill="x")

            # endregion

            # region (inside FRAME Cliente PF) (INPUT) Rede Social (Instagram, Facebook, Linkedin, etc)

            self.rede_social_cliente = ctk.CTkEntry(self.frame_cpf_e_rede_social, placeholder_text="Rede Social")
            self.rede_social_cliente.pack(side='left', padx=10, pady=5, fill="x", expand='True')

            # endregion

            # endregion

            # region (inside FRAME Cliente PF) (FRAME) Endereço: CEP (api via cep) + Número + Complemento

            #region FRAME
            self.tabFrame_Endereco = ctk.CTkFrame(self.switcher_frame_cliente_PF, fg_color="transparent")
            self.tabFrame_Endereco.pack(padx=0, pady=0, fill="x", anchor='n')
            #endregion

            #region CEP
            self.cep_cliente = ctk.CTkEntry(self.tabFrame_Endereco, placeholder_text="CEP", width=70)
            self.cep_cliente.pack(side="left", padx=10, pady=5)
            #endregion

            #region Número
            self.numero_endereco_cliente = ctk.CTkEntry(self.tabFrame_Endereco, placeholder_text="Número",
                                                             width=60)
            self.numero_endereco_cliente.pack(side="left", padx=1, pady=5)
            #endregion

            #region Complemento
            self.complemento_endereco_cliente = ctk.CTkEntry(self.tabFrame_Endereco,
                                                                  placeholder_text="Complemento", width=270)
            self.complemento_endereco_cliente.pack(side="left", padx=10, pady=5, expand=True, fill='x')
            #endregion

            # endregion

            #region  (inside FRAME Cliente PF) (SUPERFRAME 6X1) LOGRADOURO + NUMERO + BAIRRO + CIDADE + UF

            # region Frame
            self.frame_logradouro_numero_bairro_cidade_uf = ctk.CTkFrame(self.switcher_frame_cliente_PF,
                                                                      fg_color="transparent")
            self.frame_logradouro_numero_bairro_cidade_uf.pack(padx=0, pady=0, fill="x", anchor='n')
            # endregion

            # region (inside FRAME Cliente PF) (Input) Logradouro
            self.logradouro_cliente_PF = ctk.CTkEntry(self.frame_logradouro_numero_bairro_cidade_uf,
                                                       placeholder_text="Logradouro")
            self.logradouro_cliente_PF.pack(padx=10, pady=5, fill="x", anchor='n')  # after, -anchor, -before,
            # -expand, -fill, -in,
            # -ipadx,
            # -ipady, -padx, -pady, or -side
            # endregion

            # region (inside FRAME Cliente PF) (FRAME) Bairro/ Cidade/ UF

            # region (inside FRAME Cliente PF) Frame
            self.tabFrame_Bairro_Cidade_UF_cliente_PF = ctk.CTkFrame(self.frame_logradouro_numero_bairro_cidade_uf,
                                                                      fg_color="transparent")
            self.tabFrame_Bairro_Cidade_UF_cliente_PF.pack(padx=0, pady=0, fill="x", anchor='n')
            # endregion

            # region (inside FRAME Cliente PJ) (Input) Bairro
            self.bairro_endereco_cliente_PF = ctk.CTkEntry(self.tabFrame_Bairro_Cidade_UF_cliente_PF,
                                                            placeholder_text="Bairro")
            self.bairro_endereco_cliente_PF.pack(side="left", padx=10, pady=5, expand=True, fill="x")
            # endregion

            # region (inside FRAME Cliente PJ) (Input) Cidade
            self.cidade_endereco_cliente_PF = ctk.CTkEntry(self.tabFrame_Bairro_Cidade_UF_cliente_PF,
                                                            placeholder_text="Cidade", width=80)
            self.cidade_endereco_cliente_PF.pack(side="left", padx=1, pady=5, expand=True, fill="x")
            # endregion

            # region (inside FRAME Cliente PJ) (Input) UF
            self.uf_endereco_cliente_PF = ctk.CTkEntry(self.tabFrame_Bairro_Cidade_UF_cliente_PF,
                                                        placeholder_text="UF", width=60)
            self.uf_endereco_cliente_PF.pack(side="left", padx=10, pady=5, fill="x")
            # endregion

            # endregion

            #endregion

            #endregion

            #region (controlled by SWITCHER) Frame CLIENTE PJ
            self.switcher_frame_cliente_PJ = ctk.CTkFrame(self.tabview2.tab("Info. contato"), width=100,
                                                          corner_radius=8, fg_color='transparent')

            # region (inside FRAME Cliente PJ) (INPUT) CNPJ

            self.cnpj_cliente_PJ = ctk.CTkEntry(self.switcher_frame_cliente_PJ,
                                                 placeholder_text="CNPJ")
            self.cnpj_cliente_PJ.pack(padx=10, pady=5, fill="x", anchor='n')

            # endregion

            # region (inside FRAME Cliente PJ) (AUTO/INPUT) Razão Social

            self.razao_social_cliente_PJ = ctk.CTkEntry(self.switcher_frame_cliente_PJ,
                                                         placeholder_text="Razão Social")
            self.razao_social_cliente_PJ.pack(padx=10, pady=5, fill="x", anchor='n')

            # endregion

            # region (inside FRAME Cliente PJ) (AUTO/INPUT) Nome Fantasia

            self.nome_fantasia_cliente_PJ = ctk.CTkEntry(self.switcher_frame_cliente_PJ,
                                                          placeholder_text="Nome Fantasia")
            self.nome_fantasia_cliente_PJ.pack(padx=10, pady=5, fill="x", anchor='n')

            # endregion

            # region (inside FRAME Cliente PJ) (AUTO/INPUT) E-mail

            self.email_cliente_PJ = ctk.CTkEntry(self.switcher_frame_cliente_PJ,
                                                  placeholder_text="E-mail")
            self.email_cliente_PJ.pack(padx=10, pady=5, fill="x", anchor='n')

            # endregion

            # region (inside FRAME Cliente PJ) (AUTO/INPUT) DDD + Telefone

            self.telefone_cliente_PJ = ctk.CTkEntry(self.switcher_frame_cliente_PJ,
                                                     placeholder_text="DDD + Telefone")
            self.telefone_cliente_PJ.pack(padx=10, pady=5, fill="x", anchor='n')

            # endregion

            #region  (inside FRAME Cliente PJ) (SUPERFRAME 6X1) LOGRADOURO + NUMERO + BAIRRO + CIDADE + UF

            # region Frame
            self.frame_logradouro_lumero_bairro_cidade_uf = ctk.CTkFrame(self.switcher_frame_cliente_PJ,
                                                                      fg_color="transparent")
            self.frame_logradouro_lumero_bairro_cidade_uf.pack(padx=0, pady=0, fill="x", anchor='n')
            # endregion

            # region (inside FRAME Cliente PJ) (FRAME) Logradouro + Número

            # region Frame
            self.tabFrame_Logradouro_Numero_cliente_PJ = ctk.CTkFrame(self.frame_logradouro_lumero_bairro_cidade_uf,
                                                                       fg_color="transparent")
            self.tabFrame_Logradouro_Numero_cliente_PJ.pack(padx=0, pady=0, fill="x", anchor='n')
            # endregion

            # region (Input) Logradouro
            self.logradouro_cliente_PJ = ctk.CTkEntry(self.tabFrame_Logradouro_Numero_cliente_PJ,
                                                       placeholder_text="Logradouro")
            self.logradouro_cliente_PJ.pack(side="left", padx=10, pady=5, expand=True,
                                             fill="x")  # after, -anchor, -before, -expand, -fill, -in, -ipadx, -ipady, -padx, -pady, or -side
            # endregion

            # region (Input) Numero
            self.numero_endereco_cliente_PJ = ctk.CTkEntry(self.tabFrame_Logradouro_Numero_cliente_PJ,
                                                            placeholder_text="Número",
                                                            width=60)
            self.numero_endereco_cliente_PJ.pack(side="left", padx=10, pady=5)
            # endregion

            # endregion

            # region (inside FRAME Cliente PJ) (Input) Detalhes
            self.detalhes_endereco_cliente_PJ = ctk.CTkEntry(self.frame_logradouro_lumero_bairro_cidade_uf,
                                                              placeholder_text="Detalhes")
            self.detalhes_endereco_cliente_PJ.pack(padx=10, pady=5, fill="x", anchor='n')
            # endregion

            # region (inside FRAME Cliente PJ) (FRAME) Bairro/ Cidade/ UF

            # region (inside FRAME Cliente PJ) Frame
            self.tabFrame_Bairro_Cidade_UF_cliente_PJ = ctk.CTkFrame(self.frame_logradouro_lumero_bairro_cidade_uf,
                                                                      fg_color="transparent")
            self.tabFrame_Bairro_Cidade_UF_cliente_PJ.pack(padx=0, pady=0, fill="x", anchor='n')
            # endregion

            # region (inside FRAME Cliente PJ) (Input) Bairro
            self.bairro_endereco_cliente_PJ = ctk.CTkEntry(self.tabFrame_Bairro_Cidade_UF_cliente_PJ,
                                                            placeholder_text="Bairro")
            self.bairro_endereco_cliente_PJ.pack(side="left", padx=10, pady=5, expand=True, fill="x")
            # endregion

            # region (inside FRAME Cliente PJ) (Input) Cidade
            self.cidade_endereco_cliente_PJ = ctk.CTkEntry(self.tabFrame_Bairro_Cidade_UF_cliente_PJ,
                                                            placeholder_text="Cidade", width=80)
            self.cidade_endereco_cliente_PJ.pack(side="left", padx=1, pady=5, expand=True, fill="x")
            # endregion

            # region (inside FRAME Cliente PJ) (Input) UF
            self.uf_endereco_cliente_PJ = ctk.CTkEntry(self.tabFrame_Bairro_Cidade_UF_cliente_PJ,
                                                        placeholder_text="UF", width=60)
            self.uf_endereco_cliente_PJ.pack(side="left", padx=10, pady=5, fill="x")
            # endregion

            # endregion

            #endregion

            # Adicione outros elementos da aba Pessoa Física conforme necessário

            # endregion

            #endregion

            # endregion

            # region (Tab) Detalhes do Projeto

            self.tabview2.add("Detalhes projeto")

            # region (inside Tab "Detalhes projeto") (FRAME) Números RRT's + DETALHES

            #region FRAME
            self.tabFrame_RRTs = ctk.CTkFrame(self.tabview2.tab("Detalhes projeto"), fg_color="transparent")
            self.tabFrame_RRTs.pack(padx=0, pady=5, fill="x", anchor='n')
            #endregion

            #region Nº RRT Projeto
            self.numero_rrt_projeto = ctk.CTkEntry(self.tabFrame_RRTs, placeholder_text="Nº RRT Projeto")
            self.numero_rrt_projeto.pack(side="left", padx=10, pady=5, expand=True, fill="x")
            #endregion

            # region Nº RRT Execução
            self.numero_rrt_execucao = ctk.CTkEntry(self.tabFrame_RRTs, placeholder_text="Nº RRT Execução")
            self.numero_rrt_execucao.pack(side="left", padx=10, pady=5, expand=True, fill="x")
            # endregion

            #region (Texto)
            self.texto_scrollable_frame = ctk.CTkLabel(self.tabview2.tab("Detalhes projeto"), fg_color="transparent",
                                                       text='Adicione detalhes sobre cada etapa:')
            self.texto_scrollable_frame.pack(padx=0, pady=0, fill="x", anchor='n')
            #endregion

            #region Adicione detalhes sobre o projeto

            #region SCROLLABLE FRAME
            self.scrollable_frame = ctk.CTkScrollableFrame(self.tabview2.tab("Detalhes projeto"))
            self.scrollable_frame.pack(padx=10, pady=10, fill='both', expand=True)
            #endregion

            self.field_values = {} # O valor dos campos será armazenado em um dicionário

            self.create_initial_fields()

            #region (FRAME > 2 BOTÕES) Frame: Adicionar e Verificar
            self.Frame_Adicionar_Verificar = ctk.CTkFrame(self.tabview2.tab("Detalhes projeto"), fg_color="transparent")
            self.Frame_Adicionar_Verificar.pack(pady=0, padx=10, expand=True,  anchor='e')

            #region (Botão) Verificar dados (DESATIVADO)
            self.verify_button = ctk.CTkButton(self.Frame_Adicionar_Verificar, text="Verificar Dados",
                                               command=self.verify_data, width=50)
            #self.verify_button.pack(padx=10, pady=0, side='left')
            # endregion

            #region (Botão) Adicionar
            self.add_button = ctk.CTkButton(self.Frame_Adicionar_Verificar, text="Adicionar item",
                                            command=self.add_field_frame, width=60, fg_color='#3cb878', hover_color=
                                            '#20A963')
            self.add_button.pack(padx=10, pady=0, side='left')
            #endregion

            # endregion

            # Adicione outros elementos da aba Pessoa Jurídica conforme necessário

            # endregion

            #endregion

            # endregion

            # region (Tab) Pagamento

            self.tabview2.add("Pagamento")

            # region (inside Tab "Pagamento") (FRAME) Preço + Forma de pagamento + Qtd. Parcelas (opcional)

            def atualizar_estado_numero_parcelas(event):
                if self.condicoes_de_pagamento.get() == "Parcelado" or self.condicoes_de_pagamento.get() == "Cartão " \
                                                                                                            "de " \
                                                                                                            "crédito":
                    self.frame_entrada_quitacao.pack(padx=0, pady=0, fill="x", anchor='n')
                else:
                    self.frame_entrada_quitacao.pack_forget()  # Ocultar o elemento

            #region FRAME
            self.tabFrame_Pagamento_3_em_1 = ctk.CTkFrame(self.tabview2.tab("Pagamento"), fg_color="transparent")
            self.tabFrame_Pagamento_3_em_1.pack(padx=0, pady=0, fill="x", anchor='n')
            #endregion

            #region Valor do projeto
            self.valor_do_projeto = ctk.CTkEntry(self.tabFrame_Pagamento_3_em_1, placeholder_text="Valor do Projeto",
                                                 width=110)
            self.valor_do_projeto.pack(side="left", padx=10, pady=5, expand=True, fill="x")
            #endregion

            # region Prazo
            self.prazo_para_pagamento = ctk.CTkComboBox(self.tabFrame_Pagamento_3_em_1,
                                                          values=prazos_list, width=85,
                                                          command=atualizar_estado_numero_parcelas)
            self.prazo_para_pagamento.pack(side="left", padx=0, pady=5, expand=True, fill="x")
            # endregion

            # region Condições de pagamento
            self.condicoes_de_pagamento = ctk.CTkComboBox(self.tabFrame_Pagamento_3_em_1,
                                                          values=condicoes_de_pagamento_list, width=100,
                                                          command=atualizar_estado_numero_parcelas)
            self.condicoes_de_pagamento.pack(side="left", padx=10, pady=5, expand=True, fill="x")
            # endregion

            def calcular_parcela(_):

                try:
                    # Obter a opção selecionada na combobox de entrada
                    entrada_selecionada = self.porcentagem_valor_de_ENTRADA_projeto.get()
                    valor_do_projeto = self.valor_do_projeto.get()

                    # Remover o caractere '%' e converter para um número inteiro
                    entrada_selecionada = int(entrada_selecionada.rstrip('%'))
                    valor_do_projeto = int(valor_do_projeto.rstrip('.'))

                    # Calcular o valor restante para a quitação
                    quitacao = 100 - entrada_selecionada


                    pagamento_entrada = valor_do_projeto * entrada_selecionada/100 # Calculando o valor da entrada

                    pagamento_quitacao = valor_do_projeto * quitacao/100 # Calculando o valor da quitação

                    # Atualizar o valor da combobox de quitação
                    #.porcentagem_valor_de_QUITACAO_projeto.set(f"{quitacao}%")

                    # region CALCULAR VALOR DE CADA PARCELA
                    def calcular_valor_da_parcela():
                        try:
                            numero_de_parcelas_selecionada = self.numero_parcelas.get()
                            numero_de_parcelas_selecionada = int(
                                numero_de_parcelas_selecionada.split('x')[0])  # Remova a conversão para lista
                            valor_da_parcela = pagamento_quitacao / numero_de_parcelas_selecionada
                            valor_da_parcela = round(valor_da_parcela, 2)
                            return valor_da_parcela

                        except:
                            return None

                    valor_da_parcela = calcular_valor_da_parcela()

                    # endregion

                    #manipular elementos da Aba pagamento aqui

                    self.resumo_valor_do_projeto.configure(text=f"RESUMO"
                                                                f"\n\nEntrada = R$ {pagamento_entrada}\n"
                                                                f"Quitação = R$ {pagamento_quitacao}\n"
                                                                f"Valor de cada parcela = R$ {valor_da_parcela}\n")
                    self.resumo_valor_do_projeto.pack(padx=10, pady=10, anchor='n', fill='x',
                                                      expand=True)


                except ValueError: # Cai aqui, se o usuário tiver deixado o campo 'Valor do projeto' em branco
                    pass

            #region (FRAME) Entrada + Quitação (Calculado automáticamente)

            #region (Frame)
            self.frame_entrada_quitacao = ctk.CTkFrame(self.tabview2.tab("Pagamento"), fg_color='transparent')
            #self.frame_entrada_quitacao.pack(padx=0, pady=0, fill="x", anchor='n')
            #endregion

            # region número de Parcelas
            self.numero_parcelas = ctk.CTkComboBox(self.frame_entrada_quitacao,
                                                   values=numero_de_parcelas_list, command=calcular_parcela, width=95)
            self.numero_parcelas.pack(side="left", padx=10, pady=5, expand=True, fill="x")  # Exibir o elemento
            # endregion

            #region ENTRADA

            self.porcentagem_valor_de_ENTRADA_projeto = ctk.CTkComboBox(self.frame_entrada_quitacao,
                                                                   values=porcentagem_ENTRADA_list, width=95)
            self.porcentagem_valor_de_ENTRADA_projeto.pack(side='left', padx=0, pady=10, anchor='n', fill='x',
                                                           expand=True)

            def calcular_quitacao(_):

                try:
                    # Obter a opção selecionada na combobox de entrada
                    entrada_selecionada = self.porcentagem_valor_de_ENTRADA_projeto.get()
                    valor_do_projeto = self.valor_do_projeto.get()

                    # Remover o caractere '%' e converter para um número inteiro
                    entrada_selecionada = int(entrada_selecionada.rstrip('%'))
                    valor_do_projeto = int(valor_do_projeto.rstrip('.'))

                    # Calcular o valor restante para a quitação
                    quitacao = 100 - entrada_selecionada


                    pagamento_entrada = valor_do_projeto * entrada_selecionada/100 # Calculando o valor da entrada

                    pagamento_quitacao = valor_do_projeto * quitacao/100 # Calculando o valor da quitação

                    # Atualizar o valor da combobox de quitação
                    self.porcentagem_valor_de_QUITACAO_projeto.set(f"{quitacao}%")

                    # region CALCULAR VALOR DE CADA PARCELA
                    def calcular_valor_da_parcela():
                        try:
                            numero_de_parcelas_selecionada = self.numero_parcelas.get()
                            numero_de_parcelas_selecionada = int(
                                numero_de_parcelas_selecionada.split('x')[0])  # Remova a conversão para lista
                            valor_da_parcela = pagamento_quitacao / numero_de_parcelas_selecionada
                            valor_da_parcela = round(valor_da_parcela, 2)
                            return valor_da_parcela

                        except:
                            return None

                    valor_da_parcela = calcular_valor_da_parcela()

                    # endregion

                    #manipular elementos da Aba pagamento aqui

                    self.resumo_valor_do_projeto.configure(text=f"RESUMO"
                                                                f"\n\nEntrada = R$ {pagamento_entrada}\n"
                                                                f"Quitação = R$ {pagamento_quitacao}\n"
                                                                f"Valor de cada parcela = R$ {valor_da_parcela}\n")
                    self.resumo_valor_do_projeto.pack(padx=10, pady=10, anchor='e', fill='x',
                                                      expand=True)


                except ValueError: # Cai aqui, se o usuário tiver deixado o campo 'Valor do projeto' em branco
                    pass

            # Adicionar o comando 'calcular_quitacao' ao combobox de entrada
            self.porcentagem_valor_de_ENTRADA_projeto.configure(command=calcular_quitacao)

            #endregion

            #region QUITAÇÃO

            self.porcentagem_valor_de_QUITACAO_projeto = ctk.CTkComboBox(self.frame_entrada_quitacao,
                                                                        values=porcentagem_QUITACAO_list, width=95)
            self.porcentagem_valor_de_QUITACAO_projeto.pack(side='left', padx=10, pady=10, anchor='n', fill='x',
                                                           expand=True)

            #endregion

            # endregion

            # region Exibir Resumo do Projeto
            self.resumo_valor_do_projeto = ctk.CTkLabel(self.tabview2.tab("Pagamento"),
                text='')

            # endregion

            #region (inside Tab "Pagamento") NOTA

            #region (FRAME) Texto (LABEL) + Input Texto Longo (TextBox)
            self.Frame_Texto_Input_Nota = ctk.CTkFrame(self.tabview2.tab("Pagamento"), fg_color="transparent")
            self.Frame_Texto_Input_Nota.pack(padx=0, pady=0, fill="x", side='bottom')
            #endregion

            #region Nota (TEXT)
            self.texto_nota_pagamento = ctk.CTkLabel(self.Frame_Texto_Input_Nota, text='Nota:')
            self.texto_nota_pagamento.pack(padx=10, pady=5, anchor='w')

            # endregion

            #region Nota (INPUT)
            self.nota_pagamento = ctk.CTkTextbox(self.Frame_Texto_Input_Nota, activate_scrollbars=True,
                                                    width=40, height=80, fg_color='transparent', border_width=2,
                                                       border_color=cor_cinza_escuro_botao)
            self.nota_pagamento.pack(padx=10, pady=0, fill="x")

            # endregion
            #endregion

            # Adicione outros elementos da aba Pessoa Jurídica conforme necessário

            # endregion

            return self.tabview2

            #endregion

        # endregion

        # region (TAB VIEW 3) (CREATE) DOCUMENTOS

        #region Buscar modelos_documentos existentes
        def buscar_documentos():
            # Caminho para a pasta modelos_documentos
            pasta_documentos = 'resources/modelos_documentos'

            # Listar os arquivos na pasta modelos_documentos
            arquivos_contratos = os.listdir(pasta_documentos)
            lista_documentos = []
            for arquivo in arquivos_contratos:
                if arquivo.endswith('.docx'):
                    lista_documentos.append(arquivo)

            return lista_documentos

        arquivos_contratos = buscar_documentos()
        print('Documentos disponíveis:', arquivos_contratos)

        #endregion

        #region (TAB) Documentos
        def tab_view_3():

            #region (FRAME) Documentos

            #region Frame
            self.frame_documentos = ctk.CTkFrame(self)
            self.frame_documentos.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
            #endregion

            #region (SCROLLABLE FRAME) Lista de documento
            self.scrollable_frame_documentos = ctk.CTkScrollableFrame(self.frame_documentos,
                                                                      label_text='Lista de documentos',
                                                                      fg_color='transparent')

            # Posicionamento do objeto scrollable_frame_documentos na grade (row=0, column=1) dentro do widget pai
            self.scrollable_frame_documentos.pack(padx=0, pady=0, fill="both", expand=True)

            # Criação de uma lista vazia para armazenar os switches dos modelos_documentos
            self.scrollable_frame_documentos_switches = []

            # Loop para percorrer cada arquivo na lista arquivos_contratos
            for arquivo in arquivos_contratos:
                if arquivo.endswith(".docx"): # Se a extensão do arquivo for .docx
                    # Criação de um objeto switch como uma instância da classe CTkSwitch, passando o objeto scrollable_frame_documentos como mestre,
                    # e definindo o texto do switch como o nome do arquivo
                    nome_do_documento = os.path.splitext(arquivo)
                    switch = ctk.CTkSwitch(master=self.scrollable_frame_documentos, text=f"{nome_do_documento[0]}",
                                           command=self.verificar_switches, variable=ctk.BooleanVar(value=True)) #
                    # ctk.BooleanVar(value=True), define todos os Switches como 'True'.

                    # Posicionamento do objeto switch dentro do objeto scrollable_frame_documentos usando o método pack,
                    # com o preenchimento horizontal ("x") e as margens de espaçamento
                    switch.pack(padx=10, pady=5, fill="x")

                    # Adição do objeto switch à lista self.scrollable_frame_documentos_switches
                    self.scrollable_frame_documentos_switches.append(switch)

            # endregion

            # region (DROPDOWN) Formato do documento (PDF, DOCS, ou AMBOS?)

            self.extensao_documento = ctk.CTkComboBox(self.frame_documentos,
                                                              values=extensao_documento_list, width=100,
                                                      command=self.verificar_extensao)
            self.extensao_documento.pack(anchor='e', padx=10, pady=10)

            #endregion

            #endregion

            return self.frame_documentos

        # endregion

        #endregion

        #endregion

        # region (FRAME) (CREATE) BARRA DE AÇÕES

        def frame_acoes():
            self.frameacoes = ctk.CTkFrame(self, width=250, height=50)
            self.frameacoes.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

            # region (inside SIDEBAR BOTTOM) (BUTTON) Preencher documento(s)
            self.botao_preencher_documentos = ctk.CTkButton(self.frameacoes, fg_color=cor_azul_claro,
                                                            hover_color=cor_azul_escuro, width=70,
                                                            text_color='white', text='Iniciar',
                                                            command=self.iniciar)
            self.botao_preencher_documentos.pack(padx=10, pady=10, anchor='e')
            #endregion

            '''# region (inside SIDEBAR BOTTOM) (IMAGEM) Multiplos Arquivos (BOTTOM)

            self.logo_image = ctk.CTkImage(Image.open(fp="icon_multiple_files.png"), size=(20, 27))
            self.logo_label = ctk.CTkLabel(self.frameacoes, image=self.logo_image, text="")
            self.logo_label.pack(pady=10, padx=10, side="right")
            self.logo_label.bind("<Button-1>", self.iniciar)  # multiple_files_click-  Adiciona o evento
            # de clique

            # endregion

            # region (inside SIDEBAR BOTTOM) (IMAGEM) Um Arquivo (BOTTOM)

            self.logo_image = ctk.CTkImage(Image.open(fp="icon_one_file.png"), size=(20, 27), )
            self.logo_label = ctk.CTkLabel(self.frameacoes, image=self.logo_image, text="")
            self.logo_label.pack(pady=10, padx=0, side="right")
            self.logo_label.bind("<Button-1>", self.one_file_click)  # Adiciona o evento de clique

            # endregion'''

        # endregion

        # region *** CONTROLE DE VISIBILIDADE DAS TABS ***

        # Cria a guia "Profissional"
        self.tabview1 = tab_view_1()

        # Cria a guia "Cliente"
        self.tabview2 = tab_view_2()

        # Cria a guia "Documentos"
        self.tabview3 = tab_view_3()

        # Cria a guia "Documentos"
        self.frameacoes = frame_acoes()

        # Ajuste a visibilidade das guias
        self.tabview1.tkraise()  # Define a guia "Profissional" como ativa inicialmente
        self.tabview2.grid_remove()  # Oculta a guia "Cliente"
        self.tabview3.grid_remove()  # Oculta a guia "Documentos"

        # endregion

        # ███ BOTTOM ███
        # region (SIDEBAR) Logo > BOTTOM

        # region (SIDEBAR BOTTOM) Frame: LOGO (sidebar_logo)
        self.sidebar_logo = ctk.CTkFrame(self, width=50, height=20, corner_radius=8, fg_color="transparent")
        self.sidebar_logo.grid(row=2, column=1, columnspan=2, sticky="nsew", padx=10, pady=0)
        # endregion

        # region (inside SIDEBAR BOTTOM) (IMAGEM) LOGOTIPO (BOTTOM)

        # self.logo_github_image = ctk.CTkImage(Image.open("logo_github.png"), size=(45, 40))
        # self.logo_github_label = ctk.CTkLabel(self, image=self.logo_github_image, text="")
        # self.logo_github_label.grid(row=1, column=0, sticky="w", padx=10, pady=20)

        # region (inside SIDEBAR BOTTOM) (IMAGEM) LOGOTIPO (BOTTOM)

        #self.logo_image = ctk.CTkImage(Image.open(fp="FastDoc-Dark-Mode.png"), size=(113, 25))# REATIVAR LOGO
        #self.logo_label = ctk.CTkLabel(self, image=self.logo_image, text="")# REATIVAR LOGO
        #self.logo_label.grid(row=2, column=1, sticky="e", padx=10, pady=20)# REATIVAR LOGO

        # endregion

        # endregion

        # region (GRID) LAYOUT

        # LINHAS
        self.grid_rowconfigure(index=0, weight=1)  # LINHA 0
        self.grid_rowconfigure(index=1, weight=0)  # LINHA 1

        # COLUNAS
        self.grid_columnconfigure(index=0, weight=0)  # COLUNA 0
        self.grid_columnconfigure(index=1, weight=1)  # COLUNA 1

        # endregion

        # endregion

    # endregion

    #region DEF'S

    #region DEF's > DOCUMENTOS

    #region Verifica quais Documentos o usuário selecionou
    def verificar_switches(self):
        global documentos_selecionados
        documentos_selecionados = []

        for switch in self.scrollable_frame_documentos_switches:
            if switch.get() == 1:
                documentos_selecionados.append(switch.cget('text'))

        # Agora você tem a lista de modelos_documentos selecionados
        # Faça o que for necessário com essa lista
        print("Documentos selecionados:", documentos_selecionados)

        return documentos_selecionados

    #endregion

    #region Verifica se o usuário prefere .PDF, .DOCX ou AMBOS
    def verificar_extensao(self, event):
        extensao_selecionada = self.extensao_documento.get()
        if extensao_selecionada == "PDF" or extensao_selecionada == "Ambos":
            print(f'Extensão selecionada: {extensao_selecionada}')
        else:
            print(f'Extensão selecionada: {extensao_selecionada}')
    #endregion

    #endregion

    # region CONFIGS - SCROLLABLE FRAME 'Detalhes do projeto'

    #region - Cria os campos iniciais para entrada de dados
    def create_initial_fields(self):
        field_frame = self.create_field_frame()
        field_frame.pack(side='top', pady=0, expand=True)
        self.field_values[field_frame] = self.get_field_entries(field_frame)

    # endregion

    #region - Cria um frame para os campos de entrada
    def create_field_frame(self):
        field_frame = ctk.CTkFrame(self.scrollable_frame, corner_radius=8, fg_color='transparent')
        field_frame.pack(padx=10, pady=0, fill='x', expand=True)
        return field_frame

    # endregion

    #region - Obtém os campos de entrada do frame fornecido
    def get_field_entries(self, field_frame):

        # region (INPUT) Titulo
        titulo_detalhe_etapa = ctk.CTkEntry(field_frame, placeholder_text=random.choice(frases_exemplos_detalhes))
        titulo_detalhe_etapa.pack(padx=0, pady=5, fill='x', expand=True)
        # endregion

        # region (INPUT) Descrição
        descricao_detalhe_etapa = ctk.CTkTextbox(field_frame, width=10, height=60, border_width=2,
                                                 border_color=cor_cinza_escuro_botao,
                                                 fg_color='transparent')
        descricao_detalhe_etapa.pack(padx=0, pady=5, fill='x', expand=True)
        # endregion

        # Criação do botão "Deletar"
        delete_button = ctk.CTkButton(field_frame, text="Deletar", command=lambda: self.delete_field_frame(
            field_frame), width=30, fg_color='#f14f5d', hover_color='#DE293A')
        delete_button.pack(side='right')

        return titulo_detalhe_etapa, descricao_detalhe_etapa

    # endregion

    #region - Adiciona um novo frame de campos
    def add_field_frame(self):
        field_frame = self.create_field_frame()
        field_frame.pack(side='top', pady=10)
        self.field_values[field_frame] = self.get_field_entries(field_frame)

    # endregion

    #region - Deleta um frame de campos fornecido
    def delete_field_frame(self, field_frame):
        field_frame.destroy()
        del self.field_values[field_frame]

    # endregion

    #region - Verifica os dados dos campos de entrada
    def verify_data(self):
        for field_frame, (title_entry, desc_entry) in self.field_values.items():
            title = title_entry.get()
            desc = desc_entry.get('1.0', 'end-1c')  # Obtém todo o texto do CTkTextbox
            print(f"Title: {title}, Description: {desc}")

    #endregion

    # endregion

    # region DEF's > BARRA DE AÇÕES

    # region Botão iniciar
    def iniciar(self):

        print('\n---- BOTÃO "INICIAR" CLICADO ----\n')

        #region (Progress Bar) Atualiza para 99%
        self.progressbar_1.set(0.99)  # Atualize o valor da barra de progresso
        #endregion

        # region (GET) 2º - Valores dos campos

        print("Pegando os valores inseridos nos campos")
        # Obtém os valores inseridos noos campos e salva em variáveis

        # region (GET) INFORMAÇÕES DO PROFISSIONAL (OK)

        # region Profissional > Pessoa Física (OK)
        nome_completo_profissional_value = self.nome_completo_profissional.get()
        email_profissional_value = self.email_profissional.get()
        nacionalidade_profissional_value = self.nacionalidade_profissional.get()
        estado_civil_profissional_value = self.estado_civil_profissional.get()
        profissao_profissional_value = self.profissao_profissional.get()
        numero_registro_cau_crea_value = self.numero_registro_cau_crea.get()
        numero_cpf_profissional_value = self.numero_cpf_profissional.get()
        cep_profissional_value = self.cep_profissional.get()
        numero_endereco_profissional_value = self.numero_endereco_profissional.get()
        complemento_endereco_profissional_value = self.complemento_endereco_profissional.get()
        logradouro_profissional_value = self.logradouro_profissional.get()
        bairro_endereco_profissional_value = self.bairro_endereco_profissional.get()
        cidade_endereco_profissional_value = self.cidade_endereco_profissional.get()
        uf_endereco_profissional_value = self.uf_endereco_profissional.get()
        # endregion

        # region Profissional > Pessoa Jurídica (OK)
        cnpj_empresarial_value = self.cnpj_empresarial.get()
        razao_social_empresarial_value = self.razao_social_empresarial.get()
        nome_fantasia_empresarial_value = self.nome_fantasia_empresarial.get()
        logradouro_empresarial_value = self.logradouro_empresarial.get()
        numero_endereco_empresarial_value = self.numero_endereco_empresarial.get()
        detalhes_endereco_empresarial_value = self.detalhes_endereco_empresarial.get()
        bairro_endereco_empresarial_value = self.bairro_endereco_empresarial.get()
        cidade_endereco_empresarial_value = self.cidade_endereco_empresarial.get()
        uf_endereco_empresarial_value = self.uf_endereco_empresarial.get()
        email_empresarial_value = self.email_empresarial.get()
        telefone_empresarial_value = self.telefone_empresarial.get()
        # endregion

        # endregion

        # region (GET) INFORMAÇÕES DO CLIENTE (OK)

        # region Cliente > Pessoa Física (OK)
        nome_completo_cliente_value = self.nome_completo_cliente.get()
        email_cliente_value = self.email_cliente.get()
        telefone_cliente_PF_value = self.telefone_cliente_PF.get()
        nacionalidade_cliente_value = self.nacionalidade_cliente.get()
        estado_civil_cliente_value = self.estado_civil_cliente.get()
        profissao_cliente_value = self.profissao_cliente.get()
        cpf_cliente_value = self.cpf_cliente.get()
        rede_social_cliente_value = self.rede_social_cliente.get()
        cep_cliente_value = self.cep_cliente.get()
        numero_endereco_cliente_value = self.numero_endereco_cliente.get()
        complemento_endereco_cliente_value = self.complemento_endereco_cliente.get()
        logradouro_cliente_PF_value = self.logradouro_cliente_PF.get()
        bairro_endereco_cliente_PF_value = self.bairro_endereco_cliente_PF.get()
        cidade_endereco_cliente_PF_value = self.cidade_endereco_cliente_PF.get()
        uf_endereco_cliente_PF_value = self.uf_endereco_cliente_PF.get()
        # endregion

        # region Cliente > Pessoa Jurídica (OK)
        cnpj_cliente_PJ_value = self.cnpj_cliente_PJ.get()
        razao_social_cliente_PJ_value = self.razao_social_cliente_PJ.get()
        nome_fantasia_cliente_PJ_value = self.nome_fantasia_cliente_PJ.get()
        email_cliente_PJ_value = self.email_cliente_PJ.get()
        telefone_cliente_PJ_value = self.telefone_cliente_PJ.get()
        logradouro_cliente_PJ_value = self.logradouro_cliente_PJ.get()
        numero_endereco_cliente_PJ_value = self.numero_endereco_cliente_PJ.get()
        detalhes_endereco_cliente_PJ_value = self.detalhes_endereco_cliente_PJ.get()
        bairro_endereco_cliente_PJ_value = self.bairro_endereco_cliente_PJ.get()
        cidade_endereco_cliente_PJ_value = self.cidade_endereco_cliente_PJ.get()
        uf_endereco_cliente_PJ_value = self.uf_endereco_cliente_PJ.get()
        # endregion

        #region Cliente > Detalhes do projeto
        numero_rrt_projeto_value = self.numero_rrt_projeto.get()
        numero_rrt_execucao_value = self.numero_rrt_execucao.get()
        #titulo_detalhe_etapa_value = self.titulo_detalhe_etapa.get() # ARRUMAR
        #descritivo_detalhe_etapa_value = self.descritivo_detalhe_etapa.get() # ARRUMAR
        # endregion

        #region Cliente > Pagamento
        valor_do_projeto_value = self.valor_do_projeto.get()
        prazo_para_pagamento_value = self.prazo_para_pagamento.get()
        condicoes_de_pagamento_value = self.condicoes_de_pagamento.get()
        numero_parcelas_value = self.numero_parcelas.get()
        porcentagem_valor_de_ENTRADA_projeto_value = self.porcentagem_valor_de_ENTRADA_projeto.get()
        porcentagem_valor_de_QUITACAO_projeto_value = self.porcentagem_valor_de_QUITACAO_projeto.get()
        nota_pagamento_value = self.nota_pagamento.get('1.0', 'end-1c')
        #endregion

        #endregion

        # region (GET) Documentos selecionados
        documentos_selecionados = []

        for switch in self.scrollable_frame_documentos_switches:
            if switch.get() == 1:
                documentos_selecionados.append(switch.cget('text'))

        # Agora você tem a lista de modelos_documentos selecionados
        # Faça o que for necessário com essa lista
        #print("--->>> Documentos selecionados:", documentos_selecionados)
        # endregion

        #region (GET) INFORMAÇÕES SOBRE O(S) DOCUMENTO(S) + EXTENSÃO DESEJADA
        documentos_selecionados_value = documentos_selecionados
        extensao_selecionada_value = self.extensao_documento.get()
        print(f'DEBUG 01: {extensao_selecionada_value}')
        #endregion

        # region ############## APARÊNCIA ################
        appearance_value = self.appearance_mode_optionmenu.get()

        # endregion

        # endregion


        # region (UPDATE) 3º - Valores dicionário

        print("Atualizando o dicionário (user_settings.json) com os dados")
        # Cria um dicionário com os dados
        data = {

            # region (UPDATE) INFORMAÇÕES DO PROFISSIONAL (OK)

            # region Profissional > Pessoa Física (OK)
            "nome_completo_profissional": nome_completo_profissional_value,
            "email_profissional": email_profissional_value,
            "appearance_mode_optionmenu": appearance_value,
            "nacionalidade_profissional": nacionalidade_profissional_value,
            "estado_civil_profissional": estado_civil_profissional_value,
            "profissao_profissional": profissao_profissional_value,
            "numero_registro_cau_crea": numero_registro_cau_crea_value,
            "numero_cpf_profissional": numero_cpf_profissional_value,
            "cep_profissional": cep_profissional_value,
            "numero_endereco_profissional": numero_endereco_profissional_value,
            "complemento_endereco_profissional": complemento_endereco_profissional_value,
            "logradouro_profissional": logradouro_profissional_value,
            "bairro_endereco_profissional": bairro_endereco_profissional_value,
            "cidade_endereco_profissional": cidade_endereco_profissional_value,
            "uf_endereco_profissional": uf_endereco_profissional_value,
            # endregion

            # region Profissional > Pessoa Jurídica (OK)
            "cnpj_empresarial": cnpj_empresarial_value,
            "razao_social_empresarial": razao_social_empresarial_value,
            "nome_fantasia_empresarial": nome_fantasia_empresarial_value,
            "logradouro_empresarial": logradouro_empresarial_value,
            "numero_endereco_empresarial": numero_endereco_empresarial_value,
            "detalhes_endereco_empresarial": detalhes_endereco_empresarial_value,
            "bairro_endereco_empresarial": bairro_endereco_empresarial_value,
            "cidade_endereco_empresarial": cidade_endereco_empresarial_value,
            "uf_endereco_empresarial": uf_endereco_empresarial_value,
            "email_empresarial": email_empresarial_value,
            "telefone_empresarial": telefone_empresarial_value,
            # endregion

            # endregion

        }

        # endregion

        # region (POST) Valores no user_settings.JSON

        print("Salvando os dados no arquivo JSON")
        # Salva os dados no arquivo JSON
        with open("user_setting.json", "w") as file:
            json.dump(data, file)

        # endregion

        #region (POST) Valores na base de dados (Salvar no excel)
        print('A FAZER: Salvando valores na base de dados (excel)')

        def salvar_informacoes():
            # Criar um dicionário com as informações do cliente
            cliente_info = {
                'nome_completo_cliente': nome_completo_cliente_value,
                'email_cliente': email_cliente_value,
                'telefone_cliente_PF': telefone_cliente_PF_value,
                'nacionalidade_cliente': nacionalidade_cliente_value,
                'estado_civil_cliente': estado_civil_cliente_value,
                'profissao_cliente': profissao_cliente_value,
                'cpf_cliente': cpf_cliente_value,
                'rede_social_cliente': rede_social_cliente_value,
                'cep_cliente': cep_cliente_value,
                'numero_endereco_cliente': numero_endereco_cliente_value,
                'complemento_endereco_cliente': complemento_endereco_cliente_value,
                'logradouro_cliente_PF': logradouro_cliente_PF_value,
                'bairro_endereco_cliente_PF': bairro_endereco_cliente_PF_value,
                'cidade_endereco_cliente_PF': cidade_endereco_cliente_PF_value,
                'uf_endereco_cliente_PF': uf_endereco_cliente_PF_value,
                'cnpj_cliente_PJ': cnpj_cliente_PJ_value,
                'razao_social_cliente_PJ': razao_social_cliente_PJ_value,
                'nome_fantasia_cliente_PJ': nome_fantasia_cliente_PJ_value,
                'email_cliente_PJ': email_cliente_PJ_value,
                'telefone_cliente_PJ': telefone_cliente_PJ_value,
                'logradouro_cliente_PJ': logradouro_cliente_PJ_value,
                'numero_endereco_cliente_PJ': numero_endereco_cliente_PJ_value,
                'detalhes_endereco_cliente_PJ': detalhes_endereco_cliente_PJ_value,
                'bairro_endereco_cliente_PJ': bairro_endereco_cliente_PJ_value,
                'cidade_endereco_cliente_PJ': cidade_endereco_cliente_PJ_value,
                'uf_endereco_cliente_PJ': uf_endereco_cliente_PJ_value,
                'numero_rrt_projeto': numero_rrt_projeto_value,
                'numero_rrt_execucao': numero_rrt_execucao_value,
                'valor_do_projeto': valor_do_projeto_value,
                'prazo_para_pagamento': prazo_para_pagamento_value,
                'condicoes_de_pagamento': condicoes_de_pagamento_value,
                'numero_parcelas': numero_parcelas_value,
                'porcentagem_valor_de_ENTRADA_projeto': porcentagem_valor_de_ENTRADA_projeto_value,
                'porcentagem_valor_de_QUITACAO_projeto': porcentagem_valor_de_QUITACAO_projeto_value,
                'nota_pagamento': nota_pagamento_value
            }

            # Verificar se o arquivo de dados já existe
            try:
                df = pd.read_excel('resources/registros_clientes/base_de_dados.xlsx')
            except FileNotFoundError:
                # Caso não exista, criar um novo DataFrame
                df = pd.DataFrame()

            # Adicionar as informações do cliente em uma nova linha
            df = pd.concat([df, pd.DataFrame([cliente_info])], ignore_index=True)

            # Salvar o DataFrame atualizado no arquivo de dados
            df.to_excel('resources/registros_clientes/base_de_dados.xlsx', index=False)

            print("Informações do cliente salvas com sucesso!")
        salvar_informacoes()

        #endregion

        # region (Button) INICIAR --->>> LÓGICA DE PREENCHER OS DOCUMENTOS <<<---

        # AQUI DEFINIMOS TODOS OS CAMPOS OBRIGATÓRIOS
        if nome_completo_cliente_value == '':
            exibir_popup_erro('Informe o nome completo do cliente')
        elif extensao_selecionada_value == 'Extensão':
            exibir_popup_erro('Informe a extensão desejada: PDF, DOCX ou Ambos')
        else:
            # region PopUp de Inicialização (com frase randômica)

            exibir_popup_sucesso(texto=random.choice(frases_popup_iniciar))

            # endregion

            #region INICIAR PREENCHIMENTO DOS DOCUMENTOS
            print('\n---- INICIANDO O PREENCHIMENTO DOS DOCUMENTOS ----\n')

            #region Preencher documento

            # Caminho para a pasta modelos_documentos
            pasta_documentos = 'resources/modelos_documentos'
            pasta_cliente = 'resources/documentos_gerados'

            # Criar a pasta com o nome do cliente
            pasta_cliente = os.path.join(pasta_cliente, nome_completo_cliente_value)
            os.makedirs(pasta_cliente, exist_ok=True)

            documentos_selecionados_value_list = []
            print('DOCUMENTO(S) SELECIONADO(S):')
            for documento in documentos_selecionados_value:
                documento = os.path.join(documento + '.docx')
                print('-', documento)
                documentos_selecionados_value_list.append(documento)
            print(f'\nExtensão desejada: {extensao_selecionada_value}\n')

            # Listar os arquivos na pasta modelos_documentos
            arquivos_contratos = os.listdir(pasta_documentos)
            #print('ARQUIVOS CONTRATOS:', arquivos_contratos, '\n')

            for arquivo in documentos_selecionados_value_list:
                # Verificar se é um arquivo do tipo .docx
                if arquivo.endswith('.docx'):
                    #print('ARQUIVO ENDSWITH', arquivo)

                    # Caminho completo para o contrato original
                    caminho_contrato_original = os.path.join(pasta_documentos, arquivo)  # join() é usado para combinar
                    # componentes de um caminho (como diretórios e nomes de arquivos) em um único caminho.

                    # Caminho completo para o contrato, no diretório do cliente
                    nome_contrato_final = f"{os.path.splitext(arquivo)[0]} - {nome_completo_cliente_value}.docx"  # 'splitext' separa o nome
                    # da extensão.
                    caminho_contrato_final = os.path.join(pasta_cliente, nome_contrato_final)

                    # Copiar o 'contrato original' para um novo arquivo, que será salvo no diretório do cliente.
                    with open(caminho_contrato_original, 'rb') as arquivo_original:  # abre o arquivo original no modo de
                        # leitura binária ('rb')
                        with open(caminho_contrato_final, 'wb') as arquivo_final:  # abre um novo arquivo chamado
                            # "arquivo_final" no modo de escrita binária ('wb')
                            arquivo_final.write(arquivo_original.read())  # realiza a operação de cópia propriamente
                            # dita. Ela
                            # lê o conteúdo do arquivo original usando o método read() e escreve esse conteúdo no arquivo
                            # final usando o método write(). Dessa forma, o arquivo original é copiado para o arquivo final.

                    # Abrir o contrato copiado
                    documento = Document(caminho_contrato_final)

                    referencias = {

                        #region REFERÊNCIAS

                        # region DATA, MÊS E ANO
                        "DD": str(datetime.now().day),
                        "MM": str(datetime.now().month),
                        "AAAA": str(datetime.now().year),
                        # endregion

                        # region PROFISSIONAL

                        # region Profissional > Pessoa Física
                        "{nome_completo_profissional}": nome_completo_profissional_value,
                        "{email_profissional}": email_profissional_value,
                        "{nacionalidade_profissional}": nacionalidade_profissional_value,
                        "{estado_civil_profissional}": estado_civil_profissional_value,
                        "{profissao_profissional}": profissao_profissional_value,
                        "{numero_registro_cau_crea}": numero_registro_cau_crea_value,
                        "{numero_cpf_profissional}": numero_cpf_profissional_value,
                        "{cep_profissional}": cep_profissional_value,
                        "{numero_endereco_profissional}": numero_endereco_profissional_value,
                        "{complemento_endereco_profissional}": complemento_endereco_profissional_value,
                        "{logradouro_profissional}": logradouro_profissional_value,
                        "{bairro_endereco_profissional}": bairro_endereco_profissional_value,
                        "{cidade_endereco_profissional}": cidade_endereco_profissional_value,
                        "{uf_endereco_profissional}": uf_endereco_profissional_value,
                        # endregion

                        # region Profissional > Pessoa Jurídica
                        "{cnpj_empresarial}": cnpj_empresarial_value,
                        "{razao_social_empresarial}": razao_social_empresarial_value,
                        "{nome_fantasia_empresarial}": nome_fantasia_empresarial_value,
                        "{logradouro_empresarial}": logradouro_empresarial_value,
                        "{numero_endereco_empresarial}": numero_endereco_empresarial_value,
                        "{detalhes_endereco_empresarial}": detalhes_endereco_empresarial_value,
                        "{bairro_endereco_empresarial}": bairro_endereco_empresarial_value,
                        "{cidade_endereco_empresarial}": cidade_endereco_empresarial_value,
                        "{uf_endereco_empresarial}": uf_endereco_empresarial_value,
                        "{email_empresarial}": email_empresarial_value,
                        "{telefone_empresarial}": telefone_empresarial_value,
                        # endregion

                        # endregion

                        # region CLIENTE
                        # region Cliente > Info. Contato > Pessoa Física
                        "{nome_completo_cliente}": nome_completo_cliente_value,
                        "{email_cliente}": email_cliente_value,
                        "{telefone_cliente_PF}": telefone_cliente_PF_value,
                        "{nacionalidade_cliente}": nacionalidade_cliente_value,
                        "{estado_civil_cliente}": estado_civil_cliente_value,
                        "{profissao_cliente}": profissao_cliente_value,
                        "{cpf_cliente}": cpf_cliente_value,
                        "{rede_social_cliente}": rede_social_cliente_value,
                        "{cep_cliente}": cep_cliente_value,
                        "{numero_endereco_cliente}": numero_endereco_cliente_value,
                        "{complemento_endereco_cliente}": complemento_endereco_cliente_value,
                        "{logradouro_cliente_PF}": logradouro_cliente_PF_value,
                        "{bairro_endereco_cliente_PF}": bairro_endereco_cliente_PF_value,
                        "{cidade_endereco_cliente_PF}": cidade_endereco_cliente_PF_value,
                        "{uf_endereco_cliente_PF}": uf_endereco_cliente_PF_value,
                        # endregion

                        # region Cliente > Info.Contato > Pessoa Jurídica
                        "{cnpj_cliente_PJ}": cnpj_cliente_PJ_value,
                        "{razao_social_cliente_PJ}": razao_social_cliente_PJ_value,
                        "{nome_fantasia_cliente_PJ}": nome_fantasia_cliente_PJ_value,
                        "{email_cliente_PJ}": email_cliente_PJ_value,
                        "{telefone_cliente_PJ}": telefone_cliente_PJ_value,
                        "{logradouro_cliente_PJ}": logradouro_cliente_PJ_value,
                        "{numero_endereco_cliente_PJ}": numero_endereco_cliente_PJ_value,
                        "{detalhes_endereco_cliente_PJ}": detalhes_endereco_cliente_PJ_value,
                        "{bairro_endereco_cliente_PJ}": bairro_endereco_cliente_PJ_value,
                        "{cidade_endereco_cliente_PJ}": cidade_endereco_cliente_PJ_value,
                        "{uf_endereco_cliente_PJ}": uf_endereco_cliente_PJ_value,
                        # endregion

                        # region Cliente > Detalhes do projeto
                        "{numero_rrt_projeto}": numero_rrt_projeto_value,
                        "{numero_rrt_execucao}": numero_rrt_execucao_value,
                        # endregion

                        # region Cliente > Pagamento
                        "{valor_do_projeto}": valor_do_projeto_value,
                        "{prazo_para_pagamento}": prazo_para_pagamento_value,
                        "{condicoes_de_pagamento}": condicoes_de_pagamento_value,
                        "{numero_parcelas}": numero_parcelas_value,
                        "{porcentagem_valor_de_ENTRADA_projeto}": porcentagem_valor_de_ENTRADA_projeto_value,
                        "{porcentagem_valor_de_QUITACAO_projeto}": porcentagem_valor_de_QUITACAO_projeto_value,
                        "{nota_pagamento}": nota_pagamento_value,
                        # endregion
                        # endregion

                        #endregion

                    }

                    # Em cada parágrafo do documento
                    for paragrafo in documento.paragraphs:
                        texto_paragrafo = paragrafo.text  # Armazena o texto do parágrafo atual
                        for codigo in referencias:  # Itera sobre as referências de substituição
                            valor = referencias[codigo]  # Obtém o valor correspondente à referência
                            texto_paragrafo = texto_paragrafo.replace(codigo,
                                                                      valor)  # Substitui a referência pelo valor no texto do parágrafo
                        paragrafo.text = texto_paragrafo  # Atualiza o texto do parágrafo com as substituições

                    # Salvar o contrato com as alterações no diretório do cliente
                    documento.save(caminho_contrato_final)


                    # Converter para o formato escolhido (se houver conversão)
                    if extensao_selecionada_value in ['PDF', 'Ambos']:
                        caminho_contrato_pdf = os.path.splitext(caminho_contrato_final)[
                                                   0] + '.pdf'  # Gera o caminho para o arquivo PDF convertido
                        convert(caminho_contrato_final, caminho_contrato_pdf)  # Converte o contrato para PDF

                        if extensao_selecionada_value != 'Ambos':
                            os.remove(
                                caminho_contrato_final)  # Remove o contrato no formato .docx se a opção não for "Ambos"

            #endregion

            #region (POPUP) Término
            exibir_popup_termino(random.choice(frases_termino))
            #endregion

            #region (Progress Bar) Atualiza para 0%
            self.progressbar_1.set(0)  # Atualize o valor da barra de progresso
            #endregion

            #endregion

        # endregion

    # endregion

    '''def one_file_click(self, event):
        print('Gerar um documento')

    def multiple_files_click(self, event):
        print('Gerar múltiplos arquivos')'''

    # endregion

    # region DEF's > BOTÕES NA BARRA LATERAL ESQUERDA

    #region (Button) Profissional
    def btn_Profissional(self):

        self.progressbar_1.set(0)  # Atualize o valor da barra de progresso

        # region MUDANDO A COR DOS BOTÕES DA TAB LATERAL
        self.profissional_button.configure(fg_color=cor_azul_claro, hover_color=cor_azul_escuro)  # MUDA PARA AZUL
        self.cliente_button.configure(fg_color=cor_cinza_claro_botao,
                                      hover_color=cor_cinza_escuro_botao)  # MUDA PARA CINZA (PADRÃO)
        self.documentos_button.configure(fg_color=cor_cinza_claro_botao,
                                         hover_color=cor_cinza_escuro_botao)  # MUDA PARA CINZA (PADRÃO)
        # endregion

        # region CONTROLE DE VISIBILIDADE DAS GUIAS
        self.tabview1.grid()  # Exibe a guia "Profissional"
        self.tabview2.grid_remove()  # Oculta a guia "Cliente"
        self.tabview3.grid_remove()  # Oculta a guia "Documentos"
        #endregion

    #endregion

    # region (Button) Cliente
    def btn_Cliente(self):

        self.progressbar_1.set(0.33)  # Atualize o valor da barra de progresso

        # region MUDANDO A COR DOS BOTÕES DA TAB LATERAL
        self.cliente_button.configure(fg_color=cor_azul_claro, hover_color=cor_azul_escuro)  # MUDA PARA AZUL
        self.profissional_button.configure(fg_color=cor_cinza_claro_botao,
                                           hover_color=cor_cinza_escuro_botao)  # MUDA PARA CINZA (PADRÃO)
        self.documentos_button.configure(fg_color=cor_cinza_claro_botao,
                                         hover_color=cor_cinza_escuro_botao)  # MUDA PARA CINZA (PADRÃO)
        # endregion

        #region CONTROLE DE VISIBILIDADE DAS GUIAS
        self.tabview2.grid()  # Exibe a guia "Cliente"
        self.tabview1.grid_remove()  # Oculta a guia "Profissional"
        self.tabview3.grid_remove()  # Oculta a guia "Documentos"
        #endregion

    #endregion

    #region (Button) Doocumentos
    def btn_Documentos(self):

        self.progressbar_1.set(0.66)  # Atualize o valor da barra de progresso

        # region MUDANDO A COR DOS BOTÕES DA TAB LATERAL
        self.documentos_button.configure(fg_color=cor_azul_claro, hover_color=cor_azul_escuro)  # MUDA PARA AZUL
        self.profissional_button.configure(fg_color=cor_cinza_claro_botao,
                                           hover_color=cor_cinza_escuro_botao)  # MUDA PARA CINZA (PADRÃO)
        self.cliente_button.configure(fg_color=cor_cinza_claro_botao,
                                      hover_color=cor_cinza_escuro_botao)  # MUDA PARA CINZA (PADRÃO)
        # endregion

        # region CONTROLE DE VISIBILIDADE DAS GUIAS
        self.tabview3.grid()  # Exibe a guia "Documentos"
        self.tabview1.grid_remove()  # Oculta a guia "Profissional"
        self.tabview2.grid_remove()  # Oculta a guia "Cliente"
        #endregion

    #endregion

    # endregion

    #region DEF's > TAB 'Cliente'

    #region SWITCHER Cliente PF/PJ
    def switcher_cliente_PF_PJ(self):

        # SE o texto do Switcher (switcher_cliente_PF_PJ) for igual a 'Pessoa Física'
        if self.switcher_cliente_PF_PJ.cget('text') == 'Pessoa Física':
            self.switcher_cliente_PF_PJ.configure(text='Pessoa Jurídica') # SE for igual a 'Pessoa Física',
            # muda pra 'Pessoa Jurídica'

            self.switcher_frame_cliente_PF.forget()# Oculta o frame PF
            self.switcher_frame_cliente_PJ.pack(expand=True, fill='both')# Exibe o frame PJ

        # SE o texto do Switcher (switcher_cliente_PF_PJ) for igual a 'Pessoa Jurídica'
        else:
            self.switcher_cliente_PF_PJ.configure(text='Pessoa Física') # SE for igual a 'Pessoa Jurídica',
            # muda pra 'Pessoa Física'

            self.switcher_frame_cliente_PJ.forget()  # Oculta o frame PJ
            self.switcher_frame_cliente_PF.pack(expand=True, fill='both')  # Exibe o frame PF

    #endregion

    #endregion

    #endregion

    # region (GET) 4º - Valores no user_settings.JSON (LOAD DATA)

    def load_data(self):

        # Tenta carregar os dados do arquivo JSON
        with open("user_setting.json", "r") as file:
            data = json.load(file)

            # region (LOAD DATA) PAINEL LATERAL

            # region Aparência

            try:
                ################ APARÊNCIA ################
                appearance_value = data.get("appearance_mode_optionmenu", "System")
                self.appearance_mode_optionmenu.set(appearance_value)  # Define o valor do dropdown
                self.change_appearance_mode(appearance_value)  # Atualiza a aparência
            except:
                pass

            # endregion

            # endregion

            #region (LOAD DATA) PROFISSIONAL

            #region Pessoa Física (OK)

            # region Nome completo
            try:
                nome_completo_profissional_value = data.get("nome_completo_profissional", "")
                if nome_completo_profissional_value != "":
                    self.nome_completo_profissional.insert(0, nome_completo_profissional_value)  # Insere o novo valor
            except:
                pass
            # endregion

            # region E-mail
            try:
                email_profissional_value = data.get("email_profissional", "")
                self.email_profissional.delete(0, "end")  # Limpa o campo existente
                self.email_profissional.insert(0, email_profissional_value)  # Insere o novo valor no campo
            except:
                pass
            # endregion

            # region Nacionalidade
            try:
                nacionalidade_profissional_value = data.get("nacionalidade_profissional", "Nacionalidade")
                self.nacionalidade_profissional.set(nacionalidade_profissional_value)  # Define o valor do dropdown
                self.change_appearance_mode(nacionalidade_profissional_value)  # Atualiza a aparência
            except:
                pass
            # endregion

            # region Estadlo civil
            try:
                estado_civil_profissional_value = data.get("estado_civil_profissional", "Estado civil")
                self.estado_civil_profissional.set(estado_civil_profissional_value)  # Define o valor do dropdown
                self.change_appearance_mode(estado_civil_profissional_value)  # Atualiza a aparência
            except:
                pass
            # endregion

            # region Profissão
            try:
                profissao_profissional_value = data.get("profissao_profissional", "Profissão")
                self.profissao_profissional.set(profissao_profissional_value)  # Define o valor do dropdown
                self.change_appearance_mode(profissao_profissional_value)  # Atualiza a aparência
            except:
                pass
            # endregion

            # region CAU/CREA
            try:
                numero_registro_cau_crea_value = data.get("numero_registro_cau_crea", "")
                if numero_registro_cau_crea_value != "":
                    self.numero_registro_cau_crea.insert(0, numero_registro_cau_crea_value)  # Insere o novo valor
            except:
                pass
            # endregion

            # region CPF
            try:
                numero_cpf_profissional_value = data.get("numero_cpf_profissional", "")
                if numero_cpf_profissional_value != "":
                    self.numero_cpf_profissional.insert(0, numero_cpf_profissional_value)  # Insere o novo valor
            except:
                pass
            # endregion

            # region CEP
            try:
                cep_profissional_value = data.get("cep_profissional", "")
                if cep_profissional_value != "":
                    self.cep_profissional.insert(0, cep_profissional_value)  # Insere o novo valor
            except:
                pass
            # endregion

            # region Número
            try:
                numero_endereco_profissional_value = data.get("numero_endereco_profissional", "")
                if numero_endereco_profissional_value != "":
                    self.numero_endereco_profissional.insert(0,
                                                             numero_endereco_profissional_value)  # Insere o novo valor
            except:
                pass
            # endregion

            # region Complemento
            try:
                complemento_endereco_profissional_value = data.get("complemento_endereco_profissional", "")
                if complemento_endereco_profissional_value != "":
                    self.complemento_endereco_profissional.insert(0,
                                                                  complemento_endereco_profissional_value)  # Insere o novo valor
            except:
                pass
            # endregion

            # region Logradouro
            try:
                logradouro_profissional_value = data.get("logradouro_profissional", "")
                if logradouro_profissional_value != "":
                    self.logradouro_profissional.insert(0, logradouro_profissional_value)  # Insere o novo
                    # valor
            except:
                pass
            # endregion

            # region Bairro
            try:
                bairro_endereco_profissional_value = data.get("bairro_endereco_profissional", "")
                if bairro_endereco_profissional_value != "":
                    self.bairro_endereco_profissional.insert(0, bairro_endereco_profissional_value)  # Insere o
                    # novo valor
            except:
                pass
            # endregion

            # region Cidade
            try:
                cidade_endereco_profissional_value = data.get("cidade_endereco_profissional", "")
                if cidade_endereco_profissional_value != "":
                    self.cidade_endereco_profissional.insert(0, cidade_endereco_profissional_value)  # Insere o
                    # novo valor
            except:
                pass
            # endregion

            # region UF
            try:
                uf_endereco_profissional_value = data.get("uf_endereco_profissional", "")
                if uf_endereco_profissional_value != "":
                    self.uf_endereco_profissional.insert(0, uf_endereco_profissional_value)  # Insere o novo
                    # valor
            except:
                pass
            # endregion

            # endregion

            #region Pessoa Jurídica (OK)

            # region CNPJ Empresarial
            try:
                cnpj_empresarial_value = data.get("cnpj_empresarial", "")
                if cnpj_empresarial_value != "":
                    self.cnpj_empresarial.insert(0, cnpj_empresarial_value)  # Insere o novo valor
            except:
                pass
            # endregion

            # region Razão Social Empresarial
            try:
                razao_social_empresarial_value = data.get("razao_social_empresarial", "")
                if razao_social_empresarial_value != "":
                    self.razao_social_empresarial.insert(0, razao_social_empresarial_value)  # Insere o novo valor
            except:
                pass
            # endregion

            # region Nome Fantansia Empresarial
            try:
                nome_fantasia_empresarial_value = data.get("nome_fantasia_empresarial", "")
                if nome_fantasia_empresarial_value != "":
                    self.nome_fantasia_empresarial.insert(0, nome_fantasia_empresarial_value)  # Insere o novo valor
            except:
                pass
            # endregion

            # region Logradouro Empresarial
            try:
                logradouro_empresarial_value = data.get("logradouro_empresarial", "")
                if logradouro_empresarial_value != "":
                    self.logradouro_empresarial.insert(0, logradouro_empresarial_value)  # Insere o novo valor
            except:
                pass
            # endregion

            # region Numero Endereço Empresarial
            try:
                numero_endereco_empresarial_value = data.get("numero_endereco_empresarial", "")
                if numero_endereco_empresarial_value != "":
                    self.numero_endereco_empresarial.insert(0, numero_endereco_empresarial_value)  # Insere o novo valor
            except:
                pass
            # endregion

            # region Detalhes Endereço Empresarial
            try:
                detalhes_endereco_empresarial_value = data.get("detalhes_endereco_empresarial", "")
                if detalhes_endereco_empresarial_value != "":
                    self.detalhes_endereco_empresarial.insert(0, detalhes_endereco_empresarial_value)  # Insere o novo valor
            except:
                pass
            # endregion

            # region Bairro Endereço Empresarial
            try:
                bairro_endereco_empresarial_value = data.get("bairro_endereco_empresarial", "")
                if bairro_endereco_empresarial_value != "":
                    self.bairro_endereco_empresarial.insert(0, bairro_endereco_empresarial_value)  # Insere o novo valor
            except:
                pass
            # endregion

            # region Cidade Endereço Empresarial
            try:
                cidade_endereco_empresarial_value = data.get("cidade_endereco_empresarial", "")
                if cidade_endereco_empresarial_value != "":
                    self.cidade_endereco_empresarial.insert(0, cidade_endereco_empresarial_value)  # Insere o novo valor
            except:
                pass
            # endregion

            # region UF Endereço Empresarial
            try:
                uf_endereco_empresarial_value = data.get("uf_endereco_empresarial", "")
                if uf_endereco_empresarial_value != "":
                    self.uf_endereco_empresarial.insert(0, uf_endereco_empresarial_value)  # Insere o novo valor
            except:
                pass
            # endregion

            # region E-mail Empresarial
            try:
                email_empresarial_value = data.get("email_empresarial", "")
                if email_empresarial_value != "":
                    self.email_empresarial.insert(0, email_empresarial_value)  # Insere o novo valor
            except:
                pass
            # endregion

            # region Telefone Empresarial
            try:
                telefone_empresarial_value = data.get("telefone_empresarial", "")
                if telefone_empresarial_value != "":
                    self.telefone_empresarial.insert(0, telefone_empresarial_value)  # Insere o novo valor
            except:
                pass
            # endregion

            # endregion

            # endregion

    # endregion

    # region Altera a imagem do logo quando o usuário muda o tema
    def update_logo_image(self, mode):
        if mode == "dark":
            image_path = logo_dark


        else:
            image_path = logo_light

        self.logo_image = ctk.CTkImage(Image.open(fp=image_path), size=(113, 25))
        #self.logo_label.configure(image=self.logo_image) # REATIVAR LOGO

    # endregion

    # region Controla a aparência (Dark, Light ou System)
    def change_appearance_mode(self, mode):
        ctk.set_appearance_mode(mode.lower())
        self.update_logo_image(mode.lower())

    # endregion

    # Ocultar painel lateral (desativado)
    '''def show_sidebar_ELEMENTS_profissional_PF(self):

        self.tabview1 = ctk.CTkTabview(self, width=250)
        self.tabview1.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        # region (ABA) Pessoa Física
        self.tabview1.add("Pessoa Física")

        # region (inside SIDEBAR DIR. 01) (INPUT) Nome Completo

        self.nome_completo_profissional = ctk.CTkEntry(self.tabview1.tab("Pessoa Física"),
                                                       placeholder_text="Nome Completo")
        self.nome_completo_profissional.pack(padx=10, pady=5, fill="x")

        # endregion

        # region (inside SIDEBAR ESQ.) (DROPDOWN) Nacionalidades

        self.nacionalidade_profissional = ctk.CTkComboBox(self.tabview1.tab("Pessoa Física"),
                                                          values=nacionalidade_list)
        self.nacionalidade_profissional.pack(padx=10, pady=5, fill="x")

        # endregion

        # region (inside SIDEBAR ESQ.) (DROPDOWN) ESTADO CIVIL

        self.estado_civil_profissional = ctk.CTkComboBox(self.tabview1.tab("Pessoa Física"),
                                                         values=estado_civil_generico_list)
        self.estado_civil_profissional.pack(padx=10, pady=5, fill="x")

        # endregion

        # region (inside SIDEBAR ESQ.) (DROPDOWN) Profissão

        self.profissao_profissional = ctk.CTkComboBox(self.tabview1.tab("Pessoa Física"),
                                                      values=profissao_generico_list)
        self.profissao_profissional.pack(padx=10, pady=5, fill="x")

        # endregion

        # region (inside SIDEBAR DIR. 01) (INPUT) Número do Registro (CAU/CREA)

        self.numero_registro_cau_crea = ctk.CTkEntry(self.tabview1.tab("Pessoa Física"), placeholder_text="CAU/"
                                                                                                          "CREA")
        self.numero_registro_cau_crea.pack(padx=10, pady=5, fill="x")

        # endregion

        # region (inside SIDEBAR DIR. 01) (INPUT) E-mail

        self.email = ctk.CTkEntry(self.tabview1.tab("Pessoa Física"), placeholder_text="Seu e-mail")
        self.email.pack(padx=10, pady=5, fill="x")

        # endregion

        # region (inside SIDEBAR DIR. 01) (BOTÃO) Iniciar

        self.expand_button = ctk.CTkButton(self.tabview1.tab("Pessoa Física"), text="Iniciar", command=self.iniciar,
                                           fg_color="green", hover_color="#0A5C0A")
        self.expand_button.pack(padx=10, pady=5, fill="x")

        # endregion

        # Adicione outros elementos da aba Pessoa Física conforme necessário

        # endregion

        # region (ABA) Pessoa Jurídica

        self.tabview1.add("Pessoa Jurídica")
        self.cnpj = ctk.CTkEntry(self.tabview1.tab("Pessoa Jurídica"), placeholder_text="Seu CNPJ")
        self.cnpj.pack(padx=10, pady=5, fill="x")
        self.razao_social = ctk.CTkEntry(self.tabview1.tab("Pessoa Jurídica"), placeholder_text="Razão Social")
        self.razao_social.pack(padx=10, pady=5, fill="x")
        # Adicione outros elementos da aba Pessoa Jurídica conforme necessário

        # endregion

        # endregion

        # endregion'''

# endregion

#endregion

# Função principal
# @controlador_login
def iniciar():
    app = FastDocApp()  # Inicia a Janela
    app.mainloop()  # Mantém a janela aberta em loop

if __name__ == "__main__":
    iniciar()
