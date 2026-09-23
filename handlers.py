from telegram import Update
from telegram.ext import ContextTypes
from logger import logger


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    logger.info(f"/start از کاربر {user.id} (@{user.username}) دریافت شد.")
    await update.message.reply_text("سلام، حالت خوبه؟")


async def on_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not update.message or not update.message.text:
        return

    user = update.effective_user
    text = update.message.text.strip()

    logger.info(
        f"پیام از {user.id} (@{user.username}) | chat_id={update.effective_chat.id} | متن: {text!r}"
    )

    if text.startswith("سلام"):
        logger.info(f"پاسخ سلام ارسال شد برای {user.id}")
        await update.message.reply_text("سلام، حالت خوبه؟")
    else:
        logger.info(f"پاسخ پیش‌فرض ارسال شد برای {user.id}")
        await update.message.reply_text(
            "سلام! اگر می‌خوای جواب بدم بنویس: سلام"
        )


async def on_error(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.error(f"خطا در پردازش آپدیت: {context.error}", exc_info=context.error)
