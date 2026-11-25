import asyncpg
from urllib.parse import urlparse, unquote
from config import DATABASE_URL
from logger import logger


async def connect_database():
    if not DATABASE_URL:
        raise RuntimeError("DATABASE_URL تنظیم نشده است.")

    parsed = urlparse(DATABASE_URL)

    pool = await asyncpg.create_pool(
        host=parsed.hostname,
        port=parsed.port or 5432,
        user=unquote(parsed.username or ""),
        password=unquote(parsed.password or ""),
        database=parsed.path.lstrip("/"),
        ssl="require",
        min_size=1,
        max_size=5,
    )

    logger.info("اتصال به دیتابیس با موفقیت برقرار شد.")
    return pool


async def close_database(pool):
    if pool:
        await pool.close()
        logger.info("اتصال دیتابیس بسته شد.")
