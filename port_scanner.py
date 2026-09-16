import socket

alvo = input("Cole a URL/IP do site:  \n")

portas = range(1,100)

for porta in portas:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.settimeout(1.0)

    resultado = s.connect_ex((alvo,porta))

    if resultado == 0:
        print(f"[+]PORTA {porta}: ABERTA")
    else:
        print(f"[+]PORTA {porta}: FECHADA")

    s.close()

print("\n----VARREDURA CONCLUIDA!----")
