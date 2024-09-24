import tkinter as tk
from tkinter import messagebox, ttk
import pymysql
from database.db import conectar

def pesquisar():
    global cursor, conn
    nome = entry_nome.get().strip()
    bmp = entry_bmp.get().strip()

    if not nome or not bmp:
        messagebox.showwarning("Campo Obrigatório", "Por favor, preencha ambos os campos.")
        return

    try:
        conn = conectar()
        cursor = conn.cursor()

        query = "SELECT * FROM relatorio WHERE nome LIKE %s AND bmp LIKE %s"
        cursor.execute(query, (f"%{nome}%", f"%{bmp}%"))
        resultados = cursor.fetchall()

        for item in tree.get_children():
            tree.delete(item)

        if resultados:
            for linha in resultados:
                tree.insert("", "end", values=linha)
        else:
            messagebox.showinfo("Resultado", "Não identificado.")

    except pymysql.MySQLError as err:
        messagebox.showerror("Erro", f"Erro ao acessar o banco de dados: {err}")
    finally:
        cursor.close()
        conn.close()

# Interface
root = tk.Tk()
root.title("Pesquisa no Banco de Dados")

# Campos de entrada
label_nome = tk.Label(root, text="Nome:")
label_nome.grid(row=0, column=0, padx=10, pady=10)
entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1, padx=10, pady=10)

label_bmp = tk.Label(root, text="BMP:")
label_bmp.grid(row=1, column=0, padx=10, pady=10)
entry_bmp = tk.Entry(root)
entry_bmp.grid(row=1, column=1, padx=10, pady=10)

# Botão de pesquisa
botao_pesquisar = tk.Button(root, text="Pesquisar", command=pesquisar)
botao_pesquisar.grid(row=2, columnspan=2, pady=10)

# Treeview para exibir resultados
tree = ttk.Treeview(root, columns=("ID", "Nome", "Equipamento", "BMP", "Problema"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Nome", text="Nome")
tree.heading("Equipamento", text="Equipamento")
tree.heading("BMP", text="BMP")
tree.heading("Problema", text="Problema")
tree.grid(row=3, columnspan=2, padx=10, pady=10)

root.mainloop()
