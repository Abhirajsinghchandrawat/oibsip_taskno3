import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect((HOST, PORT))
  print("Connected to server!")
  while True:
    message = input("> ")
    s.sendall(message.encode('utf-8'))
    if message == "quit":
      break
  s.close()
