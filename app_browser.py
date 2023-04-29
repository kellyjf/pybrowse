#!/usr/bin/python3
# -*- coding: utf-8 -*-

# =========== TEMPLATE FILE =====================
# Replace LROOT with ui_* filename (LROOT=media)
# Replace CROOT with wrapper class name (CROOT=MediaDialog)
# =========== TEMPLATE FILE =====================

from PyQt5 import QtCore, QtGui, QtWidgets
from argparse import ArgumentParser as ap
import locale

from ui_browser import Ui_BrowserWindow

class TreeItem(QtWidgets.QTreeWidgetItem):
	def __init__(self, widget, data=None):
		self.userdata=data
		super().__init__(widget)

class BrowserWindow(QtWidgets.QMainWindow, Ui_BrowserWindow):

	# custom_signal=QtCore.pyqtSignal(int)

	def __init__(self, parent=None):
		super(QtWidgets.QMainWindow,self).__init__(parent)
		self.setupUi(self)
		self.searchButton.clicked.connect(self.search)
		self.searchLine.returnPressed.connect(self.search)
		self.moduleTree.currentItemChanged.connect(self.detail)
		#self.moduleTree.itemDoubleClicked.connect(self.detail)
		self.searchLine.setFocus()
		self.dejavu={}

	def detail(self, item, oitem):
		elem=item.userdata
		self.docEdit.setPlainText(elem.__doc__)
		self.moduleTree.resizeColumnToContents(0)

	def add_level(self,parent, level=0):
		mod=parent.userdata
		for key in mod.__dict__.keys():
			elem=mod.__dict__.get(key)
			atype=str(type(elem))
			child=TreeItem([key,atype],elem)
			parent.addChild(child)
			if 'module' in atype and elem not in self.dejavu and key[0] != '_':
				self.dejavu[elem]=1
				print(level,key,atype)
				self.add_level(child, level+1)

	def setModule(self, modname):
		self.searchLine.setText(modname)
		self.search()
		
	def search(self):
		self.moduleTree.clear()
		self.dejavu={}
		modname=self.searchLine.text()
		module=__import__(modname)
		parent=TreeItem([modname,"module"],module)
		self.moduleTree.addTopLevelItem(parent)

		self.add_level(parent)

if __name__ == "__main__":
	import sys
	import signal

	parser=ap()
	parser.add_argument("word", nargs='?', action='store',  help="Word")
	parser.add_argument("--quiet", action='store_true',  help="Run quietly")
	parser.add_argument("--limit", action='store', type=int,  help="limit")
	args=parser.parse_args()

	signal.signal(signal.SIGINT,signal.SIG_DFL)
	
	app = QtWidgets.QApplication(sys.argv)
	win=BrowserWindow()
	if args.word:
		win.setModule(args.word)
	win.show()

	sys.exit(app.exec_())

