
def calcular_irpf (lista_deducoes, renda_bruta):

        soma_deducoes = sum(lista_deducoes)
        base_calculo = (renda_bruta - soma_deducoes)
        imposto_devido = base_calculo * 0.22

        print(f"O IMPOSTO DEVIDO É R$ {imposto_devido:.2f}")


def main():

    lista_deducoes = []
    renda_bruta = float(input("Digite o valor da renda bruta anual em R$: "))

    while True:
        decisao_deducoes = input("Você tem deduções à declarar? S/N: ").upper()

        if decisao_deducoes == "S":
            deducao = float(input("Digite o valor da dedução: "))
            lista_deducoes.append(deducao)

        elif decisao_deducoes == "N":
            calcular_irpf(lista_deducoes, renda_bruta)
            break

    
if __name__=="__main__":

    main()