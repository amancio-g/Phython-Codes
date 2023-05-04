import random

# Função para adição


def add(x, y):
    return x + y

# Função para subtração


def subtract(x, y):
    return x - y

# Função para multiplicação


def multiply(x, y):
    return x * y

# Função para divisão


def divide(x, y):
    return x / y


# Imprime as opções de operação para o usuário
print("Escolha uma operação.")
print("1.Adicionar")
print("2.Subtrair")
print("3.Multiplicar")
print("4.Dividir")

# Solicita que o usuário escolha uma operação
choice = input("Digite sua escolha (1/2/3/4): ")

# Solicita que o usuário insira os números para realizar a operação
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Realiza a operação escolhida pelo usuário
if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))

elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))

elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))

elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))

else:
    print("Escolha inválida")
