import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from IPython.display import display

def load_data(title):
    titanic = pd.read_csv(title) # Read the data and convert it into pandas.DataFrame
    
    #Demonstration
    display(titanic)
    display(titanic.info())
    display(titanic.describe())
    display(titanic.isna())

    return titanic