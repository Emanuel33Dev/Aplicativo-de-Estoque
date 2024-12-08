import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from funcionalidade import adicionar_produto, preencher_planilha
from PIL import Image, ImageTk
from datetime import datetime

def criar_interface():
    # Função para tratar o evento de cadastro
    def cadastrar_produto():
        nome = entry_nome.get()
        quantidade = entry_quantidade.get()
        preco = entry_preco.get()
        data_cadastro = datetime.now()
        codigo_produto = entrada_codigo.get()  # Usando o código digitado pelo usuário

        if not nome or not quantidade or not preco or not codigo_produto:  # Verifica se todos os campos foram preenchidos
            label_status.config(text='Preencha todos os campos!', foreground='red')
            return
        try:
            quantidade = int(quantidade)
            preco = float(preco)

            # Aqui, usamos o código digitado pelo usuário em vez de gerar um código aleatório
            # O código agora será o valor inserido no campo de código
            data_cadastro = datetime.now().date()

            # Chama a função para adicionar o produto
            adicionar_produto(nome=nome, codigo_produto=codigo_produto, quantidade=quantidade, preco=preco, data_cadastro=data_cadastro)

            # Dados do produto para preencher na planilha
            dados_produto = {
                'codigo_produto': codigo_produto,  # Usando o código digitado
                'data_cadastro': str(data_cadastro),  # Converte para string para compatibilidade
                'nome': nome,
                'quantidade': quantidade,
                'preco': preco
            }

            # Caminho para a planilha que você quer preencher
            caminho_planilha = './planilha eletroleste.xlsx'

            # Chama a função para preencher a planilha
            preencher_planilha(caminho_planilha, dados_produto)

            label_status.config(text=f"Produto '{nome}' cadastrado com sucesso!", foreground='green')

            # Limpar campos de cadastro
            entry_nome.delete(0, END)
            entry_quantidade.delete(0, END)
            entry_preco.delete(0, END)
            entrada_codigo.delete(0, END)  # Limpar o campo de código também
        except ValueError:
            label_status.config(text='Quantidade e preço devem ser numéricos!', foreground='red')

    # Criar janela principal
    app = ttk.Window(themename='solar')
    app.title('Sistema de Controle de Estoque')
    app.geometry('500x400')

    app.iconbitmap('eletroleste_logo.ico')

    # Carregar o logo da empresa
    logo = Image.open('eletroleste.png')  # Substitua pelo caminho local onde você salvou a imagem

    # Obter as dimensões originais da imagem
    largura, altura = logo.size

    # Calcular a nova altura proporcional com base na largura desejada
    nova_largura = 200
    nova_altura = int((nova_largura / largura) * altura)

    # Redimensionar a imagem proporcionalmente
    logo = logo.resize((nova_largura, nova_altura))

    # Converter para PhotoImage para exibir no tkinter
    logo_tk = ImageTk.PhotoImage(logo)

    # Adicionar o logo na interface usando ttkbootstrap
    label_logo = ttk.Label(app, image=logo_tk)
    label_logo.pack(pady=10)

    # Widgets da interface
    label_titulo = ttk.Label(app, text='Cadastro de Produtos', font=('Helvetica', 16))
    label_titulo.pack(pady=10)

    frame_form = ttk.Frame(app)
    frame_form.pack(pady=10)

    # Campo do produto
    label_nome = ttk.Label(frame_form, text='Produto:')
    label_nome.grid(row=0, column=0, padx=5, pady=5, sticky=W)
    entry_nome = ttk.Entry(frame_form)
    entry_nome.grid(row=0, column=1, padx=5, pady=5)

    # Campo da quantidade
    label_quantidade = ttk.Label(frame_form, text='Quantidade:')
    label_quantidade.grid(row=1, column=0, padx=5, pady=5, sticky=W)
    entry_quantidade = ttk.Entry(frame_form)
    entry_quantidade.grid(row=1, column=1, padx=5, pady=5)

    # Campo de preço
    label_preco = ttk.Label(frame_form, text='Preço (R$):')
    label_preco.grid(row=2, column=0, padx=5, pady=5, sticky=W)
    entry_preco = ttk.Entry(frame_form)
    entry_preco.grid(row=2, column=1, padx=5, pady=5)

    # Campo do código do produto
    label_codigo = ttk.Label(frame_form, text='Código do Produto:')
    label_codigo.grid(row=3, column=0, padx=5, pady=5, sticky=W)
    entrada_codigo = ttk.Entry(frame_form)
    entrada_codigo.grid(row=3, column=1, padx=5, pady=5)

    # Botão de Cadastro
    btn_cadastrar = ttk.Button(app, text='Cadastrar Produtos', command=cadastrar_produto, bootstyle=SUCCESS)
    btn_cadastrar.pack(pady=10)

    label_status = ttk.Label(app, text="")
    label_status.pack(pady=5)

    # Manter uma referência do logo para evitar que ele seja removido da memória
    label_logo.image = logo_tk

    app.mainloop()
