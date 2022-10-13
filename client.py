# Python program to demonstrate
# command line arguments
 
 
import argparse

# Import socket module
import socket    
 
# Initialize parser
parser = argparse.ArgumentParser()
 
# Adding optional argument
parser.add_argument("-s", "--Server", help = "Server IP Address")

# Adding optional argument
parser.add_argument("-p", "--Port", help = "Port Number")

# Adding optional argument
parser.add_argument("-l", "--Client", help = "Client Log File")
 
# Read arguments from command line
args = parser.parse_args()

server=args.Server
port = int(args.Port)
clientLog = args.Client

print("Command Line Arguments - IP: ", server, "Port: ", port, "Logfile: ", clientLog)

# Create a socket object
try:

        s = socket.socket()   

except socket.error:

        print ("Error while creating a socket")

        sys.exit(1)               
 
# connect to the server on GDC
try:

        s.connect((server, port))
        print("Successfully Connected. IP: ", server, "Port: ", port)

except socket.gaierror:

        print ("Address-related error connecting to server")

        sys.exit(1)

except socket.error:

        print ("Connection error")

        sys.exit(1)

message=input("Enter a Message to send to the Server: ")
print("Sending message to Server: ", message)

#Sending a message to server
try:

        s.sendall(b"network")

except socket.error:

        print("Error sending data")

        sys.exit(1)
        
#waiting to receive data from remote server

try:

    print ("Message recieved from server \n", s.recv(1024).decode())

except socket.error:

    print ("Error receiving data")

    sys.exit(1)


# close the connection
s.close()
