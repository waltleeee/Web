import socket
import uuid
import random
import json


class Client(object):
  def __init__(self, host, port):
    self.host = host
    self.port = port
    self._buf = ""
    self._state = 0
    self._body_len = 0

  def connect(self):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((self.host, self.port))
    self.sock = sock


  def sum(self, a, b):
    return self.send_command("sum", a, b)

  def abc(self, a):
    return self.send_command("abc", a)

  def send_command(self, command_name, *args):
    data = {
      "command": command_name,
      "args": args,
    }

    data = json.dumps(data)
    
    packet = "%s\r\n" % len(data)
    packet += data 
    self.sock.send(packet)

    return self.parse_response()

  def parse_response(self):

    while True:
      #print "recv...."
      data = self.sock.recv(4096)
      self._buf += data

      while True:
        if self._state == 0:
          if "\r\n" in self._buf:
            header, self._buf = self._buf.split("\r\n", 1)
            self._state = 1
            #print "header=%s" % header
            self._body_len = int(header)
            continue

        if self._state == 1:
          if len(self._buf) >= self._body_len:
            self._state = 0
            body, self._buf = self._buf[:self._body_len], self._buf[self._body_len:]
            #print "packet=%s body=%s" % (packet_count, repr([body]))
            result = json.loads(body)
            return result["answer"]
            continue

        break
        
    

if __name__ == "__main__":


  cli = Client("127.0.0.1", 9001)
  cli.connect()

  for i in range(2**16):
    a = random.randint(0, 2**30)
    b = random.randint(0, 2**30)
    total = cli.sum(a, b)
    print i, "sum %s, %s total=%s" % (a, b, total)

  raw_input()
