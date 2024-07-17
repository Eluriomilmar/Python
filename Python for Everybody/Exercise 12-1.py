"""Change the socket program socket1.py to prompt the user for the URL so it can read any web page.
You can use split('/') to break the URL into its component parts so you can extract the host name for the socket connect call.
Add error checking using try and except to handle the condition where the user enters an improperly formatted or non-existent URL."""


import socket
try:
    website = input("Insira endereço do website: ")
    website = website.split("//")
    website.pop(0)
    website = "".join(website)
    website = website.split("/")
    print(website)
except:
    print("Endereço inválido, encerrando programa.")
else:
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((f"{website[0]}", 80))
    website = "/".join(website)
    cmd = f"GET http://{website} HTTP/1.0\r\n\r\n".encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if (len(data) < 1):
            break
        print(data.decode())
    mysock.close()