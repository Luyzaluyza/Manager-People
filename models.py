# models.py
from datetime import datetime

def validar_data(data):
    try:
        datetime.strptime(data, '%d/%m/%Y')
        return datetime.strptime(data, '%d/%m/%Y').strftime('%Y-%m-%d')
    except ValueError:
        try:
            datetime.strptime(data, '%d-%m-%Y')
            return datetime.strptime(data, '%d-%m-%Y').strftime('%Y-%m-%d')
        except ValueError:
            return None

def formatar_cpf(cpf):
    cpf_formatado = cpf.replace(".", "").replace("-", "")
    
    if len(cpf_formatado) != 11:
        raise ValueError("CPF deve conter 11 dígitos após a formatação")
    return cpf_formatado

class Pessoa:
    def __init__(self, nome, data_nascimento, endereco, cpf, estado_civil):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.cpf = formatar_cpf(cpf)
        self.estado_civil = estado_civil
