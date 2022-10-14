from sympy import Derivative, Symbol

equacao = input("Equação: ")

print("Intervalo de [a, b]")
a = int(input("a = "))
b = int(input("b = "))

def funcaoList(equacao, a, b): #Esta função calcula f(x) variando x no intervalo dado e insere os valores em uma lista
    listF = list()
    equacao = equacao.replace("x", "(x)")#assegura que não haverá problema com sinal

    for i in range(a, (b + 1)):
        #aux = int(i)
        str_var = str(i)
        nova = equacao.replace("x", str_var)
        resultado = eval(nova)
        listF.append(resultado)

    return listF

def derivadaList(equacao, a, b): #Esta função calcula f'(x) variando x no intervalo dado e insere os valores em uma lista
    listD = list()
    x = Symbol('x')
    derivada = Derivative(equacao, (x)).doit()
    derivada = str(derivada) # casting
    derivada = derivada.replace("x", "(x)")#insere "()" na equação para que na resulução não haja problemas com o sinal (+-)
    
    for i in range(a, (b + 1)):
        str_var = str(i)
        nova = derivada.replace("x", str_var)
        resultado = eval(nova)
        listD.append(resultado)
    
    return listD


intervaloFuncao = list() #vai guardar intervalos
i = 0
qtd = abs(a) + abs(b)
listFuncao = funcaoList(equacao, a, b)
listDerivada = derivadaList(equacao, a, b)
#Analisando os valores da listFuncao e listDerivada
#Para que o intervalo seja valido f(xi).f(xi+1) < 0 e f'(xi).f'(xi+1) > 0
for j in range(a, b+1):
    if i < qtd and ((listFuncao[i])*(listFuncao[i+1])) < 0:
        if ((listDerivada[i])*(listDerivada[i+1])) >= 0:
            intervaloFuncao.append([j, j+1])
    elif listFuncao[i] == 0: #é a própria raiz
        intervaloFuncao.append([j, j+1, listFuncao[i]])
    i += 1

print("\nIntervalo(s) que contém raiz:")
print(intervaloFuncao)
