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
analysis_ui = uic.loadUiType("ui\searchscene_analysis.ui")[0]


def ResetInput():
    global byArea
    byArea = True

def SetByArea():
    global byArea
    byArea = True

def SetByCategory():
    global byArea
    byArea = False

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
        #if not index.isValid() or not (0 <= index.row() < self.rowCount() \
        #    and 0 <= index.column() < self.columnCount()):
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
        ResetInput()

class SearchScene(QMainWindow, searchtable_ui):
    def __init__(self, parent = None):
        super(SearchScene,self).__init__(parent)
        self.setupUi(self)
        self.searchButton.clicked.connect(self.ShowData)
        
        for i in dm.ListMDistrict():
            self.cityBox.addItem(i)
        for i in dm.ListLCategory():
            self.LCategoryBox.addItem(i)
        for i in dm.ListSDistrict(self.cityBox.currentText()):
            self.dongBox.addItem(i)
        for i in dm.ListMCategory(self.LCategoryBox.currentText()):
            self.MCategoryBox.addItem(i)
        for i in dm.ListSCategory(self.MCategoryBox.currentText()):
            self.SCategoryBox.addItem(i)

        if byArea:
            self.byArea.setChecked(True)
            self.byCategory.setChecked(False)
        else:
            self.byArea.setChecked(False)
            self.byCategory.setChecked(True)

        self.cityBox.currentIndexChanged.connect(self.SetDistrict)
        self.LCategoryBox.currentIndexChanged.connect(self.SetMCategory)
        self.MCategoryBox.currentIndexChanged.connect(self.SetSCategory)

        self.byArea.clicked.connect(SetByArea)
        self.byCategory.clicked.connect(SetByCategory)


        
    def ShowData(self):
        #print(byArea)
        if byArea:
            li = []
            li.append(self.cityBox.currentText())
            li.append(self.dongBox.currentText())
            df = dm.DataSearch(byArea, li, manager_name)
            
        else:
            li = []
            li.append(self.LCategoryBox.currentText())
            li.append(self.MCategoryBox.currentText())
            li.append(self.SCategoryBox.currentText())
            df = dm.DataSearch(byArea, li, manager_name)


        df = df.reset_index()
        model = DataFrameModel(df)
        self.tableView.setModel(model)

    def SetDistrict(self):
        self.dongBox.clear()
        for i in dm.ListSDistrict(self.cityBox.currentText()):
            self.dongBox.addItem(i)

    def SetMCategory(self):
        self.MCategoryBox.clear()
        for i in dm.ListMCategory(self.LCategoryBox.currentText()):
            self.MCategoryBox.addItem(i)

    def SetSCategory(self):
        self.SCategoryBox.clear()
        for i in dm.ListSCategory(self.MCategoryBox.currentText()):
            self.SCategoryBox.addItem(i)

class GraphScene(QMainWindow, searchtable_ui):
    def __init__(self, parent = None):
        super(GraphScene,self).__init__(parent)
        self.setupUi(self)

class AnalysisScene(QMainWindow, analysis_ui):
    def __init__(self, parent = None):
        super(AnalysisScene,self).__init__(parent)
        self.setupUi(self)
        self.bestButton.clicked.connect(self.ShowBestData)
        self.worstButton.clicked.connect(self.ShowWorstData)

        for i in dm.ListMDistrict():
            self.cityBox.addItem(i)
        for i in dm.ListLCategory():
            self.LCategoryBox.addItem(i)
        for i in dm.ListSDistrict(self.cityBox.currentText()):
            self.dongBox.addItem(i)
        for i in dm.ListMCategory(self.LCategoryBox.currentText()):
            self.MCategoryBox.addItem(i)
        for i in dm.ListSCategory(self.MCategoryBox.currentText()):
            self.SCategoryBox.addItem(i)

        if byArea:
            self.byArea.setChecked(True)
            self.byCategory.setChecked(False)
        else:
            self.byArea.setChecked(False)
            self.byCategory.setChecked(True)

        self.cityBox.currentIndexChanged.connect(self.SetDistrict)
        self.LCategoryBox.currentIndexChanged.connect(self.SetMCategory)
        self.MCategoryBox.currentIndexChanged.connect(self.SetSCategory)

        self.byArea.clicked.connect(SetByArea)
        self.byCategory.clicked.connect(SetByCategory)
            
    def ShowBestData(self):
        if byArea:
            li = []
            li.append(self.cityBox.currentText())
            li.append(self.dongBox.currentText())
            #print(li)
            df = am.FreqBottom(byArea, li)
            
        else:
            li = []
            li.append(self.LCategoryBox.currentText())
            li.append(self.MCategoryBox.currentText())
            li.append(self.SCategoryBox.currentText())
            #print(li)
            df = am.FreqBottom(byArea, li)

        df = df.reset_index()
        #print(df)
        model = DataFrameModel(df)
        self.tableView.setModel(model)
    def ShowWorstData(self):
        if byArea:
            li = []
            li.append(self.cityBox.currentText())
            li.append(self.dongBox.currentText())
            #print(li)
            df = am.FreqTop(byArea, li)
            
        else:
            li = []
            li.append(self.LCategoryBox.currentText())
            li.append(self.MCategoryBox.currentText())
            li.append(self.SCategoryBox.currentText())
            #print(li)
            df = am.FreqTop(byArea, li)

        df = df.reset_index()
        
        model = DataFrameModel(df)
        self.tableView.setModel(model)
    def SetDistrict(self):
        self.dongBox.clear()
        for i in dm.ListSDistrict(self.cityBox.currentText()):
            self.dongBox.addItem(i)

    def SetMCategory(self):
        self.MCategoryBox.clear()
        for i in dm.ListMCategory(self.LCategoryBox.currentText()):
            self.MCategoryBox.addItem(i)

    def SetSCategory(self):
        self.SCategoryBox.clear()
        for i in dm.ListSCategory(self.MCategoryBox.currentText()):
            self.SCategoryBox.addItem(i)

class MapScene(QMainWindow, map_ui):
    def __init__(self, parent = None):
        super(MapScene,self).__init__(parent)
        self.setupUi(self)
        self.searchButton.clicked.connect(self.ShowMap)

        for i in dm.ListMDistrict():
            self.cityBox.addItem(i)
        for i in dm.ListLCategory():
            self.LCategoryBox.addItem(i)
        for i in dm.ListSDistrict(self.cityBox.currentText()):
            self.dongBox.addItem(i)
        for i in dm.ListMCategory(self.LCategoryBox.currentText()):
            self.MCategoryBox.addItem(i)
        for i in dm.ListSCategory(self.MCategoryBox.currentText()):
            self.SCategoryBox.addItem(i)

        self.cityBox.currentIndexChanged.connect(self.SetDistrict)
        self.LCategoryBox.currentIndexChanged.connect(self.SetMCategory)
        self.MCategoryBox.currentIndexChanged.connect(self.SetSCategory)
        
        data = io.BytesIO()
        #Test Code
        coordinate = (37.8199286, -122.4782551)
        m = folium.Map(
        	tiles='Stamen Terrain',
        	zoom_start=13,
        	location=coordinate
        )

        m.save(data, close_file=False)
        self.webView.setHtml(data.getvalue().decode())
    def ShowMap(self):
        li = []
        li.append(self.cityBox.currentText())
        li.append(self.dongBox.currentText())
        li.append(self.LCategoryBox.currentText())
        li.append(self.MCategoryBox.currentText())
        li.append(self.SCategoryBox.currentText())
        #print(li)
        m = mm.Map(len(li),li)
        data = io.BytesIO()
        m.save(data, close_file=False)
        self.webView.setHtml(data.getvalue().decode())

    def SetDistrict(self):
        self.dongBox.clear()
        for i in dm.ListSDistrict(self.cityBox.currentText()):
            self.dongBox.addItem(i)

    def SetMCategory(self):
        self.MCategoryBox.clear()
        for i in dm.ListMCategory(self.LCategoryBox.currentText()):
            self.MCategoryBox.addItem(i)

    def SetSCategory(self):
        self.SCategoryBox.clear()
        for i in dm.ListSCategory(self.MCategoryBox.currentText()):
            self.SCategoryBox.addItem(i)


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

    

    
