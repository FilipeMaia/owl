from PySide import QtGui, QtCore
import pyqtgraph
import numpy
from view import View

class View1D(View,QtGui.QFrame):
    viewIndexSelected = QtCore.Signal(int)
    dataItemXChanged = QtCore.Signal(object)
    dataItemYChanged = QtCore.Signal(object)
    def __init__(self,parent=None):
        View.__init__(self,parent,"plot")
        QtGui.QFrame.__init__(self,parent)
        self.hbox = QtGui.QHBoxLayout(self)
        margin = 20
        self.hbox.setContentsMargins(margin,margin,margin,margin)
        self.initPlot()
        self.hbox.addWidget(self.plot)
        self.setLayout(self.hbox)
        self.setAcceptDrops(True)
        self.plotMode = "plot"
        self.dataItemY = None
        self.dataItemX = None
        self.setPixelStack()
        self.setMovingAverage()
        self.nBins = 200
        self.stackSizeChanged.connect(self.refreshPlot)
    def initPlot(self,widgetType="plot"):
        self.lineColor = (255,255,255)
        self.lineWidth = 1
        self.line = True
        self.symbolColor = (255,255,255)
        self.symbolSize = 1
        self.symbol = None
        self.plot = pyqtgraph.PlotWidget()
        self.infLine = None
        self.addInfLine()
        space = 60
        self.p = self.plot.plot([0])#,symbol=1,symbolSize=1,symbolBrush=(255,255,255,255),symbolPen=None,pen=None)
        self.p.setPointMode(True)
        self.p.setPen(None)
        self.plot.getAxis("top").setHeight(space)
        self.plot.getAxis("bottom").setHeight(space)
        self.plot.getAxis("left").setWidth(space)
        self.plot.getAxis("right").setWidth(space)
        self.setStyle()
        #self.p.update()
    def setDataItemX(self,dataItem):
        self.dataItemX = dataItem
        if hasattr(dataItem,"fullName"): 
            self.dataItemXLabel = dataItem.fullName
        else:
            self.dataItemXLabel = ""
        self.dataItemXChanged.emit(dataItem)
    def setDataItemY(self,dataItem):
        self.dataItemY = dataItem
        if hasattr(dataItem,"fullName"):
            self.dataItemYLabel = dataItem.fullName
        else:
            self.dataItemYLabel = ""
        if dataItem.isStack:
            self.stackSize = self.dataItemY.shape(True)[0]
        else:
            self.stackSize = 0
        self.setPixelStack()
        self.setMovingAverage()
        self.dataItemYChanged.emit(dataItem)
    def setPixelStack(self,ix=None,iy=None,N=None):
        self.ix = ix
        self.iy = iy
        self.N = N
    def setMovingAverage(self,windowSize=None):
        self.windowSize = windowSize
    def toggleAutoLast(self):
        self.autoLast = not self.autoLast
    # DATA
    def updateShape(self):
        if self.dataItemY != None:
            if self.dataItemY.shape() != self.dataItemY.shape(True):
                self.refreshPlot()
    def addInfLine(self):
        if self.infLine == None:
            infLine = pyqtgraph.InfiniteLine(0,90,None,True)
            self.plot.addItem(infLine)
            infLine.sigPositionChangeFinished.connect(self.emitViewIndexSelected)    
            self.infLine = infLine
    def removeInfLine(self):
        if self.infLine != None:
            self.plot.removeItem(self.infLine)
            self.infLine = None
    def setStyle(self,**kwargs):
        self.lineWidth = kwargs.get("lineWidth",self.lineWidth)
        self.lineColor = kwargs.get("lineColor",self.lineColor)
        self.line = kwargs.get("line",self.line)
        self.symbolSize = kwargs.get("symbolSize",self.symbolSize)
        self.symbolColor = kwargs.get("symbolColor",self.symbolColor)
        self.symbol = kwargs.get("symbol",self.symbol)
        if self.line == None:
            self.p.setPen(None)
        else:
            pen = pyqtgraph.mkPen(color=self.lineColor,width=self.lineWidth)
            self.p.setPen(pen)
        self.p.setSymbol(self.symbol)
        self.p.setSymbolPen(None)
        if self.symbol != None:
            self.p.setSymbolBrush(self.symbolColor)
            self.p.setSymbolSize(self.symbolSize)
    def setPlotMode(self,plotMode):
        self.plotMode = plotMode
        if plotMode == "plot" or plotMode == "average":
            if self.dataItemX != None:
                xlabel = self.dataItemX.fullName
            else:
                xlabel = "index"
            if self.dataItemY != None:
                ylabel = self.dataItemY.fullName
            else:
                ylabel = ""
        elif plotMode == "histogram":
            ylabel = "#"
            if self.dataItemY != None:
                xlabel = self.dataItemY.fullName
            else:
                xlabel = ""
        self.plot.setLabel("bottom",xlabel)
        self.plot.setLabel("left",ylabel)
    def refreshPlot(self):
        if self.dataItemY == None:
            dataY = None
        else:
            dataY = self.dataItemY.data(ix=self.ix,iy=self.iy,N=self.N,windowSize=self.windowSize)
        if dataY == None:
            self.p.setData([0])
            self.setPlotMode(self.plotMode)
            return
        if self.p == None:
            self.initPlot()
        self.removeInfLine()
        # line show/hide does not seem to have any effect
        if self.plotMode == "plot" or self.plotMode == "average":
            if self.dataItemX == None:
                dataX = numpy.arange(dataY.shape[0])
                if self.plotMode == "plot":
                    self.addInfLine()
            else:
                dataX = self.dataItemX.data()
            if self.indexProjector.imgs != None and dataY.shape[0] == self.indexProjector.imgs.shape[0]:
                dataY = dataY[self.indexProjector.imgs]
            self.p.setData(dataX,dataY)
        elif self.plotMode == "histogram":
            if self.nBins == None:
                N = 200
            else:
                N = self.nBins
            (hist,edges) = numpy.histogram(dataY,bins=N)
            edges = (edges[:-1]+edges[1:])/2.0
            self.p.setData(edges,hist)        
        self.plot.enableAutoRange('xy')
    def refreshDisplayProp(self,props):
        if props["points"] == True:
            symbol = "o"
        else:
            symbol = None
        if props["lines"]:
            line = True
        else:
            line = None
        self.setStyle(symbol=symbol,line=line)
        self.nBins = props["N"]
        self.refreshPlot()
    def emitViewIndexSelected(self,foovalue=None):
        index = int(self.infLine.getXPos())
        self.viewIndexSelected.emit(index)
    def onPlotNBinsEdit(self):
        self.nBins = int(self.sender().text())
        self.refreshPlot()