# Average electric range

import pandas as pd
import time
from memory_profiler import profile
@profile
def func():
    start_time = time.time()
    df = pd.read_csv(r"E:\Training\rust\Datasets\Electric_Vehicle_Population_Data.csv")

    mean = df["Electric Range"].mean()


    elapsed_time = time.time() - start_time
    print(f"Elapsed: {elapsed_time:.4f} seconds")

    print(mean)

func()