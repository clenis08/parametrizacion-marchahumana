import sys
import pandas as pd
import matplotlib.pyplot as plt
#Importar aquí las librerías a utilizar

from PyQt5 import uic, QtWidgets

qtCreatorFile = "GuiDesigner.ui" #Aquí va el nombre de tu archivo

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        
        #Aquí van los botones
        self.Import_Button.clicked.connect(self.getCSV)

        
    #Aquí van las nuevas funciones
    #Esta función abre el archivo CSV    
    def getCSV(self):
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '/home')
        if filePath != "":
            print ("Dirección",filePath) #Opcional imprimir la dirección del archivo
            self.df = pd.read_csv(str(filePath))
    
  
if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()