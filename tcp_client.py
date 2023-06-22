import socket

target_host = "www.google.com"
target_port = 80

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the client
client.connect((target_host,target_port))

# Send some data
client.send(f"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# Receive some data
response = client.recv(4096)

print(response.decode())
client.close()

"""
ASSUMPTIONS:
1. Connection will always succeed
2. The server expects us to send data first instead of the server sending data first
3. The server will always return data to us in a timely fashion
We make these assumptions for simplicity's sake.
"""