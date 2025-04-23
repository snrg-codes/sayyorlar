from db import sayyoralar

def sayyoralar_ruyhati(sayyoralar):
    ruyhat = []
    for sayyora in sayyoralar:
        ruyhat.append(sayyora["sayyora_nomi"])
    return ruyhat

def sayyora_haqida(sayyoralar, sayyora):
    ruyhat = sayyoralar_ruyhati(sayyoralar)
    tanlov = ruyhat.index(sayyora.title())
    return sayyoralar[tanlov]
    # return sayyoralar[sayyoralar_ruyhati(sayyoralar).index(sayyora.title())]


# user_input = input("Sayyora nomini kiriting...:")
# info = sayyora_haqida(sayyoralar, user_input)
# print(info)



