import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPlainTextEdit, QPushButton, QMessageBox

if __name__ == '__main__':

    def handleCalc():
        info = textEdit.toPlainText() # get the txt from the box

        # 薪资20000 以上 和 以下 的人员名单
        salary_above_20k = ''
        salary_below_20k = ''
        for line in info.splitlines():
            if not line.strip():
                continue
            parts = line.split(' ')
            # 去掉列表中的空字符串内容
            parts = [p for p in parts if p]
            name, salary, age = parts
            if int(salary) >= 20000:
                salary_above_20k += name + '\n'
            else:
                salary_below_20k += name + '\n'

        QMessageBox.about(window,
                          '统计结果',
                          f'''薪资20000 以上的有：\n{salary_above_20k}
                    \n薪资20000 以下的有：\n{salary_below_20k}'''
                          )

    app = QApplication(sys.argv)
    window = QWidget()

    window.setWindowTitle('Hello World12321!')
    textEdit = QPlainTextEdit(window)
    textEdit.setPlaceholderText("请输入薪资表")
    textEdit.move(10, 25)
    textEdit.resize(300, 350)

    button = QPushButton('统计', window)
    button.move(380, 80)
    button.clicked.connect(handleCalc)

    window.show()

    sys.exit(app.exec_())
#%%
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPlainTextEdit, QPushButton, QMessageBox, QMainWindow


class Stats():
    def __init__(self):
        self.window = QMainWindow()
        self.window.resize(500, 400)
        self.window.move(300, 300)
        self.window.setWindowTitle('薪资统计')

        self.textEdit = QPlainTextEdit(self.window)
        self.textEdit.setPlaceholderText("请输入薪资表")
        self.textEdit.move(10, 25)
        self.textEdit.resize(300, 350)

        self.button = QPushButton('统计', self.window)
        self.button.move(380, 80)

        self.button.clicked.connect(self.handleCalc)


    def handleCalc(self):
        info = self.textEdit.toPlainText()

        # 薪资20000 以上 和 以下 的人员名单
        salary_above_20k = ''
        salary_below_20k = ''
        for line in info.splitlines():
            if not line.strip():
                continue
            parts = line.split(' ')
            # 去掉列表中的空字符串内容
            parts = [p for p in parts if p]
            name,salary,age = parts
            if int(salary) >= 20000:
                salary_above_20k += name + '\n'
            else:
                salary_below_20k += name + '\n'

        QMessageBox.about(self.window,
                    '统计结果',
                    f'''薪资20000 以上的有：\n{salary_above_20k}
                    \n薪资20000 以下的有：\n{salary_below_20k}'''
                    )

app = QApplication([])
stats = Stats()
stats.window.show()
app.exec_()
#%%
from PyQt5 import uic

cc= uic.loadUi("test2.ui")
cc.QPushButton
#%%
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QTextEdit, QPushButton, QPlainTextEdit, QMessageBox
from PyQt5 import uic
import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the ui file
        uic.loadUi("test2.ui", self)

        # Define Our Widgets
        # self.label = self.findChild(QLabel, "label")
        self.textedit = self.findChild(QPlainTextEdit, "plainTextEdit")
        self.button = self.findChild(QPushButton, "pushButton")
        # self.clear_button = self.findChild(QPushButton, "pushButton_2")


        # Do something
        self.button.clicked.connect(self.handleCalc)
        # self.clear_button.clicked.connect(self.clearer)

        # Show The App
        self.show()

    def handleCalc(self):
        info = self.textedit.toPlainText()

        salary_above_20k = ''
        salary_below_20k = ''
        for line in info.splitlines():
            if not line.strip():
                continue
            parts = line.split(' ')

            parts = [p for p in parts if p]
            name,salary,age = parts
            if int(salary) >= 20000:
                salary_above_20k += name + '\n'
            else:
                salary_below_20k += name + '\n'

        QMessageBox.about(UI(),
                    '统计结果',
                    f'''薪资20000 以上的有：\n{salary_above_20k}
                    \n薪资20000 以下的有：\n{salary_below_20k}'''
                    )

# Initialize The App
app = QApplication([])
UIWindow = UI()
app.exec_()
#%%

from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QTextEdit, QPushButton, QPlainTextEdit, QMessageBox
from PyQt5 import uic
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the ui file
        uic.loadUi("test2.ui", self)
        self.show()


app = QApplication([])
UIWindow = UI()
app.exec_()