from multiprocess import multiprocess_df
from functions.getsignalized import getsignalized
import pandas as pd
import os

if __name__=="__main__":
    intersections = pd.read_csv('datasets/intersections_openlr.csv')
    multiprocess_df(8, getsignalized, intersections).to_csv('outputs/signaled_intersections_openlr.csv', index=False)