import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server=SBVNB031\SQLEXPRESS;"
    "Database=Python_sql;"
)

conexao = pyodbc.connect(dados_conexao)

print('conexão efetuada com sucesso!!!')

cursor = conexao.cursor()

id_venda = 3
cliente = 'Angelina'
produto = 'plano'
data_venda = '26/02/2023'
preco = 470.50
quantidade = 2


comando = f"""INSERT INTO Vendas(id_venda, cliente, produto, data_venda, preco, quantidade)
    VALUES
        ({id_venda}, '{cliente}', '{produto}', '{data_venda}', {preco}, {quantidade})
        """
cursor.execute(comando)
cursor.commit()
print('Alteração concluida')
