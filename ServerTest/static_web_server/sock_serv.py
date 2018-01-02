import os
import socket
import threading

def handle_http_conn(cli_sock, conn_id):
  print "__file__", __file__

  BASE_DIR = os.path.abspath(os.path.dirname(__file__))

  print "BASED_DIR", BASE_DIR
  STATIC_DIR = os.path.join(BASE_DIR, "static")
  print "STATIC", STATIC_DIR

  ask = 0
  while True:
    ask += 1
    data = cli_sock.recv(4096)
    print "conn=%s ask=%s recv=%s" % (conn_id, ask, len(data))#repr([data])

    try:

      header, data = data.split("\r\n\r\n", 1)

      headers = header.split("\r\n")
      first = headers[0]
      method, url, ver = first.split(' ', 2)

      print "header1=%s" % headers[0]
      if url[:1] == "/":
        url = url[1:]


      print "method=%s url=%s ver=%s" % (method, url, ver)

      filepath =  os.path.abspath(os.path.join(STATIC_DIR, url))
      print "filepath=%s" % filepath

      rep_data = ""
      with open(filepath, "rb") as f:
        rep_data = f.read()
  
      #html = "<html><body><h1>Hello!-%s</h1></body></html>" % ask
      filename, ext = os.path.splitext(filepath)
      print "filename=%s, ext=%s" % (filename, ext)

      content_type = "text/html"

      if ext == ".png":
        content_type = "image/png"
      elif ext == ".jpg":
        content_type = "image/jpg"


      response = "HTTP/1.1 200 OK\r\n"
      response += "Content-Type: %s\r\n" % content_type
      response += "Content-Length: %s\r\n" % len(rep_data) 
      response += "\r\n"
      response += rep_data 
      cli_sock.send(response)
    except Exception as ex:
    
      rep_data = repr(ex)

      response = "HTTP/1.1 404 OK\r\n"
      response += "Content-Length: %s\r\n" % len(rep_data) 
      response += "\r\n"
      response += rep_data 

      cli_sock.send(response)

if __name__ == "__main__":


  port = 9000

  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  sock.bind(("0.0.0.0", port))
  sock.listen(50)


  last_id = 0

  while True:
    cli_sock, addr = sock.accept()
    print "client_sock", cli_sock, addr

    conn_id = last_id + 1 
    last_id = conn_id

    th = threading.Thread(target=handle_http_conn, args=[cli_sock, conn_id])
    th.setDaemon(True)
    th.start()

