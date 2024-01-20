# Networking Projects

Table of Contents

- [Bandwidth Monitor](#bandwidth_monitor)
- [Python Chat](#python_chat)
- [Web Browser](#web_browser)

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

## Web Browser

Project Overview: Utilizing Python to build simple web browser with a GUI.

```python
import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView

class SimpleWebBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.browser = QWebEngineView()
        self.browser.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.url_input = QLineEdit()
        self.go_button = QPushButton('Go')
        self.go_button.clicked.connect(self.navigate)

        layout = QVBoxLayout()
        layout.addWidget(self.url_input)
        layout.addWidget(self.go_button)
        layout.addWidget(self.browser)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.setWindowTitle('Lauren has a Web Browser')
        self.resize(800, 600)

    def navigate(self):
        url = QUrl(self.url_input.text())
        if url.scheme() == '':
            url.setScheme('http')
        self.browser.setUrl(url)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    browser = SimpleWebBrowser()
    browser.show()
    sys.exit(app.exec_())
```
<img width="664" alt="Screenshot 2024-01-20 170558" src="https://github.com/Laurenjohns/Networking-Projects/assets/107310914/933bcb4e-9f51-438d-9903-404034b190a0">


