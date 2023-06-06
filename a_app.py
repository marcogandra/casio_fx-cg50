import tools
import e_eleme as elemento
import h_coord as coordena
import i_qu_ten as queda_tensao


class Menu():
    def __init__(self):
        tools.system()
        self.opcao = 0
        self.pagina = 1

    def opcoes_pag1(self):
        tools.cls()
        print("4-Elemento")
        print("5-N.Coord.|QTD.Atm.")
        print("6-Coord. Elemento")
        print("7-Queda de Tensão")
        print("8-Elemento")
        print("1: Sair | 2: > ")

    def opcoes_pag2(self):
        tools.cls()
        print("9-Elemento")
        print("10-Elemento")
        print("11-Elemento")
        print("12-Elemento")
        print("012345678901234567890123456789")
        print("1: S | 3: <")

    def show(self):
        while True:
            if self.pagina == 1:
                self.opcoes_pag1()
            elif self.pagina == 2:
                self.opcoes_pag2()

            try:

                self.opcao = int(input("Opcao: "))

            except:
                pass

            if self.opcao == 2 and self.pagina < 2:
                self.pagina += 1
            elif self.opcao == 3 and self.pagina > 1:
                self.pagina -= 1
            elif self.opcao == 1:
                tools.cls()
                print("Fim do programa")
                break
# *****************************************
            elif self.opcao == 4:
                elemento.dados_em_tela()
            elif self.opcao == 5:
                coordena.dados_em_tela()
            elif self.opcao == 6:
                coordena.imprimir_estrutura_por_elemento()
            elif self.opcao == 7:
                queda_tensao.tela()


menu = Menu()
menu.show()
