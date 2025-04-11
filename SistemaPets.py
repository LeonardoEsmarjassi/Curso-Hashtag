import tkinter as tk
from tkinter import messagebox

# Lista para armazenar os pets cadastrados
pets = []

# Função para adicionar um novo pet
def adicionar_pet():
    tutor_nome = entry_tutor_nome.get()
    pet_nome = entry_pet_nome.get()
    especie = entry_especie.get()
    raca = entry_raca.get()
    idade = entry_idade.get()

    if tutor_nome and pet_nome and especie and raca and idade:
        # Adiciona os dados do pet na lista
        pets.append({
            "tutor_nome": tutor_nome,
            "pet_nome": pet_nome,
            "especie": especie,
            "raca": raca,
            "idade": idade
        })
        
        # Atualiza a lista exibida
        listar_pets()
        
        # Limpa os campos de entrada
        limpar_campos()
    else:
        messagebox.showwarning("Entrada inválida", "Por favor, preencha todos os campos.")

# Função para limpar os campos de entrada
def limpar_campos():
    entry_tutor_nome.delete(0, tk.END)
    entry_pet_nome.delete(0, tk.END)
    entry_especie.delete(0, tk.END)
    entry_raca.delete(0, tk.END)
    entry_idade.delete(0, tk.END)

# Função para listar todos os pets cadastrados
def listar_pets():
    lista_pets.delete(0, tk.END)
    for index, pet in enumerate(pets):
        lista_pets.insert(tk.END, f"{index+1}. {pet['pet_nome']} - {pet['especie']} - {pet['raca']} - {pet['idade']} anos")

# Função para editar um pet selecionado
def editar_pet():
    try:
        # Obtém o índice do pet selecionado
        selected_index = lista_pets.curselection()[0]
        pet = pets[selected_index]

        # Preenche os campos com os dados do pet selecionado
        entry_tutor_nome.delete(0, tk.END)
        entry_tutor_nome.insert(tk.END, pet['tutor_nome'])
        
        entry_pet_nome.delete(0, tk.END)
        entry_pet_nome.insert(tk.END, pet['pet_nome'])
        
        entry_especie.delete(0, tk.END)
        entry_especie.insert(tk.END, pet['especie'])
        
        entry_raca.delete(0, tk.END)
        entry_raca.insert(tk.END, pet['raca'])
        
        entry_idade.delete(0, tk.END)
        entry_idade.insert(tk.END, pet['idade'])
        
        # Altera a função de adicionar para editar
        btn_adicionar.config(text="Salvar Alterações", command=lambda: salvar_edicoes(selected_index))
    except IndexError:
        messagebox.showwarning("Seleção inválida", "Por favor, selecione um pet para editar.")

# Função para salvar as edições feitas
def salvar_edicoes(index):
    tutor_nome = entry_tutor_nome.get()
    pet_nome = entry_pet_nome.get()
    especie = entry_especie.get()
    raca = entry_raca.get()
    idade = entry_idade.get()

    if tutor_nome and pet_nome and especie and raca and idade:
        pets[index] = {
            "tutor_nome": tutor_nome,
            "pet_nome": pet_nome,
            "especie": especie,
            "raca": raca,
            "idade": idade
        }
        
        # Atualiza a lista exibida
        listar_pets()
        
        # Limpa os campos e volta para a função de adicionar
        limpar_campos()
        btn_adicionar.config(text="Cadastrar Pet", command=adicionar_pet)
    else:
        messagebox.showwarning("Entrada inválida", "Por favor, preencha todos os campos.")

# Função para excluir um pet
def excluir_pet():
    try:
        selected_index = lista_pets.curselection()[0]
        pets.pop(selected_index)
        listar_pets()
    except IndexError:
        messagebox.showwarning("Seleção inválida", "Por favor, selecione um pet para excluir.")

# Criando a janela principal
root = tk.Tk()
root.title("Cadastro de Pets")

# Configurando o layout
frame = tk.Frame(root)
frame.pack(pady=20)

# Labels e campos de entrada
tk.Label(frame, text="Nome do Tutor").grid(row=0, column=0, padx=10, pady=5)
entry_tutor_nome = tk.Entry(frame)
entry_tutor_nome.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame, text="Nome do Pet").grid(row=1, column=0, padx=10, pady=5)
entry_pet_nome = tk.Entry(frame)
entry_pet_nome.grid(row=1, column=1, padx=10, pady=5)

tk.Label(frame, text="Espécie").grid(row=2, column=0, padx=10, pady=5)
entry_especie = tk.Entry(frame)
entry_especie.grid(row=2, column=1, padx=10, pady=5)

tk.Label(frame, text="Raça").grid(row=3, column=0, padx=10, pady=5)
entry_raca = tk.Entry(frame)
entry_raca.grid(row=3, column=1, padx=10, pady=5)

tk.Label(frame, text="Idade (em anos)").grid(row=4, column=0, padx=10, pady=5)
entry_idade = tk.Entry(frame)
entry_idade.grid(row=4, column=1, padx=10, pady=5)

# Botão para adicionar o pet
btn_adicionar = tk.Button(frame, text="Cadastrar Pet", command=adicionar_pet)
btn_adicionar.grid(row=5, columnspan=2, pady=10)

# Lista para exibir os pets cadastrados
lista_pets = tk.Listbox(root, width=50, height=10)
lista_pets.pack(pady=10)

# Botões de editar e excluir
btn_editar = tk.Button(root, text="Editar", command=editar_pet)
btn_editar.pack(side=tk.LEFT, padx=10)

btn_excluir = tk.Button(root, text="Excluir", command=excluir_pet)
btn_excluir.pack(side=tk.LEFT, padx=10)

# Inicia a aplicação
root.mainloop()
