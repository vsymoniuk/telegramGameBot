import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))

DB_CONF = {
    'host': str(os.getenv("DB_HOST")),
    'user': str(os.getenv("DB_USER")),
    'database': str(os.getenv("DB_DATABASE")),
    'password': str(os.getenv("DB_PASSWORD")),
    'port': str(os.getenv("DB_PORT"))
}
