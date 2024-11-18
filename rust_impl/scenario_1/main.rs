use polars::prelude::*;
use std::time::Instant;

fn main(){

    let now = Instant::now();
    let df = CsvReadOptions::default()
        .try_into_reader_with_file_path(Some(r"E:\Training\rust\Datasets\Electric_Vehicle_Population_Data.csv".into()))
        .unwrap()
        .finish()
        .unwrap();

    let state_vehicles = df
                        .clone()
                        .lazy()
                        .filter(col("City").eq(lit("Seabeck")))
                        .select([
                            cols(["Electric Vehicle Type", "City"]),
                            ])
                        .collect();

    let elapsed = now.elapsed();
    println!("Elapsed: {:.2?}", elapsed);
                    
    print!("{:?}",state_vehicles)

}
