import os
import socket
import threading

def sayHello(cli_sock):
    print "Hello "


if __name__=="__main__":
    port=9000
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    sock.bind(("0.0.0.0",port))
    sock.listen(50)

    while True:

        cli_sock,addr=sock.accept()
        print "accept"

        th=threading.Thread(target=sayHello,args=[cli_sock])
        th.setDaemon(True)
        th.start()

