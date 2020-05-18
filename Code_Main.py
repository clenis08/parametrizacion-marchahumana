import threading
import random
import numpy as np
import time
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from PyQt5 import uic, QtCore, QtGui, QtWidgets
import sys
from sklearn.metrics import confusion_matrix
import seaborn as sn
import pandas as pd
import matplotlib
import serial  # Import Serial Library
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import serial  # Import Serial Library
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import re
import threading
matplotlib.use('Qt5Agg')

Y = 0
X = 0
gDataX = []
gDataY = []
gDataX.append([0.0])
gDataX.append([0.0])
gDataY.append([0.0])
gDataY.append([0.0])
hl, = plt.plot(gDataX[1], gDataX[1])
y_actu = [2, 0, 2, 2, 0, 1, 1, 2, 2, 0, 1, 2]
y_pred = [0, 0, 2, 1, 0, 2, 1, 0, 2, 0, 2, 2]

qtCreatorFile = "GuiDesigner.ui"  # Aquí va el nombre de tu archivo

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

FlagAdquisition = True


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Aquí van los botones
        self.Import_Button.clicked.connect(self.getCSV)
        self.Graph_Button.clicked.connect(self.graphics)
        self.Connect_Button.clicked.connect(self.adquisition)     

    # Aquí van las nuevas funciones
    def adquisition(self):
    
        self._timer = self.MplWidget.canvas.new_timer(
            50, [(self._update_canvas, (), {})])
        self._timer.start()
        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.legend(
            ('X Ang', 'Y Ang'), loc='upper right')
        self.MplWidget.canvas.axes.set_title('Joystick')
        
        dataCollector = threading.Thread(
            target=getData, args=(gDataX, gDataY,))
        dataCollector.start()
        
    """
        global FlagAdquisition
        if FlagAdquisition == True:
            FlagAdquisition = False
            # self.Walking_Lbl.setStyleSheet("border-image: url(:/Wk/Walking_Red.png);\n"
            #                              "border-image: url(:/Wk/Walking_Green.png);")
            self.StanUp_Lbl.setStyleSheet("border-image: url(:/SU/StanUp_Red.png);\n"
                                          "border-image: url(:/SU/StandUp_Green.png);")
            self.Laying_Lbl.setStyleSheet("border-image: url(:/La/Laying_Green.png);\n"
                                          "border-image: url(:/La/Laying_Red.png);")
            # self.Laying_Lbl.setStyleSheet("border-image: url(:/La/Laying_Red.png);\n"
            #                            "border-image: url(:/La/Laying_Green.png);")
            # self.SitDown_Lbl.setStyleSheet("border-image: url(:/SD/SitDown_Red.png);\n"
            #                            "border-image: url(:/SD/SitDown_Green.png);")
            # self.UpStairs_Lbl.setStyleSheet("border-image: url(:/US/UpStairs_Red.png);\n"
            #                            "border-image: url(:/US/UpStairs_Green.png);")
            # self.DownStair_Lbl.setStyleSheet("border-image: url(:/DS/DownStairs_Red.png);\n"
            #                            "border-image: url(:/DS/DownStairs_Green.png);")
        else:
            FlagAdquisition = True
            self.StanUp_Lbl.setStyleSheet("border-image: url(:/SU/StandUp_Green.png);\n"
                                          "border-image: url(:/SU/StanUp_Red.png);")
            self.Laying_Lbl.setStyleSheet("border-image: url(:/La/Laying_Red.png);\n"
                                          "border-image: url(:/La/Laying_Green.png);")
            # self.Walking_Lbl.setStyleSheet("border-image: url(:/Wk/Walking_Green.png);\n"
            #                         "border-image: url(:/Wk/Walking_Red.png);")
            # self.Laying_Lbl.setStyleSheet("border-image: url(:/La/Laying_Green.png);\n"
            #                       "border-image: url(:/La/Laying_Red.png);")
            # self.SitDown_Lbl.setStyleSheet("border-image: url(:/SD/SitDown_Green.png);\n"
            #                       "border-image: url(:/SD/SitDown_Red.png);")
            # self.UpStairs_Lbl.setStyleSheet("border-image: url(:/US/UpStairs_Green.png);\n"
            #                       "border-image: url(:/US/UpStairs_Red.png);")
            # self.DownStair_Lbl.setStyleSheet("border-image: url(:/DS/DownStairs_Green.png);\n"
            #                       "border-image: url(:/DS/DownStairs_Red.png);")
     """
    def _update_canvas(self):
            self.MplWidget.canvas.axes.clear()
            t = np.linspace(0, 10, 101)
            # Use fixed vertical limits to prevent autoscaling changing the scale
            # of the axis.
            self.MplWidget.canvas.axes.set_ylim(0,1024)
            # Shift the sinusoid as a function of time.
            dx_x = np.array(range(len( gDataX[1])))
            dy_x = np.array(gDataX[1])
            dx_y = np.array(range(len( gDataY[1])))
            dy_y = np.array(gDataY[1])
            self.MplWidget.canvas.axes.plot(dx_x,dy_x)
            self.MplWidget.canvas.axes.plot(dx_y,dy_y)
            self.MplWidget.canvas.draw()
    # Esta funcón abre el archivo CSV

    def graphics(self):

        fs = 500
        f = random.randint(1, 100)
        ts = 1 / fs
        length_of_signal = 100
        t = np.linspace(0, 1, length_of_signal)

        cosinus_signal = np.cos(2 * np.pi * f * t)
        sinus_signal = np.sin(2 * np.pi * f * t)
        """
        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.plot(t, cosinus_signal)
        self.MplWidget.canvas.axes.plot(t, sinus_signal)
        self.MplWidget.canvas.axes.legend(
            ('cosinus', 'sinus'), loc='upper right')
        self.MplWidget.canvas.axes.set_title('Cosinus - Sinus Signal')
        self.MplWidget.canvas.draw()
        """
        self.MplWidget_2.canvas.axes.clear()
        x = self.df['col1']
        y = self.df['col2']
        self.MplWidget_2.canvas.axes.plot(x, y)
        self.MplWidget_2.canvas.axes.legend('Col1', loc='upper right')
        self.MplWidget_2.canvas.axes.set_title('CSV file')
        self.MplWidget_2.canvas.draw()

        cm = confusion_matrix(y_actu, y_pred)

        resultado = pd.DataFrame(cm, index=['Fresh Apple', 'Fresh Banana', 'Fresh Orange'],
                                 columns=['Fresh Apple', 'Fresh Banana', 'Fresh Orange'])

        self.MxConfusion.canvas.axes.clear()
        sn.heatmap(resultado, annot=True, linewidths=1, linecolor='white',
                   ax=self.MxConfusion.canvas.axes, cmap="Reds")
        # font = {'family': 'serif',
        #       'color': 'darkred',
        #      'weight': 'normal',
        #     'size': 6}
        self.MxConfusion.canvas.axes.set_title("Matrix de confusion ")
        self.MxConfusion.canvas.axes.set_ylabel("Preditec Label")
        self.MxConfusion.canvas.axes.set_xlabel("True Label")
        self.MxConfusion.canvas.draw()
        print(cm)

    def getCSV(self):
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, 'Open file', '/home/OneDrive-correounivalle.edu.co/')
        if filePath != "":
            # Opcional imprimir la dirección del archivo
            print("Dirección", filePath)
            self.df = pd.read_csv(str(filePath))
            dfcars = pd.read_csv(str(filePath))
            # Mostrar los encabezados de las primeras cinco filas de los datos
            print(dfcars.head())
            print(dfcars.shape)  # 12 columnas, cada una de longitud 32


def getData(out_dataX, out_dataY):
    # Create Serial port object called arduinoSerialData
    with serial.Serial('com5', 115200, timeout=1) as ser:
        while True:
            line = ser.readline().decode('utf-8')  # read a '\n' terminated line
            try:
                if "Y" in line:
                    Y = float(line[1:len(line)])
                if "X" in line:
                    X = float(line[1:len(line)])
                out_dataY[1].append(Y)
                out_dataX[1].append(X)
                if len(out_dataX[1]) > 200:
                    out_dataX[1].pop(0)
                if len(out_dataY[1]) > 200:
                    out_dataY[1].pop(0)
                print(out_dataX[1])
                print(out_dataY[1])
            except:
                pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
