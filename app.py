import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication


class ejemplo_GUI (QMainWindow):
    def __init__(self):       
        super()._init_()
        uic.loadUi("GuiDesigner",self)
        
if __name__=='_main_':
    app = QApplication(sys.argv)
    GUI = ejemplo_GUI()
    GUI.show()
    sys.exit(app.exec_())
