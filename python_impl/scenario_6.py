# Count of electric vehicles by Electric Utility provider.

import pandas as pd
import time
from memory_profiler import profile

@profile
def func():
    start_time = time.time()

    df = pd.read_csv(r"E:\Training\rust\Datasets\Electric_Vehicle_Population_Data.csv")

    # Group by the "County" column and count the number of vehicles for each "Model Year"
    number_EV_vehicles_df = df.groupby(["Electric Utility","Electric Vehicle Type"]).size().reset_index(name="Vehicle Count")

    elapsed_time = time.time() - start_time
    print(f"Elapsed: {elapsed_time:.4f} seconds")

    number_EV_vehicles_df

func()