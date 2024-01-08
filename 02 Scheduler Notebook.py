# Databricks notebook source
# MAGIC %md
# MAGIC ## This is the scheduler notebook

# COMMAND ----------

dbutils.notebook.run("03 Bronze to Silver", 300)

# COMMAND ----------

dbutils.notebook.run("04 Silver to Gold", 300)
