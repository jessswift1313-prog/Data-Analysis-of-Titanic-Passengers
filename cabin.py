import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from IPython.display import display

def survival_by_class(titanic):
    #Preprocessing
    
    if(len(titanic[titanic["Pclass"].isna()]) != 0):
        raise ValueError("Pclass has empty datas")
    
    Cabine = titanic.groupby(["Pclass", "Survived"]).count()["PassengerId"]
    display(Cabine)
    
    #Visualisation
    
    fig, ax = plt.subplots(1, 1)
    
    outer = Cabine.groupby(level = 0).sum()
    inner = Cabine
    outer_colors = ["tomato", "royalblue", "forestgreen"]
    inner_colors = ["mistyrose", "tomato", "lightblue", "royalblue", "lightgreen", "forestgreen"]
    outer_labels = ["class 1", "class 2", "class 3"]
    inner_labels = ["1 ✟", "1 ♥", "2 ✟", "2 ♥", "3 ✟", "3 ♥"]
    
    ax.pie(
        outer,
        colors = outer_colors,
        labels = outer_labels,
        labeldistance = 1.2,
        wedgeprops = dict(width = 0.5, edgecolor = "white"),
        autopct = ("%4.1f%%"),
        pctdistance = 1.09,
        textprops = {"fontsize" : 8}
    )
    
    ax.pie(
        inner,
        colors = inner_colors,
        labels = inner_labels,
        labeldistance = 0.5,
        radius = 0.9,
        wedgeprops = dict(width = 0.5, edgecolor = "white"),
        autopct = "%4.1f%%",
        pctdistance = 0.75,
    )
    
    ax.legend(bbox_to_anchor = (1, 0.5))
    ax.set_title("Distribution of survivors by class")
    
    plt.show()
    fig.savefig("outputs/survival_by_cabin.png")
    plt.close()

    return