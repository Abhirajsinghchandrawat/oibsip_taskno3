import socket
import threading

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

client_list = []  # List to store connected clients

def handle_client(client_socket):
  """Handles communication with a connected client."""
  while True:
    try:
      data = client_socket.recv(1024).decode('utf-8')
      if not data:
        break
      # Broadcast message to all clients except the sender
      for client in client_list:
        if client != client_socket:
          client.sendall(f"{data}\n".encode('utf-8'))
    except ConnectionError:
      # Client disconnected, remove from list
      client_list.remove(client_socket)
      client_socket.close()
      break

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind((HOST, PORT))
  s.listen()
  print(f"Server listening on {HOST}:{PORT}")
  while True:
    conn, addr = s.accept()
    client_list.append(conn)
    print(f"Connected by {addr}")
    thread = threading.Thread(target=handle_client, args=(conn,))
    thread.start()
