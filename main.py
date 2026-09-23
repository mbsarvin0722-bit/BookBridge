from bot import build_application
from config import WEBHOOK_URL, WEBHOOK_PATH, WEBHOOK_SECRET, PORT, LISTEN
from logger import logger


def main() -> None:
    logger.info("========== شروع ربات ==========")
    logger.info(f"پایتون در حال اجرا روی {LISTEN}:{PORT}")

    try:
        app = build_application()

        webhook_full_url = f"{WEBHOOK_URL}{WEBHOOK_PATH}"
        logger.info(f"در حال ثبت وبهوک روی: {webhook_full_url}")

        app.run_webhook(
            listen=LISTEN,
            port=PORT,
            url_path=WEBHOOK_PATH,
            webhook_url=webhook_full_url,
            secret_token=WEBHOOK_SECRET or None,
            drop_pending_updates=True,
        )
    except Exception as e:
        logger.exception(f"خطای بحرانی هنگام اجرای ربات: {e}")
        raise
    finally:
        logger.info("========== ربات متوقف شد ==========")


if __name__ == "__main__":
    main()
