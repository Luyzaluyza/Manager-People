# db_utils.py
import mysql.connector
#Mude user e password para as suas definições por favor
db_config = {
    "host": "localhost",  
    "user": "root",       
    "password": "root"   
}

def criar_banco():
    try:
        conn = mysql.connector.connect(
            host=db_config["host"],
            user=db_config["user"],
            password=db_config["password"]
        )
        cursor = conn.cursor()
        
        cursor.execute("CREATE DATABASE IF NOT EXISTS people_manager")
        conn.database = "people_manager"
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pessoas (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255) NOT NULL,
                data_nascimento DATE NOT NULL,
                endereco VARCHAR(255) NOT NULL,
                cpf VARCHAR(11) NOT NULL UNIQUE,
                estado_civil VARCHAR(255) NOT NULL
            )
        """)

        conn.close()
    except Exception as e:
        print(f"Erro ao criar o banco de dados e a tabela: {str(e)}")

def conectar_banco():
    try:
        conn = mysql.connector.connect(
            host=db_config["host"],
            user=db_config["user"],
            password=db_config["password"],
            database="people_manager"
        )
        return conn
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {str(e)}")
        return None
