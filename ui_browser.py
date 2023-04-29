# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'browser.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BrowserWindow(object):
	def setupUi(self, BrowserWindow):
		BrowserWindow.setObjectName("BrowserWindow")
		BrowserWindow.resize(800, 600)
		self.centralwidget = QtWidgets.QWidget(BrowserWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
		self.verticalLayout.setObjectName("verticalLayout")
		self.horizontalLayout = QtWidgets.QHBoxLayout()
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.searchButton = QtWidgets.QPushButton(self.centralwidget)
		self.searchButton.setObjectName("searchButton")
		self.horizontalLayout.addWidget(self.searchButton)
		self.searchLine = QtWidgets.QLineEdit(self.centralwidget)
		self.searchLine.setObjectName("searchLine")
		self.horizontalLayout.addWidget(self.searchLine)
		self.verticalLayout.addLayout(self.horizontalLayout)
		self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_2.setObjectName("horizontalLayout_2")
		self.moduleTree = QtWidgets.QTreeWidget(self.centralwidget)
		self.moduleTree.setObjectName("moduleTree")
		self.horizontalLayout_2.addWidget(self.moduleTree)
		self.docEdit = QtWidgets.QTextEdit(self.centralwidget)
		self.docEdit.setObjectName("docEdit")
		self.horizontalLayout_2.addWidget(self.docEdit)
		self.verticalLayout.addLayout(self.horizontalLayout_2)
		BrowserWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(BrowserWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
		self.menubar.setObjectName("menubar")
		self.menu_File = QtWidgets.QMenu(self.menubar)
		self.menu_File.setObjectName("menu_File")
		BrowserWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(BrowserWindow)
		self.statusbar.setObjectName("statusbar")
		BrowserWindow.setStatusBar(self.statusbar)
		self.actionExit = QtWidgets.QAction(BrowserWindow)
		self.actionExit.setObjectName("actionExit")
		self.menu_File.addAction(self.actionExit)
		self.menubar.addAction(self.menu_File.menuAction())

		self.retranslateUi(BrowserWindow)
		QtCore.QMetaObject.connectSlotsByName(BrowserWindow)
		BrowserWindow.setTabOrder(self.searchLine, self.moduleTree)
		BrowserWindow.setTabOrder(self.moduleTree, self.docEdit)
		BrowserWindow.setTabOrder(self.docEdit, self.searchButton)

	def retranslateUi(self, BrowserWindow):
		_translate = QtCore.QCoreApplication.translate
		BrowserWindow.setWindowTitle(_translate("BrowserWindow", "Module Browser"))
		self.searchButton.setText(_translate("BrowserWindow", "&Search"))
		self.moduleTree.headerItem().setText(0, _translate("BrowserWindow", "Name"))
		self.moduleTree.headerItem().setText(1, _translate("BrowserWindow", "Type"))
		self.menu_File.setTitle(_translate("BrowserWindow", "&File"))
		self.actionExit.setText(_translate("BrowserWindow", "E&xit"))
