import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QStatusBar, QDialog, QPushButton, QMessageBox
from PyQt5.uic.properties import QtGui

import design  # Это наш конвертированный файл дизайна
import subprocess
import os
import matplotlib.pyplot as plt


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton.clicked.connect(self.launch_scdm)
        self.pushButtonWB.clicked.connect(self.launch_wb)
        self.pushButton_2.clicked.connect(self.browse)
        self.pushButton_4.clicked.connect(self.graph)
        # self

    def launch_wb(self):
        program = r'C:\Program Files\ANSYS Inc\v194\Framework\bin\Win64\runwb2.exe'
        subprocess.Popen(program)

    def launch_scdm(self):
        program = r'C:\Program Files\ANSYS Inc\v194\SCDM\SpaceClaim.exe'
        subprocess.Popen(program)

    def browse(self):
        self.listWidget.clear()  # На случай, если в списке уже есть элементы
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")
        # открыть диалог выбора директории и установить значение переменной
        # равной пути к выбранной директории

        if directory:  # не продолжать выполнение, если пользователь не выбрал директорию
            for file_name in os.listdir(directory):  # для каждого файла в директории
                if file_name.endswith(".txt"):
                    self.listWidget.addItem(file_name)  # добавить файл в listWidget

    def buttonClicked1(self):
        self.pushButton.setText('Запущен 1!')

    def buttonClicked2(self):
        self.pushButtonWB.setText('Запущен 2!')


    def graph(self):
        x = [1, 2, 3, 4]
        y = [2, 4, 12, 1]
        plt.plot(x, y, 'r^--')
        plt.title('Graph...', fontsize=18)
        plt.grid()
        plt.show()

    def showDialog(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        # msgBox.setFont(QFont("Arial", 12))
        # msgBox.setWindowIcon(QtGui.QIcon('about.png'))
        msgBox.setWindowIcon(QIcon('about.png'))
        msgBox.setText("OptiWidget\nМахнев Мирослав Сергеевич "+"\N{COPYRIGHT SIGN}"+"\n2020")
        msgBox.setWindowTitle("О программе")
        # msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()
        # returnValue = msgBox.exec()
        # if returnValue == QMessageBox.Ok:
        #     print('OK clicked')


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
