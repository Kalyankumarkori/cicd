from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession.builder.appName("SampleSparkApp").getOrCreate()
    input_path = "Custom_folder/input.csv"
    output_path = "Custom_folder/output"
    
    df = spark.read.csv(input_path, header=True, inferSchema=True)
    transformed_df = df.select("name", "age").filter(df["age"] > 18)
    
    transformed_df.write.mode("overwrite").csv(output_path)
    
    spark.stop()
