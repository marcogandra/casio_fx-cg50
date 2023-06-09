# def calcular_eletrons(corrente_mA):
#     # Convertendo corrente de mA para A
#     I = corrente_mA / 1000.0

#     # Convertendo corrente para carga (Coulombs)
#     Q = I * 1.0  # já que 1A = 1C/s

#     # Carga do elétron (em Coulombs)
#     carga_eletron = 1.6e-19

#     # Calculando a quantidade de elétrons
#     n_eletrons = Q / carga_eletron

#     # Imprimindo a resposta
#     print("A quantidade de elétrons que passam por segundo é de aproximadamente", round(n_eletrons))

# Testando a função com 1mA

def calcular_eletrons(corrente_mA):
    # Convertendo corrente de mA para A
    I = corrente_mA / 1000.0

    # Convertendo corrente para carga (Coulombs)
    Q = I * 1.0  # já que 1A = 1C/s

    # Carga do elétron (em Coulombs)
    carga_eletron = 1.6e-19

    # Calculando a quantidade de elétrons
    n_eletrons = Q / carga_eletron

    # Imprimindo a resposta
    valor_notacao_cientifica = "{:.2e}".format(round(n_eletrons))
    print("A quantidade de elétrons que passam por segundo é de aproximadamente",
          valor_notacao_cientifica)


def tela():
    print("Elétrons passam por segundo por uma seção transversal")
    corrente_mA = float(input("Corrente (mA): "))
    calcular_eletrons(corrente_mA)


#tela()
