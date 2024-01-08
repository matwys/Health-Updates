# Databricks notebook source
# MAGIC %md
# MAGIC ## This is notebook for mounting container
# MAGIC Go to https://\<databricks-instance\>#secrets/createScope. This URL is case sensitive; scope in createScope must be uppercase.

# COMMAND ----------

application_id = dbutils.secrets.get(scope="databricks-secrets777",key="applicationid")
tenant_id = dbutils.secrets.get(scope="databricks-secrets777",key="tenantid")
secret = dbutils.secrets.get(scope="databricks-secrets777",key="secret")

# COMMAND ----------

container_name = "health-updates"
account_name = "datalake777777"
mount_point = "/mnt/health-updates"

# COMMAND ----------

configs = {"fs.azure.account.auth.type": "OAuth",
          "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
          "fs.azure.account.oauth2.client.id": application_id,
          "fs.azure.account.oauth2.client.secret": secret,
          "fs.azure.account.oauth2.client.endpoint": f"https://login.microsoftonline.com/{tenant_id}/oauth2/token"}
 
dbutils.fs.mount(
  source = f"abfss://{container_name}@{account_name}.dfs.core.windows.net/",
  mount_point = mount_point,
  extra_configs = configs)
