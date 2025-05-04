class ContaBancaria:
	def __init__(self, saldo_inicial):
            self._saldo = saldo_inicial

def depositar(self, valor):
    if valor > 0:
        self._saldo += valor
        print(f"Depósito de {valor} realizado. Saldo atual: {self._saldo}")
    else:
            print("Valor de depósito inválido.")
            	 
            	 
    
def sacar(self,valor):
    if valor > 0 and valor <= self._saldo:
        self._saldo -= valor
        print(f"Seu saque no valor de {valor} foi realizado. Saldo atual: {self._saldo}")
       	 
    else:
        print("Saldo insuficiente para saque.")
       	 
       	 
def get_saldo(self):
    return self._saldo
   	 
conta = ContaBancaria(100)

print(conta.depositar(40))
print(conta.sacar(10))
