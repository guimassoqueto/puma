from dotenv import load_dotenv
from os import getenv
load_dotenv()

# Postgres connection
POSTGRES_DB = getenv("POSTGRES_DB", "postgres")
POSTGRES_HOST = getenv("POSTGRES_HOST", "localhost")
POSTGRES_PASSWORD = getenv("POSTGRES_PASSWORD", "password")
POSTGRES_PORT = getenv("POSTGRES_PORT", "5432")
POSTGRES_USER = getenv("POSTGRES_USER", "postgres")
TABLE_NAME = getenv("TABLE_NAME", "sports")

# puma outlet page
PUMA_SNEAKERS_URL = getenv("PUMA_SNEAKERS_URL", "")

# max concurrency
MAX_CONCURRENCY = int(getenv("MAX_CONCURRENCY", 8))

AWIN_ID=getenv("AWIN_ID", "")
AWIN_AFFID=getenv("AWIN_AFFID", "")