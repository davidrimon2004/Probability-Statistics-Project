import math
import statistics as stat
import pandas as pd
import matplotlib.pyplot as visual
import seaborn as sb
def Scatterplot(x_axis,y_axis,IndX,IndY):
    sb.scatterplot(x=x_axis,y=y_axis)
    visual.xlabel(read.columns[IndX])
    visual.ylabel(read.columns[IndY])
    visual.show()
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
#plot correalation matrix
plot=read.corr()
sb.heatmap(plot, annot=True, cmap='', fmt=".2f", cbar=True)
visual.show()
#piechart
ct=read[read.columns[8]].value_counts()
visual.pie(ct,labels=['0','1'])
visual.legend()
visual.show()
#Box Plot 
read.boxplot(column=columns[3])
visual.ylabel('')
visual.show()
