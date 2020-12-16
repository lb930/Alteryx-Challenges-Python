# Databricks notebook source
import pyspark.sql.functions as f
from pyspark.sql.functions import *

# COMMAND ----------

df = spark.read.csv("dbfs:/FileStore/tables/challenge_2_input.csv", header="true", inferSchema="true", sep=",", quote="\"", escape="\"")
df.show(2, False)

# COMMAND ----------

split_col = f.split(df['Field_1'], ',')
df = df.withColumn('poem', split_col.getItem(0))
df = df.withColumn('poem_id', split_col.getItem(1))
df = df.withColumn('date', split_col.getItem(2))
df.show(2, False)

# COMMAND ----------

df_2 = df.withColumn('poem', regexp_replace('poem', '"', ''))
df_3 = df_2.withColumn('date', regexp_replace('date', "'", ""))
df_3.show(2, False)

# COMMAND ----------

df_4 = df_3.withColumn('date', to_date(unix_timestamp(col('date'), 'dd-MMM-yy').cast("timestamp")))
df_4.show(2, False)

# COMMAND ----------

df_4.dtypes

# COMMAND ----------

df_5 = df_4.withColumn("poem_id", df_4["poem_id"].cast("int"))
df_5.show(2, False)

# COMMAND ----------

df_6 = df_5.drop('Field_1')
df_6.show(2, False)
