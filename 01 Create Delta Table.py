# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE DATABASE healthcare

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS healthcare.health_data (
# MAGIC STATUS_UPDATE_ID INT,
# MAGIC PATIENT_ID INT,
# MAGIC DATE_PROVIDED STRING,
# MAGIC FEELING_TODAY STRING,
# MAGIC IMPACT STRING,
# MAGIC INJECTION_SITE_SYMPTOMS STRING,
# MAGIC HIGHEST_TEMP DOUBLE,
# MAGIC FEVERISH_TODAY STRING,
# MAGIC GENERAL_SYMPTOMS STRING,
# MAGIC HEALTHCARE_VISIT STRING,
# MAGIC UPDATED_TIMESTAMP TIMESTAMP
# MAGIC )
# MAGIC USING delta
# MAGIC LOCATION '/mnt/health-updates/silver/health_data'
