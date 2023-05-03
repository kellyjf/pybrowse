#!/usr/bin/python3
# -*- coding: utf-8 -*-

# =========== TEMPLATE FILE =====================
# Replace LROOT with ui_* filename (LROOT=media)
# Replace CROOT with wrapper class name (CROOT=MediaDialog)
# =========== TEMPLATE FILE =====================

from PyQt5 import QtCore, QtGui, QtWidgets
from argparse import ArgumentParser as ap
import locale
import re

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
		#self.moduleTree.itemDoubleClicked.connect(self.expand)
		self.moduleTree.itemActivated.connect(self.expand)
		self.searchLine.setFocus()
		self.dejavu={}
		self.regex=re.compile("<class '(.*)'>")
	def expand(self, item):
		self.add_module(item)

	def detail(self, item, oitem):
		elem=item.userdata
		if item.text(1) in ['str','int','list','dict']:
			self.docEdit.setPlainText(str(elem))
		else:
			self.docEdit.setPlainText(elem.__doc__)

	def add_module(self,parent):
		mod=parent.userdata
		for key in mod.__dict__.keys():
			elem=mod.__dict__.get(key)
			atype=str(type(elem))
			mat=self.regex.match(atype)
			if mat:
				btype=mat.group(1)
				child=TreeItem([key,btype],elem)
				if 'module' in btype:
					font=child.font(0)
					font.setBold(True)
					child.setFont(0,font)
				elif 'function' in btype:
					child.setForeground(0,QtGui.QBrush(QtGui.QColor(0,255,0)))
				elif '.' in btype:
					child.setForeground(0,QtGui.QBrush(QtGui.QColor(0,0,255)))
			else:
				child=helpers.TreeItem([key,atype],elem)
			parent.addChild(child)

		self.moduleTree.expandItem(parent)
		self.moduleTree.resizeColumnToContents(1)
		self.moduleTree.resizeColumnToContents(0)

	def setModule(self, module):
		self.moduleTree.clear()
		self.dejavu={}
		self.module=module
		if "__name__" in dir(module):
			name=module.__name__
		else:
			name=str(module)
		parent=TreeItem([name,"module"],module)
		self.moduleTree.addTopLevelItem(parent)
		self.add_module(parent)
	
	def search(self, modname=None):
		if modname:
			self.searchLine.setText(modname)
		modname=self.searchLine.text()
		module=__import__(modname)

		self.setModule(module)

_app=QtWidgets.QApplication([])
_win=BrowserWindow()

def getBrowser(module):
	_win.setModule(module)
	_win.show()
	
	
if __name__ == "__main__":
	import sys
	import signal

	parser=ap()
	parser.add_argument("word", nargs='?', action='store',  help="Word")
	parser.add_argument("--quiet", action='store_true',  help="Run quietly")
	parser.add_argument("--limit", action='store', type=int,  help="limit")
	args=parser.parse_args()

	signal.signal(signal.SIGINT,signal.SIG_DFL)
	
	#app = QtWidgets.QApplication(sys.argv)
	win=BrowserWindow()
	if args.word:
		win.search(args.word)
	win.show()

	sys.exit(_app.exec_())

