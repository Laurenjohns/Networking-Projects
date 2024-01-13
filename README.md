# Networking Projects

## Python Chat 

Project Overview: Build a simple chat using Python. 

```python
# server file
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9999))

server.listen()

client, addr = server.accept()

done = False

while not done:
    msg = client.recv(1024).decode('utf-8')
    if msg == 'quit':
        done == True
    else:
        print(msg)
    client.send(input("Message: ").encode('utf-8'))
```

<img width="398" alt="Screenshot 2024-01-12 180706" src="https://github.com/Laurenjohns/Networking-Projects/assets/107310914/ca9779a4-8082-4121-b8ce-3143988e8aec">


```python
# client file
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("localhost", 9999))

done = False

while not done:
     client.send(input("Message: ").encode('utf-8'))
     msg = client.recv(1024).decode('utf-8')
     if msg == 'quit':
         done = True
     else:
         print(msg)
```

<img width="387" alt="Screenshot 2024-01-12 180716" src="https://github.com/Laurenjohns/Networking-Projects/assets/107310914/1f977b9f-57ac-4937-883a-7b7006aca381">

