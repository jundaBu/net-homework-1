import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 12345))
server_socket.listen(1)
print("TCP server is listening...")

conn, addr = server_socket.accept()
print(f"Connected by {addr}")

# Ask for display name
conn.send("Please enter your display name: ".encode())
display_name = conn.recv(1024).decode().strip()
print(f"Client display name: {display_name}")
conn.send(f"Welcome {display_name}! Type 'quit' to disconnect.".encode())

# Handle messages until "quit"
while True:
    try:
        data = conn.recv(1024).decode().strip()
        if not data:
            break
        
        print(f"Received from {display_name}: {data}")
        
        if data.lower() == "quit":
            print(f"{display_name} disconnected")
            break
        
        # Echo the message back
        echo_message = f"Echo: {data}"
        conn.send(echo_message.encode())
        
    except ConnectionResetError:
        print(f"{display_name} disconnected unexpectedly")
        break

conn.close()
server_socket.close()