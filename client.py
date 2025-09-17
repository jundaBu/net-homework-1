import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 12345))

# Receive prompt for display name
prompt = client_socket.recv(1024).decode()
print(prompt, end="")
display_name = input()
client_socket.send(display_name.encode())

# Receive welcome message
welcome = client_socket.recv(1024).decode()
print(welcome)

# Send messages until "quit"
while True:
    message = input("Enter a message (or 'quit' to exit): ")
    client_socket.send(message.encode())
    
    if message.lower() == "quit":
        break
    
    # Receive echoed message from server
    try:
        data = client_socket.recv(1024)
        if data:
            print("Received from server:", data.decode())
        else:
            break
    except:
        break

client_socket.close()