from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder.appName("TestApp").getOrCreate()

# Run a simple transformation
df = spark.range(5)
df.show()
