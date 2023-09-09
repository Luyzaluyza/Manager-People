# API CRUD ManagerPeople

Essa é uma API simples para a vaga de desenvolvedora back-end, um CRUD para gestão de pessoas.

## Descrição

A API CRUD ManagerPeople foi desenvolvida para permitir o cadastro e gestão de informações de pessoas de forma fácil e eficiente.

## Requisitos

- Mysql
- Python 3.x
- Flask (para fazer o download, execute `pip install Flask`)
- Conector Flask MySQL (para fazer o download, execute `pip install Flask mysql-connector-python`)
- Postman (para testar as rotas)

## Instalação

1. Clone este repositório: `git clone https://github.com/Luyzaluyza/Manager-People.git`
2. Navegue até o diretório do projeto.
3. No arquivo `db_utils.py`, altere as configurações `user` e `password` para suas credenciais do MySQL.

## Executando a Aplicação

Para iniciar a aplicação, você pode escolher uma das seguintes opções:

- Aperte F5 no seu ambiente de desenvolvimento.
- Execute `python app.py` no terminal.

A API estará disponível em `http://127.0.0.1:5000`.

## Rotas da API

- `POST /pessoa`: Cadastrar uma nova pessoa. Envie os dados da pessoa em um json no corpo da solicitação.
	Exemplo:
	POST: http://127.0.0.1:5000/pessoa
{
  "nome": "Luyza Brito",
  "data_nascimento": "20-01-2002",
  "endereco": "Rua Exemplo, 000",
  "cpf": "000.000.000-00",
  "estado_civil": "solteiro"
}

- `PUT /pessoa/{cpf}`: Atualizar os dados de uma pessoa pelo CPF. Envie os dados atualizados em um json no corpo da solicitação.
Exemplo:
	PUT:http://127.0.0.1:5000/pessoa/00000000000
{
  "nome": "Luyza Brito atualização Put",
  "data_nascimento": "20-01-2002",
  "endereco": "Rua Exemplo, 123",
  "estado_civil": "CASADO"
}

- `GET /pessoa`: Listar todas as pessoas cadastradas.
	Exemplo:
	GET:http://127.0.0.1:5000/pessoa

- `GET /pessoa/{cpf}`: Obter detalhes de uma pessoa pelo CPF.Passe o CPF da pessoa pela URL
	Exemplo:
	http://127.0.0.1:5000/pessoa/00000000000
	
	
- `DELETE /pessoa/{cpf}`: Excluir uma pessoa pelo CPF.Passe o CPF da pessoa que deseja deletar na URL
	Exemplo:
	http://127.0.0.1:5000/pessoa/00000000000
	

## Estrutura dos Dados da Pessoa

- Nome Completo
- Data de Nascimento (aceita o formato "dd/mm/yyyy" ou "dd-mm-yyyy")
- Endereço
- CPF (aceita o formato "xxx.xxx.xxx-xx" ou "xxxxxxxxxxx")
- Estado Civil

## Validação de Dados

A API valida o formato do CPF, o enum do estado civil e garante que todos os campos obrigatórios sejam preenchidos. Erros são tratados e mensagens são retornadas em caso de problemas.


## Contato
Se tiver alguma dúvida ou precisar de suporte técnico, sinta-se à vontade para entrar em contato comigo pelo e-mail luyza519@gmail.com.


--Luyza Brito <3
