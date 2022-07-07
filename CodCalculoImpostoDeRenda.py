#Rafael Richard Alves de Godoy / Turma 02
#Exercício Imposto de renda / Escola Vida Nova Tec - Python

aliquota1 = 7.5/100 #transformando o imposto para 7.5%
aliquota2 = 15/100  #transformando o imposto para 15%
aliquota3 = 22.5/100 #transformando o imposto para 22.5%
aliquota4 = 27.5/100 #transformando o imposto para 27.5%

print("\nCálculo de imposto de renda\n")
salario = float(input("Digite seu salário bruto: "))

if (salario <= 1903.98):
    print("Isento, alíquota de 0%\n")
    print("Seu salário líquido é de: ",salario)
elif (salario > 1903.98) and (salario <= 2826.65):
    print("Alíquota de 7.5%")
    valorImposto = (salario * aliquota1)    #calcula o valor do imposto 
    print("Valor do Imposto: ",valorImposto)    #imprime o valor do imposto
    salarioLiquido = (salario - valorImposto)  #calcula o salario liquido
    print("Seu salário líquido é de:",salarioLiquido) #imprime o salario liquido
elif (salario > 2826.65) and (salario <= 3751.05):
    print("Alíquota de 15%")
    valorImposto = (salario * aliquota2)    #calcula o valor do imposto 
    print("Valor do Imposto: ",valorImposto)    #imprime o valor do imposto
    salarioLiquido = (salario - valorImposto)  #calcula o salario liquido
    print("Seu salário líquido é de:",salarioLiquido) #imprime o salario liquido
elif (salario > 3751.05) and (salario <= 4664.68):
    print("Alíquota de 22.5%")
    valorImposto = (salario * aliquota3)    #calcula o valor do imposto 
    print("Valor do Imposto: ",valorImposto)    #imprime o valor do imposto
    salarioLiquido = (salario - valorImposto)  #calcula o salario liquido
    print("Seu salário líquido é de:",salarioLiquido) #imprime o salario liquido
else:
    print("Alíquota de 27.5%")
    valorImposto = (salario * aliquota4)    #calcula o valor do imposto 
    print("Valor do Imposto: ",valorImposto)    #imprime o valor do imposto
    salarioLiquido = (salario - valorImposto)  #calcula o salario liquido
    print("Seu salário líquido é de:",salarioLiquido) #imprime o salario liquido