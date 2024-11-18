use polars::prelude::*;
use std::time::Instant;

fn main() {

    
    
    let now = Instant::now();
    let df = CsvReadOptions::default()
        .try_into_reader_with_file_path(Some(r"E:\Training\rust\Datasets\Electric_Vehicle_Population_Data.csv".into()))
        .unwrap()
        .finish()
        .unwrap();
    
    let legislative_district = df
                        .clone()
                        .lazy()
                        .filter(col("Legislative District").eq(lit(15)))
                        .select([
                            cols(["Make", "Model"]),
                            ])
                        .collect();
    
    let elapsed = now.elapsed();
    println!("Elapsed: {:.2?}", elapsed);
                    
    print!("{:?}",legislative_district);
}
