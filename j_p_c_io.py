# O percentual de caráter iônico da ligação
from math import exp


def calcular_carater_ionico(en_mais_reativo, en_menos_reativo):
    delta_en = en_mais_reativo - en_menos_reativo
    carater_ionico = 100 * (1 - exp(-(0.25*(delta_en**2))))
    return carater_ionico


def tela():
    eletronegatividade_mais_reativo = float(
        input('Eletroneg mais reativo: '))
    eletronegatividade_menos_reativo = float(
        input('Eletroneg menos reativo: '))

    percentual = calcular_carater_ionico(
        eletronegatividade_mais_reativo, eletronegatividade_menos_reativo)
    print(
        'Caráter iônico: {:.2f}%'.format(percentual))
