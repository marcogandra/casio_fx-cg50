import d_dat_el as elemento
import h_coord as estrutura

def estrutura_cristalina(indice):
    return "Estrutura "+indice

def hume_rothery()
    while True:
        print("Informe ou  3 <")
        elemento_1 = input("1. elemento: ")
        elemento_2 = input("2. elemento: ")
        
        if elemento_quimico == "3":
            break
        nome_elemento_1 = "El1"
        nome_elemento_2 = "El2"
        simbolo_1 = "S1"
        simbolo_2 = "S2"
        
        
        # # Diferença de tamanho dos atomos
        # size_difference = abs(element1["radius"] - element2["radius"]) / max(element1["radius"], element2["radius"]) * 100

        # # Estrutura cristalina
        # same_crystal_structure = element1["crystal_structure"] == element2["crystal_structure"]

        # # Eletronegatividade
        # electronegativity_difference = abs(element1["electronegativity"] - element2["electronegativity"])

        # # Valencia
        # same_valency = element1["valency"] == element2["valency"]
        
        raio_atomico_1 = 1
        raio_atomico_2 = 2        
        
        print("Vl novo, ok ou  3 <")
        print("Elemento : "+simbolo_1+" | "+simbolo_2)
        print("Raio aomico: "+raio_atomico_1+" | "+raio_atomico_2)
        
        r1 = input("1. raio: ")
        
        if r1 == "3":
            break
        elif r1 == "ok":
            pass
        else:
            raio_atomico_1 = r1
        
        r2 = input("2. raio: ")
        
        if r2 == "3":
            break
        elif r2 == "ok":
            pass
        else:
            raio_atomico_2 = r2     
            
        print("Est cristalina: ")
        print("1: "+estrutura_cristalina_1)
        print("2: "+estrutura_cristalina_2)   
        est1 = input("1 - indice:")
        est2 = input("2 - indice:")
        
        if est1 == "3":
            break
        elif est1 == "ok":
            pass
        else:
            estrutura_cristalina_1 = estrutura_cristalina(est1)
            
            
        


        
        estrutura_cristalina_1 = "Estrutura 1"
        estrutura_cristalina_2 = "Estrutura 2"
        
        eletronegatividade_1 = 1
        eletronegatividade_2 = 2
        
        valencia_1 = 1
        valencia_2 = 2
        
        dados = [[    
                    "Comparação entre "+nome_elemento_1+" | "+nome_elemento_1+",
                    "Raio antomico:"+raio_atomico_1+" | "+raio_atomico_2,
                    "Estrutura cristalina:"+estrutura_cristalina_1+" | "+estrutura_cristalina_2,
                    "Eletronegatividade:"+eletronegatividade_1+" | "+eletronegatividade_2,
                    "Valencia:"+valencia_1+" | "+valencia_2,
                    "-"*50,
        ]]
                
    # Imprimir relatorio
    print()
    print("===============================================")
    print(f"Elemento: {element1['name']} | Raio atômico: {element1['radius']} | Estrutura Cristalina : {element1['crystal_structure']} | Eletronegatividade: {element1['electronegativity']} | Valencia: {element1['valency']}")
    print(f"Elemento: {element2['name']} | Raio atômico: {element2['radius']} | Estrutura Cristalina : {element2['crystal_structure']} | Eletronegatividade: {element2['electronegativity']} | Valencia: {element2['valency']}")    
    print("===============================================")
    print("1. Diferença de tamanho dos atomos: A diferença no raio atômico entre os dois elementos deve ser inferior a 15%.")
    print(f"1. Diferença de tamanho dos atomos: {size_difference:.2f}%")
    print("===============================================")
    print("2. Estrutura cristalina: Os dois elementos devem possuir a mesma estrutura cristalina.")    
    print(f"2. Estrutura cristalina: {'mesma' if same_crystal_structure else 'diferente'}")
    print("===============================================")   
    print("3. Eletronegatividade: Os dois elementos devem ter eletronegatividades semelhantes.") 
    print(f"3. Diferença de eletronegatividade: {electronegativity_difference:.2f}")
    print("===============================================")   
    print("4. Valencia: Os dois elementos devem ter valencias semelhantes.")
    print(f"4. Valencia: {'mesma' if same_valency else 'diferente'}")    