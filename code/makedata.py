"""
This file contains code for creating data frames and preparing them
to be analyzed in the other relevant files.
"""
import numpy as np
import pandas as pd


# Check whether our data file exists. If the file does not exist
# then create the appropriate index and columns and save to the
# file where it belongs
if os.path.isfile("../data/stepdata.csv") is False:
    # Create the date ranges
    startdate = pd.datetime(2016, 1, 1, 0, 0)
    enddate = pd.datetime(2016, 12, 31, 23, 59)
    dates = pd.date_range(start=startdate, end=enddate, freq="1min")

    # Create columns for everyone participating
    names = ["Andrew", "Austin", "Chase", "Grey", "Jenna",
             "Jess", "Kevin", "Reid", "Stephen", "Winston"]

    # Create the main data frame and save as csv file
    steps_df = pd.DataFrame(columns=names, index=dates)

else:
    # Read the data that we already have into pandas
    steps_df = pd.read_csv("../data/stepdata.csv",
                           index_col=0, parse_dates=True)

    # Find last date with NO null data
    startdate = steps_df.dropna().index[-1]
    enddate = pd.datetime(2016, 12, 31, 23, 59)

# Save final data back to csv    
steps_df.to_csv("../data/stepdata.csv")
