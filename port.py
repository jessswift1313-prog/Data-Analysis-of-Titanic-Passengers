import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from IPython.display import display

def survival_by_port(titanic):
    #Preprocessing
    
    Embarked = titanic.groupby(["Embarked"]).count()
    Nan_Embarked = titanic[titanic["Embarked"].isna()]
    display(Embarked["PassengerId"])
    display(Nan_Embarked)
    print(f"The number of people who doesn't have information about embarked is {len(Nan_Embarked)}")
    
    Nan_Embarked = titanic[titanic["Embarked"].isna()]
    display(Nan_Embarked["Name"])
    
    titanic.at[61, "Embarked"] = "S"
    titanic.at[829, "Embarked"] = "S"
    
    display(len(titanic[titanic["Embarked"].isna()]) == 0)
    
    #Visualisation
    
    fig, ax = plt.subplots(1, 1)
    
    Port = titanic.groupby(["Embarked","Survived"])["PassengerId"].count() / len(titanic) * 100
    
    outer = Port.groupby(level = 0).sum()
    inner = Port
    outer_colors = ["tomato", "royalblue", "forestgreen"]
    inner_colors = ["mistyrose", "tomato", "lightblue", "royalblue", "lightgreen", "forestgreen"]
    outer_labels = ["C", "Q", "S"]
    inner_labels = ["C ✟", "C ♥", "Q ✟", "Q ♥", "S ✟", "S ♥"]
    
    ax.pie(
        outer,
        colors = outer_colors,
        radius = 1,
        labels = outer_labels,
        labeldistance = 1.23,
        autopct = ("%4.1f%%"), # place the numbers
        pctdistance = 1.11,
        wedgeprops = dict(width = 0.5, edgecolor = "white"), # width -> central empty circle
        textprops = dict(fontsize = 10)
    )
    
    #inner.plot(ax=..., kind = 'pie')
    ax.pie(
        inner,
        colors = inner_colors,
        radius = 0.9,
        labels = inner_labels,
        labeldistance = 0.55,
        autopct = ("%4.1f%%"),
        pctdistance = 0.85,
        wedgeprops = dict(width = 0.5, edgecolor = "white"),
        textprops = dict(fontsize = 8),
    )
    ax.legend(loc = 'center left',bbox_to_anchor = (1, .5))
    ax.set_title("Distribution of survivors according to port", fontsize = 11)
    
    plt.show()
    fig.savefig("outputs/survival_by_port.png")
    plt.close()
    
    return