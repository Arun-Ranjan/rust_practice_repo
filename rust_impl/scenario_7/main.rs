use polars::prelude::*;
use std::time::Instant;


fn main() {
    let now = Instant::now();
    let df = CsvReadOptions::default()
        .try_into_reader_with_file_path(Some(r"E:\Training\rust\Datasets\Electric_Vehicle_Population_Data.csv".into()))
        .unwrap()
        .finish()
        .unwrap();
    
    
    
    let number_EV_vehicles_df = df
                            .lazy()
                            .group_by([col("Make"),col("Model Year")])
                            .agg([col("Make").count().alias("Vehicle Count")])
                            .collect();
    
    
    let elapsed = now.elapsed();
    println!("Elapsed: {:.2?}", elapsed);
    
    println!("{:?}", number_EV_vehicles_df);
}
