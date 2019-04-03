# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\cpsc2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import json
import requests
import csv

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(644, 325)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.productNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.productNameLabel.setGeometry(QtCore.QRect(40, 150, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.productNameLabel.setFont(font)
        self.productNameLabel.setObjectName("productNameLabel")
        self.itemLabel = QtWidgets.QLabel(self.centralwidget)
        self.itemLabel.setGeometry(QtCore.QRect(40, 30, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.itemLabel.setFont(font)
        self.itemLabel.setObjectName("itemLabel")
        self.titleBox = QtWidgets.QComboBox(self.centralwidget)
        self.titleBox.setGeometry(QtCore.QRect(200, 30, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.titleBox.setFont(font)
        self.titleBox.setObjectName("titleBox")
        self.titleBox.addItem("")
        self.titleBox.addItem("")
        self.titleBox.addItem("")
        self.titleBox.addItem("")
        self.titleBox.addItem("")
        self.titleBox.addItem("")
        self.titleBox.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 210, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.manufacturerLabel = QtWidgets.QLabel(self.centralwidget)
        self.manufacturerLabel.setGeometry(QtCore.QRect(40, 90, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.manufacturerLabel.setFont(font)
        self.manufacturerLabel.setObjectName("manufacturerLabel")
        self.recallDateStart = QtWidgets.QSpinBox(self.centralwidget)
        self.recallDateStart.setGeometry(QtCore.QRect(200, 210, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.recallDateStart.setFont(font)
        self.recallDateStart.setMinimum(2005)
        self.recallDateStart.setMaximum(2019)
        self.recallDateStart.setObjectName("recallDateStart")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(470, 30, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.manufacturer = QtWidgets.QLineEdit(self.centralwidget)
        self.manufacturer.setGeometry(QtCore.QRect(200, 90, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.manufacturer.setFont(font)
        self.manufacturer.setObjectName("manufacturer")
        self.productName = QtWidgets.QLineEdit(self.centralwidget)
        self.productName.setGeometry(QtCore.QRect(200, 150, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.productName.setFont(font)
        self.productName.setObjectName("productName")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 644, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.CPSCCall)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def CPSCCall(self):
        title = self.titleBox.currentText()
        manufacturer = self.manufacturer.text()
        recalldatestart = self.recallDateStart.text()
        productname = self.productName.text()
        title = title.replace(" ","%20")
        manufacturer = manufacturer.replace(" ","%20")
        productname = productname.replace(" ","%20")
        base_url = 'https://www.saferproducts.gov/RestWebServices/Recall?Format=JSON' + '&RecallDateStart=' + '{}'.format(recalldatestart)
        
        if title != '':
            title_query_string = '&Title=' + '{}'.format(title)
        else:
            title_query_string = ''
        
        if manufacturer != '':
            manu_query_string = '&Manufacturer=' + '{}'.format(manufacturer)
        else:
            manu_query_string=''
        
        if productname != '':
            prodname_query_string = '&ProductName=' + '{}'.format(productname)
        else:
            prodname_query_string = ''
        
        call_url = base_url + title_query_string + manu_query_string + prodname_query_string

        print(call_url)

        result = requests.get(call_url)

        recalls = json.loads(result.content)

        RecallID = []
        RecallDate = []
        RecallNumber = []
        Description = []
        URL = []
        Title = []
        ProductName = []
        ProductType = []
        ProductCatID = []
        Manufacturer = []
        Hazards = []
        resplen = len(recalls)

        for i in range(resplen):
            RecallID.append(recalls[i]['RecallID'])
        for i in range(resplen):
            RecallDate.append(recalls[i]['RecallDate'])
        for i in range(resplen):
            RecallNumber.append(recalls[i]['RecallNumber'])
        for i in range(resplen):
            Description.append(recalls[i]['Description'])
        for i in range(resplen):
            foo = len(recalls[i]['Products'])
            bar = []
            if (foo == 0):
                ProductName.append('')
            else:
                for j in range(foo):
                    bar.append(recalls[i]['Products'][j]['Name'])
                ProductName.append(bar)
                
        for i in range(resplen):
            foo = len(recalls[i]['Products'])
            bar = []
            if (foo == 0):
                ProductType.append('')
            else:
                for j in range(foo):
                    bar.append(recalls[i]['Products'][j]['Type'])
                ProductType.append(bar)
        for i in range(resplen):
            foo = len(recalls[i]['Products'])
            bar = []
            if (foo == 0):
                ProductCatID.append('')
            else:
                for j in range(foo):
                    bar.append(recalls[i]['Products'][j]['CategoryID'])
                ProductCatID.append(bar)
        for i in range(resplen):
            Title.append(recalls[i]['Title'])
        for i in range(resplen):
            URL.append(recalls[i]['URL'])
        for i in range(resplen):
            foo = len(recalls[i]['Hazards'])
            bar = []
            for j in range(foo):
                bar.append(recalls[i]['Hazards'][j]['Name'])
            Hazards.append(bar)
        for i in range(resplen):
            foo = len(recalls[i]['Manufacturers'])
            bar = []
            for j in range(foo):
                bar.append(recalls[i]['Manufacturers'][j]['Name'])
            Manufacturer.append(bar)

        lists = [RecallID, RecallDate, RecallNumber, Description, URL, Title, ProductName, ProductType, ProductCatID, Manufacturer, Hazards]
        df = pd.concat([pd.Series(x) for x in lists], axis=1)
        df.columns = ['RecallID', 'RecallDate', 'RecallNumber', 'Description', 'URL', 'Title', 'ProductName', 'ProductType', 'ProductCatID', 'Manufacturer', 'Hazards']
        df.to_csv('C:/Recalls.csv', index = False)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.productNameLabel.setText(_translate("MainWindow", "Product Name"))
        self.itemLabel.setText(_translate("MainWindow", "Item"))
        self.titleBox.setItemText(0, _translate("MainWindow", "Car Seat"))
        self.titleBox.setItemText(1, _translate("MainWindow", "Crib"))
        self.titleBox.setItemText(2, _translate("MainWindow", "High Chair"))
        self.titleBox.setItemText(3, _translate("MainWindow", "Infant Seat"))
        self.titleBox.setItemText(4, _translate("MainWindow", "Stroller"))
        self.titleBox.setItemText(5, _translate("MainWindow", "Swing"))
        self.titleBox.setItemText(6, _translate("MainWindow", ""))
        self.label.setText(_translate("MainWindow", "Start Year"))
        self.manufacturerLabel.setText(_translate("MainWindow", "Manufacturer"))
        self.pushButton.setText(_translate("MainWindow", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

