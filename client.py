import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 12345))


prompt = client_socket.recv(1024).decode()
print(prompt, end="")
display_name = input()
client_socket.send(display_name.encode())


welcome = client_socket.recv(1024).decode()
print(welcome)


while True:
    message = input("Enter a message (or 'quit' to exit): ")
    client_socket.send(message.encode())
    
    if message.lower() == "quit":
        break
    
    data = client_socket.recv(1024)
    if data:
        print("Received from server:", data.decode())
    else:
        break

        

client_socket.close()