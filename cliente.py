import socket

IP_SERVIDOR = input("Digite o IP do servidor")

PORTA = 8000

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

conexao = (IP_SERVIDOR, PORTA)

udp.connect(conexao)

while 1:
    Mensagem = input("->")
    udp.send(bytes(Mensagem, "utf8"))

udp.close()
