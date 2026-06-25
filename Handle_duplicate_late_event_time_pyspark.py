from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.window import Window

spark = SparkSession.builder \
    .appName("DuplicateAndLateEventDetection") \
    .getOrCreate()

# ---------------------------------------------------
# Add arrival order
# ---------------------------------------------------

data = [
    (1, "C1", "E1", "2026-06-24T10:00:00"),
    (2, "C1", "E2", "2026-06-24T10:05:00"),
    (3, "C1", "E1", "2026-06-24T10:00:00"),  # Duplicate + Late
    (4, "C1", "E3", "2026-06-24T09:55:00"),  # Late
    (5, "C2", "E4", "2026-06-24T11:00:00"),
    (6, "C2", "E5", "2026-06-24T10:50:00")   # Late
]

columns = ["arrival_order","customer_id","event_id","event_time"]


df = spark.createDataFrame(data, columns)

df = df.withColumn("event_time",to_timestamp("event_time"))


print("Original Data")
df.show(truncate=False)

# =====================================================
# DUPLICATE DETECTION
# =====================================================

duplicate_window = Window.partitionBy("customer_id","event_id").orderBy("arrival_order")


duplicates_df = df.withColumn("row_num",row_number().over(duplicate_window)).filter(col("row_num") > 1).drop("row_num")

print("Duplicates")
duplicates_df.show(truncate=False)

# =====================================================
# TRUE LATE EVENT DETECTION
# =====================================================

late_window = Window.partitionBy("customer_id").orderBy("arrival_order").rowsBetween(Window.unboundedPreceding,-1)



df = df.withColumn("max_previous_event_time",max("event_time").over(late_window))


late_events_df = df.filter(col("event_time") < col("max_previous_event_time"))

print("Late Events")
late_events_df.show(truncate=False)