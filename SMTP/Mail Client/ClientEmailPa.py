from socket import *
import ssl
from http import client
import base64

#Monanshi Shah - 250855901
#Ryan Hellowell - 250841733

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = ("smtp.gmail.com", 587);
# Create socket called clientSocket and establish a TCP connection with mailserver
# Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM);
clientSocket.connect(mailserver);

# Fill in end
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')
# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

tlsCommand = "STARTTLS\r\n"
clientSocket.send(tlsCommand.encode())
recvTLS = clientSocket.recv(1024).decode()
print(recvTLS)

wrappedSocket = ssl.wrap_socket(clientSocket)

authCommand = "AUTH LOGIN\r\n"
wrappedSocket.send(authCommand.encode())
recvAuth = wrappedSocket.recv(1024).decode()
# Send MAIL FROM command and print server response.
username = input("Please enter username: ")
password = input("Please enter password: ")
username = (username.encode("utf-8"))
password = (password.encode("utf-8"))
base64_user = (base64.b64encode(username) + "\r\n".encode("utf-8"))
base64_pass = (base64.b64encode(password) + "\r\n".encode("utf-8"))

wrappedSocket.send(base64_user)
recvU = wrappedSocket.recv(1024).decode()
wrappedSocket.send(base64_pass)
recvP = wrappedSocket.recv(1024).decode()

# Fill in start
recUsername = input("Enter the recipient username: ")
mailFrom = "MAIL FROM:<" + username.decode() + ">\r\n"
wrappedSocket.send(mailFrom.encode())
recv2 = wrappedSocket.recv(1024).decode()
print(recv2);
# Fill in end

# Send RCPT TO command and print server response.

# Fill in start
rcptTo = "RCPT TO:<" + recUsername + ">\r\n"
wrappedSocket.send(rcptTo.encode())
recv3 = wrappedSocket.recv(1024).decode()
print(recv3);
# Fill in end

# Send DATA command and print server response.

# Fill in start
data = "DATA\r\n"
wrappedSocket.send(data.encode())
recv4 = wrappedSocket.recv(1024).decode()
print(recv4);
# Fill in end

# Send message data.

# Fill in start
subject = "Subject: Email Application\r\n"
msg = "I sent this using an email client I created.\r\n"
endmsg = "\r\n.\r\n"
wrappedSocket.send(subject.encode())
wrappedSocket.send(msg.encode())
# Message ends with a single period.

# Fill in start
wrappedSocket.send(endmsg.encode())
# Fill in end
recv5 = wrappedSocket.recv(1024).decode()
print(recv5);

# Send QUIT command and get server response.

# Fill in start
q = "QUIT\r\n"
wrappedSocket.send(q.encode())
recv6 = wrappedSocket.recv(1024).decode()
print(recv6);
# Fill in end
