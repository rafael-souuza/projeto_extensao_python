import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from database.db import salvar_dados_no_banco

def salvar_dados():
    """Coleta os dados da interface e salva no banco de dados."""
    nome = entry_nome.get()
    equipamento = entry_equipamento.get()
    bmp = entry_bmp.get()
    problema = entry_problema.get()

    if not (nome and equipamento and bmp and problema):
        messagebox.showwarning("Aviso", "Todos os campos devem ser preenchidos!")
        return

    try:
        salvar_dados_no_banco(nome, equipamento, bmp, problema)
        messagebox.showinfo("Sucesso", "Dados salvos com sucesso!")
        entry_nome.delete(0, tk.END)
        entry_equipamento.delete(0, tk.END)
        entry_bmp.delete(0, tk.END)
        entry_problema.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro: {e}")

# Configuração da interface gráfica
app = tk.Tk()
app.title("Aplicativo de Relatório")
app.geometry("600x400")  # Define um tamanho maior para a janela
app.configure(bg="#f0f0f0")  # Cor de fundo

# Estilo do ttk
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 12), background="#f0f0f0")
style.configure("TEntry", font=("Helvetica", 12), padding=5)
style.configure("TButton", font=("Helvetica", 12), padding=5)

# Adiciona os componentes à interface usando grid
tk.Label(app, text="Nome do Usuário").grid(row=0, column=0, padx=20, pady=10, sticky="w")
entry_nome = ttk.Entry(app)
entry_nome.grid(row=0, column=1, padx=20, pady=10, sticky="ew")

tk.Label(app, text="Equipamento").grid(row=1, column=0, padx=20, pady=10, sticky="w")
entry_equipamento = ttk.Entry(app)
entry_equipamento.grid(row=1, column=1, padx=20, pady=10, sticky="ew")

tk.Label(app, text="BMP").grid(row=2, column=0, padx=20, pady=10, sticky="w")
entry_bmp = ttk.Entry(app)
entry_bmp.grid(row=2, column=1, padx=20, pady=10, sticky="ew")

tk.Label(app, text="Problema").grid(row=3, column=0, padx=20, pady=10, sticky="w")
entry_problema = ttk.Entry(app)
entry_problema.grid(row=3, column=1, padx=20, pady=10, sticky="ew")

tk.Button(app, text="Salvar", command=salvar_dados).grid(row=4, column=0, columnspan=2, pady=20)

# Expande a coluna da entrada
app.grid_columnconfigure(1, weight=1)

app.mainloop()
