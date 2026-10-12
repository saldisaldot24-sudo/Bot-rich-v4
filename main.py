import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 BOT KAYA V4 AKTIF 24 JAM 🔥\n\n"
        "Bot sudah jalan di Render.com\n"
        "✅ Anti 100% used\n"
        "Ketik /signal untuk cek"
    )

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📈 SIGNAL KAYA V4\n\n"
        "Pair: BTC/USDT\n"
        "TF: 5M\n"
        "Status: Bot Aktif di Cloud ✅\n"
        "Setup lengkap RICH V4 nanti kita upgrade disini"
    )

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot Online 24 Jam di Render")

if __name__ == '__main__':
    if not BOT_TOKEN:
        print("ERROR: Set TELEGRAM_BOT_TOKEN di Render")
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("signal", signal))
    app.add_handler(CommandHandler("status", status))
    print("BOT KAYA V4 RUNNING...")
    app.run_polling()
