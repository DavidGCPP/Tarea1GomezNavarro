def check_char(x):  # método check_char, tiene como parámetro x
    if isinstance(x, str):  # revisa si la entrada es un string
        if len(x) == 1:  # revisa si es solo un caracter
            if str.isalpha(x):  # revisa si es alfanumerico
                print("0")
                return 0  # regresa un 0 si todo es correcto
            else:
                print("No es letra")
                return 1  # regresa un 1 si lo que se ingreso NO es una letra
        else:
            print("No es unico")
            return 2  # regresa un 2 si la entrada presenta mas de un caracter
    else:
        print("No es string")
        return 3  # regresa un 3 si la entrada no es un string del todo


def caps_switch(t):  # metodo caps_switch, tiene como parametro la entrada t
    if check_char(t) == 0:  # si check_char regresa un 0 todo esta correcto
        print(t.swapcase())
        return t.swapcase()  # si el caracter fue correcto, hace el cambio
