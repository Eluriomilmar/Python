import time

indentacao = 0
aumenta_diminui = True

while True:
    time.sleep(0.2)
    if aumenta_diminui == True:
        print(" " * indentacao + "*" * 20)
        indentacao += 1
        if indentacao == 20:
            aumenta_diminui = False
    else:
        print(" " * indentacao + "*" * 20)
        indentacao -= 1
        if indentacao == 0:
            aumenta_diminui = True