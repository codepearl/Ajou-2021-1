import datamanager as dm
#import graphmanager as gm
#import analysismanager as am
#import mapmanager as mm
import pandas as pd

#input = 0 #user input code (temp)
#categories = []
#return_data #pandas.DataFrame
#return_graph #format undecided (expect plot)
#return_map #format undecided
manager_name = "scenemanager"

#def ShowMainScreen():
    #nonValue-Returning
    
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


if __name__ == '__main__':
    #call function
    #iteration for program

    Test()

    #ShowMainScreen()
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

    
