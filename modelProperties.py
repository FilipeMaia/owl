# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modelProperties.ui'
#
# Created: Tue Jul  8 00:10:26 2014
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ModelProperties(object):
    def setupUi(self, ModelProperties):
        ModelProperties.setObjectName("ModelProperties")
        ModelProperties.resize(262, 328)
        self.gridLayout = QtGui.QGridLayout(ModelProperties)
        self.gridLayout.setObjectName("gridLayout")
        self.centerY = QtGui.QDoubleSpinBox(ModelProperties)
        self.centerY.setMinimum(-10000.0)
        self.centerY.setMaximum(10000.0)
        self.centerY.setObjectName("centerY")
        self.gridLayout.addWidget(self.centerY, 1, 1, 1, 1)
        self.centerX = QtGui.QDoubleSpinBox(ModelProperties)
        self.centerX.setMinimum(-10000.0)
        self.centerX.setMaximum(10000.0)
        self.centerX.setObjectName("centerX")
        self.gridLayout.addWidget(self.centerX, 0, 1, 1, 1)
        self.scaling = QtGui.QDoubleSpinBox(ModelProperties)
        self.scaling.setDecimals(5)
        self.scaling.setMaximum(100.0)
        self.scaling.setSingleStep(0.1)
        self.scaling.setProperty("value", 1.0)
        self.scaling.setObjectName("scaling")
        self.gridLayout.addWidget(self.scaling, 3, 1, 1, 1)
        self.diameter = QtGui.QDoubleSpinBox(ModelProperties)
        self.diameter.setMaximum(10000.0)
        self.diameter.setSingleStep(5.0)
        self.diameter.setProperty("value", 100.0)
        self.diameter.setObjectName("diameter")
        self.gridLayout.addWidget(self.diameter, 2, 1, 1, 1)
        self.label_3 = QtGui.QLabel(ModelProperties)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label = QtGui.QLabel(ModelProperties)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_4 = QtGui.QLabel(ModelProperties)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_2 = QtGui.QLabel(ModelProperties)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.visibilitySlider = QtGui.QSlider(ModelProperties)
        self.visibilitySlider.setMinimum(-1)
        self.visibilitySlider.setMaximum(101)
        self.visibilitySlider.setProperty("value", 50)
        self.visibilitySlider.setOrientation(QtCore.Qt.Horizontal)
        self.visibilitySlider.setObjectName("visibilitySlider")
        self.verticalLayout.addWidget(self.visibilitySlider)
        self.experiment = QtGui.QPushButton(ModelProperties)
        self.experiment.setObjectName("experiment")
        self.verticalLayout.addWidget(self.experiment)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fitCenterPushButton = QtGui.QPushButton(ModelProperties)
        self.fitCenterPushButton.setObjectName("fitCenterPushButton")
        self.horizontalLayout.addWidget(self.fitCenterPushButton)
        self.fitModelPushButton = QtGui.QPushButton(ModelProperties)
        self.fitModelPushButton.setObjectName("fitModelPushButton")
        self.horizontalLayout.addWidget(self.fitModelPushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 5, 0, 1, 2)
        self.label_5 = QtGui.QLabel(ModelProperties)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.maskRadius = QtGui.QSpinBox(ModelProperties)
        self.maskRadius.setMaximum(10000)
        self.maskRadius.setProperty("value", 100)
        self.maskRadius.setObjectName("maskRadius")
        self.gridLayout.addWidget(self.maskRadius, 4, 1, 1, 1)

        self.retranslateUi(ModelProperties)
        QtCore.QMetaObject.connectSlotsByName(ModelProperties)

    def retranslateUi(self, ModelProperties):
        ModelProperties.setWindowTitle(QtGui.QApplication.translate("ModelProperties", "Model Properties", None, QtGui.QApplication.UnicodeUTF8))
        ModelProperties.setTitle(QtGui.QApplication.translate("ModelProperties", "Model Properties", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ModelProperties", "Diameter [nm]:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ModelProperties", "Center X [px]:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ModelProperties", "Intensity [mJ/µm2]:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ModelProperties", "Center Y [px]:", None, QtGui.QApplication.UnicodeUTF8))
        self.experiment.setText(QtGui.QApplication.translate("ModelProperties", "Experiment...", None, QtGui.QApplication.UnicodeUTF8))
        self.fitCenterPushButton.setText(QtGui.QApplication.translate("ModelProperties", "Fit center", None, QtGui.QApplication.UnicodeUTF8))
        self.fitModelPushButton.setText(QtGui.QApplication.translate("ModelProperties", "Fit model", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("ModelProperties", "Mask radius [px]:", None, QtGui.QApplication.UnicodeUTF8))
