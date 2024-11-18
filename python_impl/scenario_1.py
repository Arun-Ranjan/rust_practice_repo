# Vehicles that are electric(any EV type) in a specific state(e.g., California)

import pandas as pd
import time
from memory_profiler import profile
@profile
def func():

    # city = input("Enter the city name")
    start_time = time.time()

    # Read the CSV file
    df = pd.read_csv(r"E:\Training\rust\Datasets\Electric_Vehicle_Population_Data.csv")

    # Filter and select the required columns
    state_vehicles = df[df["City"] == "Seabeck"][["Electric Vehicle Type", "City"]]

    elapsed_time = time.time() - start_time
    print(f"Elapsed: {elapsed_time:.4f} seconds")
    state_vehicles


func()