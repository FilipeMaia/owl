from Qt import QtGui, QtCore
import pyqtgraph
import numpy
from view import View
import h5proxy as h5py

class View1D(QtGui.QFrame,View):
    viewIndexSelected = QtCore.Signal(int)
    viewValueSelected = QtCore.Signal(list)
    dataItemXChanged = QtCore.Signal(object)
    dataItemYChanged = QtCore.Signal(object)
    needDataset = QtCore.Signal(str)
    datasetChanged = QtCore.Signal(h5py.Dataset,str)

    def __init__(self,parent=None,indexProjector=None):
        QtGui.QFrame.__init__(self,parent)
        View.__init__(self,parent,indexProjector,"plot")
        self.hbox = QtGui.QHBoxLayout(self)
        margin = 20
        self.hbox.setContentsMargins(margin,margin,margin,margin)
        self.dataItemY = None
        self.dataItemX = None
        self.initPlot()
        self.hbox.addWidget(self.plot)
        self.setLayout(self.hbox)
        self.setAcceptDrops(True)
        self.plotMode = "plot"
        #self.setPixelStack()
        self.setWindowSize()
        self.nBins = 200
        self.img = None
    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore() 
    def dropEvent(self, e):
        self.needDataset.emit(e.mimeData().text())

    def clearView(self):
	self.stackSize = 0
	self.integrationMode = None

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
    def onPixelClicked(self,info):
        if self.dataItemY is not None and info is not None:
            if self.dataItemY.isStack:
                self.img = int(info["img"])
                self.refreshPlot()
        if info is not None:
            if self.dataItemY is not None:
                dataY = self.dataItemY.data()
                self.viewValueSelected.emit([info["img"], dataY[info["img"]]])
            if self.infLine is not None:
                self.infLine.setValue(info["img"])
    def setDataItemX(self,dataItem):
        if self.dataItemX is not None:
            self.dataItemX.deselectStack()
        self.dataItemX = dataItem
        if hasattr(dataItem,"fullName"): 
            self.dataItemXLabel = dataItem.fullName
            self.dataItemX.selectStack()
        else:
            self.dataItemXLabel = ""
        self.dataItemXChanged.emit(dataItem)
    def setDataItemY(self,dataItem):
        if self.dataItemY is not None:
            self.dataItemY.deselectStack()
        self.dataItemY = dataItem
        if self.dataItemY.isStack:
            self.img = 0
        else:
            self.img = None
        if hasattr(dataItem,"fullName"):
            self.dataItemYLabel = dataItem.fullName
            self.dataItemY.selectStack()
        else:
            self.dataItemYLabel = ""
        #self.setPixelStack()
        self.dataItemYChanged.emit(dataItem)
    def setWindowSize(self,windowSize=None):
        if windowSize is None:
            self._windowSize = 100
        else:
            self._windowSize = windowSize
    def windowSize(self):
        if self.plotMode == "average":
            return self._windowSize
        else:
            return None
    def toggleAutoLast(self):
        self.autoLast = not self.autoLast
    # DATA
    def onStackSizeChanged(self,newStackSize):
        #self.stackSize = newStackSize
        if self.dataItemY is not None:
            self.refreshPlot()
    def addInfLine(self):
        if self.infLine is None:
            infLine = pyqtgraph.InfiniteLine(0,90,None,True)
            self.plot.addItem(infLine)
            infLine.sigPositionChangeFinished.connect(self.emitViewIndexSelected)    
            self.infLine = infLine
            if self.dataItemY:
                dataY = self.dataItemY.data()
                self.viewValueSelected.emit([0, dataY[0]])
    def removeInfLine(self):
        if self.infLine is not None:
            self.plot.removeItem(self.infLine)
            self.infLine = None
    def setStyle(self,**kwargs):
        self.lineWidth = kwargs.get("lineWidth",self.lineWidth)
        self.lineColor = kwargs.get("lineColor",self.lineColor)
        self.line = kwargs.get("line",self.line)
        self.symbolSize = kwargs.get("symbolSize",self.symbolSize)
        self.symbolColor = kwargs.get("symbolColor",self.symbolColor)
        self.symbol = kwargs.get("symbol",self.symbol)
        if self.line is None:
            self.p.setPen(None)
        else:
            pen = pyqtgraph.mkPen(color=self.lineColor,width=self.lineWidth)
            self.p.setPen(pen)
        self.p.setSymbol(self.symbol)
        self.p.setSymbolPen(None)
        if self.symbol is not None:
            self.p.setSymbolBrush(self.symbolColor)
            self.p.setSymbolSize(self.symbolSize)
    def setPlotMode(self,plotMode):
        self.plotMode = plotMode
        if plotMode == "plot" or plotMode == "average":
            if self.dataItemX is not None:
                xlabel = self.dataItemX.fullName
            else:
                xlabel = "index"
            if self.dataItemY is not None:
                ylabel = self.dataItemY.fullName
            else:
                ylabel = ""
        elif plotMode == "histogram":
            ylabel = "#"
            if self.dataItemY is not None:
                xlabel = self.dataItemY.fullName
            else:
                xlabel = ""
        self.plot.setLabel("bottom",xlabel)
        self.plot.setLabel("left",ylabel)
    def refreshPlot(self):
        if self.dataItemY is None:
            dataY = None
        else:
            dataY = self.dataItemY.data1D(windowSize=self.windowSize(),img=self.img)
        if dataY is None:
            self.p.setData([0])
            self.setPlotMode(self.plotMode)
            return
        if self.p is None:
            self.initPlot()
        self.removeInfLine()
        # line show/hide does not seem to have any effect
        if self.plotMode == "plot" or self.plotMode == "average":
            if self.dataItemX is None:
                dataX = numpy.arange(dataY.shape[0])
                if self.plotMode == "plot":
                    self.addInfLine()
            else:
                dataX = self.dataItemX.data()
            if self.indexProjector.imgs is not None and dataY.shape[0] == self.indexProjector.imgs.shape[0]:
                dataY = dataY[self.indexProjector.imgs]
            validMask = numpy.isfinite(dataX)*numpy.isfinite(dataY)
            self.p.setData(dataX[validMask],dataY[validMask])
        elif self.plotMode == "histogram":
            #if self.nBins is None:
            #    N = 200
            #else:
            N = self.nBins
            (hist,edges) = numpy.histogram(dataY,bins=N)
            edges = (edges[:-1]+edges[1:])/2.0
            self.p.setData(edges,hist)        
        self.plot.enableAutoRange('xy')
    def refreshDisplayProp(self,props):
        if props["points"] is True:
            symbol = "o"
        else:
            symbol = None
        if props["lines"]:
            line = True
        else:
            line = None
        self.setStyle(symbol=symbol,line=line)
        #self.nBins = props["N"]
        self.refreshPlot()
    def emitViewIndexSelected(self,foovalue=None):
        index = int(round(self.infLine.getXPos()))
        self.viewIndexSelected.emit(index)
        if self.dataItemY is not None:
            dataY = self.dataItemY.data()
            self.viewValueSelected.emit([index, dataY[index]])
    #def onPlotNBinsEdit(self):
    #    self.nBins = int(self.sender().text())
    #    self.refreshPlot()
