import pandas as pd
from database.db import conectar

def gerar_planilha():
    try:
        conn = conectar()
        query = "SELECT nome, equipamento, bmp, problema FROM relatorio"
        df = pd.read_sql(query, conn)
        df.to_excel('relatorio.xlsx', index=False)
        print("Planilha gerada com sucesso!")
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        if conn.is_connected():
            conn.close()

if __name__ == "__main__":
    gerar_planilha()
