def calcule_dobro(p_valor):
    return p_valor * 2
def calcule_triplo(p_valor):
    return p_valor * 3
if __name__ == '__main__':
    valor = int(input("digite um número: "))
    print("valor retornado pela função:",calcule_dobro(valor))
    print("valor retornado pela função calcule_triplo: ", calcule_triplo(valor))