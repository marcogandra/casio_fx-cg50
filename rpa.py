import pyautogui as pg
import time
import os
import ctypes
from ctypes import wintypes

exceto = ["boot.py", "rpa.py", "teste.py",]


def toggle_caps_lock():
    # Define necessary constants
    VK_CAPITAL = 0x14
    KEYEVENTF_KEYUP = 0x02
    KEYEVENTF_EXTENDEDKEY = 0x01

    # Create a generic KEYBDINPUT structure
    KEYBDINPUT = ctypes.c_ulong*6
    ki = KEYBDINPUT(0, 0, 0, 0, 0, 0)

    # Fill in the necessary fields
    ki[0] = VK_CAPITAL
    ki[1] = 0  # scancode
    ki[2] = KEYEVENTF_EXTENDEDKEY
    ki[4] = 0  # dwExtraInfo

    # Check if Caps Lock is already on
    if ctypes.windll.user32.GetKeyState(VK_CAPITAL):
        # If it is, we need to send two key events: a key down and a key up
        ki[2] = 0  # key down
        ctypes.windll.user32.keybd_event(*ki)
        ki[2] = KEYEVENTF_KEYUP  # key up
        ctypes.windll.user32.keybd_event(*ki)


# Lista para armazenar os arquivos Python encontrados
# arquivos_py = []


def gerar_arquivos_py():
    # Percorre todos os diretorios e subdiretorios a partir do diretorio atual
    arquivos_py = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            # Verifica se o arquivo e um arquivo Python e não esta na lista de arquivos a serem ignorados
            if file.endswith('.py') and file not in exceto:
                # Adiciona o arquivo à lista de arquivos Python
                arquivos_py.append(os.path.join(file))
    return arquivos_py


def copiar(arquivos_py):
    # for i in range(5):
    #     pg.click("exit.png")
    #     time.sleep(0.1)

    # time.sleep(1)

    # if pg.locateOnScreen("python2.png") == None and pg.locateOnScreen("python.png") == None and pg.locateOnScreen("matriz.png") == None and pg.locateOnScreen("grafico.png") == None:
    #     pg.click("menu.png")
    #     time.sleep(1)
    inicio()

    time.sleep(2)
    for i in range(5):
        pg.press("F")
        time.sleep(0.2)
    pg.press("F3")
    time.sleep(1)
    pg.press("F1")
    time.sleep(1)
    pg.typewrite("D:\\Arquivos\\FUMEC\\7-2023-1\\Calculadora\\")
    time.sleep(1)
    pg.press("enter")
    time.sleep(1)

    # arquivos_py = gerar_arquivos_py()

    for arquivo in arquivos_py:
        pg.typewrite('"'+arquivo+'"')
        time.sleep(0.1)
        pg.typewrite(" ")

    time.sleep(1)
    pg.press("enter")
    time.sleep(1)
    pg.press("F1")
    time.sleep(1)

    for i in range(len(arquivos_py)):
        pg.press("F6")
        time.sleep(2)

    pg.click("exit.png")
    time.sleep(1)
    pg.click("menu.png")
    time.sleep(1)


def inicio():
    toggle_caps_lock()
    pg.click("casio.png")

    if pg.locateOnScreen("python2.png") == None and pg.locateOnScreen("python.png") == None and pg.locateOnScreen("matriz.png") == None and pg.locateOnScreen("grafico.png") == None:

        if pg.locateOnScreen("fim.png") != None:
            pg.click("exit.png")
            time.sleep(1)
            pg.click("menu.png")
            time.sleep(0.2)

        elif pg.locateOnScreen("submenu.png") != None or pg.locateOnScreen("submenu_elemento.png") != None:

            for i in range(5):
                pg.press("backspace")
                time.sleep(0.2)

            pg.press("3")
            time.sleep(0.2)
            pg.press("enter")
            time.sleep(1)
            pg.press("1")
            time.sleep(0.2)
            pg.press("enter")
            time.sleep(2)
            pg.click("menu.png")

        elif pg.locateOnScreen("4_elemento.png") != None:
            pg.press("1")
            time.sleep(0.2)
            pg.press("enter")
            time.sleep(2)
            pg.click("menu.png")

        elif pg.locateOnScreen("prompt_python.png") != None:
            pg.click("exit.png")
            time.sleep(1)
            pg.click("menu.png")
            time.sleep(1)

        else:
            for i in range(5):
                pg.click("exit.png")
                time.sleep(0.2)

            time.sleep(2)
            pg.click("menu.png")
            time.sleep(1)

    pg.click("exit.png")
    time.sleep(2)
    pg.click("casio.png")
    time.sleep(2)


def inicio_python():
    inicio()
    time.sleep(1)
    for i in range(5):
        pg.press("H")
        time.sleep(0.1)
    for i in range(5):
        pg.press("a")
        time.sleep(0.1)

    # pg.press("F2")
    # time.sleep(1)
    # pg.click("exit.png")
    # time.sleep(1)
    # # verificar se a imagem "pasta_casio.png" esta na tela
    # if pg.locateOnScreen("pasta_casio.png") != None:
    #     pg.press("F6")
    #     time.sleep(1)

    # pg.press("down")
    time.sleep(1)


def apagar(arquivos_py):
    inicio_python()

    if len(arquivos_py) == 1:
        pg.press(arquivos_py[0][0])
        time.sleep(1)
        pg.press("F5")
        time.sleep(1)
        pg.press("F1")
        time.sleep(1.5)
        return None

    for i in range(len(arquivos_py)):
        pg.press("F5")
        time.sleep(1)
        pg.press("F1")
        time.sleep(1.5)


def teste_coordenacao():
    inicio_python()
    time.sleep(1)
    pg.press("F1")

    time.sleep(3)
    pg.press("5")
    time.sleep(1)
    pg.press("enter")


def teste_elemento(simbolo):
    inicio_python()
    pg.press("F1")

    time.sleep(2)
    pg.press("4")
    time.sleep(1)
    pg.press("enter")
    time.sleep(1)
    pg.typewrite(simbolo)
    time.sleep(0.2)

    pg.press("enter")
    pg.press("3")
    time.sleep(1)
    pg.press("1")
    pg.press("enter")
    pg.press("1")
    pg.click("exit.png")


def encerrar():
    pass


def copiar_py_especifico():
    arquivos_py = gerar_arquivos_py()

    for i, arquivo in enumerate(arquivos_py):
        print("["+str(i+1)+"] - "+arquivo)

    opcao = int(input("Arquivo: "))

    arquivos_py = [arquivos_py[opcao-1]]
    print("Arquivo escolhido: "+arquivos_py[0])
    time.sleep(1)
    apagar(arquivos_py)
    time.sleep(2)
    copiar(arquivos_py)


if __name__ == "__main__":
    while True:
        # inicio_python()
        # break
        toggle_caps_lock()
        print("_"*50)
        print("Menu")
        print("_"*50)
        print("[1] - Apagar programas")
        print("[2] - Copiar programas")
        print("[3] - Testar elemento")
        print("[4] - Apagar e copiar programas")
        print("[5] - Testar coordenacao")
        print("[6] - Copiar programa específico")
        print("[0] - Sair")
        print("_"*50)
        opcao = input("Opcao: ")
        print("_"*50)
        if opcao == "1":
            arquivos_py = gerar_arquivos_py()
            apagar(arquivos_py)
        elif opcao == "2":
            arquivos_py = gerar_arquivos_py()
            copiar(arquivos_py)
        elif opcao == "3":
            simbolo = input("Simbolo: ")
            teste_elemento(simbolo)
        elif opcao == "4":
            arquivos_py = gerar_arquivos_py()
            apagar(arquivos_py)
            time.sleep(2)
            copiar(arquivos_py)
        elif opcao == "5":
            teste_coordenacao()
        elif opcao == "6":
            copiar_py_especifico()

        elif opcao == "0":
            break
        else:
            print("Opcao invalida")
        print(f"Operação [{opcao}] executada com sucesso")

    print("Fim do programa")
