import datamanager as dm
#import graphmanager as gm
#import analysismanager as am
#import mapmanager as mm
import pandas as pd
import tkinter as tk

manager_name = "scenemanager"
screen = tk.Tk()
searchButton = 0
tableButton = 0
graphButton = 0
recommendButton = 0
mapButton = 0
exitButton = 0
mainLabel = 0

#input = 0 #user input code (temp)
#categories = []
#return_data #pandas.DataFrame
#return_graph #format undecided (expect plot)
#return_map #format undecided

def SetMainScreen():
    screen.title("Pear129")
    screen.geometry("800x600")
    screen.resizable(False, False) #Fix
    MakeLabel()
    MakeButton()

def ShowMainScreen():
    screen.mainloop()
    #nonValue-Returning
    
def MakeButton():
    #searchButton = tk.Button(screen, text="Search", bg="yellow", command=ClickSearchButton)
    #searchButton.place(x=20,y=20)
    #searchButton.pack()
    tableButton = tk.Button(screen, text="데이터 조회(Table)", command=ClickTableSearchButton)
    #tableButton.grid(row=1, column=1)
    tableButton.pack()

    graphButton = tk.Button(screen, text="데이터 조회(Graph)", command=ClickGraphSearchButton)
    #graphButton.grid(row=1, column=2)
    graphButton.pack()

    mapButton = tk.Button(screen, text="지도 조회", command=ClickMapButton)
    #graphButton.grid(row=1, column=3)
    mapButton.pack()
    exitButton = tk.Button(screen, text="종료", command=ClickExitButton)
    #graphButton.grid(row=1, column=4)
    exitButton.pack()

def ClickSearchButton():
    print("버튼 클릭")
    
def ClickTableSearchButton():
    print("Table버튼 클릭")
def ClickGraphSearchButton():
    print("Graph버튼 클릭")
def ClickRecommendSearchButton():
    print("Recommend버튼 클릭")
def ClickMapButton():
    print("Map버튼 클릭")
def ClickExitButton():
    print("Exit버튼 클릭")
    

def MakeLabel():
    mainLabel = tk.Label(screen, text="\n창업 지원 프로그램에 오신 것을 환영합니다.\n메뉴를 선택하세요")
    mainLabel.pack()
    
#def SelectMenu():
    #return something

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
    ShowMainScreen()
    #input = SelectMenu()

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

    #End Process

    
