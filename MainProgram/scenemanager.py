import datamanager as dm
#import graphmanager as gm
#import analysismanager as am
#import mapmanager as mm
import pandas as pd
import sys

from PyQt5.QtWidgets import *
from PyQt5 import uic

manager_name = "scenemanager"
main_ui = uic.loadUiType("ui\mainscene.ui")[0]
searchtable_ui = uic.loadUiType("ui\searchscene_table.ui")[0]

class MainScene(QMainWindow, main_ui):
    def __init__(self, parent=None):
        super(MainScene,self).__init__(parent)
        self.setupUi(self)

class SearchScene(QMainWindow, searchtable_ui):
    def __init__(self, parent = None):
        super(SearchScene,self).__init__(parent)
        self.setupUi(self)

app = QApplication(sys.argv)
mainScene = MainScene()
searchScene = SearchScene()
screen = QStackedWidget()

#input = 0 #user input code (temp)
#categories = []
#return_data #pandas.DataFrame
#return_graph #format undecided (expect plot)
#return_map #format undecided


def SetMainScreen():
    screen.addWidget(mainScene)
    screen.addWidget(searchScene)
    screen.resize(900,600)
    screen.setWindowTitle("Pear129")

def ShowMainScreen():
    screen.show()
    app.exec_()
    #nonValue-Returning

def SetButtonEvent():
    mainScene.tableButton.clicked.connect(lambda: screen.setCurrentIndex(1))
    mainScene.exitButton.clicked.connect(lambda: sys.exit()) #End Process
    searchScene.backButton.clicked.connect(lambda: screen.setCurrentIndex(0))
    

#def OrSelectCategory():
    #return something

#def AndSelectCategory():
    #return something

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
    SetMainScreen()
    SetButtonEvent()
    ShowMainScreen()
    
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

    

    
