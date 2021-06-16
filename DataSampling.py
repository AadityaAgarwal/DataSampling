import csv
import pandas as pd
import plotly_express as px
import plotly.figure_factory as ff
import statistics
import random
import plotly.graph_objects as go

df=pd.read_csv('DataSampling.csv')
data=list(df['reading_time'])

mean=statistics.mean(data)
print(mean)
dataset=[]

def randMean():
    for i in range(0,30):
        randIndex=random.randint(0,len(data)-1)
        value=data[randIndex]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

def showFig(meanList):
    df=meanList
    mean=statistics.mean(df)
    print(mean)
    fig=ff.create_distplot([meanList],['readingTime'],show_hist=False)
    fig.show()

def sample():
    meanList=[]
    for i in range(0,100):
        mean=randMean()
        meanList.append(mean)

    showFig(meanList)
sample()    