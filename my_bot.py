from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes


TOKEN = "8074264010:AAE3vcGnBpz2yoL2LQrvGwWbJhc91p4NIsQ"
"YOUR_BOT_TOKEN_HERE"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я твой первый бот :)")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет!")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("Бот запущен!")
    print("Я учусь делать чат-ботов!")
    app.run_polling()

if __name__ == "__main__":
    main()