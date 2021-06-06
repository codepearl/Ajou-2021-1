import datamanager as dm
import graphmanager as gm
import analysismanager as am
import mapmanager as mm
import pandas as pd
import sys
import os, io
import folium
import matplotlib.pyplot as plt

from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5 import uic, QtCore
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

manager_name = "scenemanager"

main_ui = uic.loadUiType("ui\mainscene.ui")[0]
searchtable_ui = uic.loadUiType("ui\searchscene_table.ui")[0]
map_ui = uic.loadUiType("ui\searchscene_map.ui")[0]
analysis_ui = uic.loadUiType("ui\searchscene_analysis.ui")[0]
graph_ui = uic.loadUiType("ui\searchscene_graph.ui")[0]
wordcloud_ui = uic.loadUiType("ui\searchscene_wc.ui")[0]
staff_ui = uic.loadUiType("ui\staffscene.ui")[0]


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
        pixmap = QPixmap("img/title.png")
        self.mainLabel.setPixmap(pixmap)

class SearchScene(QMainWindow, searchtable_ui):
    def __init__(self, parent = None):
        super(SearchScene,self).__init__(parent)
        self.setupUi(self)
        self.searchButton.clicked.connect(self.ShowData)
        self.backButton.clicked.connect(self.ResetByArea)
        
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

        pixmap = QPixmap("img/data_title.png")
        self.titleLabel.setPixmap(pixmap)
                
    def ShowData(self):
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

    def ResetByArea(self):
        ResetInput()
        if byArea:
            self.byArea.setChecked(True)
            self.byCategory.setChecked(False)
        else:
            self.byArea.setChecked(False)
            self.byCategory.setChecked(True)

class GraphScene(QMainWindow, graph_ui):
    def __init__(self, parent = None):
        super(GraphScene,self).__init__(parent)
        self.setupUi(self)
        self.countButton.clicked.connect(self.ShowCountData)
        self.pieButton.clicked.connect(self.ShowPieData)
        self.backButton.clicked.connect(self.ClearFigure)
        self.backButton.clicked.connect(self.ResetByArea)

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

        #self.fig = plt.figure(figsize=[10,4]) #plt.Figure()
        #self.canvas = FigureCanvas(self.fig)
        self.img = QLabel("이 곳에 그래프가 나타납니다. 데이터 양이 많은 경우 오래 걸릴 수 있습니다.", self)
        #self.img.setAlignment(AlignCenter)
        self.graphLayout.addWidget(self.img)
        #self.graphLayout.addWidget(self.canvas)#here 
        #self.addToolBar(NavigationToolbar(self.canvas, self))
        #self.canvas.show()

        pixmap = QPixmap("img/graph_title.png")
        self.titleLabel.setPixmap(pixmap)
        
    def ShowCountData(self):
        if byArea:
            li = []
            li.append(self.cityBox.currentText())
            li.append(self.dongBox.currentText())
        else:
            li = []
            li.append(self.LCategoryBox.currentText())
            li.append(self.MCategoryBox.currentText())
            li.append(self.SCategoryBox.currentText())
        #plt.clf()
        #gh = gm.GetCountplot(byArea, li, manager_name)
        gm.GetCountplot(byArea, li, manager_name)
        pixmap = QPixmap("graph/count.png")
        self.img.setPixmap(pixmap)
        #self.fig = plt.Figure()
        #self.canvas.draw()
        
    def ShowPieData(self):
        if byArea:
            li = []
            li.append(self.cityBox.currentText())
            li.append(self.dongBox.currentText())
        else:
            li = []
            li.append(self.LCategoryBox.currentText())
            li.append(self.MCategoryBox.currentText())
            li.append(self.SCategoryBox.currentText())
        #have issue            

        gh = gm.GetPie(byArea, li, manager_name)
        pixmap = QPixmap("graph/pie.png")
        self.img.setPixmap(pixmap)
        #plt.show()
        #self.fig = plt.Figure()
        #self.canvas.draw()
    def ClearFigure(self):
        #plt.clf()
        plt.cla()

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

    def ResetByArea(self):
        ResetInput()
        if byArea:
            self.byArea.setChecked(True)
            self.byCategory.setChecked(False)
        else:
            self.byArea.setChecked(False)
            self.byCategory.setChecked(True)

class AnalysisScene(QMainWindow, analysis_ui):
    def __init__(self, parent = None):
        super(AnalysisScene,self).__init__(parent)
        self.setupUi(self)
        self.bestButton.clicked.connect(self.ShowBestData)
        self.worstButton.clicked.connect(self.ShowWorstData)
        self.backButton.clicked.connect(self.ResetByArea)

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

        pixmap = QPixmap("img/analysis_title.png")
        self.titleLabel.setPixmap(pixmap)
        
            
    def ShowBestData(self):
        plt.cla()
        if byArea:
            li = []
            li.append(self.cityBox.currentText())
            li.append(self.dongBox.currentText())
            df = am.FreqBottom(byArea, li)
            
        else:
            li = []
            li.append(self.LCategoryBox.currentText())
            li.append(self.MCategoryBox.currentText())
            li.append(self.SCategoryBox.currentText())
            df = am.FreqBottom(byArea, li)

        #df = df.reset_index()
        model = DataFrameModel(df)
        self.tableView.setModel(model)
        
        
    def ShowWorstData(self):
        plt.cla()
        if byArea:
            li = []
            li.append(self.cityBox.currentText())
            li.append(self.dongBox.currentText())
            df = am.FreqTop(byArea, li)
            
        else:
            li = []
            li.append(self.LCategoryBox.currentText())
            li.append(self.MCategoryBox.currentText())
            li.append(self.SCategoryBox.currentText())
            df = am.FreqTop(byArea, li)

        #df = df.reset_index()
        
        model = DataFrameModel(df)
        self.tableView.setModel(model)
        
    def ClearFigure(self):
        plt.cla()
        
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

    def ResetByArea(self):
        ResetInput()
        if byArea:
            self.byArea.setChecked(True)
            self.byCategory.setChecked(False)
        else:
            self.byArea.setChecked(False)
            self.byCategory.setChecked(True)

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
        m = mm.StartMap();

        m.save(data, close_file=False)
        self.webView.setHtml(data.getvalue().decode())

        pixmap = QPixmap("img/map_title.png")
        self.titleLabel.setPixmap(pixmap)
        
    def ShowMap(self):
        li = []
        li.append(self.cityBox.currentText())
        li.append(self.dongBox.currentText())
        li.append(self.LCategoryBox.currentText())
        li.append(self.MCategoryBox.currentText())
        li.append(self.SCategoryBox.currentText())
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
            
class WordCloudScene(QMainWindow, wordcloud_ui):
    def __init__(self, parent = None):
        super(WordCloudScene,self).__init__(parent)
        self.setupUi(self)
        self.bestButton.clicked.connect(self.ShowBestData)
        self.worstButton.clicked.connect(self.ShowWorstData)
        self.backButton.clicked.connect(self.ResetByArea)

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

        #self.fig = plt.figure(figsize=[10,4]) #plt.Figure()
        #self.canvas = FigureCanvas(self.fig)
        self.img = QLabel("이 곳에 그래프가 나타납니다. 데이터 양이 많은 경우 오래 걸릴 수 있습니다.", self)
        #self.img.setAlignment(AlignCenter)
        self.graphLayout.addWidget(self.img)
        #self.graphLayout.addWidget(self.canvas)#here 
        #self.addToolBar(NavigationToolbar(self.canvas, self))
        #self.canvas.show()
        pixmap = QPixmap("img/wc_title.png")
        self.titleLabel.setPixmap(pixmap)
        
    def ShowBestData(self):
        if byArea:
            li = []
            li.append(self.cityBox.currentText())
            li.append(self.dongBox.currentText())
            am.WordCloudBottom(byArea, li)
        else:
            li = []
            li.append(self.LCategoryBox.currentText())
            li.append(self.MCategoryBox.currentText())
            li.append(self.SCategoryBox.currentText())
            am.WordCloudBottom(byArea, li)
        pixmap = QPixmap("graph/wordcloud.png")
        self.img.setPixmap(pixmap)
        
    def ShowWorstData(self):
        if byArea:
            li = []
            li.append(self.cityBox.currentText())
            li.append(self.dongBox.currentText())
            am.WordCloudTop(byArea, li)
        else:
            li = []
            li.append(self.LCategoryBox.currentText())
            li.append(self.MCategoryBox.currentText())
            li.append(self.SCategoryBox.currentText())
            am.WordCloudTop(byArea, li)        

        pixmap = QPixmap("graph/wordcloud.png")
        self.img.setPixmap(pixmap)
    def ClearFigure(self):
        #plt.clf()
        plt.cla()

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

    def ResetByArea(self):
        ResetInput()
        if byArea:
            self.byArea.setChecked(True)
            self.byCategory.setChecked(False)
        else:
            self.byArea.setChecked(False)
            self.byCategory.setChecked(True)

class StaffScene(QMainWindow, staff_ui):
    def __init__(self, parent = None):
        super(StaffScene,self).__init__(parent)
        self.setupUi(self)
        self.searchButton.clicked.connect(self.ShowData)

        self.img = QLabel("보고싶은 정보를 선택해주세요.", self)

        self.graphLayout.addWidget(self.img)
        pixmap = QPixmap("img/end_title.png")
        self.titleLabel.setPixmap(pixmap)
        
    def ShowData(self):      
        pixmap = QPixmap("graph/wordcloud.png")
        self.img.setPixmap(pixmap)

app = QApplication(sys.argv)
mainScene = MainScene()
searchScene = SearchScene()
graphScene = GraphScene()
analysisScene = AnalysisScene()
wordcloudScene = WordCloudScene()
mapScene = MapScene()
staffScene = StaffScene()
screen = QStackedWidget()

def SetScreen():
    screen.addWidget(mainScene)     #mainScene index 0
    screen.addWidget(searchScene)   #searchScene index 1
    screen.addWidget(graphScene)   #graphScene index 2
    screen.addWidget(analysisScene)   #analysisScene index 3
    screen.addWidget(wordcloudScene)    #wordcloudScene index 4
    screen.addWidget(mapScene)      #mapScene index 5
    screen.addWidget(staffScene)      #mapScene index 6
    screen.resize(1215, 715)
    screen.setWindowTitle("Pear129")
    screen.setWindowIcon(QIcon("img/icon.png"))

def ShowScreen():
    screen.show()
    app.exec_()
    #nonValue-Returning
    
def SetButton():
    mainScene.tableButton.clicked.connect(lambda: screen.setCurrentIndex(1))
    mainScene.graphButton.clicked.connect(lambda: screen.setCurrentIndex(2))
    mainScene.recommendButton.clicked.connect(lambda: screen.setCurrentIndex(3))
    mainScene.wcButton.clicked.connect(lambda: screen.setCurrentIndex(4))
    mainScene.mapButton.clicked.connect(lambda: screen.setCurrentIndex(5))
    mainScene.staffButton.clicked.connect(lambda: screen.setCurrentIndex(6))
    mainScene.exitButton.clicked.connect(lambda: sys.exit()) #End Process
    
    searchScene.backButton.clicked.connect(lambda: screen.setCurrentIndex(0))
    graphScene.backButton.clicked.connect(lambda: screen.setCurrentIndex(0))
    analysisScene.backButton.clicked.connect(lambda: screen.setCurrentIndex(0))
    wordcloudScene.backButton.clicked.connect(lambda: screen.setCurrentIndex(0))
    mapScene.backButton.clicked.connect(lambda: screen.setCurrentIndex(0))
    staffScene.backButton.clicked.connect(lambda: screen.setCurrentIndex(0))
    
#if __name__ == '__init__':


if __name__ == '__main__':
    
    SetScreen()
    SetButton()
    ShowScreen()
    
