import pymysql

db_config = {
    'user': 'root',
    'password': '1234',
    'host': 'localhost',
    'database': 'ATIC'
}

def conectar():
   try:
        return pymysql.connect(**db_config)
   except pymysql.MySQLError as err:
        raise RuntimeError(f"Erro ao conectar ao banco de dados: {err}")


def salvar_dados_no_banco(nome, equipamento, bmp, problema):
    conn = None
    cursor = None
    try:
        conn = conectar()
        cursor = conn.cursor()
        query = "INSERT INTO relatorio (nome, equipamento, bmp, problema) VALUES (%s, %s, %s, %s)"

        
        cursor.execute(query, (nome, equipamento, bmp, problema))

        
        conn.commit()
    except pymysql.MySQLError as err:
        raise RuntimeError(f"Erro ao salvar dados no banco de dados: {err}")
    finally:
        
        if cursor:
            cursor.close()
        if conn and conn.open:
            conn.close()


