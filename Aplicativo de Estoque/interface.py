import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from funcionalidade import adicionar_produto  # Confirme se o nome do arquivo está correto!


def criar_interface():
    # Função para tratar o evento de cadastro
    def cadastrar_produto():
        nome = entry_nome.get()
        quantidade = entry_quantidade.get()
        preco = entry_preco.get()

        if not nome or not quantidade or not preco:
            label_status.config(text='Preencha todos os campos!', foreground='red')
            return

        # Verificação para garantir que quantidade e preço são numéricos
        if not quantidade.isdigit():
            label_status.config(text='Quantidade deve ser um número inteiro!', foreground='red')
            return
        if not isfloat(preco):
            label_status.config(text='Preço deve ser um número válido!', foreground='red')
            return

        # Convertendo para os tipos corretos
        quantidade = int(quantidade)
        preco = float(preco)

        # Chama a função para adicionar o produto
        adicionar_produto(nome=nome, quantidade=quantidade, preco=preco)
        label_status.config(text=f"Produto '{nome}' cadastrado com sucesso!", foreground='green')

        # Limpar campos de cadastro após 2 segundos
        entry_nome.delete(0, END)
        entry_quantidade.delete(0, END)
        entry_preco.delete(0, END)

        # Limpar a mensagem de status após 2 segundos
        app.after(2000, lambda: label_status.config(text=""))

    # Função auxiliar para verificar se é um número flutuante válido
    def isfloat(value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    # Criar janela principal
    app = ttk.Window(themename='solar')
    app.title('Sistema de Controle de Estoque')
    app.geometry('400x300')

    # Widgets da interface
    label_titulo = ttk.Label(app, text='Cadastro de Produtos', font=('Helvetica', 16))
    label_titulo.pack(pady=10)

    frame_form = ttk.Frame(app)
    frame_form.pack(pady=10)

    # Campo do nome
    label_nome = ttk.Label(frame_form, text='Nome:')
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

    # Botão de Cadastro
    btn_cadastrar = ttk.Button(app, text='Cadastrar Produto', command=cadastrar_produto, bootstyle=SUCCESS)
    btn_cadastrar.pack(pady=10)

    # Label de status
    label_status = ttk.Label(app, text="")
    label_status.pack(pady=5)

    app.mainloop()
