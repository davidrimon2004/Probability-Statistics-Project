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
preg=read[read.columns[0]]         
gloc=read[read.columns[1]]             
pressure=read[read.columns[2]]
thick=read[read.columns[3]]
insulin=read[read.columns[4]]
bmi=read[read.columns[5]]
diabetes=read[read.columns[6]]
age=read[read.columns[7]]
outcome=read[read.columns[8]]
