# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guncelle.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormG(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(339, 358)
        Form.setMaximumSize(QtCore.QSize(339, 358))
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 321, 351))
        self.groupBox.setMaximumSize(QtCore.QSize(331, 351))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.lb_urunAdi = QtWidgets.QLabel(self.groupBox)
        self.lb_urunAdi.setGeometry(QtCore.QRect(10, 50, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lb_urunAdi.setFont(font)
        self.lb_urunAdi.setObjectName("lb_urunAdi")
        self.lb_urunAcklamasi = QtWidgets.QLabel(self.groupBox)
        self.lb_urunAcklamasi.setGeometry(QtCore.QRect(10, 120, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lb_urunAcklamasi.setFont(font)
        self.lb_urunAcklamasi.setObjectName("lb_urunAcklamasi")
        self.ln_urunAdi_guncel = QtWidgets.QLineEdit(self.groupBox)
        self.ln_urunAdi_guncel.setGeometry(QtCore.QRect(180, 50, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.ln_urunAdi_guncel.setFont(font)
        self.ln_urunAdi_guncel.setObjectName("ln_urunAdi_guncel")
        self.ln_urunAciklamasi_guncel = QtWidgets.QLineEdit(self.groupBox)
        self.ln_urunAciklamasi_guncel.setGeometry(QtCore.QRect(180, 130, 113, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.ln_urunAciklamasi_guncel.setFont(font)
        self.ln_urunAciklamasi_guncel.setObjectName("ln_urunAciklamasi_guncel")
        self.bt_guncelle = QtWidgets.QPushButton(self.groupBox)
        self.bt_guncelle.setGeometry(QtCore.QRect(0, 310, 93, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.bt_guncelle.setFont(font)
        self.bt_guncelle.setObjectName("bt_guncelle")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.ln_depoKodu_guncel = QtWidgets.QLineEdit(self.groupBox)
        self.ln_depoKodu_guncel.setGeometry(QtCore.QRect(180, 90, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.ln_depoKodu_guncel.setFont(font)
        self.ln_depoKodu_guncel.setObjectName("ln_depoKodu_guncel")
        self.ln_RafNo_Guncel = QtWidgets.QLineEdit(self.groupBox)
        self.ln_RafNo_Guncel.setGeometry(QtCore.QRect(180, 210, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.ln_RafNo_Guncel.setFont(font)
        self.ln_RafNo_Guncel.setObjectName("ln_RafNo_Guncel")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 170, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 250, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.ln_markaEkle_guncel = QtWidgets.QLineEdit(self.groupBox)
        self.ln_markaEkle_guncel.setGeometry(QtCore.QRect(180, 250, 113, 22))
        self.ln_markaEkle_guncel.setObjectName("ln_markaEkle_guncel")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 210, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.ln_dolapNo_guncel = QtWidgets.QLineEdit(self.groupBox)
        self.ln_dolapNo_guncel.setGeometry(QtCore.QRect(180, 170, 113, 22))
        self.ln_dolapNo_guncel.setObjectName("ln_dolapNo_guncel")
        self.Doldur = QtWidgets.QPushButton(self.groupBox)
        self.Doldur.setGeometry(QtCore.QRect(100, 310, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.Doldur.setFont(font)
        self.Doldur.setObjectName("Doldur")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Güncelle"))
        self.groupBox.setTitle(_translate("Form", "Güncelle"))
        self.lb_urunAdi.setText(_translate("Form", "Ürün Adı:"))
        self.lb_urunAcklamasi.setText(_translate("Form", "Ürün Açıklaması:"))
        self.bt_guncelle.setText(_translate("Form", "Güncelle"))
        self.label_2.setText(_translate("Form", "Depo Kodu:"))
        self.label.setText(_translate("Form", "Dolap No:"))
        self.label_3.setText(_translate("Form", "Marka:"))
        self.label_6.setText(_translate("Form", "Raf No:"))
        self.Doldur.setText(_translate("Form", "Otomatik Doldur"))