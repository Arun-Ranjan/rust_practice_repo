# Vehicles registered in a specific legislative district (e.g., Legislative District 15)

import pandas as pd
import time
from memory_profiler import profile

@profile
def func():
    start_time = time.time()
    df = pd.read_csv(r"E:\Training\rust\Datasets\Electric_Vehicle_Population_Data.csv")

    legislative_district = df[df["Legislative District"] == 15][["Make", "Model"]]

    elapsed_time = time.time() - start_time
    print(f"Elapsed: {elapsed_time:.4f} seconds")

    print(legislative_district.shape)
    legislative_district.head()


func()