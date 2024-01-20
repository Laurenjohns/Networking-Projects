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


