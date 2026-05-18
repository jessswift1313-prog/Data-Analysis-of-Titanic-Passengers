import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from IPython.display import display

def survival_by_gender(titanic):
    #Preprocessing
    
    survival_by_sex = titanic.groupby(["Sex", "Survived"]).count()
    
    number = len(titanic)
    survival_by_sex_percentage = survival_by_sex / number * 100
    
    display(survival_by_sex_percentage.style.format("{:.2f}%"))
    
    Sex = survival_by_sex_percentage["PassengerId"]
    
    display(Sex.apply(lambda x: f"{x:.2f}%"))
    
    #Visualisation
    
    fig, ax = plt.subplots(1, 1)
    
    outer = Sex.groupby(level = 0).sum()
    inner = Sex
    outer_colors = ["tomato", "royalblue"]
    inner_colors = ["mistyrose", "tomato", "lightblue", "royalblue"]
    outer_labels = ["female", "male"]
    inner_labels = ["female ✟", "female ♥", "male ✟", "male ♥"]
    
    ax.pie(
        outer,
        colors = outer_colors,
        radius = 1,
        labels = outer_labels,
        labeldistance = 1.2,
        autopct = ("%4.1f%%"), # place the numbers
        pctdistance = 1.08,
        wedgeprops = dict(width = 0.5, edgecolor = "white"), # width -> central empty circle
        textprops = dict(fontsize = 12)
    )
    
    ax.pie(
        inner,
        colors = inner_colors,
        radius = 0.9,
        labels = inner_labels,
        labeldistance = 0.5,
        autopct = ("%4.1f%%"),
        pctdistance = 0.8,
        wedgeprops = dict(width = 0.5, edgecolor = "white"),
        textprops = dict(fontsize = 10),
    )
    ax.legend(bbox_to_anchor = (1.3, 0.5))
    ax.set_title("Répartition des surviants selon le sexe")
    
    plt.show()
    fig.savefig("outputs/survival_by_gender.png")
    plt.close()
    
    return 