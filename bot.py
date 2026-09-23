from telegram.ext import Application, CommandHandler, MessageHandler, filters
from config import BOT_TOKEN
from handlers import start, on_message, on_error
from logger import logger


def build_application() -> Application:
    logger.info("در حال ساخت اپلیکیشن ربات...")

    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, on_message)
    )
    application.add_error_handler(on_error)

    logger.info("هندلرها با موفقیت ثبت شدند.")
    return application
