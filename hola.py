def number(dig1:int, dig2:int):
    if dig1 > dig2:
        return dig1
    elif dig2 > dig1:
        return dig2
    elif dig1 == dig2:
        raise Exception("No puedes ingresar los mismos digitos")
    
print(number(20,20))