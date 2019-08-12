from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtWidgets import

import time
import traceback, sys


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.counter = 0

        layout = QVBoxLayout()

        self.l = QLabel("Start")
        b = QPushButton("DANGER!")
        b.pressed.connect(self.oh_no)

        layout.addWidget(self.l)
        layout.addWidget(b)

        w = QWidget()
        w.setLayout(layout)

        self.setCentralWidget(w)

        self.show()

        myclass = MyClass()
        myclass.moveToThread()


        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.recurring_timer)
        self.timer.start()

    def oh_no(self):
        # Pass the function to execute
        pass

    def recurring_timer(self):
        self.counter += 1
        self.l.setText("Counter: %d" % self.counter)


class MyClass(QObject):
    def __init__(self):
        self.var = 1

    def cycle_1(self):
        i = 0
        while i < 10:
            time.sleep(1000)
            print('thread_1: ', i)
            i += 1

    def cycle_2(self):
        i = 0
        while i < 10:
            time.sleep(1000)
            print('thread_2: ', i)
            i += 1


app = QApplication([])
window = MainWindow()
app.exec_()