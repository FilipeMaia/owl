# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pattersonProperties.ui'
#
# Created: Fri Sep 26 15:18:52 2014
#      by: pyside-uic 0.2.13 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from Qt import QtCore, QtGui

class Ui_PattersonProperties(object):
    def setupUi(self, PattersonProperties):
        PattersonProperties.setObjectName("PattersonProperties")
        PattersonProperties.resize(262, 317)
        self.gridLayout = QtGui.QGridLayout(PattersonProperties)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtGui.QLabel(PattersonProperties)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.maskSmooth = QtGui.QDoubleSpinBox(PattersonProperties)
        self.maskSmooth.setMinimum(0.0)
        self.maskSmooth.setMaximum(10000.0)
        self.maskSmooth.setObjectName("maskSmooth")
        self.gridLayout.addWidget(self.maskSmooth, 1, 1, 1, 1)
        self.darkfield = QtGui.QCheckBox(PattersonProperties)
        self.darkfield.setText("")
        self.darkfield.setObjectName("darkfield")
        self.gridLayout.addWidget(self.darkfield, 3, 1, 1, 1)
        self.label_4 = QtGui.QLabel(PattersonProperties)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        self.darkfieldX = QtGui.QSpinBox(PattersonProperties)
        self.darkfieldX.setMinimum(-10000)
        self.darkfieldX.setMaximum(10000)
        self.darkfieldX.setObjectName("darkfieldX")
        self.gridLayout.addWidget(self.darkfieldX, 4, 1, 1, 1)
        self.label_5 = QtGui.QLabel(PattersonProperties)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)
        self.imageThreshold = QtGui.QDoubleSpinBox(PattersonProperties)
        self.imageThreshold.setDecimals(3)
        self.imageThreshold.setMaximum(100000.0)
        self.imageThreshold.setProperty("value", 30.0)
        self.imageThreshold.setObjectName("imageThreshold")
        self.gridLayout.addWidget(self.imageThreshold, 0, 1, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pattersonPushButton = QtGui.QPushButton(PattersonProperties)
        self.pattersonPushButton.setObjectName("pattersonPushButton")
        self.verticalLayout.addWidget(self.pattersonPushButton)
        self.gridLayout.addLayout(self.verticalLayout, 7, 0, 1, 2)
        self.label = QtGui.QLabel(PattersonProperties)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.darkfieldSigma = QtGui.QSpinBox(PattersonProperties)
        self.darkfieldSigma.setObjectName("darkfieldSigma")
        self.gridLayout.addWidget(self.darkfieldSigma, 6, 1, 1, 1)
        self.darkfieldY = QtGui.QSpinBox(PattersonProperties)
        self.darkfieldY.setMinimum(-10000)
        self.darkfieldY.setMaximum(10000)
        self.darkfieldY.setObjectName("darkfieldY")
        self.gridLayout.addWidget(self.darkfieldY, 5, 1, 1, 1)
        self.label_3 = QtGui.QLabel(PattersonProperties)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.label_6 = QtGui.QLabel(PattersonProperties)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_7 = QtGui.QLabel(PattersonProperties)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)
        self.maskThreshold = QtGui.QDoubleSpinBox(PattersonProperties)
        self.maskThreshold.setDecimals(3)
        self.maskThreshold.setMaximum(1.0)
        self.maskThreshold.setSingleStep(0.01)
        self.maskThreshold.setObjectName("maskThreshold")
        self.gridLayout.addWidget(self.maskThreshold, 2, 1, 1, 1)

        self.retranslateUi(PattersonProperties)
        QtCore.QMetaObject.connectSlotsByName(PattersonProperties)

    def retranslateUi(self, PattersonProperties):
        PattersonProperties.setWindowTitle(QtGui.QApplication.translate("PattersonProperties", "Patterson Properties", None, QtGui.QApplication.UnicodeUTF8))
        PattersonProperties.setTitle(QtGui.QApplication.translate("PattersonProperties", "Patterson Properties", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("PattersonProperties", "Dark field:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("PattersonProperties", "Dark field Y:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("PattersonProperties", "Dark field sigma:", None, QtGui.QApplication.UnicodeUTF8))
        self.pattersonPushButton.setText(QtGui.QApplication.translate("PattersonProperties", "Patterson", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("PattersonProperties", "Mask smooth:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("PattersonProperties", "Dark field X:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("PattersonProperties", "Image threshold:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("PattersonProperties", "Mask threshold:", None, QtGui.QApplication.UnicodeUTF8))

