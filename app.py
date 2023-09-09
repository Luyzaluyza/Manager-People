from flask import Flask, request, jsonify
import mysql.connector  
from db_utils import criar_banco, conectar_banco
from models import Pessoa, validar_data, formatar_cpf

app = Flask(__name__)

criar_banco()
@app.route('/pessoa', methods=['POST'])
def criar_pessoa():

    data = request.json
    try:
        nome = data['nome']
        data_nascimento = data['data_nascimento']
        endereco = data['endereco']
        cpf = data['cpf']
        estado_civil = data['estado_civil'].strip().upper()  

        
        estados_civis_validos = ['SOLTEIRO', 'CASADO', 'DIVORCIADO', 'VIÚVO', 'UNIÃO ESTÁVEL']
        if estado_civil not in estados_civis_validos:
            mensagem_erro = f"Estado civil inválido. Por favor, passe um dos valores: {', '.join(estados_civis_validos)}"
            return jsonify({"message": mensagem_erro}), 400

        data_nascimento_mysql = validar_data(data_nascimento)
        if data_nascimento_mysql is None:
            return jsonify({"message": "Data de nascimento inválida"}), 400

        conn = conectar_banco()
        if conn is not None:
            cursor = conn.cursor()
            pessoa = Pessoa(nome, data_nascimento_mysql, endereco, cpf, estado_civil)
            try:
                cursor.execute("""
                    INSERT INTO pessoas (nome, data_nascimento, endereco, cpf, estado_civil)
                    VALUES (%s, %s, %s, %s, %s)
                """, (pessoa.nome, pessoa.data_nascimento, pessoa.endereco, pessoa.cpf, pessoa.estado_civil))
                conn.commit()
                conn.close()
                return jsonify({"message": "Pessoa criada com sucesso"}), 201
            except mysql.connector.IntegrityError as e:
                if "Duplicate entry" in str(e):
                    return jsonify({"message": "Não é possível cadastrar uma pessoa com um CPF já existente"}), 400
                else:
                    return jsonify({"message": "Erro ao cadastrar a pessoa"}), 500
        else:
            return jsonify({"message": "Erro ao conectar ao banco de dados"}), 500
    except Exception as e:
        return jsonify({"message": str(e)}), 400
    
    
@app.route('/pessoa/<string:cpf>', methods=['PUT'])
def atualizar_pessoa(cpf):
    data = request.json
    try:
        nome = data.get('nome')
        data_nascimento = data.get('data_nascimento')
        endereco = data.get('endereco')
        estado_civil = data.get('estado_civil')
        cpf_novo = data.get('cpf')  

        if cpf_novo:
            return jsonify({"message": "Não é possível alterar o CPF"}), 400  

        data_nascimento_formatada = validar_data(data_nascimento)

        if not data_nascimento_formatada:
            return jsonify({"message": "Data de nascimento inválida"}), 400

        conn = conectar_banco()
        if conn is not None:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE pessoas
                SET nome = %s, data_nascimento = %s, endereco = %s, estado_civil = %s
                WHERE cpf = %s
            """, (nome, data_nascimento_formatada, endereco, estado_civil, cpf))
            conn.commit()
            conn.close()
            return jsonify({"message": "Pessoa atualizada com sucesso"}), 200
        else:
            return jsonify({"message": "Erro ao conectar ao banco de dados"}), 500
    except ValueError as e:
        return jsonify({"message": str(e)}), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 400


@app.route('/pessoa/<string:cpf>', methods=['GET'])
def buscar_pessoa(cpf):
    conn = conectar_banco()
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM pessoas WHERE cpf = %s", (cpf,))
        pessoa = cursor.fetchone()
        conn.close()

        if pessoa:
            return jsonify({"nome": pessoa[1], "data_nascimento": str(pessoa[2]), "endereco": pessoa[3], "cpf": pessoa[4], "estado_civil": pessoa[5]})
        else:
            return jsonify({"message": "Pessoa não encontrada"}), 404
    else:
        return jsonify({"message": "Erro ao conectar ao banco de dados"}), 500

@app.route('/pessoa', methods=['GET'])
def listar_pessoas():
    conn = conectar_banco()
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM pessoas")
        pessoas = cursor.fetchall()
        conn.close()

        lista_pessoas = []
        for pessoa in pessoas:
            lista_pessoas.append({
                "nome": pessoa[1],
                "data_nascimento": str(pessoa[2]),
                "endereco": pessoa[3],
                "cpf": pessoa[4],
                "estado_civil": pessoa[5]
            })

        return jsonify({"pessoas": lista_pessoas})
    else:
        return jsonify({"message": "Erro ao conectar ao banco de dados"}), 500
    
@app.route('/pessoa/<string:cpf>', methods=['DELETE'])
def apagar_pessoa(cpf):
    conn = conectar_banco()
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM pessoas WHERE cpf = %s", (cpf,))
        conn.commit()
        conn.close()
        return jsonify({"message": "Pessoa apagada com sucesso"}), 200
    else:
        return jsonify({"message": "Erro ao conectar ao banco de dados"}), 500

if __name__ == '__main__':
    app.run(debug=True)
