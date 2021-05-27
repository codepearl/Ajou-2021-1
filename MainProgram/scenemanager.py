import datamanager as dm
#import graphmanager as gm
import analysismanager as am
import mapmanager as mm
import pandas as pd
import sys
import os, io
import folium

from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5 import uic, QtCore

manager_name = "scenemanager"

main_ui = uic.loadUiType("ui\mainscene.ui")[0]
searchtable_ui = uic.loadUiType("ui\searchscene_table.ui")[0]
map_ui = uic.loadUiType("ui\searchscene_map.ui")[0]

class DataFrameModel(QtCore.QAbstractTableModel):
    DtypeRole = QtCore.Qt.UserRole + 1000
    ValueRole = QtCore.Qt.UserRole + 1001

    def __init__(self, df=pd.DataFrame(), parent=None):
        super(DataFrameModel, self).__init__(parent)
        self._dataframe = df

    def SetDataFrame(self, dataframe):
        self.beginResetModel()
        self._dataframe = dataframe.copy()
        self.endResetModel()

    def DataFrame(self):
        return self._dataframe

    dataFrame = QtCore.pyqtProperty(pd.DataFrame, fget=DataFrame, fset=SetDataFrame)

    #Ignore code conventions because of overriding
    @QtCore.pyqtSlot(int, QtCore.Qt.Orientation, result=str)
    def headerData(self, section: int, orientation: QtCore.Qt.Orientation, role: int = QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return self._dataframe.columns[section]
            else:
                return str(self._dataframe.index[section])
        return QtCore.QVariant()

    def rowCount(self, parent=QtCore.QModelIndex()):
        if parent.isValid():
            return 0
        return len(self._dataframe.index)

    def columnCount(self, parent=QtCore.QModelIndex()):
        if parent.isValid():
            return 0
        return self._dataframe.columns.size

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if not index.isValid() or not (0 <= index.row() < self.rowCount() \
            and 0 <= index.column() < self.columnCount()):
            return QtCore.QVariant()
        row = self._dataframe.index[index.row()]
        col = self._dataframe.columns[index.column()]
        dt = self._dataframe[col].dtype

        val = self._dataframe.iloc[row][col]
        if role == QtCore.Qt.DisplayRole:
            return str(val)
        elif role == DataFrameModel.ValueRole:
            return val
        if role == DataFrameModel.DtypeRole:
            return dt
        return QtCore.QVariant()

    def roleNames(self):
        roles = {
            QtCore.Qt.DisplayRole: b'display',
            DataFrameModel.DtypeRole: b'dtype',
            DataFrameModel.ValueRole: b'value'
        }
        return roles

class MainScene(QMainWindow, main_ui):
    def __init__(self, parent = None):
        super(MainScene,self).__init__(parent)
        self.setupUi(self)

class SearchScene(QMainWindow, searchtable_ui):
    def __init__(self, parent = None):
        super(SearchScene,self).__init__(parent)
        self.setupUi(self)
        self.searchButton.clicked.connect(self.ShowData)

    def ShowData(self):
        df = dm.DataSearch(True, "Test", manager_name)
        model = DataFrameModel(df)
        self.tableView.setModel(model)

class GraphScene(QMainWindow, searchtable_ui):
    def __init__(self, parent = None):
        super(GraphScene,self).__init__(parent)
        self.setupUi(self)

class AnalysisScene(QMainWindow, searchtable_ui):
    def __init__(self, parent = None):
        super(AnalysisScene,self).__init__(parent)
        self.setupUi(self)
        self.searchButton.clicked.connect(self.ShowData)

    def ShowData(self):
        df = am.Recommend(True, "Test")
        model = DataFrameModel(df)
        self.tableView.setModel(model)

class MapScene(QMainWindow, map_ui):
    def __init__(self, parent = None):
        super(MapScene,self).__init__(parent)
        self.setupUi(self)
        self.searchButton.clicked.connect(self.ShowMap)
        
        data = io.BytesIO()
        m = mm.Map(5,"Test") #Test
        m.save(data, close_file=False)
        self.webView.setHtml(data.getvalue().decode())
    def ShowMap(self):
        #Test Code
        coordinate = (37.8199286, -122.4782551)
        m = folium.Map(
        	tiles='Stamen Terrain',
        	zoom_start=13,
        	location=coordinate
        )
        data = io.BytesIO()
        m.save(data, close_file=False)
        self.webView.setHtml(data.getvalue().decode())


app = QApplication(sys.argv)
mainScene = MainScene()
searchScene = SearchScene()
graphScene = GraphScene()
analysisScene = AnalysisScene()
mapScene = MapScene()
screen = QStackedWidget()

#input = 0 #user input code (temp)
#categories = []
#return_data #pandas.DataFrame
#return_graph #format undecided (expect plot)
#return_map #format undecided


def SetScreen():
    screen.addWidget(mainScene)     #mainScene index 0
    screen.addWidget(searchScene)   #searchScene index 1
    screen.addWidget(graphScene)   #graphScene index 2
    screen.addWidget(analysisScene)   #analysisScene index 3
    screen.addWidget(mapScene)      #mapScene index 4
    screen.resize(900,600)
    screen.setWindowTitle("Pear129")

def ShowScreen():
    screen.show()
    app.exec_()
    #nonValue-Returning
    
def SetButton():
    mainScene.tableButton.clicked.connect(lambda: screen.setCurrentIndex(1))
    mainScene.graphButton.clicked.connect(lambda: screen.setCurrentIndex(2))
    mainScene.recommendButton.clicked.connect(lambda: screen.setCurrentIndex(3))
    mainScene.mapButton.clicked.connect(lambda: screen.setCurrentIndex(4))
    mainScene.exitButton.clicked.connect(lambda: sys.exit()) #End Process
    
    searchScene.backButton.clicked.connect(lambda: screen.setCurrentIndex(0))
    graphScene.backButton.clicked.connect(lambda: screen.setCurrentIndex(0))
    analysisScene.backButton.clicked.connect(lambda: screen.setCurrentIndex(0))
    mapScene.backButton.clicked.connect(lambda: screen.setCurrentIndex(0))
    
def Test():
    testData = TestGetDummy()
    TestPrintDummy(testData)
    
def TestGetDummy():
    return dm.DataSearch(True, "Test", manager_name)

def TestPrintDummy(data):
    print(data)

#if __name__ == '__init__':


if __name__ == '__main__':
    #call function
    #iteration for program

    #Test()
    SetScreen()
    SetButton()
    ShowScreen()
    
    #Process by case depending on the input
    #if(input == )

    #Data,Graph,Analysis
    #categories = OrSelectCategory()
    #return_data = dm.DataSearch(categories, manager_name)
    #return_data = am.DataSearch(categories)
    #return_graph = gm.GetGraph(categories)

    #Map
    #categories = AndSelectCategory()
    #return_map = mm.GetMap(categories)

    #Display returns

    

    
