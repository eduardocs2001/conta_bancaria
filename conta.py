from bd import banco_dados
bd = banco_dados()

class conta:

    def cadastrar(self, nome, banco, numero, saldo, limite, email):
        saldo = saldo
        limite = limite
        nome = nome
        numero_conta = numero
        banco = banco
        email = email
        bd.insert(numero_conta, nome, banco, saldo, limite, email)


    def transferi(self, _numero_conta_t, _numero_conta_r, valor):
        saldos = bd.retorna_saldo_transferencia(_numero_conta_t, _numero_conta_r)
        saldo_r = saldos[0]
        saldo_t = saldos[1]
        limite_t = saldos[2]
        if (saldo_t + limite_t) - valor >= 0:
            bd.atualizar_saldo(_numero_conta_r, saldo_r + valor)
            bd.atualizar_saldo(_numero_conta_t, saldo_t - valor)
        else:
            print('Valor insuficiente!')


    def sacar(self, numero_conta, valor):
        saldo = bd.retorna_saldo_transferencia(numero_conta, None)
        valor_total = saldo[0] + saldo[1]
        if valor_total >= 0:
            bd.atualizar_saldo(numero_conta, saldo[0] - valor)
            print('Valor sacado!')
        else:
            print('Saldo insuficiente!')



    def deposita(self, numero_conta, valor):
        saldo = bd.retorna_saldo_transferencia(numero_conta, None)
        bd.atualizar_saldo(numero_conta, saldo[0]+valor)
        print('Deposito realizado com sucesso!')