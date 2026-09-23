import os
from dotenv import load_dotenv
from logger import logger

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN", "")
WEBHOOK_URL = os.getenv("WEBHOOK_URL", "").rstrip("/")
WEBHOOK_PATH = os.getenv("WEBHOOK_PATH", "/telegram/webhook")
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET", "")
PORT = int(os.getenv("PORT", "10000"))
LISTEN = os.getenv("LISTEN", "0.0.0.0")

if not BOT_TOKEN:
    logger.critical("BOT_TOKEN تنظیم نشده است. برنامه متوقف می‌شود.")
    raise RuntimeError("BOT_TOKEN تنظیم نشده.")

if not WEBHOOK_URL:
    logger.critical("WEBHOOK_URL تنظیم نشده است. برنامه متوقف می‌شود.")
    raise RuntimeError("WEBHOOK_URL تنظیم نشده.")

logger.info("تنظیمات با موفقیت بارگذاری شد.")
logger.info(f"WEBHOOK_URL = {WEBHOOK_URL}{WEBHOOK_PATH}")
logger.info(f"LISTEN = {LISTEN}:{PORT}")
