import tkinter as tk
from tkinter import messagebox
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

tk.Label(app, text="Nome do Usuário").pack(pady=5)
entry_nome = tk.Entry(app)
entry_nome.pack(pady=5)

tk.Label(app, text="Equipamento").pack(pady=5)
entry_equipamento = tk.Entry(app)
entry_equipamento.pack(pady=5)

tk.Label(app, text="BMP").pack(pady=5)
entry_bmp = tk.Entry(app)
entry_bmp.pack(pady=5)

tk.Label(app, text="Problema").pack(pady=5)
entry_problema = tk.Entry(app)
entry_problema.pack(pady=5)

tk.Button(app, text="Salvar", command=salvar_dados).pack(pady=20)

app.mainloop()
