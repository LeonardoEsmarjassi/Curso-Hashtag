import tkinter as tk
from tkinter import messagebox

# Lista para armazenar as vistorias cadastradas
vistorias = []

# Função para adicionar uma nova vistoria
def adicionar_vistoria():
    placa = entry_placa.get()
    carro = entry_carro.get()
    indicacao = entry_indicacao.get()
    valor = entry_valor.get()
    forma_pagamento = entry_forma_pagamento.get()
    vistoriador = entry_vistoriador.get()

    # Verifica se todos os campos foram preenchidos
    if placa and carro and indicacao and valor and forma_pagamento and vistoriador:
        try:
            valor = float(valor)
        except ValueError:
            messagebox.showwarning("Valor inválido", "Por favor, insira um valor numérico para o valor da vistoria.")
            return
        
        # Adiciona a vistoria na lista
        vistorias.append({
            "placa": placa,
            "carro": carro,
            "indicacao": indicacao,
            "valor": valor,
            "forma_pagamento": forma_pagamento,
            "vistoriador": vistoriador
        })
        
        # Atualiza a lista exibida
        listar_vistorias()
        somar_valores()

        # Limpa os campos de entrada
        limpar_campos()
    else:
        messagebox.showwarning("Entrada inválida", "Por favor, preencha todos os campos.")

# Função para limpar os campos de entrada
def limpar_campos():
    entry_placa.delete(0, tk.END)
    entry_carro.delete(0, tk.END)
    entry_indicacao.delete(0, tk.END)
    entry_valor.delete(0, tk.END)
    entry_forma_pagamento.delete(0, tk.END)
    entry_vistoriador.delete(0, tk.END)

# Função para listar todas as vistorias cadastradas
def listar_vistorias():
    lista_vistorias.delete(0, tk.END)
    for index, vistoria in enumerate(vistorias):
        lista_vistorias.insert(tk.END, f"{index+1}. {vistoria['placa']} - {vistoria['carro']} - {vistoria['indicacao']} - R${vistoria['valor']} - {vistoria['forma_pagamento']} - Vistoriador: {vistoria['vistoriador']}")

# Função para somar os valores das vistorias
def somar_valores():
    total = sum(vistoria['valor'] for vistoria in vistorias)
    label_total.config(text=f"Total do dia: R${total:.2f}")

# Função para editar uma vistoria selecionada
def editar_vistoria():
    try:
        # Obtém o índice da vistoria selecionada
        selected_index = lista_vistorias.curselection()[0]
        vistoria = vistorias[selected_index]

        # Preenche os campos com os dados da vistoria selecionada
        entry_placa.delete(0, tk.END)
        entry_placa.insert(tk.END, vistoria['placa'])
        
        entry_carro.delete(0, tk.END)
        entry_carro.insert(tk.END, vistoria['carro'])
        
        entry_indicacao.delete(0, tk.END)
        entry_indicacao.insert(tk.END, vistoria['indicacao'])
        
        entry_valor.delete(0, tk.END)
        entry_valor.insert(tk.END, vistoria['valor'])
        
        entry_forma_pagamento.delete(0, tk.END)
        entry_forma_pagamento.insert(tk.END, vistoria['forma_pagamento'])
        
        entry_vistoriador.delete(0, tk.END)
        entry_vistoriador.insert(tk.END, vistoria['vistoriador'])
        
        # Altera a função de adicionar para editar
        btn_adicionar.config(text="Salvar Alterações", command=lambda: salvar_edicoes(selected_index))
    except IndexError:
        messagebox.showwarning("Seleção inválida", "Por favor, selecione uma vistoria para editar.")

# Função para salvar as edições feitas
def salvar_edicoes(index):
    placa = entry_placa.get()
    carro = entry_carro.get()
    indicacao = entry_indicacao.get()
    valor = entry_valor.get()
    forma_pagamento = entry_forma_pagamento.get()
    vistoriador = entry_vistoriador.get()

    if placa and carro and indicacao and valor and forma_pagamento and vistoriador:
        try:
            valor = float(valor)
        except ValueError:
            messagebox.showwarning("Valor inválido", "Por favor, insira um valor numérico para o valor da vistoria.")
            return

        vistorias[index] = {
            "placa": placa,
            "carro": carro,
            "indicacao": indicacao,
            "valor": valor,
            "forma_pagamento": forma_pagamento,
            "vistoriador": vistoriador
        }

        # Atualiza a lista exibida
        listar_vistorias()
        somar_valores()

        # Limpa os campos e volta para a função de adicionar
        limpar_campos()
        btn_adicionar.config(text="Cadastrar Vistoria", command=adicionar_vistoria)
    else:
        messagebox.showwarning("Entrada inválida", "Por favor, preencha todos os campos.")

# Função para excluir uma vistoria
def excluir_vistoria():
    try:
        selected_index = lista_vistorias.curselection()[0]
        vistorias.pop(selected_index)
        listar_vistorias()
        somar_valores()
    except IndexError:
        messagebox.showwarning("Seleção inválida", "Por favor, selecione uma vistoria para excluir.")

# Criando a janela principal
root = tk.Tk()
root.title("Cadastro de Vistorias")

# Configurando o layout
frame = tk.Frame(root)
frame.pack(pady=20)

# Labels e campos de entrada
tk.Label(frame, text="Placa do Veículo").grid(row=0, column=0, padx=10, pady=5)
entry_placa = tk.Entry(frame)
entry_placa.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame, text="Carro").grid(row=1, column=0, padx=10, pady=5)
entry_carro = tk.Entry(frame)
entry_carro.grid(row=1, column=1, padx=10, pady=5)

tk.Label(frame, text="Indicação").grid(row=2, column=0, padx=10, pady=5)
entry_indicacao = tk.Entry(frame)
entry_indicacao.grid(row=2, column=1, padx=10, pady=5)

tk.Label(frame, text="Valor").grid(row=3, column=0, padx=10, pady=5)
entry_valor = tk.Entry(frame)
entry_valor.grid(row=3, column=1, padx=10, pady=5)

tk.Label(frame, text="Forma de Pagamento").grid(row=4, column=0, padx=10, pady=5)
entry_forma_pagamento = tk.Entry(frame)
entry_forma_pagamento.grid(row=4, column=1, padx=10, pady=5)

tk.Label(frame, text="Vistoriador").grid(row=5, column=0, padx=10, pady=5)
entry_vistoriador = tk.Entry(frame)
entry_vistoriador.grid(row=5, column=1, padx=10, pady=5)

# Botão para adicionar a vistoria
btn_adicionar = tk.Button(frame, text="Cadastrar Vistoria", command=adicionar_vistoria)
btn_adicionar.grid(row=6, columnspan=2, pady=10)

# Lista para exibir as vistorias cadastradas
lista_vistorias = tk.Listbox(root, width=80, height=10)
lista_vistorias.pack(pady=10)

# Botões de editar, excluir e somar
btn_editar = tk.Button(root, text="Editar", command=editar_vistoria)
btn_editar.pack(side=tk.LEFT, padx=10)

btn_excluir = tk.Button(root, text="Excluir", command=excluir_vistoria)
btn_excluir.pack(side=tk.LEFT, padx=10)

# Exibir o total do dia
label_total = tk.Label(root, text="Total do dia: R$0.00", font=('Arial', 14))
label_total.pack(pady=10)

# Inicia a aplicação
root.mainloop()
