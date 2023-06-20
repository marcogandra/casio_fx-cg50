import tools

ELEMENT_DATA = {
    'H':  {'nome': 'Hidrogenio', 'numero_atomico': 1, 'massa_atomica': 1.0079, 'raio_atomico': 53, 'estrutura_cristalina': 'hexagonal', 'eletronegatividade': 2.2, 'valencia': 1, 'atomos_celula': 2, 'densidade': 0.0000899},
    'He': {'nome': 'Helio', 'numero_atomico': 2, 'massa_atomica': 4.0026, 'raio_atomico': 31, 'estrutura_cristalina': 'hexagonal', 'eletronegatividade': '', 'valencia': 0, 'atomos_celula': 2, 'densidade': 0.0001785},
    'Li': {'nome': 'Litio', 'numero_atomico': 3, 'massa_atomica': 6.94, 'raio_atomico': 167, 'estrutura_cristalina': 'cubica', 'eletronegatividade': 0.98, 'valencia': 1, 'atomos_celula': 2, 'densidade': 0.534},
    'Be': {'nome': 'Berilio', 'numero_atomico': 4, 'massa_atomica': 9.0122, 'raio_atomico': 112, 'estrutura_cristalina': 'hexagonal', 'eletronegatividade': 1.57, 'valencia': 2, 'atomos_celula': 2, 'densidade': 1.85},
    'B':  {'nome': 'Boro', 'numero_atomico': 5, 'massa_atomica': 10.81, 'raio_atomico': 87, 'estrutura_cristalina': 'romboedrica', 'eletronegatividade': 2.04, 'valencia': 3, 'atomos_celula': 2, 'densidade': 2.34},
    'C':  {'nome': 'Carbono', 'numero_atomico': 6, 'massa_atomica': 12.011, 'raio_atomico': 67, 'estrutura_cristalina': 'hexagonal', 'eletronegatividade': 2.55, 'valencia': 4, 'atomos_celula': 2, 'densidade': 2.267},
    'N':  {'nome': 'Nitrogenio', 'numero_atomico': 7, 'massa_atomica': 14.007, 'raio_atomico': 56, 'estrutura_cristalina': 'hexagonal', 'eletronegatividade': 3.04, 'valencia': 3, 'atomos_celula': 2, 'densidade': 0.0012506},
    'O':  {'nome': 'Oxigenio', 'numero_atomico': 8, 'massa_atomica': 15.999, 'raio_atomico': 48, 'estrutura_cristalina': 'cubica', 'eletronegatividade': 3.44, 'valencia': 2, 'atomos_celula': 4, 'densidade': 0.001429},
    'F':  {'nome': 'Fluor', 'numero_atomico': 9, 'massa_atomica': 18.998, 'raio_atomico': 42, 'estrutura_cristalina': 'cubica', 'eletronegatividade': 3.98, 'valencia': 1, 'atomos_celula': 4, 'densidade': 0.001696},
    'Ne': {'nome': 'Neonio', 'numero_atomico': 10, 'massa_atomica': 20.180, 'raio_atomico': 38, 'estrutura_cristalina': 'cubica', 'eletronegatividade': '', 'valencia': 0, 'atomos_celula': 4, 'densidade': 0.0008999},
    'Na': {'nome': 'Sodio', 'numero_atomico': 11, 'massa_atomica': 22.990, 'raio_atomico': 190, 'estrutura_cristalina': 'cubica', 'eletronegatividade': 0.93, 'valencia': 1, 'atomos_celula': 2, 'densidade': 0.971},
    'Mg': {'nome': 'Magnesio', 'numero_atomico': 12, 'massa_atomica': 24.305, 'raio_atomico': 145, 'estrutura_cristalina': 'hexagonal', 'eletronegatividade': 1.31, 'valencia': 2, 'atomos_celula': 2, 'densidade': 1.738},
    'Al': {'nome': 'Aluminio', 'numero_atomico': 13, 'massa_atomica': 26.982, 'raio_atomico': 118, 'estrutura_cristalina': 'cubica', 'eletronegatividade': 1.61, 'valencia': 3, 'atomos_celula': 4, 'densidade': 2.698},
    'Si': {'nome': 'Silicio', 'numero_atomico': 14, 'massa_atomica': 28.085, 'raio_atomico': 111, 'estrutura_cristalina': 'cubica', 'eletronegatividade': 1.9, 'valencia': 4, 'atomos_celula': 8, 'densidade': 2.3296},
    'P':  {'nome': 'Fosforo', 'numero_atomico': 15, 'massa_atomica': 30.974, 'raio_atomico': 98, 'estrutura_cristalina': 'cubica', 'eletronegatividade': 2.19, 'valencia': 3, 'atomos_celula': 4, 'densidade': 1.82},
    'S':  {'nome': 'Enxofre', 'numero_atomico': 16, 'massa_atomica': 32.06, 'raio_atomico': 88, 'estrutura_cristalina': 'ortorrombica', 'eletronegatividade': 2.58, 'valencia': 2, 'atomos_celula': 8, 'densidade': 2.07},
    'Cl': {'nome': 'Cloro', 'numero_atomico': 17, 'massa_atomica': 35.45, 'raio_atomico': 79, 'estrutura_cristalina': 'ortorrombica', 'eletronegatividade': 3.16, 'valencia': 1, 'atomos_celula': 2, 'densidade': 0.003214},
    'Ar': {'nome': 'Argonio', 'numero_atomico': 18, 'massa_atomica': 39.948, 'raio_atomico': 71, 'estrutura_cristalina': 'cubica', 'eletronegatividade': '', 'valencia': 0, 'atomos_celula': 4, 'densidade': 0.0017837},
    'K':  {'nome': 'Potassio', 'numero_atomico': 19, 'massa_atomica': 39.098, 'raio_atomico': 243, 'estrutura_cristalina': 'cubica', 'eletronegatividade': 0.82, 'valencia': 1, 'atomos_celula': 2, 'densidade': 0.862},
    'Ca': {'nome': 'Calcio', 'numero_atomico': 20, 'massa_atomica': 40.078, 'raio_atomico': 194, 'estrutura_cristalina': 'cubica', 'eletronegatividade': 1.0, 'valencia': 2, 'atomos_celula': 2, 'densidade': 1.54},
    'Sc': {'nome': 'Escandio', 'numero_atomico': 21, 'massa_atomica': 44.956, 'raio_atomico': 184, 'estrutura_cristalina': 'hexagonal', 'eletronegatividade': 1.36, 'valencia': 3, 'atomos_celula': 2, 'densidade': 2.989},
    'Ti': {'nome': 'Titanio', 'numero_atomico': 22, 'massa_atomica': 47.867, 'raio_atomico': 176, 'estrutura_cristalina': 'hexagonal', 'eletronegatividade': 1.54, 'valencia': 4, 'atomos_celula': 2, 'densidade': 4.54},
    'V':  {'nome': 'Vanadio', 'numero_atomico': 23, 'massa_atomica': 50.942, 'raio_atomico': 171, 'estrutura_cristalina': 'cubica', 'eletronegatividade': 1.63, 'valencia': 5, 'atomos_celula': 2, 'densidade': 6.11},
    'Cr': {'nome': 'Cromo', 'numero_atomico': 24, 'massa_atomica': 51.996, 'raio_atomico': 166, 'estrutura_cristalina': 'cubica', 'eletronegatividade': 1.66, 'valencia': 6, 'atomos_celula': 2, 'densidade': 7.19},
    'Mn': {'nome': 'Manganes', 'numero_atomico': 25, 'massa_atomica': 54.938, 'raio_atomico': 161, 'estrutura_cristalina': 'cubica', 'eletronegatividade': 1.55, 'valencia': 7, 'atomos_celula': 2, 'densidade': 7.21},
    'Fe': {'nome': 'Ferro', 'numero_atomico': 26, 'massa_atomica': 55.845, 'raio_atomico': 156, 'estrutura_cristalina': 'cubica', 'eletronegatividade': 1.83, 'valencia': 2, 'atomos_celula': 2, 'densidade': 7.874},
    'Co': {'nome': 'Cobalto', 'numero_atomico': 27, 'massa_atomica': 58.933, 'raio_atomico': 152, 'estrutura_cristalina': 'hexagonal', 'eletronegatividade': 1.88, 'valencia': 2, 'atomos_celula': 2, 'densidade': 8.9},
    'Ni': {'nome': 'Niquel', 'numero_atomico': 28, 'massa_atomica': 58.693, 'raio_atomico': 149, 'estrutura_cristalina': 'cubica', 'eletronegatividade': 1.91, 'valencia': 2, 'atomos_celula': 4, 'densidade': 8.908},
    'Cu': {'nome': 'Cobre', 'numero_atomico': 29, 'massa_atomica': 63.546, 'raio_atomico': 145, 'estrutura_cristalina': 'cubica', 'eletronegatividade': 1.9, 'valencia': 1, 'atomos_celula': 4, 'densidade': 8.96},
    'Zn': {'nome': 'Zinco', 'numero_atomico': 30, 'massa_atomica': 65.38, 'raio_atomico': 134, 'estrutura_cristalina': 'hexagonal', 'eletronegatividade': 1.65, 'valencia': 2, 'atomos_celula': 2, 'densidade': 7.14},
    'Ga': {'nome': 'Galio', 'numero_atomico': 31, 'massa_atomica': 69.723, 'raio_atomico': 136, 'estrutura_cristalina': 'ortorrombica', 'eletronegatividade': 1.81, 'valencia': 3, 'atomos_celula': 4, 'densidade': 5.907},
    'Ge': {'nome': 'Germanio', 'numero_atomico': 32, 'massa_atomica': 72.63, 'raio_atomico': 125, 'estrutura_cristalina': 'cubica', 'eletronegatividade': 2.01, 'valencia': 4, 'atomos_celula': 4, 'densidade': 5.323},
    'As': {'nome': 'Arsenio', 'numero_atomico': 33, 'massa_atomica': 74.922, 'raio_atomico': 114, 'estrutura_cristalina': 'romboedrica', 'eletronegatividade': 2.18, 'valencia': 3, 'atomos_celula': 4, 'densidade': 5.776},
    'Se': {'nome': 'Selenio', 'numero_atomico': 34, 'massa_atomica': 78.971, 'raio_atomico': 103, 'estrutura_cristalina': 'hexagonal', 'eletronegatividade': 2.55, 'valencia': 2, 'atomos_celula': 3, 'densidade': 4.809},
    'Br': {'nome': 'Bromo', 'numero_atomico': 35, 'massa_atomica': 79.904, 'raio_atomico': 94, 'estrutura_cristalina': 'ortorrombica', 'eletronegatividade': 2.96, 'valencia': 1, 'atomos_celula': 2, 'densidade': 3.102},
    'Kr': {'nome': 'Criptonio', 'numero_atomico': 36, 'massa_atomica': 83.798, 'raio_atomico': 88, 'estrutura_cristalina': 'cubica', 'eletronegatividade': '', 'valencia': 0, 'atomos_celula': 4, 'densidade': 0.003733},
    'Rb': {'nome': 'Rubidio', 'numero_atomico': 37, 'massa_atomica': 85.468, 'raio_atomico': 265, 'estrutura_cristalina': 'cubica', 'eletronegatividade': 0.82, 'valencia': 1, 'atomos_celula': 2, 'densidade': 1.532},
    'Sr': {'nome': 'Estroncio', 'numero_atomico': 38, 'massa_atomica': 87.62, 'raio_atomico': 219, 'estrutura_cristalina': 'cubica', 'eletronegatividade': 0.95, 'valencia': 2, 'atomos_celula': 2, 'densidade': 2.64},
    'Y':  {'nome': 'Itrio', 'numero_atomico': 39, 'massa_atomica': 88.906, 'raio_atomico': 212, 'estrutura_cristalina': 'hexagonal', 'eletronegatividade': 1.22, 'valencia': 3, 'atomos_celula': 2, 'densidade': 4.469},
    'Zr': {'nome': 'Zirconio', 'numero_atomico': 40, 'massa_atomica': 91.224, 'raio_atomico': 206, 'estrutura_cristalina': 'hexagonal', 'eletronegatividade': 1.33, 'valencia': 4, 'atomos_celula': 2, 'densidade': 6.506},
    'Nb': {'nome': 'Niobio', 'numero_atomico': 41, 'massa_atomica': 92.906, 'raio_atomico': 198, 'estrutura_cristalina': 'cubica', 'eletronegatividade': 1.6, 'valencia': 5, 'atomos_celula': 2, 'densidade': 8.57},
    'Mo': {'nome': 'Molibdenio', 'numero_atomico': 42, 'massa_atomica': 95.95, 'raio_atomico': 190, 'estrutura_cristalina': 'cubica', 'eletronegatividade': 2.16, 'valencia': 6, 'atomos_celula': 2, 'densidade': 10.22},
    'Tc': {'nome': 'Tecnecio', 'numero_atomico': 43, 'massa_atomica': 98, 'raio_atomico': 183, 'estrutura_cristalina': 'hexagonal', 'eletronegatividade': 1.9, 'valencia': 7, 'atomos_celula': 2, 'densidade': 11.5},
    'Ru': {'nome': 'Rutenio', 'numero_atomico': 44, 'massa_atomica': 101.07, 'raio_atomico': 178, 'estrutura_cristalina': 'hexagonal', 'eletronegatividade': 2.2, 'valencia': 8, 'atomos_celula': 2, 'densidade': 12.37},
    'Rh': {'nome': 'Rodio', 'numero_atomico': 45, 'massa_atomica': 102.91, 'raio_atomico': 173, 'estrutura_cristalina': 'cubica', 'eletronegatividade': 2.28, 'valencia': 3, 'atomos_celula': 4, 'densidade': 12.41},
    'Pd': {'nome': 'Paladio', 'numero_atomico': 46, 'massa_atomica': 106.42, 'raio_atomico': 169, 'estrutura_cristalina': 'cubica', 'eletronegatividade': 2.2, 'valencia': 2, 'atomos_celula': 4, 'densidade': 12.02},
    'Ag': {'nome': 'Prata', 'numero_atomico': 47, 'massa_atomica': 107.87, 'raio_atomico': 165, 'estrutura_cristalina': 'cubica', 'eletronegatividade': 1.93, 'valencia': 1, 'atomos_celula': 4, 'densidade': 10.501},
    'Cd': {'nome': 'Cadmio', 'numero_atomico': 48, 'massa_atomica': 112.41, 'raio_atomico': 161, 'estrutura_cristalina': 'hexagonal', 'eletronegatividade': 1.69, 'valencia': 2, 'atomos_celula': 2, 'densidade': 8.69},
    'In': {'nome': 'Indio', 'numero_atomico': 49, 'massa_atomica': 114.82, 'raio_atomico': 156, 'estrutura_cristalina': 'tetragonal', 'eletronegatividade': 1.78, 'valencia': 3, 'atomos_celula': 4, 'densidade': 7.31},
    'Sn': {'nome': 'Estanho', 'numero_atomico': 50, 'massa_atomica': 118.71, 'raio_atomico': 145, 'estrutura_cristalina': 'tetragonal', 'eletronegatividade': 1.96, 'valencia': 4, 'atomos_celula': 2, 'densidade': 7.287},
    'Sb': {'nome': 'Antimonio', 'numero_atomico': 51, 'massa_atomica': 121.76, 'raio_atomico': 133, 'estrutura_cristalina': 'romboedrica', 'eletronegatividade': 2.05, 'valencia': 3, 'atomos_celula': 4, 'densidade': 6.685},
    'Te': {'nome': 'Telurio', 'numero_atomico': 52, 'massa_atomica': 127.6, 'raio_atomico': 123, 'estrutura_cristalina': 'hexagonal', 'eletronegatividade': 2.1, 'valencia': 2, 'atomos_celula': 2, 'densidade': 6.232},
    'I':  {'nome': 'Iodo', 'numero_atomico': 53, 'massa_atomica': 126.904, 'raio_atomico': 115, 'estrutura_cristalina': 'ortorrombica', 'eletronegatividade': 2.66, 'valencia': 1, 'atomos_celula': 4, 'densidade': 4.93},
    'Xe': {'nome': 'Xenonio', 'numero_atomico': 54, 'massa_atomica': 131.29, 'raio_atomico': 108, 'estrutura_cristalina': 'cubica', 'eletronegatividade': '', 'valencia': 0, 'atomos_celula': 4, 'densidade': 0.005887},
    'Cs': {'nome': 'Cesio', 'numero_atomico': 55, 'massa_atomica': 132.91, 'raio_atomico': 298, 'estrutura_cristalina': 'cubica', 'eletronegatividade': 0.79, 'valencia': 1, 'atomos_celula': 2, 'densidade': 1.873},
    'Ba': {'nome': 'Bario', 'numero_atomico': 56, 'massa_atomica': 137.33, 'raio_atomico': 253, 'estrutura_cristalina': 'cubica', 'eletronegatividade': 0.89, 'valencia': 2, 'atomos_celula': 2, 'densidade': 3.594},
    'La': {'nome': 'Lantanio', 'numero_atomico': 57, 'massa_atomica': 138.91, 'raio_atomico': 195, 'estrutura_cristalina': 'hexagonal', 'eletronegatividade': 1.1, 'valencia': 3, 'atomos_celula': 2, 'densidade': 6.145},
    'Ce': {'nome': 'Cerio', 'numero_atomico': 58, 'massa_atomica': 140.12, 'raio_atomico': 185, 'estrutura_cristalina': 'cubica', 'eletronegatividade': 1.12, 'valencia': 3, 'atomos_celula': 2, 'densidade': 6.77},
    'Pr': {'nome': 'Praseodimio', 'numero_atomico': 59, 'massa_atomica': 140.91, 'raio_atomico': 247, 'estrutura_cristalina': 'hexagonal', 'eletronegatividade': 1.13, 'valencia': 3, 'atomos_celula': 2, 'densidade': 6.77},
    'Nd': {'nome': 'Neodimio', 'numero_atomico': 60, 'massa_atomica': 144.24, 'raio_atomico': 206, 'estrutura_cristalina': 'hexagonal', 'eletronegatividade': 1.14, 'valencia': 3, 'atomos_celula': 2, 'densidade': 7.01},
    'Pm': {'nome': 'Promecio', 'numero_atomico': 61, 'massa_atomica': 145, 'raio_atomico': 205, 'estrutura_cristalina': 'hexagonal', 'eletronegatividade': 1.13, 'valencia': 3, 'atomos_celula': 2, 'densidade': 7.26},
    'Sm': {'nome': 'Samario', 'numero_atomico': 62, 'massa_atomica': 150.36, 'raio_atomico': 238, 'estrutura_cristalina': 'rhombohedral', 'eletronegatividade': 1.17, 'valencia': 3, 'atomos_celula': 2, 'densidade': 7.52},
    'Eu': {'nome': 'Europio', 'numero_atomico': 63, 'massa_atomica': 151.96, 'raio_atomico': 231, 'estrutura_cristalina': 'cubica', 'eletronegatividade': 1.2, 'valencia': 2, 'atomos_celula': 2, 'densidade': 5.24},
    'Gd': {'nome': 'Gadolinio', 'numero_atomico': 64, 'massa_atomica': 157.25, 'raio_atomico': 233, 'estrutura_cristalina': 'hexagonal', 'eletronegatividade': 1.2, 'valencia': 3, 'atomos_celula': 2, 'densidade': 7.90},
    'Tb': {'nome': 'Terbio', 'numero_atomico': 65, 'massa_atomica': 158.93, 'raio_atomico': 225, 'estrutura_cristalina': 'hexagonal', 'eletronegatividade': 1.1, 'valencia': 3, 'atomos_celula': 2, 'densidade': 8.23},
    'Dy': {'nome': 'Disprosio', 'numero_atomico': 66, 'massa_atomica': 162.50, 'raio_atomico': 228, 'estrutura_cristalina': 'hexagonal', 'eletronegatividade': 1.22, 'valencia': 3, 'atomos_celula': 2, 'densidade': 8.55},
    'Ho': {'nome': 'Holmio', 'numero_atomico': 67, 'massa_atomica': 164.93, 'raio_atomico': 226, 'estrutura_cristalina': 'hexagonal', 'eletronegatividade': 1.23, 'valencia': 3, 'atomos_celula': 2, 'densidade': 8.80},
    'Er': {'nome': 'erbio', 'numero_atomico': 68, 'massa_atomica': 167.26, 'raio_atomico': 226, 'estrutura_cristalina': 'hexagonal', 'eletronegatividade': 1.24, 'valencia': 3, 'atomos_celula': 2, 'densidade': 9.07},
    'Tm': {'nome': 'Tulio', 'numero_atomico': 69, 'massa_atomica': 168.93, 'raio_atomico': 222, 'estrutura_cristalina': 'hexagonal', 'eletronegatividade': 1.25, 'valencia': 2, 'atomos_celula': 2, 'densidade': 9.32},
    'Lu': {'nome': 'Lutecio', 'numero_atomico': 71, 'massa_atomica': 174.97, 'raio_atomico': 217, 'estrutura_cristalina': 'hexagonal', 'eletronegatividade': 1.27, 'valencia': 3, 'atomos_celula': 2, 'densidade': 9.841},
    'Hf': {'nome': 'Hafnio', 'numero_atomico': 72, 'massa_atomica': 178.49, 'raio_atomico': 208, 'estrutura_cristalina': 'hexagonal', 'eletronegatividade': 1.3, 'valencia': 4, 'atomos_celula': 2, 'densidade': 13.31},
    'Ta': {'nome': 'Tantalo', 'numero_atomico': 73, 'massa_atomica': 180.95, 'raio_atomico': 200, 'estrutura_cristalina': 'cubica', 'eletronegatividade': 1.5, 'valencia': 5, 'atomos_celula': 2, 'densidade': 16.654},
    'W':  {'nome': 'Tungstenio', 'numero_atomico': 74, 'massa_atomica': 183.84, 'raio_atomico': 193, 'estrutura_cristalina': 'cubica', 'eletronegatividade': 2.36, 'valencia': 6, 'atomos_celula': 2, 'densidade': 19.25},
    'Re': {'nome': 'Renio', 'numero_atomico': 75, 'massa_atomica': 186.21, 'raio_atomico': 188, 'estrutura_cristalina': 'hexagonal', 'eletronegatividade': 1.9, 'valencia': 7, 'atomos_celula': 2, 'densidade': 21.02},
    'Os': {'nome': 'osmio', 'numero_atomico': 76, 'massa_atomica': 190.23, 'raio_atomico': 185, 'estrutura_cristalina': 'hexagonal', 'eletronegatividade': 2.2, 'valencia': 8, 'atomos_celula': 2, 'densidade': 22.59},
    'Ir': {'nome': 'Iridio', 'numero_atomico': 77, 'massa_atomica': 192.22, 'raio_atomico': 180, 'estrutura_cristalina': 'cubica', 'eletronegatividade': 2.2, 'valencia': 3, 'atomos_celula': 4, 'densidade': 22.42},
    'Pt': {'nome': 'Platina', 'numero_atomico': 78, 'massa_atomica': 195.08, 'raio_atomico': 177, 'estrutura_cristalina': 'cubica', 'eletronegatividade': 2.28, 'valencia': 2, 'atomos_celula': 4, 'densidade': 21.45},
    'Au': {'nome': 'Ouro', 'numero_atomico': 79, 'massa_atomica': 196.97, 'raio_atomico': 174, 'estrutura_cristalina': 'cubica', 'eletronegatividade': 2.54, 'valencia': 3, 'atomos_celula': 4, 'densidade': 19.32},
    'Hg': {'nome': 'Mercurio', 'numero_atomico': 80, 'massa_atomica': 200.59, 'raio_atomico': 171, 'estrutura_cristalina': 'rhombohedral', 'eletronegatividade': 2.00, 'valencia': 2, 'atomos_celula': 2, 'densidade': 13.55},
    'Tl': {'nome': 'Talio', 'numero_atomico': 81, 'massa_atomica': 204.38, 'raio_atomico': 156, 'estrutura_cristalina': 'hexagonal', 'eletronegatividade': 2.04, 'valencia': 3, 'atomos_celula': 2, 'densidade': 11.85},
    'Pb': {'nome': 'Chumbo', 'numero_atomico': 82, 'massa_atomica': 207.2, 'raio_atomico': 154, 'estrutura_cristalina': 'cubica', 'eletronegatividade': 2.33, 'valencia': 4, 'atomos_celula': 4, 'densidade': 11.34},
    'Bi': {'nome': 'Bismuto', 'numero_atomico': 83, 'massa_atomica': 208.98, 'raio_atomico': 143, 'estrutura_cristalina': 'rhombohedral', 'eletronegatividade': 2.02, 'valencia': 3, 'atomos_celula': 2, 'densidade': 9.78},
    'Po': {'nome': 'Polonio', 'numero_atomico': 84, 'massa_atomica': 209, 'raio_atomico': 168, 'estrutura_cristalina': 'cubica', 'eletronegatividade': 2.0, 'valencia': 4, 'atomos_celula': 2, 'densidade': 9.32},
    'At': {'nome': 'Astato', 'numero_atomico': 85, 'massa_atomica': 210, 'raio_atomico': 145, 'estrutura_cristalina': '-', 'eletronegatividade': 2.2, 'valencia': 1, 'atomos_celula': '-', 'densidade': '-'},
    'Rn': {'nome': 'Radonio', 'numero_atomico': 86, 'massa_atomica': 222, 'raio_atomico': 120, 'estrutura_cristalina': '-', 'eletronegatividade': '-', 'valencia': 0, 'atomos_celula': '-', 'densidade': '-'},
    'Fr': {'nome': 'Francio', 'numero_atomico': 87, 'massa_atomica': 223, 'raio_atomico': '-', 'estrutura_cristalina': '-', 'eletronegatividade': 0.7, 'valencia': 1, 'atomos_celula': '-', 'densidade': '-'},
    'Ra': {'nome': 'Radio', 'numero_atomico': 88, 'massa_atomica': 226, 'raio_atomico': 215, 'estrutura_cristalina': 'cubica', 'eletronegatividade': 0.9, 'valencia': 2, 'atomos_celula': 2, 'densidade': 5.5},
    'Ac': {'nome': 'Actinio', 'numero_atomico': 89, 'massa_atomica': 227, 'raio_atomico': 195, 'estrutura_cristalina': 'cubica', 'eletronegatividade': 1.1, 'valencia': 3, 'atomos_celula': 2, 'densidade': 10.07},
    'Th': {'nome': 'Torio', 'numero_atomico': 90, 'massa_atomica': 232.04, 'raio_atomico': 179, 'estrutura_cristalina': 'cubica', 'eletronegatividade': 1.3, 'valencia': 4, 'atomos_celula': 2, 'densidade': 11.72},
    'Pa': {'nome': 'Protactinio', 'numero_atomico': 91, 'massa_atomica': 231.04, 'raio_atomico': 184, 'estrutura_cristalina': 'tetragonal', 'eletronegatividade': 1.5, 'valencia': 5, 'atomos_celula': 4, 'densidade': 15.37},
    'U':  {'nome': 'Uranio', 'numero_atomico': 92, 'massa_atomica': 238.03, 'raio_atomico': 138, 'estrutura_cristalina': 'ortorrombica', 'eletronegatividade': 1.38, 'valencia': 6, 'atomos_celula': 4, 'densidade': 19.1},
    'Np': {'nome': 'Neptunio', 'numero_atomico': 93, 'massa_atomica': 237, 'raio_atomico': 190, 'estrutura_cristalina': 'ortorrombica', 'eletronegatividade': 1.36, 'valencia': 5, 'atomos_celula': 4, 'densidade': 20.45},
    'Pu': {'nome': 'Plutonio', 'numero_atomico': 94, 'massa_atomica': 244, 'raio_atomico': 187, 'estrutura_cristalina': 'monoclinica', 'eletronegatividade': 1.28, 'valencia': 6, 'atomos_celula': 4, 'densidade': 19.84},
    'Am': {'nome': 'Americio', 'numero_atomico': 95, 'massa_atomica': 243, 'raio_atomico': 180, 'estrutura_cristalina': 'hexagonal', 'eletronegatividade': 1.3, 'valencia': 6, 'atomos_celula': 2, 'densidade': 13.69},
    'Cm': {'nome': 'Curio', 'numero_atomico': 96, 'massa_atomica': 247, 'raio_atomico': 174, 'estrutura_cristalina': 'hexagonal', 'eletronegatividade': 1.3, 'valencia': 3, 'atomos_celula': 2, 'densidade': 13.51},
    'Bk': {'nome': 'Berkelio', 'numero_atomico': 97, 'massa_atomica': 247, 'raio_atomico': 170, 'estrutura_cristalina': 'hexagonal', 'eletronegatividade': 1.3, 'valencia': 3, 'atomos_celula': 2, 'densidade': 14.79},
    'Cf': {'nome': 'Californio', 'numero_atomico': 98, 'massa_atomica': 251, 'raio_atomico': 186, 'estrutura_cristalina': 'hexagonal', 'eletronegatividade': 1.3, 'valencia': 3, 'atomos_celula': 2, 'densidade': 15.1},
    'Es': {'nome': 'Einstenio', 'numero_atomico': 99, 'massa_atomica': 252, 'raio_atomico': '-', 'estrutura_cristalina': '-', 'eletronegatividade': 1.3, 'valencia': 3, 'atomos_celula': '-', 'densidade': '-'},
    'Fm': {'nome': 'Fermio', 'numero_atomico': 100, 'massa_atomica': 257, 'raio_atomico': '-', 'estrutura_cristalina': '-', 'eletronegatividade': 1.3, 'valencia': 3, 'atomos_celula': '-', 'densidade': '-'},
    'Md': {'nome': 'Mendelevio', 'numero_atomico': 101, 'massa_atomica': 258, 'raio_atomico': '-', 'estrutura_cristalina': '-', 'eletronegatividade': 1.3, 'valencia': 3, 'atomos_celula': '-', 'densidade': '-'},
    'No': {'nome': 'Nobelio', 'numero_atomico': 102, 'massa_atomica': 259, 'raio_atomico': '-', 'estrutura_cristalina': '-', 'eletronegatividade': 1.3, 'valencia': 3, 'atomos_celula': '-', 'densidade': '-'},
    'Lr': {'nome': 'Laurencio', 'numero_atomico': 103, 'massa_atomica': 266, 'raio_atomico': '-', 'estrutura_cristalina': '-', 'eletronegatividade': 1.3, 'valencia': 3, 'atomos_celula': '-', 'densidade': '-'},
    'Rf': {'nome': 'Rutherfordio', 'numero_atomico': 104, 'massa_atomica': 267, 'raio_atomico': '-', 'estrutura_cristalina': '-', 'eletronegatividade': '-', 'valencia': 4, 'atomos_celula': '-', 'densidade': '-'},
    'Db': {'nome': 'Dubnio', 'numero_atomico': 105, 'massa_atomica': 270, 'raio_atomico': '-', 'estrutura_cristalina': '-', 'eletronegatividade': '-', 'valencia': 5, 'atomos_celula': '-', 'densidade': '-'},
    'Sg': {'nome': 'Seaborgio', 'numero_atomico': 106, 'massa_atomica': 271, 'raio_atomico': '-', 'estrutura_cristalina': '-', 'eletronegatividade': '-', 'valencia': 6, 'atomos_celula': '-', 'densidade': '-'},
    'Bh': {'nome': 'Bohrio', 'numero_atomico': 107, 'massa_atomica': 270, 'raio_atomico': '-', 'estrutura_cristalina': '-', 'eletronegatividade': '-', 'valencia': 7, 'atomos_celula': '-', 'densidade': '-'},
    'Hs': {'nome': 'Hassio', 'numero_atomico': 108, 'massa_atomica': 277, 'raio_atomico': '-', 'estrutura_cristalina': '-', 'eletronegatividade': '-', 'valencia': '-', 'atomos_celula': '-', 'densidade': '-'},
    'Mt': {'nome': 'Meitnerio', 'numero_atomico': 109, 'massa_atomica': 276, 'raio_atomico': '-', 'estrutura_cristalina': '-', 'eletronegatividade': '-', 'valencia': '-', 'atomos_celula': '-', 'densidade': '-'},
    'Ds': {'nome': 'Darmstadio', 'numero_atomico': 110, 'massa_atomica': 281, 'raio_atomico': '-', 'estrutura_cristalina': '-', 'eletronegatividade': '-', 'valencia': '-', 'atomos_celula': '-', 'densidade': '-'},
    'Rg': {'nome': 'Roentgenio', 'numero_atomico': 111, 'massa_atomica': 282, 'raio_atomico': '-', 'estrutura_cristalina': '-', 'eletronegatividade': '-', 'valencia': '-', 'atomos_celula': '-', 'densidade': '-'},
    'Cn': {'nome': 'Copernicio', 'numero_atomico': 112, 'massa_atomica': 285, 'raio_atomico': '-', 'estrutura_cristalina': '-', 'eletronegatividade': '-', 'valencia': '-', 'atomos_celula': '-', 'densidade': '-'},
    'Nh': {'nome': 'Nihonio', 'numero_atomico': 113, 'massa_atomica': 286, 'raio_atomico': '-', 'estrutura_cristalina': '-', 'eletronegatividade': '-', 'valencia': '-', 'atomos_celula': '-', 'densidade': '-'},
    'Fl': {'nome': 'Flerovio', 'numero_atomico': 114, 'massa_atomica': 289, 'raio_atomico': '-', 'estrutura_cristalina': '-', 'eletronegatividade': '-', 'valencia': '-', 'atomos_celula': '-', 'densidade': '-'},
    'Mc': {'nome': 'Moscovio', 'numero_atomico': 115, 'massa_atomica': 290, 'raio_atomico': '-', 'estrutura_cristalina': '-', 'eletronegatividade': '-', 'valencia': '-', 'atomos_celula': '-', 'densidade': '-'},
    'Lv': {'nome': 'Livermorio', 'numero_atomico': 116, 'massa_atomica': 293, 'raio_atomico': '-', 'estrutura_cristalina': '-', 'eletronegatividade': '-', 'valencia': '-', 'atomos_celula': '-', 'densidade': '-'},
    'Ts': {'nome': 'Tenessino', 'numero_atomico': 117, 'massa_atomica': 294, 'raio_atomico': '-', 'estrutura_cristalina': '-', 'eletronegatividade': '-', 'valencia': '-', 'atomos_celula': '-', 'densidade': '-'},
    'Og': {'nome': 'Oganesson', 'numero_atomico': 118, 'massa_atomica': 294, 'raio_atomico': '-', 'estrutura_cristalina': '-', 'eletronegatividade': '-', 'valencia': '-', 'atomos_celula': '-', 'densidade': '-'},
}

# elementos_2 = {
#     'H': {'Nome': 'Hidrogênio', 'Massa Atômica': 1.008, 'Densidade do Sólido (g/cm³)': None, 'Estrutura Cristalina': None, 'Ponto de Fusão (°C)': None},
#     'He': {'Nome': 'Hélio', 'Massa Atômica': 4.003, 'Densidade do Sólido (g/cm³)': None, 'Estrutura Cristalina': None, 'Ponto de Fusão (°C)': None},
#     'Li': {'Nome': 'Lítio', 'Massa Atômica': 6.941, 'Densidade do Sólido (g/cm³)': 0.533, 'Estrutura Cristalina': 'ccc', 'Ponto de Fusão (°C)': 180.6},
#     'Be': {'Nome': 'Berílio', 'Massa Atômica': 9.012, 'Densidade do Sólido (g/cm³)': 1.85, 'Estrutura Cristalina': 'hc', 'Ponto de Fusão (°C)': 1289},
#     "B": {"Nome": "Boro", "Massa Atômica": 10.81, "Densidade do Sólido (g/cm³)": 2.34, "Estrutura Cristalina": "rômbica", "Ponto de Fusão (°C)": 2075},
#     "C": {"Nome": "Carbono", "Massa Atômica": 12.01, "Densidade do Sólido (g/cm³)": 2.26, "Estrutura Cristalina": "hexagonal", "Ponto de Fusão (°C)": 3500},
#     "N": {"Nome": "Nitrogênio", "Massa Atômica": 14.01, "Densidade do Sólido (g/cm³)": 1.03, "Estrutura Cristalina": None, "Ponto de Fusão (°C)": -210},
#     'O': {'Nome': 'Oxigênio', 'Massa Atômica': None, "Densidade do Sólido (g/cm³)": None, "Estrutura Cristalina": 'cúbica de face centrada', 'Ponto de Fusão (°C)': 660.4},
#     '15': {'Nome': 'Fósforo', 'Massa Atômica': 30.97, 'Densidade do Sólido (g/cm³)': 1.82, 'Estrutura Cristalina': None, 'Ponto de Fusão (°C)': 44.1},
#     '16': {'Nome': 'Enxofre', 'Massa Atômica': 32.06, 'Densidade do Sólido (g/cm³)': 2.07, 'Estrutura Cristalina': None, 'Ponto de Fusão (°C)': 115.2},
#     '17': {'Nome': 'Cloro', 'Massa Atômica': 35.45, 'Densidade do Sólido (g/cm³)': 1.56, 'Estrutura Cristalina': None, 'Ponto de Fusão (°C)': -101},
#     "Ar": {"Nome": "Argônio", "Massa Atômica": 39.95, "Densidade do Sólido (g/cm³)": None, "Estrutura Cristalina": None, "Ponto de Fusão (°C)": -189},
#     "K": {"Nome": "Potássio", "Massa Atômica": 39.10, "Densidade do Sólido (g/cm³)": 0.86, "Estrutura Cristalina": "cúbica de corpo centrado", "Ponto de Fusão (°C)": 63.4},
#     "Ca": {"Nome": "Cálcio", "Massa Atômica": 40.08, "Densidade do Sólido (g/cm³)": 1.54, "Estrutura Cristalina": "cúbica de face centrada", "Ponto de Fusão (°C)": 842},
#     "Sc": {"Nome": "Escândio", "Massa Atômica": 44.96, "Densidade do Sólido (g/cm³)": 2.99, "Estrutura Cristalina": "hexagonal compacta", "Ponto de Fusão (°C)": 1541},
#     "Ti": {"Nome": "Titânio", "Massa Atômica": 47.87, "Densidade do Sólido (g/cm³)": 4.54, "Estrutura Cristalina": "hexagonal compacta", "Ponto de Fusão (°C)": 1668},
#     "V": {"Nome": "Vanádio", "Massa Atômica": 50.94, "Densidade do Sólido (g/cm³)": 6.11, "Estrutura Cristalina": "cúbica de corpo centrado", "Ponto de Fusão (°C)": 1910},
#     "Cr": {"Nome": "Cromo", "Massa Atômica": 52.00, "Densidade do Sólido (g/cm³)": 7.19, "Estrutura Cristalina": None, "Ponto de Fusão (°C)": 1907},
#     'Mn': {'Nome': 'Manganês', 'Massa Atômica': 54.94, 'Densidade do Sólido (g/cm³)': 7.21, 'Estrutura Cristalina': None, 'Ponto de Fusão (°C)': 1246},
#     'Fe': {'Nome': 'Ferro', 'Massa Atômica': 55.85, 'Densidade do Sólido (g/cm³)': 7.87, 'Estrutura Cristalina': None, 'Ponto de Fusão (°C)': 1538},
#     'Co': {'Nome': 'Cobalto', 'Massa Atômica': 58.93, 'Densidade do Sólido (g/cm³)': 8.90, 'Estrutura Cristalina': None, 'Ponto de Fusão (°C)': 1495},
#     'Ni': {'Nome': 'Níquel', 'Massa Atômica': 58.69, 'Densidade do Sólido (g/cm³)': 8.91, 'Estrutura Cristalina': None, 'Ponto de Fusão (°C)': 1453},
#     "Cu": {"Nome": "Cobre", "Massa Atômica": 63.55, "Densidade do Sólido (g/cm³)": 8.96, "Estrutura Cristalina": "cúbica de face centrada", "Ponto de Fusão (°C)": 1083},
#     "Zn": {"Nome": "Zinco", "Massa Atômica": 65.38, "Densidade do Sólido (g/cm³)": 7.14, "Estrutura Cristalina": None, "Ponto de Fusão (°C)": 419},
#     'Ga': {'Nome': 'Gálio', 'Massa Atômica': 69.72, 'Densidade do Sólido (g/cm³)': 5.91, 'Estrutura Cristalina': None, 'Ponto de Fusão (°C)': 30},
#     'Ge': {'Nome': 'Germânio', 'Massa Atômica': 72.63, 'Densidade do Sólido (g/cm³)': 5.32, 'Estrutura Cristalina': None, 'Ponto de Fusão (°C)': 937},
#     "As": {"Nome": "Arsênio", "Massa Atômica": 74.92, "Densidade do Sólido (g/cm³)": 5.73, "Estrutura Cristalina": None, "Ponto de Fusão (°C)": 817},
#     'Se': {'Nome': 'Selênio', 'Massa Atômica': 78.96, 'Densidade do Sólido (g/cm³)': 4.82, 'Estrutura Cristalina': None, 'Ponto de Fusão (°C)': 221},
#     "Br": {"Nome": "Bromo", "Massa Atômica": 79.90, "Densidade do Sólido (g/cm³)": 3.12, "Estrutura Cristalina": None, "Ponto de Fusão (°C)": -7.2},
#     'Kr': {'Nome': 'Criptônio', 'Massa Atômica': 83.80, 'Densidade do Sólido (g/cm³)': 0.00375, 'Estrutura Cristalina': None, 'Ponto de Fusão (°C)': -157},
#     "Rb": {"Nome": "Rubídio", "Massa Atômica": 85.47, "Densidade do Sólido (g/cm³)": 1.53, "Estrutura Cristalina": "cúbica de corpo centrado", "Ponto de Fusão (°C)": 39.3},
#     "Sr": {"Nome": "Estrôncio", "Massa Atômica": 87.62, "Densidade do Sólido (g/cm³)": 2.63, "Estrutura Cristalina": None, "Ponto de Fusão (°C)": 769},
#     'Y': {'Nome': 'Ítrio', 'Massa Atômica': 88.91, 'Densidade do Sólido (g/cm³)': 4.47, 'Estrutura Cristalina': None, 'Ponto de Fusão (°C)': 1526},
#     'Zr': {'Nome': 'Zircônio', 'Massa Atômica': 91.22, 'Densidade do Sólido (g/cm³)': 6.51, 'Estrutura Cristalina': None, 'Ponto de Fusão (°C)': 1855},
#     'Nb': {'Nome': 'Nióbio', 'Massa Atômica': 92.91, 'Densidade do Sólido (g/cm³)': 8.57, 'Estrutura Cristalina': None, 'Ponto de Fusão (°C)': 2477},
#     "Mo": {"Nome": "Molibdênio", "Massa Atômica": 95.94, "Densidade do Sólido (g/cm³)": 10.22, "Estrutura Cristalina": None, "Ponto de Fusão (°C)": 2623},
#     "Tc": {"Nome": "Tecnécio", "Massa Atômica": 98.91, "Densidade do Sólido (g/cm³)": 11.5, "Estrutura Cristalina": None, "Ponto de Fusão (°C)": 2157},
#     "Ru": {"Nome": "Rutênio", "Massa Atômica": 101.07, "Densidade do Sólido (g/cm³)": 12.41, "Estrutura Cristalina": None, "Ponto de Fusão (°C)": 2334},
#     "Rh": {"Nome": "Ródio", "Massa Atômica": 102.91, "Densidade do Sólido (g/cm³)": 12.41, "Estrutura Cristalina": None, "Ponto de Fusão (°C)": 1966},
#     "Pd": {"Nome": "Paládio", "Massa Atômica": 106.42, "Densidade do Sólido (g/cm³)": 12.02, "Estrutura Cristalina": None, "Ponto de Fusão (°C)": 1552},
#     "Ag": {"Nome": "Prata", "Massa Atômica": 107.87, "Densidade do Sólido (g/cm³)": 10.49, "Estrutura Cristalina": "cúbica de face centrada", "Ponto de Fusão (°C)": 961.8},
#     "Cd": {"Nome": "Cádmio", "Massa Atômica": 112.41, "Densidade do Sólido (g/cm³)": 8.65, "Estrutura Cristalina": None, "Ponto de Fusão (°C)": 321},
#     'In': {'Nome': 'Índio', 'Massa Atômica': 114.82, 'Densidade do Sólido (g/cm³)': 7.31, 'Estrutura Cristalina': None, 'Ponto de Fusão (°C)': 157},
#     'Sn': {'Nome': 'Estanho', 'Massa Atômica': 118.71, 'Densidade do Sólido (g/cm³)': 7.31, 'Estrutura Cristalina': None, 'Ponto de Fusão (°C)': 231.9},
#     'Sb': {'Nome': 'Antimônio', 'Massa Atômica': 121.76, 'Densidade do Sólido (g/cm³)': 6.69, 'Estrutura Cristalina': None, 'Ponto de Fusão (°C)': 630},
#     "Te": {"Nome": "Telúrio", "Massa Atômica": 127.60, "Densidade do Sólido (g/cm³)": 6.24, "Estrutura Cristalina": None, "Ponto de Fusão (°C)": 449.5},
#     "I": {"Nome": "Iodo", "Massa Atômica": 126.90, "Densidade do Sólido (g/cm³)": 4.93, "Estrutura Cristalina": None, "Ponto de Fusão (°C)": 113.7},
#     'Xe': {'Nome': 'Xenônio', 'Massa Atômica': 131.29, 'Densidade do Sólido (g/cm³)': None, 'Estrutura Cristalina': None, 'Ponto de Fusão (°C)': -111.8},
#     "Cs": {"Nome": "Césio", "Massa Atômica": 132.91, "Densidade do Sólido (g/cm³)": 1.93, "Estrutura Cristalina": "cúbica de face centrada", "Ponto de Fusão (°C)": 28.4},
#     "Ba": {"Nome": "Bário", "Massa Atômica": 137.33, "Densidade do Sólido (g/cm³)": 3.51, "Estrutura Cristalina": "cúbica de face centrada", "Ponto de Fusão (°C)": 727},
#     "La": {"Nome": "Lantânio", "Massa Atômica": 138.91, "Densidade do Sólido (g/cm³)": 6.15, "Estrutura Cristalina": None, "Ponto de Fusão (°C)": 920},
#     'Ce': {'Nome': 'Cério', 'Massa Atômica': 140.12, 'Densidade do Sólido (g/cm³)': 6.77, 'Estrutura Cristalina': 'cúbica de face centrada', 'Ponto de Fusão (°C)': 798},
#     'Pr': {'Nome': 'Praseodímio', 'Massa Atômica': 140.91, 'Densidade do Sólido (g/cm³)': 6.48, 'Estrutura Cristalina': None, 'Ponto de Fusão (°C)': 931},
#     'Nd': {'Nome': 'Neodímio', 'Massa Atômica': 144.24, 'Densidade do Sólido (g/cm³)': 7.01, 'Estrutura Cristalina': None, 'Ponto de Fusão (°C)': 1024},
#     "Pm": {"Nome": "Promécio", "Massa Atômica": 145, "Densidade do Sólido (g/cm³)": None, "Estrutura Cristalina": None, "Ponto de Fusão (°C)": 1042},
#     'Sm': {'Nome': 'Samário', 'Massa Atômica': 150.36, 'Densidade do Sólido (g/cm³)': 7.54, 'Estrutura Cristalina': 'romboédrica', 'Ponto de Fusão (°C)': 1072},
#     "Eu": {"Nome": "Európio", "Massa Atômica": 151.96, "Densidade do Sólido (g/cm³)": 5.25, "Estrutura Cristalina": "cúbica de face centrada", "Ponto de Fusão (°C)": 822},
#     'Gd': {'Nome': 'Gadolínio', 'Massa Atômica': 157.25, 'Densidade do Sólido (g/cm³)': 7.87, 'Estrutura Cristalina': 'hexagonal compacta', 'Ponto de Fusão (°C)': 1313},
#     'Tb': {'Nome': 'Térbio', 'Massa Atômica': 158.93, 'Densidade do Sólido (g/cm³)': 8.27, 'Estrutura Cristalina': 'hexagonal compacta', 'Ponto de Fusão (°C)': 1356},
#     "Dy": {"Nome": "Disprósio", "Massa Atômica": 162.50, "Densidade do Sólido (g/cm³)": 8.53, "Estrutura Cristalina": "hexagonal compacta", "Ponto de Fusão (°C)": 1412},
#     "Ho": {"Nome": "Hólmio", "Massa Atômica": 164.93, "Densidade do Sólido (g/cm³)": 8.80, "Estrutura Cristalina": None, "Ponto de Fusão (°C)": 1474},
#     'Er': {'Nome': 'Érbio', 'Massa Atômica': 167.26, 'Densidade do Sólido (g/cm³)': 9.04, 'Estrutura Cristalina': 'hexagonal compacta', 'Ponto de Fusão (°C)': 1529},
#     "Tm": {"Nome": "Túlio", "Massa Atômica": 168.93, "Densidade do Sólido (g/cm³)": 9.33, "Estrutura Cristalina": None, "Ponto de Fusão (°C)": 1545},
#     "Lu": {"Nome": "Lutécio", "Massa Atômica": 174.97, "Densidade do Sólido (g/cm³)": 9.84, "Estrutura Cristalina": "hexagonal compacta", "Ponto de Fusão (°C)": 1663},
#     'Hf': {'Nome': 'Háfnio', 'Massa Atômica': 178.49, 'Densidade do Sólido (g/cm³)': 13.28, 'Estrutura Cristalina': 'hexagonal compacta', 'Ponto de Fusão (°C)': 2233},
#     'Ta': {'Nome': 'Tântalo', 'Massa Atômica': 180.95, 'Densidade do Sólido (g/cm³)': 16.67, 'Estrutura Cristalina': 'cúbica de corpo centrado', 'Ponto de Fusão (°C)': 3017},
#     "W": {"Nome": "Tungstênio", "Massa Atômica": 183.85, "Densidade do Sólido (g/cm³)": 19.25, "Estrutura Cristalina": None, "Ponto de Fusão (°C)": 3422},
#     "Re": {"Nome": "Rênio", "Massa Atômica": 186.20, "Densidade do Sólido (g/cm³)": 21.02, "Estrutura Cristalina": None, "Ponto de Fusão (°C)": 3186},
#     'Os': {'Nome': 'Ósmio', 'Massa Atômica': 190.20, 'Densidade do Sólido (g/cm³)': 22.58, 'Estrutura Cristalina': 'hexagonal compacta', 'Ponto de Fusão (°C)': 3033},
#     "Ir": {"Nome": "Irídio", "Massa Atômica": 192.22, "Densidade do Sólido (g/cm³)": 22.55, "Estrutura Cristalina": "cúbica de face centrada", "Ponto de Fusão (°C)": 2447},
#     "Pt": {"Nome": "Platina", "Massa Atômica": 195.09, "Densidade do Sólido (g/cm³)": 21.44, "Estrutura Cristalina": None, "Ponto de Fusão (°C)": 1769},
#     'Au': {'Nome': 'Ouro', 'Massa Atômica': 196.97, 'Densidade do Sólido (g/cm³)': 19.28, 'Estrutura Cristalina': 'cúbica de face centrada', 'Ponto de Fusão (°C)': 1064},
#     'Hg': {'Nome': 'Mercúrio', 'Massa Atômica': 200.59, 'Densidade do Sólido (g/cm³)': None, 'Estrutura Cristalina': None, 'Ponto de Fusão (°C)': -39},
#     "Tl": {"Nome": "Tálio", "Massa Atômica": 204.37, "Densidade do Sólido (g/cm³)": 11.87, "Estrutura Cristalina": None, "Ponto de Fusão (°C)": 304},
#     "Pb": {"Nome": "Chumbo", "Massa Atômica": 207.20, "Densidade do Sólido (g/cm³)": 11.34, "Estrutura Cristalina": "cúbica de face centrada", "Ponto de Fusão (°C)": 327},
#     "Bi": {"Nome": "Bismuto", "Massa Atômica": 208.98, "Densidade do Sólido (g/cm³)": 9.80, "Estrutura Cristalina": None, "Ponto de Fusão (°C)": 271},
#     "Po": {"Nome": "Polônio", "Massa Atômica": 209, "Densidade do Sólido (g/cm³)": 9.2, "Estrutura Cristalina": "cúbica de face centrada", "Ponto de Fusão (°C)": 254},
#     "At": {"Nome": "Ástato", "Massa Atômica": 210, "Densidade do Sólido (g/cm³)": None, "Estrutura Cristalina": None, "Ponto de Fusão (°C)": 302},
#     "Rn": {"Nome": "Radônio", "Massa Atômica": 222, "Densidade do Sólido (g/cm³)": None, "Estrutura Cristalina": None, "Ponto de Fusão (°C)": -71},
#     'Fr': {'Nome': 'Frâncio', 'Massa Atômica': 223, 'Densidade do Sólido (g/cm³)': None, 'Estrutura Cristalina': 'cúbica de corpo centrado', 'Ponto de Fusão (°C)': 27},
#     'Ra': {'Nome': 'Rádio', 'Massa Atômica': 226.03, 'Densidade do Sólido (g/cm³)': 5.0, 'Estrutura Cristalina': 'cúbica de face centrada', 'Ponto de Fusão (°C)': 700},
#     "Ac": {"Nome": "Actínio", "Massa Atômica": 227.03, "Densidade do Sólido (g/cm³)": 10.07, "Estrutura Cristalina": "cúbica de face centrada", "Ponto de Fusão (°C)": 1050},
#     "Th": {"Nome": "Tório", "Massa Atômica": 232.04, "Densidade do Sólido (g/cm³)": 11.72, "Estrutura Cristalina": None, "Ponto de Fusão (°C)": 1750},
#     "Pa": {"Nome": "Protactínio", "Massa Atômica": 231.04, "Densidade do Sólido (g/cm³)": 15.37, "Estrutura Cristalina": "cúbica de corpo centrado", "Ponto de Fusão (°C)": 1572},
#     "U": {"Nome": "Urânio", "Massa Atômica": 238.03, "Densidade do Sólido (g/cm³)": 19.05, "Estrutura Cristalina": None, "Ponto de Fusão (°C)": 1132},
#     "Np": {"Nome": "Neptúnio", "Massa Atômica": 237.05, "Densidade do Sólido (g/cm³)": 20.45, "Estrutura Cristalina": None, "Ponto de Fusão (°C)": 644},
#     'Pu': {'Nome': 'Plutônio', 'Massa Atômica': 244, 'Densidade do Sólido (g/cm³)': None, 'Estrutura Cristalina': None, 'Ponto de Fusão (°C)': 640},
#     'Am': {'Nome': 'Amerício', 'Massa Atômica': 243, 'Densidade do Sólido (g/cm³)': None, 'Estrutura Cristalina': None, 'Ponto de Fusão (°C)': 994},
#     'Cm': {'Nome': 'Cúrio', 'Massa Atômica': 247, 'Densidade do Sólido (g/cm³)': None, 'Estrutura Cristalina': None, 'Ponto de Fusão (°C)': 1340},
#     'Bk': {'Nome': 'Berquélio', 'Massa Atômica': 247, 'Densidade do Sólido (g/cm³)': None, 'Estrutura Cristalina': None, 'Ponto de Fusão (°C)': 986},    
#     "Cf": {"Nome": "Califórnio", "Massa Atômica": 251, "Densidade do Sólido (g/cm³)": None, "Estrutura Cristalina": None, "Ponto de Fusão (°C)": 900},
#     'Es': {'Nome': 'Einstênio', 'Massa Atômica': 252, 'Densidade do Sólido (g/cm³)': None, 'Estrutura Cristalina': None, 'Ponto de Fusão (°C)': 860},
#     'Fm': {'Nome': 'Férmio', 'Massa Atômica': 257, 'Densidade do Sólido (g/cm³)': None, 'Estrutura Cristalina': None, 'Ponto de Fusão (°C)': 1527},
#     'Md': {'Nome': 'Mendelévio', 'Massa Atômica': 258, 'Densidade do Sólido (g/cm³)': None, 'Estrutura Cristalina': None, 'Ponto de Fusão (°C)': 827},
#     "No": {"Nome": "Nobélio", "Massa Atômica": 259, "Densidade do Sólido (g/cm³)": None, "Estrutura Cristalina": None, "Ponto de Fusão (°C)": 827},
#     "Lr": {"Nome": "Laurêncio", "Massa Atômica": 262.11 , "Densidade do Sólido (g/cm³)": 15.6 , "Estrutura Cristalina":"hexagonal", "Ponto de Fusão (°C)": 1627},
#     "Rf": {"Nome": "Rutherfórdio", "Massa Atômica": 267, "Densidade do Sólido (g/cm³)": None, "Estrutura Cristalina": None, "Ponto de Fusão (°C)": 2100},    
#     "Db": {"Nome": "Dúbnio", "Massa Atômica": 270, "Densidade do Sólido (g/cm³)": None, "Estrutura Cristalina": None, "Ponto de Fusão (°C)": None},
#     "Sg": {"Nome": "Seabórgio", "Massa Atômica": 271, "Densidade do Sólido (g/cm³)": None, "Estrutura Cristalina": None, "Ponto de Fusão (°C)": None},
#     "Bh": {"Nome": "Bóhrio", "Massa Atômica": 270, "Densidade do Sólido (g/cm³)": None, "Estrutura Cristalina": None, "Ponto de Fusão (°C)": None},
#     'Hs': {'Nome': 'Hássio', 'Massa Atômica': 277, 'Densidade do Sólido (g/cm³)': None, 'Estrutura Cristalina': None, 'Ponto de Fusão (°C)': None},
#     'Mt': {'Nome': 'Meitnério', 'Massa Atômica': 278, 'Densidade do Sólido (g/cm³)': None, 'Estrutura Cristalina': None, 'Ponto de Fusão (°C)': None},
#     'Ds': {'Nome': 'Darmstádio', 'Massa Atômica': 281.16 , 'Densidade do Sólido (g/cm³)': 34.8 , 'Estrutura Cristalina':"hexagonal", 'Ponto de Fusão (°C)': None},
#     'Rg': {'Nome': 'Roentgênio', 'Massa Atômica': 282, 'Densidade do Sólido (g/cm³)': None, 'Estrutura Cristalina': None, 'Ponto de Fusão (°C)': None},
#     "Cn": {"Nome": "Copernício", "Massa Atômica": 285, "Densidade do Sólido (g/cm³)": None, "Estrutura Cristalina": None, "Ponto de Fusão (°C)": None},
#     "Fl": {"Nome": "Fleróvio", "Massa Atômica": 289, "Densidade do Sólido (g/cm³)": None, "Estrutura Cristalina": None, "Ponto de Fusão (°C)": None},
#     "Mc": {"Nome": "Moscóvio", "Massa Atômica": 288, "Densidade do Sólido (g/cm³)": None, "Estrutura Cristalina": None, "Ponto de Fusão (°C)": None},
#     'Lv': {'Nome': 'Livermório', 'Massa Atômica': 293, 'Densidade do Sólido (g/cm³)': None, 'Estrutura Cristalina': None, 'Ponto de Fusão (°C)': None},
#     'Ts': {'Nome': 'Tennesso', 'Massa Atômica': 294, 'Densidade do Sólido (g/cm³)': None, 'Estrutura Cristalina': None, 'Ponto de Fusão (°C)': None},
#     "Og": {"Nome": "Oganessônio", "Massa Atômica": 294, "Densidade do Sólido (g/cm³)": None, "Estrutura Cristalina": None, "Ponto de Fusão (°C)": None},
# }        

resistividade_ohmXm = [
    {"H": 1.0e8},
    {"He": 1.0e-8},
    {"Li": 9.28e-9},
    {"Be": 4.0e-7},
    {"B": 1.0e6},
    {"C": 3.5e5},
    {"N": 1.7e8},
    {"O": 2.2e5},
    {"F": 1.5e22},
    {"Ne": 1.2e-8},
    {"Na": 4.9e-8},
    {"Mg": 4.45e-8},
    {"Al": 2.65e-8},
    {"Si": 6.4e2},
    {"P": 1.0e3},
    {"S": 2.0e16},
    {"Cl": 2.3e16},
    {"Ar": None}, # Argônio é um gás nobre e não possui resistividade
    {"K": 7.17e-8}, 
    {'Ca': None}, # Cálcio é um metal alcalino terroso e não possui resistividade
	{"Sc" : None}, # Escândio é um metal de transição e não possui valor conhecido de resistividade
	{"Ti" : None}, # Titânio é um metal de transição e não possui valor conhecido de resistividade
	{"V" : None}, # Vanádio é um metal de transição e não possui valor conhecido de resistividade
	{"Cr" : None}, # Cromo é um metal de transição e não possui valor conhecido de resistividade
	{"Mn" : None}, # Manganês é um metal de transição e não possui valor conhecido de resistividade
	{"Fe" : 1.0e-7},
	{"Co" : 6.0e-8},
    {"Ni": 6.84e-8},
    {"Cu": 1.68e-8},
    {"Zn": 5.9e-8},
    {"Ga": 4.52e-8},
    {"Ge": 4.6e2},
    {"As": 4.7e-7},
    {"Se": 1.0e6},
    {"Br": None}, # Bromo é um halogênio líquido e não possui valor conhecido de resistividade
	{"Kr" : None}, # Criptônio é um gás nobre e não possui valor conhecido de resistividade
	{"Rb" : 1.2e-7}, 
	{"Sr" : None}, # Estrôncio é um metal alcalino terroso e não possui valor conhecido de resistividade
	{"Y" : None}, # Ítrio é um metal de transição e não possui valor conhecido de resistividade
	{"Zr" : None}, # Zircônio é um metal de transição e não possui valor conhecido de resistividade
	{"Nb" : None}, # Nióbio é um metal de transição e não possui valor conhecido de resistividade
	{"Mo" : None}, # Molibdênio é um metal de transição e não possui valor conhecido de resistividade
	{"Tc" : None}, # Tecnécio é um elemento sintético e não possui valor conhecido de resistividade
	{"Ru" : 7.0e-8},
	{"Rh" : 4.5e-8},
	{"Pd" : 1.05e-7},
	{"Ag" : 1.59e-8},
	{"Cd" : 6.9e-8},
	{"In" : 8.37e-8},
	{"Sn" : 1.09e-7},
	{"Sb" : 3.7e-7},     
    {"Te": 4.5e6},
    {"I": 1.0e23},
    {"Xe": None}, # Xenônio é um gás nobre e não possui valor conhecido de resistividade
    {"Cs": 2.09e-7},
    {"Ba": None}, # Bário é um metal alcalino terroso e não possui valor conhecido de resistividade
    {"La": None}, # Lantânio é um lantanídeo e não possui valor conhecido de resistividade
    {"Ce": None}, # Cério é um lantanídeo e não possui valor conhecido de resistividade
    {"Pr": None}, # Praseodímio é um lantanídeo e não possui valor conhecido de resistividade
    {"Nd": None}, # Neodímio é um lantanídeo e não possui valor conhecido de resistividade
    {"Pm": None}, # Promécio é um elemento sintético e não possui valor conhecido de resistividade
    {"Sm": None}, # Samário é um lantanídeo e não possui valor conhecido de resistividade
    {"Eu": None}, # Európio é um lantanídeo e não possui valor conhecido de resistividade
    {"Gd": None}, # Gadolínio é um lantanídeo e não possui valor conhecido de resistividade
    {"Tb": None}, # Térbio é um lantanídeo e não possui valor conhecido de resistividade
    {"Dy": None}, # Disprósio é um lantanídeo e não possui valor conhecido de resistividade
    {"Ho": None}, # Hólmio é um lantanídeo e não possui valor conhecido de resistividade
    {"Er": None}, # Erbium é um lantanídeo e não possui valor conhecido de resistividade
    {"Tm": None}, # Túlio é um lantanídeo e não possui valor conhecido de resistividade
    {"Yb": 5.0e-8},
    {"Lu": 6.7e-8},
    {"Hf": 4.2e-7},
    {"Ta": 1.3e-7},
    {"W": 5.6e-8},
    {"Re": 1.3e-6},
    {"Os": 8.2e-8},
    {"Ir": 5.0e-8},
    {"Pt": 1.06e-7},
    {"Au": 2.35e-8},
    {"Hg": 9.6e-7},
    {"Tl": 4.2e-7},
    {"Pb": 2.1e-7},
    {"Bi": 1.3e-6},
    {"Po": None}, # Polônio é um elemento radioativo e não possui valor conhecido de resistividade
    {"At": None}, # Astato é um elemento radioativo e não possui valor conhecido de resistividade
    {"Rn": None}, # Radônio é um gás nobre e não possui valor conhecido de resistividade
    {"Fr": None}, # Frâncio é um metal alcalino e não possui valor conhecido de resistividade
    {"Ra": None}, # Rádio é um metal alcalino terroso e não possui valor conhecido de resistividade
    {"Ac": None}, # Actínio é um actinídeo e não possui valor conhecido de resistividade
    {"Th": None}, # Tório é um actinídeo e não possui valor conhecido de resistividade
    {"Pa": None}, # Protactínio é um actinídeo e não possui valor conhecido de resistividade
    {"U": None}, # Urânio é um actinídeo e não possui valor conhecido de resistividade
    {"Np": None}, # Netúnio é um actinídeo e não possui valor conhecido de resistividade
    {"Pu": None}, # Plutônio é um elemento radioativo e não possui valor conhecido de resistividade
    {"Am": None}, # Amerício é um elemento radioativo e não possui valor conhecido de resistividade        
    {"Cm": None}, # Cúrio é um actinídeo e não possui valor conhecido de resistividade
    {"Bk": None}, # Berquélio é um actinídeo e não possui valor conhecido de resistividade
    {"Cf": None}, # Califórnio é um actinídeo e não possui valor conhecido de resistividade
    {"Es": None}, # Einstênio é um actinídeo e não possui valor conhecido de resistividade
    {"Fm": None}, # Férmio é um actinídeo e não possui valor conhecido de resistividade
    {"Md": None}, # Mendelévio é um elemento sintético e não possui valor conhecido de resistividade
    {"No": None}, # Nobélio é um elemento sintético e não possui valor conhecido de resistividade
    {"Lr": None}, # Laurêncio é um elemento sintético e não possui valor conhecido de resistividade
    {"Rf": None}, # Rutherfórdio é um elemento sintético e não possui valor conhecido de resistividade
    {"Db": None}, # Dúbnio é um elemento sintético e não possui valor conhecido de resistividade
    {"Sg": None}, # Seabórgio é um elemento sintético e não possui valor conhecido de resistividade
    {"Bh": None}, # Bohrío é um elemento sintético e não possui valor conhecido de resistividade
    {"Hs": None}, # Hássio é um elemento sintético e não possui valor conhecido de resistividade
    {"Mt": None}, # Meitnério é um elemento sintético e não possui valor conhecido de resistividade
    {"Ds": None}, # Darmstádio é um elemento sintético e não possui valor conhecido de resistividade
    {"Rg": None}, # Roentgênio é um elemento sintético e não possui valor conhecido de resistividade      
]  

def elemento(chave):
    # Converte a chave para a primeira letra maiuscula e o restante minuscula
    #chave_formatada = chave.capitalize()
    chave_formatada = tools.ajustar_simbolo(chave)
    
    # Procura pelo simbolo diretamente
    if chave_formatada in ELEMENT_DATA:
        return ELEMENT_DATA[chave_formatada]

    # Procura pelo nome
    for simbolo, dados in ELEMENT_DATA.items():
        if dados['nome'].lower() == chave.lower():
            return ELEMENT_DATA[simbolo]

    # Se não encontrou, retorna None
    return None



# i = 0
# for chave in ELEMENT_DATA:
#     print(chave, ELEMENT_DATA[chave]['nome'])
#     i += 1
#     if i == 5:
#         X = input('Pressione enter para continuar')
#         i = 0
