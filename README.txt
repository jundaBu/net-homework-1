Jordy Martinez Garcia, Juan David Buitrago Martinez

To execute the code first run the server.py file on the terminal, when this file is running
run the client.py file on a separate terminal. 
After this in the terminal where you executed the client.py file it will prompt you to enter
a display name to then be able to start writing the messages. 

MESSAGE FLOW
The client wait for the user to enter the message. Then it first checks if the message is 
"quit," if this is true the client stops. When this is false the client sends the message 
to the server, the server then takes this message and echoes it back to the client, when 
the client recieves the message back it displays the echoed text, this loop keeps repeating
until the user types "quit."