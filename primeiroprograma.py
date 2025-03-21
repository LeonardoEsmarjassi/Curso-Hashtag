import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from datetime import datetime

# Lista para armazenar as informações dos veículos
veiculos_dia = []

def submit_form():
    try:
        # Coleta as informações do formulário
        veiculo = {
            "placa": entry_placa.get(),
            "modelo": entry_modelo.get(),
            "tipo_servico": entry_tipo_servico.get(),
            "pago": float(entry_pago.get().replace(",", ".")),
            "vistoriador": entry_vistoriador.get(),
            "forma_pagamento": entry_forma_pagamento.get().lower(),
            "indicacao": entry_indicacao.get(),
            "data": datetime.now().strftime("%Y-%m-%d")
        }

        # Validação da forma de pagamento
        formas_validas = {"debito", "credito", "dinheiro", "pix", "fatura"}
        if veiculo["forma_pagamento"] not in formas_validas:
            messagebox.showerror("Erro", "Forma de pagamento inválida. Por favor, insira uma das opções: Débito, Crédito, Dinheiro, Pix, Fatura.")
            return

        veiculos_dia.append(veiculo)

        # Exibe uma mensagem de confirmação
        messagebox.showinfo("Informações Recebidas", f'Veículo {veiculo["placa"]} registrado com sucesso.')

        # Limpar os campos após o envio
        for entry in (entry_placa, entry_modelo, entry_tipo_servico, entry_pago, entry_vistoriador, entry_forma_pagamento, entry_indicacao):
            entry.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Erro", "Valor pago inválido. Por favor, insira um número válido.")

def consultar_veiculos():
    data_atual = datetime.now().strftime("%Y-%m-%d")
    veiculos_dia_do_mes = [v for v in veiculos_dia if v["data"] == data_atual]

    if not veiculos_dia_do_mes:
        messagebox.showinfo("Sem registros", "Nenhum veículo registrado hoje.")
    else:
        consulta_window = tk.Toplevel(root)
        consulta_window.title("Consulta de Veículos Feitos no Dia")
        consulta_window.geometry("1200x600")

        columns = ("Placa", "Veículo", "Serviço", "Valor", "Vistoriador", "Forma de Pagamento", "Indicação")
        tree = ttk.Treeview(consulta_window, columns=columns, show="headings", selectmode="browse")
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=150, anchor="center")

        for v in veiculos_dia_do_mes:
            tree.insert("", "end", values=(
                v["placa"], v["modelo"], v["tipo_servico"], f"R${v['pago']:.2f}", v["vistoriador"], v["forma_pagamento"], v["indicacao"]
            ))

        tree.pack(fill="both", expand=True, padx=10, pady=10)
        ttk.Button(consulta_window, text="Editar Veículo", command=lambda: editar_veiculo(veiculos_dia_do_mes, tree)).pack(pady=10)

def editar_veiculo(veiculos, tree):
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Erro", "Nenhum veículo selecionado.")
        return

    item_index = tree.index(selected_item[0])
    veiculo = veiculos[item_index]

    editar_window = tk.Toplevel(root)
    editar_window.title("Editar Veículo")
    editar_window.geometry("500x400")

    entries = {}
    fields = ["Placa", "Veículo", "Serviço", "Valor", "Vistoriador", "Forma de Pagamento", "Indicação"]
    for i, field in enumerate(fields):
        ttk.Label(editar_window, text=f"{field}:").grid(row=i, column=0, sticky="w", padx=5, pady=5)
        entry = ttk.Entry(editar_window)
        entry.grid(row=i, column=1, sticky="ew", padx=5, pady=5)
        key = field.lower().replace(" ", "_")
        entry.insert(0, veiculo[key])
        entries[field] = entry

    def salvar_edicao():
        try:
            for field in fields:
                key = field.lower().replace(" ", "_")
                veiculo[key] = entries[field].get() if key != "pago" else float(entries[field].get().replace(",", "."))
            tree.item(selected_item[0], values=(
                veiculo["placa"], veiculo["modelo"], veiculo["tipo_servico"], f"R${veiculo['pago']:.2f}", veiculo["vistoriador"], veiculo["forma_pagamento"], veiculo["indicacao"]
            ))
            messagebox.showinfo("Sucesso", "Veículo atualizado com sucesso.")
            editar_window.destroy()
        except ValueError:
            messagebox.showerror("Erro", "Valor pago inválido. Por favor, insira um número válido.")

    ttk.Button(editar_window, text="Salvar", command=salvar_edicao).grid(row=len(fields), column=0, columnspan=2, pady=10)

def fechar_caixa():
    data_atual = datetime.now().strftime("%Y-%m-%d")
    veiculos_dia_do_mes = [v for v in veiculos_dia if v["data"] == data_atual]
    
    if not veiculos_dia_do_mes:
        messagebox.showinfo("Fechar Caixa", "Nenhum veículo registrado hoje.")
    else:
        caixa_window = tk.Toplevel(root)
        caixa_window.title("Fechamento de Caixa do Dia")
        caixa_window.geometry("1200x600")

        columns = ("Placa", "Veículo", "Serviço", "Valor", "Vistoriador", "Forma de Pagamento", "Indicação")
        tree = ttk.Treeview(caixa_window, columns=columns, show="headings", selectmode="browse")
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=150, anchor="center")

        for v in veiculos_dia_do_mes:
            tree.insert("", "end", values=(
                v["placa"], v["modelo"], v["tipo_servico"], f"R${v['pago']:.2f}", v["vistoriador"], v["forma_pagamento"], v["indicacao"]
            ))

        tree.pack(fill="both", expand=True, padx=10, pady=10)

        totais_pagamento = {"debito": 0, "credito": 0, "dinheiro": 0, "pix": 0, "fatura": 0}
        for v in veiculos_dia_do_mes:
            forma_pagamento = v["forma_pagamento"]
            if forma_pagamento in totais_pagamento:
                totais_pagamento[forma_pagamento] += v["pago"]

        lista_pagamentos = "\n".join(
            [f"{forma.capitalize()}: R${totais_pagamento[forma]:.2f}" for forma in totais_pagamento if totais_pagamento[forma] > 0]
        )

        ttk.Label(caixa_window, text=f"Totais por Forma de Pagamento:\n{lista_pagamentos}", font=("Arial", 12)).pack(pady=10)

# Criação da janela principal
root = tk.Tk()
root.title("Cadastro de Informações de Serviço")
root.geometry("1000x400")

style = ttk.Style()
style.theme_use("clam")

frame_form = ttk.Frame(root, padding="20")
frame_form.pack(fill="both", expand=True)

fields = [
    ("Placa", 0, 0), ("Veículo", 0, 2), ("Serviço", 0, 4),
    ("Valor", 1, 0), ("Vistoriador", 1, 2), ("Forma de Pagamento", 1, 4), ("Indicação", 1, 6)
]

entries = {}
for text, row, col in fields:
    ttk.Label(frame_form, text=f"{text}:").grid(row=row, column=col, sticky="w", padx=5, pady=5)
    entry = ttk.Entry(frame_form)
    entry.grid(row=row, column=col + 1, sticky="ew", padx=5, pady=5)
    key = text.lower().replace(" ", "_")
    entries[key] = entry

entry_placa = entries["placa"]
entry_modelo = entries["veículo"]
entry_tipo_servico = entries["serviço"]
entry_pago = entries["valor"]
entry_vistoriador = entries["vistoriador"]
entry_forma_pagamento = entries["forma_de_pagamento"]
entry_indicacao = entries["indicação"]

ttk.Button(frame_form, text="Registrar Veículo", command=submit_form).grid(row=2, column=0, columnspan=4, pady=10)
ttk.Button(frame_form, text="Consultar Veículos Feitos no Dia", command=consultar_veiculos).grid(row=2, column=4, columnspan=4, pady=5)
ttk.Button(frame_form, text="Fechar Caixa", command=fechar_caixa).grid(row=3, column=0, columnspan=8, pady=5)

root.mainloop()
