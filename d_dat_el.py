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
