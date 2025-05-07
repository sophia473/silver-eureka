def mostra_valor(valor1):
    print("parâmetro recebido: ", valor1)
def mostrar_dois_valores(valor1,valor2):
    print("valores dos dois parâmetros recebido:", valor1,valor2)
if __name__ == '__main__':
    # print("primeira forma de fazer (sem variáveis, passa o valor direto):")
    # mostra_valor(5)
    # mostra_valor(23.8)
    # print("segunda forma de fazer(com variavéis, sem input):")
    # v_inteiro = 43
    # mostra_valor(v_inteiro)
    # v_real = 37.4
    # mostra_valor(v_real)
    # print("terceira forma de fazer(com variavéis, com inpunt):")
    # v_inteiro = int(input("valor inteiro: "))
    # mostra_valor(v_inteiro)
    # v_real= float(input("valor real: "))
    # mostra_valor(v_real)
    a = int(input("digite o valor 1: "))
    b= int(input("digite o valor 2:"))
    mostrar_dois_valores(a,b)



