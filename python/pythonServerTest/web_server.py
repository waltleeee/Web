import socket

def main():
 
  s_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s_sock.bind(("127.0.0.1", 8080))
  s_sock.listen(50)

  while True:
    c_sock, addr = s_sock.accept()
    print "connect", c_sock, addr
print "Hello"

if __name__ == "__main__":#avoid other script import web_server and run main()
  print "main"
  main()

