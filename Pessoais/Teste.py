from pythonping import ping

try:
    print(ping("google.com", timeout=1))
except:
    print("não rolou")
else:
    print("rolou")