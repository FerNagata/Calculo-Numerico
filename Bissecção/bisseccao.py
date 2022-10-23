equacao = input("Equação: ")
precisao = float(input("Precisão: "))
print("Intrvalo [a, b] que contém uma raiz: ")
a = int(input("a = "))
b = int(input("b = "))

def mostraTabela(pos, neg, xlinha, func, crit): #Tabela
    print("%.4f"%pos, "\t"*2, "%.4f"%neg, "\t"*2, "%.4f"%xlinha, "\t"*2, "%.4f"%func, "\t"*2, "%.4f"%crit)

equacao = equacao.replace("x", "(x)")#Evita erros com sinal (+/-)
funcaoA = equacao.replace("x", str(a))
funcaoB = equacao.replace("x", str(b))

funcaoA = eval(funcaoA)
funcaoB = eval(funcaoB)
#Verifica se f(a) é + ou -. Caso f(a) for positivo f(b) tem que ser negativo, ou f(a) = - | f(b) = +
if funcaoA >= 0:
    positivo = a
    negativo = b
else:
    negativo = a
    positivo = b

xlinha = (a+b)/2

func = equacao.replace("x", str(xlinha))
func = eval(func)

criterio = abs(b-a)/2 #Outro criterio de parada: |b-a|/2 

while(abs(func)>precisao and criterio>precisao): #Critérios de parada
    mostraTabela(positivo, negativo, xlinha, func, criterio)
    if func >= 0:
        positivo = xlinha
    else:
        negativo = xlinha
    xlinha = (positivo + negativo)/2
    func = equacao.replace("x", str(xlinha))
    func = eval(func)
    criterio = abs(positivo-negativo)/2

mostraTabela(positivo, negativo, xlinha, func, criterio)
print("A raiz será: {}" .format(xlinha))