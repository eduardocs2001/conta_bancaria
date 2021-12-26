import sqlite3


class banco_dados:

    def __init__(self):
        self._conn = sqlite3.connect('clientes.db')
        self._cursor = self._conn.cursor()


    def criando_tabela(self):
        self._cursor.execute("""
         CREATE TABLE clientes (
            n_conta INTEGER NOT NULL PRIMARY KEY,
            nome TEXT NOT NULL,
            banco TEXT NOT NULL,
            saldo REAL NOT NULL,
            limite REAL NOT NULL,
            email TEXT
             )
         """)
        print('Tabela criada com sucesso!')
        self._conn.close()

    def insert(self, n_conta, nome, banco, saldo, limite, email):
        dados = [n_conta, nome, banco, saldo, limite, email]
        self._cursor.execute("""INSERT INTO clientes (n_conta, nome, banco, saldo, limite, email) VALUES (?, ?, ?, ?, ?, ?)""", dados)
        self._conn.commit()
        print('Dados inseridos com sucesso!')
        self._conn.close()


    def ler_dados(self, n_conta):
        self._cursor.execute(f'SELECT * FROM clientes WHERE n_conta = {int(n_conta)}')
        dados = self._cursor.fetchall()
        numero = dados[0][0]
        nome = dados[0][1]
        banco = dados[0][2]
        saldo = str(dados[0][3])
        limite = str(dados[0][4])
        print( f'Banco:{banco}\n' 
               f'Número da conta:{numero}\n'
               f'Nome:{nome}\n' 
               f'Saldo: R${saldo.replace(".",",")}\n' 
               f'Limite: R${limite.replace(".",",")}\n')



    def retorna_saldo_transferencia(self, n_conta_t, n_conta_r=None):
        dados = []
        if n_conta_r != None:
            self._cursor.execute(f'SELECT saldo FROM clientes WHERE n_conta = {int(n_conta_r)}')
            recebe = self._cursor.fetchall()
            dados.append(recebe[0][0])

        else:
            pass
        self._cursor.execute(f'SELECT saldo, limite FROM clientes WHERE n_conta = {int(n_conta_t)}')
        transferi = self._cursor.fetchall()
        dados.append(transferi[0][0])
        dados.append(transferi[0][1])
        return dados




    def atualizar_saldo(self, n_conta, novo_saldo):
        self._cursor.execute("UPDATE clientes SET saldo = ? WHERE n_conta = ?", (novo_saldo, n_conta))
        self._conn.commit()




    #função apenas para teste
    def mostra_todas_contas(self):
        self._cursor.execute("SELECT * FROM clientes")
        clientes = self._cursor.fetchall()
        for cliente in clientes:
            print(cliente)
            print('\n\n-------------------------------------------------------------\n')