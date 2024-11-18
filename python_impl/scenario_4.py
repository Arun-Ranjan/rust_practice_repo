# Make and Model of the top high-range electric vehicle

import pandas as pd
import time
from memory_profiler import profile

@profile
def func():
    start_time = time.time()
    df = pd.read_csv(r"E:\Training\rust\Datasets\Electric_Vehicle_Population_Data.csv")
    sorted_df = df.sort_values(by="Electric Range", ascending=False)
    make_model = sorted_df[["Make", "Model","Electric Range"]]

    elapsed_time = time.time() - start_time
    print(f"Elapsed: {elapsed_time:.4f} seconds")

    make_model.head(5)


func()