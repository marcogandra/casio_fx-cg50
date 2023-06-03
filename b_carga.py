def carca(simbolo):
    valencia = {
    'H': 1, 'He': 0, 'Li': 1, 'Be': 2, 'B': 3, 'C': 4, 'N': 5, 'O': 6, 'F': 7, 'Ne': 0,
    'Na': 1, 'Mg': 2, 'Al': 3, 'Si': 4, 'P': 5, 'S': 6, 'Cl': 7, 'Ar': 0, 'K': 1, 'Ca': 2,
    'Sc': 3, 'Ti': 4, 'V': 5, 'Cr': 6, 'Mn': 7, 'Fe': 6, 'Co': 7, 'Ni': 6, 'Cu': 1, 'Zn': 2,
    'Ga': 3, 'Ge': 4, 'As': 5, 'Se': 6, 'Br': 7, 'Kr': 0, 'Rb': 1, 'Sr': 2, 'Y': 3, 'Zr': 4,
    'Nb': 5, 'Mo': 6, 'Tc': 7, 'Ru': 8, 'Rh': 1, 'Pd': 2, 'Ag': 1, 'Cd': 2, 'In': 3, 'Sn': 4,
    'Sb': 5, 'Te': 6, 'I': 7, 'Xe': 0, 'Cs': 1, 'Ba': 2, 'La': 3, 'Ce': 4, 'Pr': 5, 'Nd': 6,
    'Pm': 7, 'Sm': 2, 'Eu': 3, 'Gd': 4, 'Tb': 5, 'Dy': 6, 'Ho': 7, 'Er': 2, 'Tm': 3, 'Yb': 4,
    'Lu': 5, 'Hf': 6, 'Ta': 7, 'W': 6, 'Re': 7, 'Os': 8, 'Ir': 1, 'Pt': 2, 'Au': 1, 'Hg': 2,
    'Tl': 3, 'Pb': 4, 'Bi': 5, 'Th': 4, 'Pa': 5, 'U': 6, 'Np': 7, 'Pu': 8, 'Am': 3, 'Cm': 4,
    'Bk': 5, 'Cf': 6, 'Es': 7, 'Fm': 8, 'Md': 3, 'No': 4, 'Lr': 5, 'Rf': 6, 'Db': 7,
    'Sg': 8, 'Bh': 3, 'Hs': 4, 'Mt': 5, 'Ds': 6, 'Rg': 7, 'Cn': 8, 'Nh': 3, 'Fl': 4,
    'Mc': 5, 'Lv': 6, 'Ts': 7, 'Og': 8, 'Po': 6, 'At': 7, 'Rn': 0, 'Fr': 1, 'Ra': 2, 'Ac': 3, }
    return valencia[simbolo]

#print(carca('H'))
