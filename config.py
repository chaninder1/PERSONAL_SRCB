import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7943610633:AAFq-SCESxtCo1K_eut2ky34uRM4pApAhBs")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "27808501"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "9edcc32d1848771360efa9379868d352")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "123456789"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://chanpreet151515:mqlqGcvhGi9aVEgY@cluster0.uzvrequ.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "beastxsrcb")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
