# Networking Projects

Table of Contents

- [Bandwidth Monitor](#bandwidth_monitor)
- [Python Chat](#python_chat)

---

## Bandwidth Monitor

Project Overview: Utilizing Python to build a bandwitdh monitor.

```python
import time
import psutil

last_received = psutil.net_io_counters().bytes_recv
last_sent = psutil.net_io_counters().bytes_sent
last_total = last_received + last_sent

while True:
  bytes_received = psutil.net_io_counters().bytes_recv
  bytes_sent = psutil.net_io_counters().bytes_sent
  bytes_total = bytes_received + bytes_sent

  new_received = bytes_received - last_received
  new_sent = bytes_sent - last_sent
  new_total = bytes_total - last_total

  mb_new_received = new_received / 1024 / 1024
  mb_new_sent = new_sent / 1024 / 1024
  mb_new_total = new_total / 1024 / 1024

  print(f"{mb_new_received:.2f} MB received, {mb_new_sent:.2f} MB sent, {mb_new_total:.2f} MB total")

  last_received = bytes_received
  last_sent = bytes_sent
  last_total = bytes_total

  time.sleep(1)
```

<img width="354" alt="Screenshot 2024-01-12 184038" src="https://github.com/Laurenjohns/Networking-Projects/assets/107310914/afcb9fe0-c1de-4b44-8237-55d8b1d831bb">

---

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

