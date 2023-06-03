import casioplot as plot


# def clear():

#     plot.clear_screen()


def show():
    plot.show_screen()


def text_size(n):
    global tsz
    tsz = n
    if n != 0 and n != 2:
        tsz = 1


def color(r, g, b):
    global clr
    clr = (r, g, b)


def put_string(row, col, s):
    global clr, tsz
    if tsz == 0:
        plot.draw_string(col*8, row*14, str(s), clr, "small")
    elif tsz == 1:
        plot.draw_string(col*12, row*17, str(s), clr, "medium")
    else:
        plot.draw_string(col*18, row*21, str(s), clr, "large")





# clear()
text_size(1)
color(0, 0, 0)
put_string(1, 1, "Elemento: ")
show()
