# Read a CSV file from the Lakehouse Files area
df = spark.read.format("csv") \
    .option("header", "true") \
    .load("Files/raw/your_file.csv")

df.show(10)
