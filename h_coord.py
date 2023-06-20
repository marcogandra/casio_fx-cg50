import tools


# # estrutura_coordenacao = [
# #     {"estrutura": "01-cubica_simples",          "sigla": "CS",  "atomos_por_celula_unitaria": 1, "fator_atomo_na_celula_unitaria_por_vertice": "1/8",
# #         "numero_coordenacao":  6, "fator_empacotamento": 0.52, "numero_vertices": 8, "parametro_de_reticulado": "a = 2 R | a^3 = 8R^3",
# #         "Elementos": ['Po']},

# #     {"estrutura": "02-cubica_de_corpo_central", "sigla": "CCC", "atomos_por_celula_unitaria": 8, "fator_atomo_na_celula_unitaria_por_vertice": "1/8",
# #      "numero_coordenacao":  8, "fator_empacotamento": 0.68, "numero_vertices": 8,  "parametro_de_reticulado": "a = 4R/(3)^1/2 | a^3 = 32R^3/3",
# #      "Elementos": ['Cs', 'Rb', 'K', 'Ba', 'Sr', 'Na', 'Li']},

# #     {"estrutura": "03-cubica_de_face_central",  "sigla": "CFC", "atomos_por_celula_unitaria": 12, "fator_atomo_na_celula_unitaria_por_vertice": "1/8",
# #      "numero_coordenacao": 12, "fator_empacotamento": 0.74, "numero_vertices": 8,  "parametro_de_reticulado": "a = 4R/(2)^1/2 | a^3 = 16R^3/2",
# #      "Elementos": ['Mg', 'Ca', 'Y', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu']},

# #     {"estrutura": "04-hexagonal_compacta",      "sigla": "CCC", "atomos_por_celula_unitaria": 12, "fator_atomo_na_celula_unitaria_por_vertice": "1/8",
# #      "numero_coordenacao": 12, "fator_empacotamento": 0.74, "numero_vertices": 8,  "parametro_de_reticulado": "a = 4R/(2)^1/2 | a^3 = 16R^3/2",
# #      "Elementos": ['Zn', 'Cd', 'Be', 'Mg', 'Ti', 'Zr', 'Hf', 'Sc', 'Y', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu']},
# #     # ["05-hexagonal_simples", 6, ['Be']],
# #     # ["06-ortorrombica_simples", 6, ['P', 'As', 'Sb', 'Bi', 'Te', 'Se', 'S', 'O', 'Po']],
# #     # ["07-ortorrombica_de_base_central", 8, ['Sn', 'Ge', 'Si', 'C', 'N']],
# #     # ["08-ortorrombica_de_corpo_centr", 8, ['Al', 'Ga', 'In', 'Tl']],
# #     # ["09-ortorrombica_de_face_central", 8, ['Cr', 'Mo', 'W', 'V', 'Nb', 'Ta']],
# #     # ["10-romboedrica_simples", 6, ['Hg', 'Cd', 'Zn', 'Be']],
# #     # ["11-tetragonal_simples", 4, ['Th', 'Ti', 'Zr', 'Hf', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu']],
# #     # ["12-tetragonal_de_corpo_central", 8, ['Sn', 'Ge', 'Si', 'C', 'N']],
# #     # ["13-monoclinica_simples", 4, ['P', 'As', 'Sb', 'Bi', 'Te', 'Se', 'S', 'O', 'Po']],
# #     # ["14-monoclinica_de_base_central", 4, ['Al', 'Ga', 'In', 'Tl']],
# #     # ["15-triclinica_simples", 6, ['Cr', 'Mo', 'W', 'V', 'Nb', 'Ta']],
# #     # ["16-trigonal_simples", 3, ['Be']],
# #     # Adicione outras estruturas cristalinas e seus numeros de coordenação aqui
# # ]

# As principais correções incluem:

# A estrutura cúbica de corpo central (CCC) possui 2 átomos por célula unitária, não 8.
# A estrutura cúbica de face central (CFC) possui 4 átomos por célula unitária, não 12.
# A estrutura hexagonal compacta (HC) tem uma sigla diferente (HC em vez de CCC),
# tem 6 átomos por célula unitária, não 12,
# e tem um fator diferente para o átomo na célula unitária por vértice (1/6 em vez de 1/8).
# Além disso, o número de vértices é 12, não 8, e o parâmetro de reticulado é "a = 2R | c = 4R/(3)^1/2".

estrutura_coordenacao = [
    {"estrutura": "01-cubica_simples",          "sigla": "CS",  "atomos_por_celula_unitaria": 1, "fator_atomo_na_celula_unitaria_por_vertice": "1/8",
        "numero_coordenacao":  6, "fator_empacotamento": 0.524, "numero_vertices": 8, "parametro_de_reticulado": "a = 2R | a^3 = 8R^3",
        "Elementos": ['Po']},
    
    {"estrutura": "02-cubica_de_corpo_central", "sigla": "CCC", "atomos_por_celula_unitaria": 2, "fator_atomo_na_celula_unitaria_por_vertice": "8/8",
     "numero_coordenacao":  8, "fator_empacotamento": 0.68, "numero_vertices": 8,  "parametro_de_reticulado": "a = 4R/raiz(3) | a^3 = 64/3*raiz(3)",
     #"Elementos": ['Cs', 'Rb', 'K', 'Ba', 'Sr', 'Na', 'Li']},
     "Elementos": ["Li", "Na", "K", "V", "Cr", "Fe", "Cu", "Rb", "Nb", "Mo", "Ag", "Cs", "Ba", "Eu", "Ta", "W", "Fr", ]},
    
    {"estrutura": "03-cubica_de_face_central",  "sigla": "CFC", "atomos_por_celula_unitaria": 4, "fator_atomo_na_celula_unitaria_por_vertice": "1/8",
     "numero_coordenacao": 12, "fator_empacotamento": 0.74, "numero_vertices": 8,  "parametro_de_reticulado": "a = 4*raiz(2)R | a^3 = (32/raiz(2))R^3",
    # "Elementos": ['Mg', 'Ca', 'Y', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu']},
    "Elementos": ["Al", "Ca", "Sc", "Ni", "Sr", "Rh", "Pd", "Ce", "Yb", "Ir", "Pt", "Au", "Pb", "Ac", "Th",]},
    
    {"estrutura": "04-hexagonal_compacta",      "sigla": "HC", "atomos_por_celula_unitaria": 6, "fator_atomo_na_celula_unitaria_por_vertice": "1/6",
     "numero_coordenacao": 12, "fator_empacotamento": 0.74, "numero_vertices": 12,  "parametro_de_reticulado": "a = 2*raiz(2)R | a^3 = (32/raiz(2))R^3",
     #"Elementos": ['Zn', 'Cd', 'Be', 'Mg', 'Ti', 'Zr', 'Hf', 'Sc', 'Y', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu']},
     "Elementos":['Be', 'Mg', 'Ti', 'Co', 'Zn', 'Y', 'Zr', 'Tc', 'Ru', 'Cd', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Lu', 'Hf', 'Re', 'Os', 'Tl']},
]


def dados_em_tela():
    try:
        dados = []

        for estrutura in estrutura_coordenacao:
            tela = gerar_tela_parte_1(estrutura)
            dados.append(tela)
            tela = gerar_tela_parte_2(estrutura)
            dados.append(tela)

        tools.tela(dados)

    except Exception as e:
        print("Erro: ", i, " - ", e)


def gerar_tela_parte_1(estrutura, elemento=""):
    if elemento != "":
        elemento = tools.ajustar_simbolo(elemento)
        elemento = " | Elem: "+elemento

    tela = ["Est. Crist. Metais: "+estrutura["estrutura"] + elemento]
    tela.append("-"*50)

    tela.append("Sigla: "+estrutura["sigla"])

    tela.append("atomos_por_celula_unitaria: " +
                str(estrutura["atomos_por_celula_unitaria"])+" atomo")

    tela.append("Fator atomo na celula unitaria por vertice: " +
                str(estrutura["fator_atomo_na_celula_unitaria_por_vertice"]))

    tela.append("N de coordenacao-atm vizinhos: " +
                str(estrutura["numero_coordenacao"]))

    tela.append("Numero de vertices: " +
                str(estrutura["numero_vertices"]))

    tela.append("Reticulado (REDE): " +
                str(estrutura["parametro_de_reticulado"]))

    tela.append("Fator de empacotamento: " +
                str(estrutura["fator_empacotamento"]))

    return tela


def gerar_tela_parte_2(estrutura, elemento=""):
    if elemento != "":
        elemento = tools.ajustar_simbolo(elemento)
        elemento = " | Elem: "+elemento

    tela = ["Est. Crist. Metais: "+estrutura["estrutura"] + elemento]
    tela.append("-"*50)
    tela.append(
        "N tot atm: n_vert * at_cel_unit_vert = at_por_cel_unit")
    tela.append("Num total de atomos: " + str(estrutura["numero_vertices"]) + " * " + str(
        estrutura["fator_atomo_na_celula_unitaria_por_vertice"]) + " = " + str(estrutura["atomos_por_celula_unitaria"]))
    tela.append(
        "Vol ocup at Va=n_tot_at * vol_um_at = 4/3*pi*R^3")
    tela.append(
        "Vol ocup por atom Va = 1 * Vol_1_atom = 4/3 * pi * R^3")
    tela.append("Vol da celula unitaria: Vc = a^3")
    tela.append("Vol da cel unit: Vc = " +
                estrutura["parametro_de_reticulado"])
    tela.append("Fator de empacotamento FE:  1 * Va / Vc")
    vc = str(estrutura["parametro_de_reticulado"]).split(' = ')
    tela.append(
        "Fator de empac FE:  (1 *  4/3 * pi * R^3) / "+vc[2])

    return tela


def obter_estrutura_por_elemento(elemento):
    elemento = tools.ajustar_simbolo(elemento)
    for estrutura in estrutura_coordenacao:
        if elemento in estrutura["Elementos"]:
            return estrutura
    return None  # retorna None se o elemento não for encontrado


def imprimir_estrutura_por_elemento():
    while True:
        print("Elemento ou 3 <")
        elemento = input('Elemento: ')

        if elemento == '3':
            break

        elemento = tools.ajustar_simbolo(elemento)
        estrutura = obter_estrutura_por_elemento(elemento)

        if estrutura is not None:
            dados = []
            tela = gerar_tela_parte_1(estrutura, elemento)
            dados.append(tela)
            tela = gerar_tela_parte_2(estrutura, elemento)
            dados.append(tela)

            tools.tela(dados)
            # for chave, valor in estrutura.items():
            #     print(f'{chave}: {valor}')
        else:
            print('O elemento '+elemento+' não foi encontrado.')


# dados_em_tela()

# imprimir_estrutura_por_elemento()
