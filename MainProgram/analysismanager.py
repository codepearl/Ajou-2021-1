from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
import datamanager as dm

manager_name="analysismanager"


def FreqTop(isArea, li): #Freq=빈도, Top=빈도수 상위
    dmdata = dm.DataSearch(isArea, li, manager_name)
    countsdata=dmdata.value_counts().rename_axis('Red Ocean').reset_index(name='Counts')
    perdata=(dmdata.value_counts(normalize=True).rename_axis('Red Ocean').reset_index(name='Percentage'))*100
    perdata.drop('Red Ocean',axis=1,inplace=True)
    perdata=perdata.round(1)
    totaldata=pd.concat([countsdata,perdata],axis=1)
    freqtotal=totaldata.head(15)
    return freqtotal

def FreqBottom(isArea, li): #Freq=빈도, Bottom=빈도수 하위
    dmdata = dm.DataSearch(isArea, li, manager_name)
    countsdata=dmdata.value_counts(ascending=True).rename_axis('Blue Ocean').reset_index(name='Counts')
    perdata=(dmdata.value_counts(normalize=True,ascending=True).rename_axis('Blue Ocean').reset_index(name='Percentage'))*100
    perdata.drop('Blue Ocean',axis=1,inplace=True)
    perdata=perdata.round(1)
    totaldata=pd.concat([countsdata,perdata],axis=1)
    freqtotal=totaldata.head(15)
    return freqtotal

def WordCloudTop(isArea, li):
    dmdata=FreqTop(isArea,li)
    wcdata=dmdata['Red Ocean']
    wc_all=''
    for i in range(len(wcdata)):
        wc_all=wc_all+wcdata[i]+' '
    wc_all=str(wc_all)
    wc_gui=WordCloud(width=1000,height=600,background_color="white",random_state=0,font_path=r'c:\windows\Fonts\malgun.ttf')
    wc_gui_show=wc_gui.generate(wc_all)
    #plt.imshow(wc_gui_show)
    wc_gui_show.to_file('graph/wordcloud.png')
    plt.axis("off")
    #return plt.show()

def WordCloudBottom(isArea, li):
    dmdata=FreqBottom(isArea,li)
    wcdata=dmdata['Blue Ocean']
    wc_all=''
    for i in range(len(wcdata)):
        wc_all=wc_all+wcdata[i]+' '
    wc_all=str(wc_all)
    wc_gui=WordCloud(width=1000,height=600,background_color="white",random_state=0,font_path=r'c:\windows\Fonts\malgun.ttf')
    wc_gui_show=wc_gui.generate(wc_all)
    wc_gui_show.to_file('graph/wordcloud.png')
    #plt.imshow(wc_gui_show)
    plt.axis("off")
    #return plt.show()
