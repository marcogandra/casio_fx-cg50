# Queda de tenção
import tools


def calcular_queda_de_tensao(resistividade, comprimento, diametro, corrente):
    import math

    # Converter o diâmetro de mm para metros
    diametro = diametro / 1000

    # Calcular a área da seção transversal do fio
    area = math.pi * (diametro/2)**2

    # Calcular a resistência
    resistencia = resistividade * (comprimento / area)

    # Calcular a queda de tensão
    tensao = corrente * resistencia

    # Converter tensão para mV e μV
    tensao_mV = tensao * 1000
    tensao_uV = tensao * 1e6

    return tensao, tensao_mV, tensao_uV


def tela():

    print("Informe ou  3 <")
    resistividade = float(input("Resistividade (9.9e-9): "))
    comprimento = float(input("Comprimento (m): "))
    diametro = float(input("Diametro (mm): "))
    corrente = float(input("Resistividade (A): "))

    if resistividade == "3":
        return
# Exemplo de uso
# resistividade = 1.68 * 1e-8  # resistividade do cobre em ohm.m
# comprimento = 10  # 10 metros
# diametro = 1  # 1 mm
# corrente = 10  # 10 Amperes

    tensao, tensao_mV, tensao_uV = calcular_queda_de_tensao(
        resistividade, comprimento, diametro, corrente)

# print("Queda de tensão: {:.3f} V".format(tensao))
# print("Queda de tensão: {:.3f} mV".format(tensao_mV))
# print("Queda de tensão: {:.3f} μV".format(tensao_uV))

    dados = [["Resistividade (9.9e-9: " + str(resistividade),
              "Comprimento (m): " + str(comprimento),
              "Diametro (mm): " + str(diametro),
              "Corrente (A):" + str(corrente),
              "*******************************",
              "Queda de tensão: {:.3f} V".format(tensao),
              "Queda de tensão: {:.3f} mV".format(tensao_mV),
              "Queda de tensão: {:.3f} μV".format(tensao_uV),
              ],
             ]
    tools.tela(dados)


# tela()
