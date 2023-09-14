import socket

IP_SERVIDOR = '192.168.0.126'

PORTA = 8000

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

conexao = (IP_SERVIDOR, PORTA)

udp.connect(conexao)

while 1:
    Mensagem = input("->")
    udp.send(bytes(Mensagem, "utf8"))

udp.close()