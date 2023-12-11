
# Calculadora de Aumento Salarial

print("Descubra o valor do seu aumento.")

# Solicitar o salário ao usuário
salario = float(input("Qual é o seu salário atual? "))

# Validar se o salário é válido (não negativo)
while salario < 0:
    print('\nDigite um valor válido!')
    salario = float(input("Qual é o seu salário atual? "))

# Calcular e exibir o aumento com base nas faixas salariais
if salario <= 400:
    percentual = 15
elif salario <= 800:
    percentual = 12
elif salario <= 1200:
    percentual = 10
elif salario <= 2000:
    percentual = 7
else:
    percentual = 4

novo_salario = salario + (salario * (percentual / 100))
reajuste_ganho = salario * (percentual / 100)

print(f"Novo salário: {novo_salario:.2f} \nReajuste ganho: {reajuste_ganho:.2f} \nEm percentual: {percentual} %")
