#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from pprint import pprint
from PyQt5.QtWidgets import (QApplication, QWidget,QMainWindow,QAction,qApp,
                             QGridLayout, QVBoxLayout, QHBoxLayout,
                             QLabel, QLineEdit, QPushButton, QDialog)
from PyQt5.QtGui import *
from PyQt5.QtCore import *

#計算補助用関数
def Ligation(vector_final_pmol,insert_final_pmol,final_total_volume,
             vector_length,insert_length,
             vector_amount,insert_amount):

    vector_ng = vector_final_pmol * 660.0 * vector_length / 1000.0
    insert_ng = insert_final_pmol * 660.0 * insert_length / 1000.0
    vector_ul = vector_ng / vector_amount
    insert_ul = insert_ng / insert_amount
    print(vector_ul)
    print(insert_ul)
    rate_vector = vector_ul/(vector_ul+insert_ul)
    rate_insert = insert_ul/(vector_ul+insert_ul) 
    result_vector = final_total_volume*rate_vector
    result_insert = final_total_volume*rate_insert
    result = [result_vector,result_insert]
    return result

def gotaq(final_volume, master_X):
    b = 50/final_volume
    Green = 10/b*master_X
    dNTP = 1/b*master_X
    pF = 2/b*master_X
    pR = 2/b*master_X
    taq = 0.25/b*master_X
    DNA = 2/b*master_X
    DW = 33/b*master_X
    result = [Green,dNTP,pF,pR,taq,DNA,DW]
    return result

def extaq(final_volume, master_X):
    b = 50/final_volume
    buffer = 5/b*master_X
    dNTP = 4/b*master_X
    pF = 2/b*master_X
    pR = 2/b*master_X
    taq = 0.2/b*master_X
    DNA = 2/b*master_X
    DW = 34.8/b*master_X
    result = [buffer,dNTP,pF,pR,taq,DNA,DW]
    return result

def KODplus(final_volume, master_X):
    b = 50 / final_volume
    buffer = 5 / b * master_X
    dNTP = 5 / b * master_X
    MgSO4 = 2 / b * master_X
    pF = 1.5 / b * master_X
    pR = 1.5 / b * master_X
    KOD = 1 / b * master_X
    DNA = 1 / b * master_X
    DW = 34 / b * master_X
    result = [buffer, dNTP, MgSO4, pF, pR, KOD, DNA, DW]
    return result


class IndexWindow(QMainWindow):

    ################### GUI CORE (INDEX) #########################
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Tools for Cloning -INDEX-')
        self.statusBar().showMessage('This is a status bar')
        menuBar = self.menuBar()
        menuBar2 = self.menuBar()

        menuBar.setNativeMenuBar(False) #only for MacOS
        menuBar2.setNativeMenuBar(False)  # only for MacOS

        ### ligation ###
        file_menu = menuBar.addMenu('&Tools')
        ligation_action = QAction(QIcon('Pictures/ligation.png'), '&Ligation', self)
        ligation_action.setShortcut('Ctrl+Q')
        ligation_action.setStatusTip('program for ligation')
        ligation_action.triggered.connect(self.makeLigation)
        file_menu.addAction(ligation_action)

        ### PCR mastermix ###
        file_menu2 = menuBar2.addMenu('&PCR')
        gotaq_action = QAction(QIcon('Pictures/promega.jpg'), '&GoTaq', self)
        gotaq_action.setShortcut('Ctrl+Q')
        gotaq_action.setStatusTip('program for GoTaq')
        gotaq_action.triggered.connect(self.GOTAQ)
        file_menu2.addAction(gotaq_action)

        extaq_action = QAction(QIcon('Pictures/takara2.png'), '&ExTaq', self)
        extaq_action.setShortcut('Ctrl+W')
        extaq_action.setStatusTip('program for Extaq')
        extaq_action.triggered.connect(self.EXTAQ)
        file_menu2.addAction(extaq_action)

        kodplus_action = QAction(QIcon('Pictures/takara2.png'), '&KODplus', self)
        kodplus_action.setShortcut('Ctrl+E')
        kodplus_action.setStatusTip('program for KODplus')
        kodplus_action.triggered.connect(self.KODplus)
        file_menu2.addAction(kodplus_action)


        self.setGeometry(300, 300, 400, 200)

    def makeLigation(self):

        subwindow = Subwindow()
        subwindow.show()

    def GOTAQ(self):
        subwindow = Subwindow2()
        subwindow.show()

    def EXTAQ(self):
        subwindow = Subwindow3()
        subwindow.show()

    def KODplus(self):
        subwindow = Subwindow4()
        subwindow.show()

    ################### Calculate for Ligation #####################
class Subwindow(QWidget):
    def __init__(self, parent=None):
        super(Subwindow, self).__init__(parent)

        self.w = QDialog(parent)

        self.inputLine = QLineEdit()
        self.inputLine2 = QLineEdit()
        self.inputLine3 = QLineEdit()
        self.inputLine4 = QLineEdit()
        self.inputLine5 = QLineEdit()
        self.inputLine6 = QLineEdit()
        self.inputLine7 = QLineEdit()
        self.outputLine1 = QLineEdit()
        self.outputLine2 = QLineEdit()
        self.outputLine1.setReadOnly(True)
        self.outputLine2.setReadOnly(True)

        self.calcButton = QPushButton("&Calc")
        self.calcButton.clicked.connect(self.calc)

        lineLayout = QGridLayout()
        lineLayout.addWidget(QLabel("Final total volme: "), 0, 0)
        lineLayout.addWidget(self.inputLine, 0, 1)
        lineLayout.addWidget(QLabel("Final Vector pmol rate: "), 1, 0)
        lineLayout.addWidget(self.inputLine2, 1, 1)
        lineLayout.addWidget(QLabel("Final Insert pmol rate: "), 2, 0)
        lineLayout.addWidget(self.inputLine3, 2, 1)
        lineLayout.addWidget(QLabel("Vector DNA amount (ng/ul): "), 3, 0)
        lineLayout.addWidget(self.inputLine4, 3, 1)
        lineLayout.addWidget(QLabel("Insert DNA amount (ng/ul): "), 4, 0)
        lineLayout.addWidget(self.inputLine5, 4, 1)
        lineLayout.addWidget(QLabel("Vector length (bp): "), 5, 0)
        lineLayout.addWidget(self.inputLine6, 5, 1)
        lineLayout.addWidget(QLabel("Insert length (bp): "), 6, 0)
        lineLayout.addWidget(self.inputLine7, 6, 1)

        lineLayout.addWidget(QLabel("############# Result ############"),7,0)

        lineLayout.addWidget(QLabel("Vector ul"),8,0)
        lineLayout.addWidget(self.outputLine1, 8, 1)
        lineLayout.addWidget(QLabel("Insert ul"),9,0)
        lineLayout.addWidget(self.outputLine2,9,1)


        buttonLayout = QVBoxLayout()
        buttonLayout.addWidget(self.calcButton)

        mainLayout = QHBoxLayout()
        mainLayout.addLayout(lineLayout)
        mainLayout.addLayout(buttonLayout)

        self.w.setLayout(mainLayout)
        self.setWindowTitle("Calculate about Ligation")

    def calc(self):
        final_total_volume = float(self.inputLine.text())
        vector_final_pmol = float(self.inputLine2.text())
        insert_final_pmol = float(self.inputLine3.text())
        vector_amount = float(self.inputLine4.text())
        insert_amount = float(self.inputLine5.text())
        vector_length = float(self.inputLine6.text())
        insert_length = float(self.inputLine7.text())

        r = Ligation(vector_final_pmol,insert_final_pmol,final_total_volume,
             vector_length,insert_length,
             vector_amount,insert_amount)
        r1 = r[0]
        r2 = r[1]
        self.outputLine1.setText(str(round(r1,6)))
        self.outputLine2.setText(str(round(r2,6)))

    def show(self):
        self.w.exec_()

class Subwindow2(QWidget):
    def __init__(self, parent=None):
        super(Subwindow2, self).__init__(parent)

        self.w = QDialog(parent)
        self.w.setWindowTitle('GoTaq, Calculate about MasterMix')
        self.inputLine = QLineEdit()
        self.inputLine2 = QLineEdit()
        self.outputLine1 = QLineEdit()
        self.outputLine2 = QLineEdit()
        self.outputLine3 = QLineEdit()
        self.outputLine4 = QLineEdit()
        self.outputLine5 = QLineEdit()
        self.outputLine6 = QLineEdit()
        self.outputLine7 = QLineEdit()
        self.outputLine8 = QLineEdit()

        self.outputLine1.setReadOnly(True)
        self.outputLine2.setReadOnly(True)
        self.outputLine3.setReadOnly(True)
        self.outputLine4.setReadOnly(True)
        self.outputLine5.setReadOnly(True)
        self.outputLine6.setReadOnly(True)
        self.outputLine7.setReadOnly(True)
        self.outputLine8.setReadOnly(True)
        self.calcButton = QPushButton("&Calc")
        self.calcButton.clicked.connect(self.calc)

        lineLayout = QGridLayout()

        lineLayout.addWidget(QLabel("Final volume: "), 0, 0)
        lineLayout.addWidget(self.inputLine, 0, 1)
        lineLayout.addWidget(QLabel("Master Mix X"), 1, 0)
        lineLayout.addWidget(self.inputLine2, 1, 1)
        lineLayout.addWidget(QLabel("############# Result ############"), 2, 0)
        lineLayout.addWidget(QLabel("DW water: "), 3, 0)
        lineLayout.addWidget(self.outputLine1, 3, 1)
        lineLayout.addWidget(QLabel("5X green: "), 4, 0)
        lineLayout.addWidget(self.outputLine2, 4, 1)
        lineLayout.addWidget(QLabel("Nucleotide Mix: "), 5, 0)
        lineLayout.addWidget(self.outputLine3, 5, 1)
        lineLayout.addWidget(QLabel("goTaq: "), 6, 0)
        lineLayout.addWidget(self.outputLine4, 6, 1)
        lineLayout.addWidget(QLabel("primer Foward: "), 7, 0)
        lineLayout.addWidget(self.outputLine5, 7, 1)
        lineLayout.addWidget(QLabel("primer Revese: "),8,0)
        lineLayout.addWidget(self.outputLine6, 8, 1)
        lineLayout.addWidget(QLabel("DNA template: "),9,0)
        lineLayout.addWidget(self.outputLine7,9,1)


        buttonLayout = QVBoxLayout()
        buttonLayout.addWidget(self.calcButton)

        mainLayout = QHBoxLayout()
        mainLayout.addLayout(lineLayout)
        mainLayout.addLayout(buttonLayout)

        self.w.setLayout(mainLayout)
        self.setWindowTitle("Calculate about MasterMix")

    def calc(self):
        final_volume = float(self.inputLine.text())
        Master_X = float(self.inputLine2.text())
        """
        vector_amount = float(self.inputLine3.text())
        insert_amount = float(self.inputLine4.text())
        vector_length = float(self.inputLine5.text())
        insert_length = float(self.inputLine6.text())
        """
        r = gotaq(final_volume,Master_X)
        #result = [Green, dNTP, pF, pR, taq, DNA, DW]
        self.outputLine1.setText(str(round(r[6],6)))#DW
        self.outputLine2.setText(str(round(r[0],6)))#Green
        self.outputLine3.setText(str(round(r[1], 6)))#dNTP
        self.outputLine4.setText(str(round(r[4], 6)))#gotaq
        self.outputLine5.setText(str(round(r[2], 6)))#primerF
        self.outputLine6.setText(str(round(r[3], 6)))#primerR
        self.outputLine7.setText(str(round(r[5], 6)))#DNA

    def show(self):
        self.w.exec_()

class Subwindow3(QWidget):
    def __init__(self, parent=None):
        super(Subwindow3, self).__init__(parent)

        self.w = QDialog(parent)
        self.w.setWindowTitle('ExTaq, Calculate about MasterMix')
        self.inputLine = QLineEdit()
        self.inputLine2 = QLineEdit()
        self.outputLine1 = QLineEdit()
        self.outputLine2 = QLineEdit()
        self.outputLine3 = QLineEdit()
        self.outputLine4 = QLineEdit()
        self.outputLine5 = QLineEdit()
        self.outputLine6 = QLineEdit()
        self.outputLine7 = QLineEdit()
        self.outputLine8 = QLineEdit()

        self.outputLine1.setReadOnly(True)
        self.outputLine2.setReadOnly(True)
        self.outputLine3.setReadOnly(True)
        self.outputLine4.setReadOnly(True)
        self.outputLine5.setReadOnly(True)
        self.outputLine6.setReadOnly(True)
        self.outputLine7.setReadOnly(True)
        self.outputLine8.setReadOnly(True)
        self.calcButton = QPushButton("&Calc")
        self.calcButton.clicked.connect(self.calc)

        lineLayout = QGridLayout()

        lineLayout.addWidget(QLabel("Final volume: "), 0, 0)
        lineLayout.addWidget(self.inputLine, 0, 1)
        lineLayout.addWidget(QLabel("Master Mix X"), 1, 0)
        lineLayout.addWidget(self.inputLine2, 1, 1)
        lineLayout.addWidget(QLabel("############# Result ############"), 2, 0)
        lineLayout.addWidget(QLabel("DW water: "), 3, 0)
        lineLayout.addWidget(self.outputLine1, 3, 1)
        lineLayout.addWidget(QLabel("10X buffer: "), 4, 0)
        lineLayout.addWidget(self.outputLine2, 4, 1)
        lineLayout.addWidget(QLabel("dNTP Mix: "), 5, 0)
        lineLayout.addWidget(self.outputLine3, 5, 1)
        lineLayout.addWidget(QLabel("Ex Taq: "), 6, 0)
        lineLayout.addWidget(self.outputLine4, 6, 1)
        lineLayout.addWidget(QLabel("primer Foward: "), 7, 0)
        lineLayout.addWidget(self.outputLine5, 7, 1)
        lineLayout.addWidget(QLabel("primer Revese: "),8,0)
        lineLayout.addWidget(self.outputLine6, 8, 1)
        lineLayout.addWidget(QLabel("DNA template: "),9,0)
        lineLayout.addWidget(self.outputLine7,9,1)


        buttonLayout = QVBoxLayout()
        buttonLayout.addWidget(self.calcButton)

        mainLayout = QHBoxLayout()
        mainLayout.addLayout(lineLayout)
        mainLayout.addLayout(buttonLayout)

        self.w.setLayout(mainLayout)
        self.setWindowTitle("Calculate about MasterMix")

    def calc(self):
        final_volume = float(self.inputLine.text())
        Master_X = float(self.inputLine2.text())

        r = extaq(final_volume,Master_X)
        #result = [Green, dNTP, pF, pR, taq, DNA, DW]
        self.outputLine1.setText(str(round(r[6],6)))#DW
        self.outputLine2.setText(str(round(r[0],6)))#Green
        self.outputLine3.setText(str(round(r[1], 6)))#dNTP
        self.outputLine4.setText(str(round(r[4], 6)))#gotaq
        self.outputLine5.setText(str(round(r[2], 6)))#primerF
        self.outputLine6.setText(str(round(r[3], 6)))#primerR
        self.outputLine7.setText(str(round(r[5], 6)))#DNA

class Subwindow4(QWidget):
    def __init__(self, parent=None):
            super(Subwindow4, self).__init__(parent)

            self.w = QDialog(parent)
            self.w.setWindowTitle('KODplus, Calculate about MasterMix')
            self.inputLine = QLineEdit()
            self.inputLine2 = QLineEdit()
            self.outputLine1 = QLineEdit()
            self.outputLine2 = QLineEdit()
            self.outputLine3 = QLineEdit()
            self.outputLine4 = QLineEdit()
            self.outputLine5 = QLineEdit()
            self.outputLine6 = QLineEdit()
            self.outputLine7 = QLineEdit()
            self.outputLine8 = QLineEdit()
            self.outputline9 = QLineEdit()

            self.outputLine1.setReadOnly(True)
            self.outputLine2.setReadOnly(True)
            self.outputLine3.setReadOnly(True)
            self.outputLine4.setReadOnly(True)
            self.outputLine5.setReadOnly(True)
            self.outputLine6.setReadOnly(True)
            self.outputLine7.setReadOnly(True)
            self.outputLine8.setReadOnly(True)
            self.outputline9.setReadOnly(True)
            self.calcButton = QPushButton("&Calc")
            self.calcButton.clicked.connect(self.calc)

            lineLayout = QGridLayout()

            lineLayout.addWidget(QLabel("Final volume: "), 0, 0)
            lineLayout.addWidget(self.inputLine, 0, 1)
            lineLayout.addWidget(QLabel("Master Mix X"), 1, 0)
            lineLayout.addWidget(self.inputLine2, 1, 1)
            lineLayout.addWidget(QLabel("############# Result ############"), 2, 0)
            lineLayout.addWidget(QLabel("DW water: "), 3, 0)
            lineLayout.addWidget(self.outputLine1, 3, 1)
            lineLayout.addWidget(QLabel("10X buffer: "), 4, 0)
            lineLayout.addWidget(self.outputLine2, 4, 1)
            lineLayout.addWidget(QLabel("dNTP Mix: "), 5, 0)
            lineLayout.addWidget(self.outputLine3, 5, 1)
            lineLayout.addWidget(QLabel("MgSO4: "), 6, 0)
            lineLayout.addWidget(self.outputLine4, 6, 1)
            lineLayout.addWidget(QLabel("KODplus: "), 7, 0)
            lineLayout.addWidget(self.outputLine5, 7, 1)
            lineLayout.addWidget(QLabel("primer Forward: "), 8, 0)
            lineLayout.addWidget(self.outputLine6, 8, 1)
            lineLayout.addWidget(QLabel("primer Reverse: "), 9, 0)
            lineLayout.addWidget(self.outputLine7, 9, 1)
            lineLayout.addWidget(QLabel("DNA template: "), 10, 0)
            lineLayout.addWidget(self.outputLine8, 10, 1)


            buttonLayout = QVBoxLayout()
            buttonLayout.addWidget(self.calcButton)

            mainLayout = QHBoxLayout()
            mainLayout.addLayout(lineLayout)
            mainLayout.addLayout(buttonLayout)

            self.w.setLayout(mainLayout)
            self.setWindowTitle("Calculate about MasterMix")

    def calc(self):
            final_volume = float(self.inputLine.text())
            Master_X = float(self.inputLine2.text())

            r = KODplus(final_volume, Master_X)
            #  result = [buffer, dNTP, MgSO4, pF, pR, taq, DNA, DW]
            self.outputLine1.setText(str(round(r[7], 6)))  # DW
            self.outputLine2.setText(str(round(r[0], 6)))  # 10Xbuffer
            self.outputLine3.setText(str(round(r[1], 6)))  # dNTP
            self.outputLine4.setText(str(round(r[2], 6)))  # MgSO4
            self.outputLine5.setText(str(round(r[5], 6)))  # KODplus
            self.outputLine6.setText(str(round(r[3], 6)))  # primerF
            self.outputLine7.setText(str(round(r[4], 6)))  # primerR
            self.outputLine8.setText(str(round(r[6], 6)))  # DNA

    def show(self):
        self.w.exec_()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    pprint("input parameters = " + str(sys.argv))
    window = IndexWindow()
    window.show()
    sys.exit(app.exec_())