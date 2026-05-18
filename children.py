import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from IPython.display import display

def survival_by_children(titanic):
    titanic_age = titanic[titanic["Age"].notna()]
    display(titanic_age)
    
    children = titanic_age[titanic_age["Age"] < 18]
    Age = children.groupby(["Survived"]).count() / len(children) * 100
    display(Age["PassengerId"].apply(lambda x : f"{x:.2f}%"))
    
    print()
    survival_rate_children = len(children[children["Survived"] == 1]) / len(children) * 100
    print(f"The survival rate of the children is {survival_rate_children:.2f}%")

    return