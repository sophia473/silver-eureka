def retorna_soma(v1,v2):
    return v1 + v2
def retorna_soma_2(v1,v2):
    return v1 + v2
def mostra_soma(v1,v2):
    print('resultado da soma:', v1 + v2)
if __name__ == '__main__':
    n1 = int(input('digite o primeiro número:'))
    n2 = int(input("digite o segundo número: "))
print('soma =', retorna_soma_2(n1, n2))
print("soma com valores reais (2.1 e 3.3 =", retorna_soma_2(2.1,3.3))
mostra_soma(n1,n2)