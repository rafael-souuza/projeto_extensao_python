

from database.db import conectar

def testar_conexao():
    try:
        conn = conectar()
        if conn.is_connected():
            print("Conexão com o banco de dados estabelecida com sucesso!")
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
    finally:
        if conn.is_connected():
            conn.close()

if __name__ == "__main__":
    testar_conexao()
