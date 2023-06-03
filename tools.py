import math

try:
    import os
except:
    import casioplot as plot


def system():
    try:
        import os
        return "PYTHON"
    except:
        import casioplot as plot
        return "CASIO"


def get_exe_key():
    try:
        print("\n[EXE] to continue")
        x = input()
    except:
        pass
    return x


def cls():
    print("\n" * 10)


def clear():
    plot.clear_screen()


def show():
    plot.show_screen()


def color(r, g, b):
    global clr
    clr = (r, g, b)


def text_size(n):
    global tsz
    tsz = n
    if n != 0 and n != 2:
        tsz = 1


def get_dot(x, y):
    return plot.get_pixel(x, y)


def line(x1, y1, x2, y2):
    global clr
    x = x1
    y = y1
    dx = abs(x2-x1)
    dy = abs(y2-y1)
    sx = 1 if x1 < x2 else -1 if x1 > x2 else 0
    sy = 1 if y1 < y2 else -1 if y1 > y2 else 0
    ix = dy//2
    iy = dx//2
    pixels = dx+1 if dx > dy else dy+1

    while pixels:
        plot.set_pixel(x, y, clr)
        ix += dx

    if ix >= dy:
        ix -= dy
        x += sx
        iy += dy
    if iy >= dx:
        iy -= dx
        y += sy
    pixels -= 1


def circle(xc, yc, r):
    global clr
    x = -1
    y = r
    d = -3-2*r

    while x <= y:
        x += 1
        if d < 0:
            d = d+6+4*x
        else:
            d = d+10+4*(x-y)

        y -= 1
        plot.set_pixel(xc+x, yc+y, clr)
        plot.set_pixel(xc+x, yc-y, clr)
        plot.set_pixel(xc-x, yc+y, clr)
        plot.set_pixel(xc-x, yc-y, clr)
        plot.set_pixel(xc+y, yc+x, clr)
        plot.set_pixel(xc+y, yc-x, clr)
        plot.set_pixel(xc-y, yc+x, clr)
        plot.set_pixel(xc-y, yc-x, clr)


def circle_fill(xc, yc, r):
    x = -1
    y = r
    d = -3-2*y
    while x <= y:
        x += 1
        if d < 0:
            d = d+6+4*x
        else:
            d = d+10+4*(x-y)
            y -= 1
        line(xc+x, yc+y, xc-x, yc+y)
        line(xc+x, yc-y, xc-x, yc-y)
        line(xc+y, yc+x, xc-y, yc+x)
        line(xc+y, yc-x, xc-y, yc-x)


def box(x1, y1, x2, y2):
    line(x1, y1, x2, y1)
    line(x1, y2, x2, y2)
    line(x1, y1, x1, y2)
    line(x2, y1, x2, y2)


def box_fill(x1, y1, x2, y2):
    for y in range(y1, y2+1):
        line(x1, y, x2, y)


def pause(n):
    for i in range(n):
        for _ in range(1000000):
            pass


def put_string(row, col, s):
    global clr, tsz
    if tsz == 0:
        plot.draw_string(col*8, row*14, str(s), clr, "small")
    elif tsz == 1:
        plot.draw_string(col*12, row*17, str(s), clr, "medium")
    else:
        plot.draw_string(col*18, row*21, str(s), clr, "large")

# Lista de lista, a primeira lista e de telas e a segunda e das linhas das telas

def ajustar_simbolo(elemento):
    if not len(elemento) > 2:
        if len(elemento) == 1:
            resultado = elemento[0].upper()
        else:
            resultado = elemento[0].upper() + elemento[1].lower()
    else:
        resultado = elemento

    return resultado

def tela(dados):
    try:
        clr = (0, 0, 0)
        sistema = system()
        
        if sistema == "CASIO":
            for tela_dados in dados:            
                clear()
                linha = 0
                for texto in tela_dados:
                    linha += 1
                    plot.draw_string(0, linha*14, texto, clr, "small")
                show()
                pause(2)
        else:
            cls()
            for tela_dados in dados:
                for linha, texto in enumerate(tela_dados):
                    print(texto)
            get_exe_key()
    except Exception as e:
        print("Erro em tela(): ", e)
        get_exe_key()
        pass
