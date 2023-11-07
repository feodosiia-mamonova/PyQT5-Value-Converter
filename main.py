import sys
from PyQt5 import uic, QtCore  # Importing uic
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit, QApplication, QMainWindow, QLCDNumber

# Importing a library
import sqlite3

# Connecting to the database
con = sqlite3.connect("A.db")

# Creating a cursor
cur = con.cursor()


class UiWeight(object):  # Display class 2 of the screen - weight
    def setupUi(self, Weight):
        uic.loadUi('Weight.ui', self)  # Uploading the design
        self.retranslateUi(Weight)
        QtCore.QMetaObject.connectSlotsByName(Weight)

    def retranslateUi(self, Weight):
        _translate = QtCore.QCoreApplication.translate



class Weight(QMainWindow, UiWeight):  # the class where the button is connected
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.commandLinkButton.clicked.connect(self.weight_db)


    def weight_db(self):  # a function for displaying data using a database on the screen
        # checking whether the characters entered are numbers
        if self.lineEdit.text().isdigit() and self.lineEdit.text().replace('.', '',
                                                                           1).isdigit() and self.lineEdit.text().lstrip(
            '-').isdigit():
            x = float(self.lineEdit.text())
            y = float(
                cur.execute("""SELECT result FROM weight where m1 = ? and m2 = ?"""
                            , (self.comboBox.currentText(), self.comboBox_2.currentText())).fetchone()[0])
            self.lcdNumber_2.display(x * y)
        else:
            self.lcdNumber_2.display('Error')


class UiTime(object):  # Display class 2 of the screen - time
    def setupUi(self, Time):
        uic.loadUi('Time.ui', self)  # Uploading the design
        self.retranslateUi(Time)
        QtCore.QMetaObject.connectSlotsByName(Time)


    def retranslateUi(self, Time):
        _translate = QtCore.QCoreApplication.translate


class Time(QMainWindow, UiTime):  # the class where the button is connected
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.commandLinkButton.clicked.connect(self.time_db)

    def time_db(self):  # a function for displaying data using a database on the screen
        # checking whether the characters entered are numbers
        if self.lineEdit.text().isdigit() and self.lineEdit.text().replace('.', '', 1).isdigit() and self.lineEdit.text().lstrip('-').isdigit():
            x = float(self.lineEdit.text())
            y = float(
                cur.execute("""SELECT result FROM time where m1 = ? and m2 = ?"""
                            , (self.comboBox.currentText(), self.comboBox_2.currentText())).fetchone()[0])
            self.lcdNumber_2.display(x * y)
        else:
            self.lcdNumber_2.display('Error')


class UiPressure(object):  # Display class 2 of the screen - pressure
    def setupUi(self, Pressure):
        uic.loadUi('Pressure.ui', self)  # Uploading the design
        self.retranslateUi(Pressure)
        QtCore.QMetaObject.connectSlotsByName(Pressure)

    def retranslateUi(self, Pressure):
        _translate = QtCore.QCoreApplication.translate


class Pressure(QMainWindow, UiPressure):  # the class where the button is connected
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.commandLinkButton.clicked.connect(self.pressure_db)

    def pressure_db(self):  # a function for displaying data using a database on the screen
        # checking whether the characters entered are numbers
        if self.lineEdit.text().isdigit() and self.lineEdit.text().replace('.', '',1).isdigit() and self.lineEdit.text().lstrip('-').isdigit():
            x = float(self.lineEdit.text())
            y = float(
                cur.execute("""SELECT result FROM pressure where m1 = ? and m2 = ?"""
                            , (self.comboBox.currentText(), self.comboBox_2.currentText())).fetchone()[0])
            self.lcdNumber_2.display(x * y)
        else:
            self.lcdNumber_2.display('Error')


class UiLength(object):  # Display class 2 of the screen - Length
    def setupUi(self, Length):
        uic.loadUi('Length.ui', self)  # Uploading the design
        self.retranslateUi(Length)
        QtCore.QMetaObject.connectSlotsByName(Length)

    def retranslateUi(self, Length):
        _translate = QtCore.QCoreApplication.translate


class Length(QMainWindow, UiLength):  # the class where the button is connected
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.commandLinkButton.clicked.connect(self.length_db)

    def length_db(self):
        # checking whether the characters entered are numbers
        if self.lineEdit.text().isdigit() and self.lineEdit.text().replace('.', '',
                                                                           1).isdigit() and self.lineEdit.text().lstrip(
            '-').isdigit():
            x = float(self.lineEdit.text())
            y = float(
                cur.execute("""SELECT distinct result FROM length where m1 = ? and m2 = ?"""
                            , (self.comboBox.currentText(), self.comboBox_2.currentText())).fetchone()[0])
            self.lcdNumber_2.display(x * y)
        else:
            self.lcdNumber_2.display('Error')


class UiVolume(object):  # Display class 2 of the screen - Volume
    def setupUi(self, Volume):
        uic.loadUi('Volume.ui', self)  # Uploading the design
        self.retranslateUi(Volume)
        QtCore.QMetaObject.connectSlotsByName(Volume)

    def retranslateUi(self, Volume):
        _translate = QtCore.QCoreApplication.translate


class Volume(QMainWindow, UiVolume):  # the class where the button is connected
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.commandLinkButton.clicked.connect(self.volume_db)

    def volume_db(self):  # a function for displaying data using a database on the screen
        # checking whether the characters entered are numbers
        if self.lineEdit.text().isdigit() and self.lineEdit.text().replace('.', '',
                                                                           1).isdigit() and self.lineEdit.text().lstrip(
            '-').isdigit():
            x = float(self.lineEdit.text())
            y = float(
                cur.execute("""SELECT result FROM volume where m1 = ? and m2 = ?"""
                            , (self.comboBox.currentText(), self.comboBox_2.currentText())).fetchone()[0])
            self.lcdNumber_2.display(x * y)
        else:
            self.lcdNumber_2.display('Error')


class UiAmountInformation(object):  # Display class 2 of the screen - Amount Information
    def setupUi(self, Amountinformation):
        uic.loadUi('Amount_information.ui', self)  # Uploading the design
        self.retranslateUi(Amountinformation)
        QtCore.QMetaObject.connectSlotsByName(Amountinformation)

    def retranslateUi(self, Amountinformation):
        _translate = QtCore.QCoreApplication.translate


class Amountinformation(QMainWindow, UiAmountInformation):  # the class where the button is connected
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.commandLinkButton.clicked.connect(self.amountinformation_db)

    def amountinformation_db(self):  # a function for displaying data using a database on the screen
        # checking whether the characters entered are numbers
        if self.lineEdit.text().isdigit() and self.lineEdit.text().replace('.', '',
                                                                           1).isdigit() and self.lineEdit.text().lstrip(
            '-').isdigit():
            x = float(self.lineEdit.text())
            y = float(
                cur.execute("""SELECT result FROM amount_information where m1 = ? and m2 = ?"""
                            , (self.comboBox.currentText(), self.comboBox_2.currentText())).fetchone()[0])
            self.lcdNumber_2.display(x * y)
        else:
            self.lcdNumber_2.display('Error')


class UiArea(object):  # Display class 2 of the screen - Area
    def setupUi(self, Area):
        uic.loadUi('Area.ui', self)  # Uploading the design
        self.retranslateUi(Area)
        QtCore.QMetaObject.connectSlotsByName(Area)

    def retranslateUi(self, Area):
        _translate = QtCore.QCoreApplication.translate


class Area(QMainWindow, UiArea):  # the class where the button is connected
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.commandLinkButton.clicked.connect(self.area_db)

    def area_db(self):  # a function for displaying data using a database on the screen
        # checking whether the characters entered are numbers
        if self.lineEdit.text().isdigit() and self.lineEdit.text().replace('.', '',
                                                                           1).isdigit() and self.lineEdit.text().lstrip(
            '-').isdigit():
            x = float(self.lineEdit.text())
            y = float(
                cur.execute("""SELECT result FROM area where m1 = ? and m2 = ?"""
                            , (self.comboBox.currentText(), self.comboBox_2.currentText())).fetchone()[0])
            self.lcdNumber_2.display(x * y)
        else:
            self.lcdNumber_2.display('Error')


class UiTemperature(object):  # Display class 2 of the screen - Temperature
    def setupUi(self, Temperature):
        uic.loadUi('Temperature.ui', self)  # Uploading the design
        self.retranslateUi(Temperature)
        QtCore.QMetaObject.connectSlotsByName(Temperature)

    def retranslateUi(self, Temperature):
        _translate = QtCore.QCoreApplication.translate


class Temperature(QMainWindow, UiTemperature):  # the class where the button is connected
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.commandLinkButton.clicked.connect(self.temperature_db)

    def temperature_db(self):  # a function for displaying data using a database on the screen
        # checking whether the characters entered are numbers
        if self.lineEdit.text().isdigit() and self.lineEdit.text().replace('.', '',
                                                                           1).isdigit() and self.lineEdit.text().lstrip(
            '-').isdigit():
            x = float(self.lineEdit.text())
            y = float(
                cur.execute("""SELECT result FROM temperature where m1 = ? and m2 = ?"""
                            , (self.comboBox.currentText(), self.comboBox_2.currentText())).fetchone()[0])
            self.lcdNumber_2.display(x * y)
        else:
            self.lcdNumber_2.display('Error')


class UiEnergy(object):  # Display class 2 of the screen - Energy
    def setupUi(self, Energy):
        uic.loadUi('Energy.ui', self)  # Uploading the design
        self.retranslateUi(Energy)
        QtCore.QMetaObject.connectSlotsByName(Energy)

    def retranslateUi(self, Energy):
        _translate = QtCore.QCoreApplication.translate


class Energy(QMainWindow, UiEnergy):  # the class where the button is connected
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.commandLinkButton.clicked.connect(self.energy_db)

    def energy_db(self):  # a function for displaying data using a database on the screen
        # checking whether the characters entered are numbers
        if self.lineEdit.text().isdigit() and self.lineEdit.text().replace('.', '',
                                                                           1).isdigit() and self.lineEdit.text().lstrip(
            '-').isdigit():
            x = float(self.lineEdit.text())
            y = float(
                cur.execute("""SELECT result FROM energy where m1 = ? and m2 = ?"""
                            , (self.comboBox.currentText(), self.comboBox_2.currentText())).fetchone()[0])
            self.lcdNumber_2.display(x * y)
        else:
            self.lcdNumber_2.display('Error')


class UiMyWidget(object):  # main window class
    def setupUi(self, QMainWindow):
        uic.loadUi('Main.ui', self)  # Uploading the design
        self.retranslateUi(QMainWindow)
        QtCore.QMetaObject.connectSlotsByName(QMainWindow)

    def retranslateUi(self, QMainWindow):
        _translate = QtCore.QCoreApplication.translate


class MyWidget(QMainWindow, UiMyWidget):  # a class where the user clicks through to the second screen
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.commandLinkButton.clicked.connect(
            self.show_window_Time)  # button to switch the time to the screen
        self.commandLinkButton_2.clicked.connect(
            self.show_window_Pressure)  # a button to switch the pressure to the screen
        self.commandLinkButton_3.clicked.connect(
            self.show_window_Length)  # the button to switch to the screen Length
        self.commandLinkButton_4.clicked.connect(
            self.show_window_Weight)  # a button to switch to the screen Weight

        self.commandLinkButton_5.clicked.connect(
            self.show_window_Volume)  # a button to switch the volume to the screen
        self.commandLinkButton_6.clicked.connect(
            self.show_window_amount_information)  # a button to switch the amount of information to the screen
        self.commandLinkButton_7.clicked.connect(
            self.show_window_Area)  # the button to switch to the screen area
        self.commandLinkButton_8.clicked.connect(
            self.show_window_temperature)  # the button to switch to the screen Temperature
        self.commandLinkButton_9.clicked.connect(
            self.show_window_energy)  # the button to switch to the Energy screen

    def show_window_Weight(self):  # displaying the Weight window
        self.w5 = Weight()
        self.w5.show()

    def show_window_Time(self):  # Time window display
        self.w2 = Time()
        self.w2.show()

    def show_window_Pressure(self):  # Pressure window display
        self.w3 = Pressure()
        self.w3.show()

    def show_window_Length(self):  # display window Length
        self.w4 = Length()
        self.w4.show()

    def show_window_Volume(self):  # displaying the Volume window
        self.w6 = Volume()
        self.w6.show()

    def show_window_amount_information(self):  # displaying the Amount of Information window
        self.w7 = Amountinformation()
        self.w7.show()

    def show_window_Area(self):  # displaying the Area window
        self.w8 = Area()
        self.w8.show()

    def show_window_temperature(self):  # displaying the Temperature window
        self.w9 = Temperature()
        self.w9.show()

    def show_window_energy(self):  # displaying the Energy window
        self.w10 = Energy()
        self.w10.show()


if __name__ == '__main__':  # conclusion
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
