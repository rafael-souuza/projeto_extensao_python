import mysql.connector

db_config = {
    'user': 'root',
    'password': '1234',
    'host': 'localhost',
    'database': 'ATIC'}


def conectar():
    return mysql.connector.connect(**db_config)

def salvar_dados_no_banco(nome, equipamento, bmp, problema):
    try:
        conn = conectar()
        cursor = conn.cursor()
        query = "INSERT INTO relatorio (nome, equipamento, bmp, problema) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (nome, equipamento, bmp, problema))
        conn.commit()
    except mysql.connector.Error as err:
        raise RuntimeError(f"Erro ao conectar ao banco de dados: {err}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
