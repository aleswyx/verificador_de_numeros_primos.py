# Este programa pede que o usuário digite um número inteiro positivo e, em seguida, verifica se o número é primo ou não.

numero = int(input("Digite um número inteiro positivo: "))

# Verificando se o número é primo
e_primo = True
for i in range(2, numero):
    if numero % i == 0:
        e_primo = False
        break

# Exibindo a mensagem apropriada
if e_primo:
    print(numero, "é um número primo")
else:
    print(numero, "não é um número primo")
