うぃぇimport socket
import threading

def handle_conn(cli_sock):
 while True:
            data=cli_sock.recv(4096)#一次收4096 byte
            print "recv=%s" % repr([data])

            html="<html><body><h1>Hello Walt</h1></body></html>"
            response="HTTP/1.1 200 OK\r\n"
            response+="Content-Length: %s\r\n" % len(html)
            response+="\r\n" #\r\n\r\nはhead定義終了　あとはdata
            response+=html

            cli_sock.send(response)

if __name__=="__main__":

    port=9000

    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)#

    #可以接受對外連線
    sock.bind(("0.0.0.0",port))

    #只接受自己
    #sock.bind("127.0.0.1",por)

    #只接受內往
    #sock.bind("192.168.0.1",port)

    #瞬間只機受50個使用者
    sock.listen(50)

    while True:
        cli_sock,addr=sock.accept()
        print "client_sock",cli_sock,addr

        th=threading.Thread(target=handle_conn,args=[cli_sock])#これで　第二ユーサは第一ユーサを待ちすることが必要ない
        th.setDaemon(True)#
        th.start()
       

