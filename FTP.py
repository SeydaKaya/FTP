# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from ftplib import FTP
import ftplib
import sys
import os




class Ui_MainWindow(object):
    ftp = None
    
    def Connect(self):
        try:
            self.userName=self.user_name.text()
            self.passWord=self.password.text()
            self.ipNumber=self.ip_address.text()
            self.Port=self.port.text()
            
            if self.userName != "" and self.passWord != "" and self.ipNumber != "" and self.Port != "":
                if self.ftp != None:
                    self.disconnect()
                
                self.Port=int(self.Port)
                self.ftp = FTP()
                self.ftp.encoding = "UTF-8"
                self.fonk_sonuclari.append("Durum : "+self.ftp.connect(host=self.ipNumber, port=self.Port))
                login = self.ftp.login(user=self.userName, passwd=self.passWord)
                self.fonk_sonuclari.append(login)
                self.showFiles()
        except ftplib.all_errors as e:
            self.fonk_sonuclari.append("Hata : " + e.args[0])
         
    def showFiles(self):
        if self.ftp != None:
            try:
                self.uzak_text.setText("")
                self.local_text.setText("")
                for x in self.ftp.mlsd(facts=["type", "size", "perm"]):
                    dosyaAdi = ""
                    if x[1]["type"] == "dir":
                        dosyaAdi += "// "
                    dosyaAdi += x[0]
                    self.uzak_text.append(dosyaAdi)
                     
                for x in os.listdir():
                    dosyaAdi = ""
                    if os.path.isdir(x):
                        dosyaAdi += "// "
                    dosyaAdi += x
                    self.local_text.append(dosyaAdi)
            except ftplib.all_errors as e:
                self.fonk_sonuclari.append("Hata : " + e.args[0])
          
    def fileUpload(self):
        if self.ftp != None:
            try:
                file_name=self.line_fileName.text()
                myFile=open(file_name,'rb')
                self.fonk_sonuclari.append("Durum : "+self.ftp.storbinary('STOR '+file_name, myFile))
                self.showFiles()
            except os.error as e:
                self.fonk_sonuclari.append("Hata : " + e.args[1])
            except ftplib.all_errors as e:
                self.fonk_sonuclari.append("Hata : " + e.args[0])
    
    def fileDownload(self):
        if self.ftp != None:
            try:
                file_name=self.line_fileName.text()
                myFile = open(file_name,'wb')
                self.fonk_sonuclari.append("Durum : "+self.ftp.retrbinary('RETR '+file_name, myFile.write))
                self.showFiles()
            except ftplib.all_errors as e:
                self.fonk_sonuclari.append("Hata : " + e.args[0])
         
    def createFolder(self):
        if self.ftp != None:
            try:
                folderName=self.line_folderName.text()
                self.fonk_sonuclari.append(self.ftp.mkd(folderName))
                self.showFiles()
            except ftplib.all_errors as e:
                self.fonk_sonuclari.append("Hata : " + e.args[0])
        
    def deleteFolder(self):
        if self.ftp != None:
            try:
                folderName=self.line_folderName.text()
                self.fonk_sonuclari.append("Durum : "+self.ftp.rmd(folderName))
                self.showFiles()
            except ftplib.all_errors as e:
                self.fonk_sonuclari.append("Hata : " + e.args[0])
        
    def renameFile(self):
        if self.ftp != None:
            try:
                availableName=self.av_file_name.text()
                newFileName=self.new_file_name.text()
                self.fonk_sonuclari.append("Durum : "+self.ftp.rename(availableName, newFileName))
                self.showFiles()
            except ftplib.all_errors as e:
                self.fonk_sonuclari.append("Hata : " + e.args[0])
    
    def deleteFile(self):
        if self.ftp != None:
            try:
                fileName=self.line_fileName.text()
                self.fonk_sonuclari.append("Durum : "+self.ftp.delete(fileName))
                self.showFiles()
            except ftplib.all_errors as e:
                self.fonk_sonuclari.append("Hata : " + e.args[0])
         
    def disconnect(self):
        if self.ftp != None:
            self.fonk_sonuclari.append("Durum : "+self.ftp.quit())
            self.ftp.close()
            self.ftp = None
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.username = QtWidgets.QLabel(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(40, 10, 61, 16))
        self.username.setObjectName("username")
        self.label_file= QtWidgets.QLabel(self.centralwidget)
        self.label_file.setGeometry(QtCore.QRect(330, 10, 71, 20))
        self.label_file.setObjectName("label_file")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 50, 61, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 90, 61, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 130, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(590, 10, 77, 13))
        self.label_7.setObjectName("label_7")
        self.connect_btn = QtWidgets.QPushButton(self.centralwidget)
        self.connect_btn.setGeometry(QtCore.QRect(110, 160, 111, 23))
        self.connect_btn.setObjectName("connect_btn")
        self.deleteFile_btn = QtWidgets.QPushButton(self.centralwidget)
        self.deleteFile_btn.setGeometry(QtCore.QRect(410, 100, 111, 23))
        self.deleteFile_btn.setObjectName("deleteFile_btn")
        self.upload_btn = QtWidgets.QPushButton(self.centralwidget)
        self.upload_btn.setGeometry(QtCore.QRect(410, 40, 111, 23))
        self.upload_btn.setObjectName("upload_btn")
        self.download_btn = QtWidgets.QPushButton(self.centralwidget)
        self.download_btn.setGeometry(QtCore.QRect(410, 70, 111, 23))
        self.download_btn.setObjectName("download_btn")
        self.create_btn = QtWidgets.QPushButton(self.centralwidget)
        self.create_btn.setGeometry(QtCore.QRect(680, 40, 111, 23))
        self.create_btn.setObjectName("create_btn")
        self.delete_btn = QtWidgets.QPushButton(self.centralwidget)
        self.delete_btn.setGeometry(QtCore.QRect(680, 70, 111, 23))
        self.delete_btn.setObjectName("delete_btn")
        self.rename_btn = QtWidgets.QPushButton(self.centralwidget)
        self.rename_btn.setGeometry(QtCore.QRect(570, 200, 111, 23))
        self.rename_btn.setObjectName("rename_btn")
        self.disconnet_btn = QtWidgets.QPushButton(self.centralwidget)
        self.disconnet_btn.setGeometry(QtCore.QRect(110, 190, 111, 23))
        self.disconnet_btn.setObjectName("disconnet_btn")
        self.user_name = QtWidgets.QLineEdit(self.centralwidget)
        self.user_name.setGeometry(QtCore.QRect(110, 10, 113, 20))
        self.user_name.setObjectName("user_name")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(110, 50, 113, 20))
        self.password.setObjectName("password")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ip_address = QtWidgets.QLineEdit(self.centralwidget)
        self.ip_address.setGeometry(QtCore.QRect(110, 90, 113, 20))
        self.ip_address.setObjectName("ip_address")
        self.port = QtWidgets.QLineEdit(self.centralwidget)
        self.port.setGeometry(QtCore.QRect(110, 130, 113, 20))
        self.port.setObjectName("port")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(450, 140, 121, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(480, 170, 111, 20))
        self.label_6.setObjectName("label_6")
        self.av_file_name = QtWidgets.QLineEdit(self.centralwidget)
        self.av_file_name.setGeometry(QtCore.QRect(570, 140, 113, 20))
        self.av_file_name.setObjectName("av_file_name")
        self.new_file_name = QtWidgets.QLineEdit(self.centralwidget)
        self.new_file_name.setGeometry(QtCore.QRect(570, 170, 113, 20))
        self.new_file_name.setObjectName("new_file_name")
        self.line_fileName=QtWidgets.QLineEdit(self.centralwidget)
        self.line_fileName.setGeometry(QtCore.QRect(410, 10, 113, 20))
        self.line_fileName.setObjectName("line_fileName")
        self.line_folderName= QtWidgets.QLineEdit(self.centralwidget)
        self.line_folderName.setGeometry(QtCore.QRect(680, 10, 113, 20))
        self.line_folderName.setObjectName("line_folderName")
        
        self.local_text = QtWidgets.QTextEdit(self.centralwidget)
        self.local_text.setGeometry(QtCore.QRect(30, 380, 351, 171))
        self.local_text.setObjectName("local_text")
        self.local_text.setReadOnly(True)
        self.uzak_text = QtWidgets.QTextEdit(self.centralwidget)
        self.uzak_text.setGeometry(QtCore.QRect(420, 380, 351, 171))
        self.uzak_text.setObjectName("uzak_text")
        self.local_text.setReadOnly(True)
        self.fonk_sonuclari = QtWidgets.QTextEdit(self.centralwidget)
        self.fonk_sonuclari.setGeometry(QtCore.QRect(30, 250, 741, 101))
        self.fonk_sonuclari.setObjectName("fonk_sonuclari")
        self.fonk_sonuclari.setReadOnly(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        
        self.connect_btn.clicked.connect(self.Connect)
        self.deleteFile_btn.clicked.connect(self.deleteFile)
        self.disconnet_btn.clicked.connect(self.disconnect)
        self.upload_btn.clicked.connect(self.fileUpload)
        self.download_btn.clicked.connect(self.fileDownload)
        self.create_btn.clicked.connect(self.createFolder)
        self.delete_btn.clicked.connect(self.deleteFolder)
        self.rename_btn.clicked.connect(self.renameFile)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
            
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.username.setText(_translate("MainWindow", "USER NAME:"))
        self.label_2.setText(_translate("MainWindow", "PASSWORD:"))
        self.label_3.setText(_translate("MainWindow", "IP ADDRESS:"))
        self.label_4.setText(_translate("MainWindow", "PORT:"))
        self.connect_btn.setText(_translate("MainWindow", "CONNECT"))
        self.deleteFile_btn.setText(_translate("MainWindow", "DELETE FILE"))
        self.upload_btn.setText(_translate("MainWindow", "FILE UPLOAD"))
        self.download_btn.setText(_translate("MainWindow", "FILE DOWNLOAD"))
        self.create_btn.setText(_translate("MainWindow", "CREATE FOLDER"))
        self.delete_btn.setText(_translate("MainWindow", "DELETE FOLDER"))
        self.rename_btn.setText(_translate("MainWindow", "FILE RENAME"))
        self.disconnet_btn.setText(_translate("MainWindow", "DISCONNECT"))
        self.label_5.setText(_translate("MainWindow", "AVAILABLE FILE NAME :"))
        self.label_6.setText(_translate("MainWindow", "NEW FILE NAME :"))
        self.label_file.setText(_translate("MainWindow", "FILE NAME :"))
        self.label_7.setText(_translate("MainWindow", "FOLDER NAME :"))
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()

