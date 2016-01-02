"""
This file reads in the stepdata.csv file and performs some
basic analysis and generates relevant plots from it.
"""
import numpy as np
import pandas as pd


steps_df = pd.read_csv("../data/stepdata.csv",
                       index_col=0, parse_dates=True)

