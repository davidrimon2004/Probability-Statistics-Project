import math
import statistics as stat
import pandas as pd
data ="Diabetes Dataset.csv"
def Bar(x,y,IndX,IndY):
    mat.bar(x,y)
    mat.xlabel(read.columns[IndX])
    mat.ylabel(read.columns[IndY])
    mat.show()
data ="Diabetes Dataset.csv"
read=pd.read_csv(data)
preg=read['Pregnancies']         #index=0
gloc=read['Glucose']             #index=1
pressure=read['BloodPressure']   #index=2
