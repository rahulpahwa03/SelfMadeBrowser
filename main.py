import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('<--', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        #forward button
        forward_btn = QAction('-->', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        #reload button
        rld_btn = QAction("Reload", self)
        rld_btn.triggered.connect(self.browser.reload)
        navbar.addAction(rld_btn)

        # home button
        home_btn = QAction('home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        #url bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))

    def navigate_yt(self):
        pass

    def navigate_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName("Self made browser")
window = MainWindow()
app.exec_()