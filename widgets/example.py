import sys
from PyQt5.QtCore import Qt,QSize
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QColor, QPen, QBrush
from qcustomplot import QCustomPlot, QCPBars, QCP, QCPGraph, QCPScatterStyle
import numpy as np
import random
if __name__ == '__main__':

    app = QApplication(sys.argv)


    w = QCustomPlot()

    
    contentsize = QSize(1024, 640)
    w.setMinimumSize(contentsize)
    
    timeData = [np.random.random()*100 for i in range(250)]
    x = np.arange(250)

    dwPoints = QCPGraph(w.xAxis, w.yAxis);
    w.yAxis.setRange(0,max(timeData)*1.05)
    w.xAxis.setRange(0,max(x)*1.05)
    dwPoints.setLineStyle(QCPGraph.lsLine);
    #dwPoints.setScatterStyle(QCPScatterStyle(QCPScatterStyle.ssCircle,Qt.red,Qt.blue,5));
    dwPoints.setData(x,timeData);
    graphPen = QPen()
    graphPen.setColor(QColor(0,0,0));
    graphPen.setWidthF(5);
    dwPoints.setPen(graphPen);
    w.rescaleAxes()
    w.replot()
    w.show()
    sys.exit(app.exec())
