import tools
#import MAtomica as MassaAtomica
#import carga
import d_dat_el as dat_elem


ELEMENTOS = {'H': ('H', 'Hidrogenio'), 'He': ('He', 'Helio'),
             'Li': ('Li', 'Litio'), 'Be': ('Be', 'Berilio'), 'B': ('B', 'Boro'),
             'C': ('C', 'Carbono'), 'N': ('N', 'Nitrogenio'), 'O': ('O', 'Oxigenio'),
             'F': ('F', 'Fluor'), 'Ne': ('Ne', 'Neonio'), 'Na': ('Na', 'Sodio'),
             'Mg': ('Mg', 'Magnesio'), 'Al': ('Al', 'Aluminio'), 'Si': ('Si', 'Silicio'),
             'P': ('P', 'Fosforo'), 'S': ('S', 'Enxofre'), 'Cl': ('Cl', 'Cloro'),
             'Ar': ('Ar', 'Argonio'), 'K': ('K', 'Potassio'), 'Ca': ('Ca', 'Calcio'),
             'Sc': ('Sc', 'Escandio'), 'Ti': ('Ti', 'Titanio'), 'V': ('V', 'Vanadio'),
             'Cr': ('Cr', 'Cromio'), 'Mn': ('Mn', 'Manganes'), 'Fe': ('Fe', 'Ferro'),
             'Co': ('Co', 'Cobalto'), 'Ni': ('Ni', 'Niquel'), 'Cu': ('Cu', 'Cobre'),
             'Zn': ('Zn', 'Zinco'), 'Ga': ('Ga', 'Galio'), 'Ge': ('Ge', 'Germanio'),
             'As': ('As', 'Arsenio'), 'Se': ('Se', 'Selenio'), 'Br': ('Br', 'Bromo'),
             'Kr': ('Kr', 'Criptonio'), 'Rb': ('Rb', 'Rubidio'), 'Sr': ('Sr', 'Estroncio'),
             'Y': ('Y', 'Itrio'), 'Zr': ('Zr', 'Zirconio'), 'Nb': ('Nb', 'Niobio'),
             'Mo': ('Mo', 'Molibdenio'), 'Tc': ('Tc', 'Tecnecio'), 'Ru': ('Ru', 'Rutenio'),
             'Rh': ('Rh', 'Rodio'), 'Pd': ('Pd', 'Paladio'), 'Ag': ('Ag', 'Prata'),
             'Cd': ('Cd', 'Cadmio'), 'In': ('In', 'Indio'), 'Sn': ('Sn', 'Estanho'),
             'Sb': ('Sb', 'Antimonio'), 'Te': ('Te', 'Telurio'), 'I': ('I', 'Iodo'),
             'Xe': ('Xe', 'Xenonio'), 'Cs': ('Cs', 'Cesio'), 'Ba': ('Ba', 'Bario'),
             'La': ('La', 'Lantanio'), 'Ce': ('Ce', 'Cerio'), 'Pr': ('Pr', 'Praseodimio'),
             'Nd': ('Nd', 'Neodimio'), 'Pm': ('Pm', 'Promecio'), 'Sm': ('Sm', 'Samario'),
             'Eu': ('Eu', 'Europio'), 'Gd': ('Gd', 'Gadolinio'), 'Tb': ('Tb', 'Terbio'),
             'Dy': ('Dy', 'Disprosio'), 'Ho': ('Ho', 'Holmio'), 'Er': ('Er', 'Erbio'),
             'Tm': ('Tm', 'Tulio'), 'Yb': ('Yb', 'Iterbio'), 'Lu': ('Lu', 'Lutecio'),
             'Hf': ('Hf', 'Hafnio'), 'Ta': ('Ta', 'Tantalo'), 'W': ('W', 'Tungstenio'),
             'Re': ('Re', 'Renio'), 'Os': ('Os', 'Osmio'), 'Ir': ('Ir', 'Iridio'),
             'Pt': ('Pt', 'Platina'), 'Au': ('Au', 'Ouro'), 'Hg': ('Hg', 'Mercurio'),
             'Tl': ('Tl', 'Talio'), 'Pb': ('Pb', 'Chumbo'), 'Bi': ('Bi', 'Bismuto'),
             'Th': ('Th', 'Torio'), 'Pa': ('Pa', 'Protactinio'), 'U': ('U', 'Uranio'),
             'Np': ('Np', 'Netunio'), 'Pu': ('Pu', 'Plutonio'), 'Am': ('Am', 'Americio'),
             'Cm': ('Cm', 'Curio'), 'Bk': ('Bk', 'Berquelio'), 'Cf': ('Cf', 'Californio'),
             'Es': ('Es', 'Einstenio'), 'Fm': ('Fm', 'Fermio'), 'Md': ('Md', 'Mendelevio'),
             'No': ('No', 'Nobelio'), 'Lr': ('Lr', 'Laurencio'),
             'Rf': ('Rf', 'Rutherfordio'), 'Db': ('Db', 'Dubnio'), 'Sg': ('Sg', 'Seaborgio'),
             'Bh': ('Bh', 'Bohrio'), 'Hs': ('Hs', 'Hassio'), 'Mt': ('Mt', 'Meitnerio'),
             'Ds': ('Ds', 'Darmstadtio'), 'Rg': ('Rg', 'Roentgenio'),
             'Cn': ('Cn', 'Copernicio'), 'Nh': ('Nh', 'Nihonio'), 'Fl': ('Fl', 'Flerovio'),
             'Mc': ('Mc', 'Moscovio'), 'Lv': ('Lv', 'Livermorio'), 'Ts': ('Ts', 'Tenessino'),
             'Og': ('Og', 'Oganessonio')}


def nome_elemento(elemento):
    elemento = tools.ajustar_simbolo(elemento)

    if elemento in ELEMENTOS:
        return ELEMENTOS[elemento]
    for simbolo, nome in ELEMENTOS.values():
        if elemento.upper() == nome.upper():
            return (simbolo, nome)

    print("Elemento ", elemento, " não encontrado")
    return ("nada", "nada")


def dados_em_tela():
    # pass
    while True:
        tools.cls()

        print("Informe ou  3 <")
        elemento_quimico = input("Elemento: ")

        if elemento_quimico == "3":
            break

        try:
            simbolo, nome = nome_elemento(elemento_quimico)
            elemento = dat_elem.elemento(simbolo)

            dados = [["Elemento: " + elemento["nome"],
                      "Simbolo: " + simbolo,
                      "Numero atomico: " + str(elemento["numero_atomico"]),
                      "Massa atomica: " + str(elemento["massa_atomica"]).replace(".", ","),
                      "Raio atomico: " + str(elemento["raio_atomico"]),
                      "estrutura cristalina: " + elemento["estrutura_cristalina"],
                      "eletronegatividade: " + str(elemento["eletronegatividade"]).replace(".", ","),
                      "Atomos por celula unitaria: " + str(elemento["atomos_celula"]),
                      "Densidade: " + str(float(elemento["densidade"])).replace(".", ","),
                      "Carga / Valencia: " + str(elemento["valencia"]),
                      ],
                     ]
            tools.tela(dados)

        except Exception as e:
            print("Erro: ", e)
            input("Pressione ENTER")
