from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "38498066"))
API_HASH = getenv("API_HASH", "c9696114751feacdeb1b4487f5839a1a")

BOT_TOKEN = getenv("BOT_TOKEN", " ")
OWNER_ID = int(getenv("OWNER_ID", "8703802029"))

MONGO_DB_URI = getenv("mongodb+srv://vivek:1234567890@cluster0.c48d8ih.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
MUST_JOIN = getenv("MUST_JOIN", "ALPHA_SAYS")
