# Se importan los métodos
from metodost1 import check_char
from metodost1 import caps_switch

# Test de exito para check_char


def test_1():
    for i in range(65, 91):  # se recorre A-Z en sus valores ASCII
        if check_char(chr(i)) != 0:  # si check_char != 0 hubo un error
            assert False  # se envia un error
    for a in range(97, 123):  # se recorren las letras de la a hasta la z
        if check_char(chr(a)) != 0:
            assert False
    assert True  # si se llega a este punto significa que no hubo error


# Test de exito para caps_switch


def test_2():
    for i in range(65, 91):  # se recorre A-Z en sus valores ASCII
        if caps_switch(chr(i)) != chr(i).swapcase():
            assert False
    for a in range(97, 123):
        if caps_switch(chr(a)) != chr(a).swapcase():
            assert False
    assert True


# Test de fallo por mas de un caracter
# Si el caracter es corrector retorna un 0


def test_3():
    assert check_char("Hola") == 0


# Test de fallo por no ser alfanumerico


def test_4():
    assert check_char("1:") == 0


# Test de fallo por no ser caracter o string


def test_5():
    assert check_char([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 0
