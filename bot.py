from telegram.ext import Application, CommandHandler, MessageHandler, filters
from config import BOT_TOKEN
from handlers import start, on_message, on_error
from database import connect_database, close_database
from logger import logger


async def post_init(application: Application) -> None:
    logger.info("در حال اتصال به دیتابیس...")
    pool = await connect_database()
    application.bot_data["db_pool"] = pool


async def post_shutdown(application: Application) -> None:
    pool = application.bot_data.get("db_pool")
    await close_database(pool)


def build_application() -> Application:
    logger.info("در حال ساخت اپلیکیشن ربات...")

    application = (
        Application.builder()
        .token(BOT_TOKEN)
        .post_init(post_init)
        .post_shutdown(post_shutdown)
        .build()
    )

    application.add_handler(CommandHandler("start", start))
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, on_message)
    )
    application.add_error_handler(on_error)

    logger.info("هندلرها با موفقیت ثبت شدند.")
    return application
