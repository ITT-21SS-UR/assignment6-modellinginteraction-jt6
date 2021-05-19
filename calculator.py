#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic, Qt, QtCore


class Calculator(QMainWindow):
    # loads the ui and activates the button_listener
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("calculator.ui", self)
        sys.stdout.write("event,input,timestamp_msSinceEpoch\n")
        self.button_clicked()

    # logs every important keystroke
    def log_key(message):
        def log_key_event(func):
            def logging(self, event):
                numbers_operators = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '+', '-', '*', '/']
                if event.text() in numbers_operators:
                    timestamp = QtCore.QDateTime.currentMSecsSinceEpoch()
                    sys.stdout.write("%s,%s,%d\n" % (message, str(event.text()), timestamp))
                elif event.key() == QtCore.Qt.Key_Return:
                    equ = self.ui.calc_output.text()
                    try:
                        ans = eval(equ)
                    except SyntaxError:
                        ans = "No valid input"
                    timestamp = QtCore.QDateTime.currentMSecsSinceEpoch()
                    sys.stdout.write("%s,%s,%d\n" %
                                     (message, "Calculate (Result: " + str(ans) + ")", timestamp))
                elif event.key() == 16777219:
                    timestamp = QtCore.QDateTime.currentMSecsSinceEpoch()
                    sys.stdout.write("%s,%s,%d\n" % (message, "Delete", timestamp))
                elif event.key() == 16777223:
                    timestamp = QtCore.QDateTime.currentMSecsSinceEpoch()
                    sys.stdout.write("%s,%s,%d\n" % (message, "Clear", timestamp))
                else:
                    timestamp = QtCore.QDateTime.currentMSecsSinceEpoch()
                    sys.stdout.write("%s,%s,%d\n" % (message, "Other", timestamp))
                func(self, event)
            return logging
        return log_key_event

    # handles the event when a key is pressed
    @log_key("Key")
    def keyPressEvent(self, event):
        numbers_operators = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '+', '-', '*', '/']
        if event.text() in numbers_operators:
            self.input_key(event.text())
        elif event.key() == QtCore.Qt.Key_Return:
            self.input_key('=')
        elif event.key() == QtCore.Qt.Key_Backspace:
            self.input_key('d')
        elif event.key() == QtCore.Qt.Key_Delete:
            self.input_key('c')

    # decides which character has to be added or what action has to be done for each keystroke
    def input_key(self, char):
        if char == '=':
            equ = self.ui.calc_output.text()
            try:
                answer = eval(equ)
                self.ui.calc_output.setText(str(answer))
            except SyntaxError:
                self.ui.calc_output.setText("ERROR")
        elif char == 'd':
            text = self.ui.calc_output.text()
            self.ui.calc_output.setText(text[0:len(text) - 1])
        elif char == 'c':
            self.ui.calc_output.setText("")
        else:
            text = self.ui.calc_output.text()
            self.ui.calc_output.setText(text + char)

    # initiate the button click listeners and connects them with the display
    def button_clicked(self):
        self.ui.btn_0.clicked.connect(lambda x: self.input_button('0'))
        self.ui.btn_1.clicked.connect(lambda x: self.input_button('1'))
        self.ui.btn_2.clicked.connect(lambda x: self.input_button('2'))
        self.ui.btn_3.clicked.connect(lambda x: self.input_button('3'))
        self.ui.btn_4.clicked.connect(lambda x: self.input_button('4'))
        self.ui.btn_5.clicked.connect(lambda x: self.input_button('5'))
        self.ui.btn_6.clicked.connect(lambda x: self.input_button('6'))
        self.ui.btn_7.clicked.connect(lambda x: self.input_button('7'))
        self.ui.btn_8.clicked.connect(lambda x: self.input_button('8'))
        self.ui.btn_9.clicked.connect(lambda x: self.input_button('9'))
        self.ui.btn_dot.clicked.connect(lambda x: self.input_button('.'))
        self.ui.btn_plus.clicked.connect(lambda x: self.input_button('+'))
        self.ui.btn_minus.clicked.connect(lambda x: self.input_button('-'))
        self.ui.btn_mul.clicked.connect(lambda x: self.input_button('*'))
        self.ui.btn_div.clicked.connect(lambda x: self.input_button('/'))
        self.ui.btn_equal.clicked.connect(lambda x: self.input_button('='))
        self.ui.btn_delete.clicked.connect(lambda x: self.input_button('d'))
        self.ui.btn_delete_all.clicked.connect(lambda x: self.input_button('c'))

    # logs every button press
    def log_button(message):
        def log_button_event(func):
            def logging(self, text):
                numbers_operators = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '+', '-', '*', '/']
                if text in numbers_operators:
                    timestamp = QtCore.QDateTime.currentMSecsSinceEpoch()
                    sys.stdout.write("%s,%s,%d\n" % (message, text, timestamp))
                elif text == '=':
                    equ = self.ui.calc_output.text()
                    try:
                        ans = eval(equ)
                    except SyntaxError:
                        ans = "No valid input"
                    timestamp = QtCore.QDateTime.currentMSecsSinceEpoch()
                    sys.stdout.write("%s,%s,%d\n" % (message, text + " (Result: " + str(ans) + ")", timestamp))
                elif text == 'd':
                    timestamp = QtCore.QDateTime.currentMSecsSinceEpoch()
                    sys.stdout.write("%s,%s,%d\n" % (message, "DEL (removed last character)", timestamp))
                elif text == 'c':
                    timestamp = QtCore.QDateTime.currentMSecsSinceEpoch()
                    sys.stdout.write("%s,%s,%d\n" % (message, "AC (all cleared)", timestamp))
                func(self, text)
            return logging
        return log_button_event

    # decides which character has to be added or what action has to be done for each button press
    @log_button("Button")
    def input_button(self, char):
        if char == '=':
            equ = self.ui.calc_output.text()
            try:
                answer = eval(equ)
                self.ui.calc_output.setText(str(answer))
            except SyntaxError:
                self.ui.calc_output.setText("ERROR")
        elif char == 'd':
            text = self.ui.calc_output.text()
            self.ui.calc_output.setText(text[0:len(text) - 1])
        elif char == 'c':
            self.ui.calc_output.setText("")
        else:
            text = self.ui.calc_output.text()
            self.ui.calc_output.setText(text + char)


# main function - initiate application and view
if __name__ == '__main__':
    app = Qt.QApplication(sys.argv)
    view = Calculator()
    view.show()
    sys.exit(app.exec_())
