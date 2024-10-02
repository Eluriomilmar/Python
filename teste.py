import win32gui

def pos_janela(nome_janela):
    janela = win32gui.FindWindow(None, nome_janela)
    return win32gui.GetWindowRect(janela)

a = pos_janela("Velha")
print(a)