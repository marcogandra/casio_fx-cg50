import tools
import e_eleme as elemento
import h_coord as coordena
import i_qu_ten as queda_tensao
import l_cal_el as calcular_qtd_eletrons_por_segundo_secao_transversal
import j_p_c_io as calcular_carater_ionico
import f_HumeRo as regra_de_hume_robinson


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
        # Elétrons passam por segundo por uma seção transversal
        print("8-N. El. passam")
        print("1: Sair | 2: > ")

    def opcoes_pag2(self):
        tools.cls()
        print("9-cal.car.ionico")
        print("10-Regra de Hume Robinson")
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
            elif self.opcao == 8:
                calcular_qtd_eletrons_por_segundo_secao_transversal.tela()
            elif self.opcao == 9:
                calcular_carater_ionico.tela()
            elif self.opcao == 10:
                regra_de_hume_robinson.hume_rothery()


menu = Menu()
menu.show()
