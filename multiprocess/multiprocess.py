from multiprocessing import Pool
import pandas as pd

def multiprocess_df(num_process, f, df):
    input_dfs = []
    increment = len(df)//num_process
    for i in range(num_process):
        input_dfs.append(df[i*increment:(i+1)*increment].reset_index(drop=True))
    with Pool(num_process) as p:
        output_dfs = p.map(f, input_dfs)
    return pd.concat(output_dfs)