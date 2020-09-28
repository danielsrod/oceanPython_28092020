print("Input de informações")

nome = str(input("Digite seu nome: ")).capitalize()
idade = int(input("Digite sua idade: "))
genero = str(input(("Sexo: "))).capitalize()

print(f"Olá {nome}, você possui {idade} anos de idade e é do sexo {genero}")
print(f"Já pensou no que você fará no seu aniversário de {idade + 1} anos?")