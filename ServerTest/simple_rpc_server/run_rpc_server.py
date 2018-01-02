import os
import socket
import threading
import json


class Connection(object):

  def __init__(self, sock):
    self.sock = sock

  def start(self):
    t = threading.Thread(target=self.run)
    t.setDaemon(True)
    t.start()



  def send_answer(self, answer):

    data = json.dumps({"answer": answer})
    
    packet = "%s\r\n" % len(data)
    packet += data 
    self.sock.send(packet)


  def packet_received(self, packet):
    data = json.loads(packet)
    #print "data=", data
    command = data["command"]
    if command == "sum":
      a, b = data["args"]
      answer = a + b
      print "sum", a, b, answer
      self.send_answer(answer)
  

  def run(self):
    sock = self.sock

    buf = ""

    state = 0
    body_len = 0

    packet_count = 0

    while True:
      data = sock.recv(4096)

      #print "data=%s" % repr([data])
      if len(data) < 1:
        raise Exception("ConnectionLost")

      buf += data

      while True:
        if state == 0:
          if "\r\n" in buf:
            header, buf = buf.split("\r\n", 1)
            state = 1
            #print "header=%s" % header
            body_len = int(header)
            continue

        if state == 1:
          if len(buf) >= body_len:
            state = 0
            body, buf = buf[:body_len], buf[body_len:]
            packet_count += 1
            #print "packet=%s body=%s" % (packet_count, repr([body]))
            self.packet_received(body)
            continue

        break
        


        



def main():


  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  sock.bind(("0.0.0.0", 9001))
  sock.listen(50)

  while True:
    csock, addr = sock.accept()

    conn = Connection(csock)
    conn.start()
    



if __name__ == "__main__":
  main()
