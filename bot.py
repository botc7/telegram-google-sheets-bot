import logging
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ConversationHandler, ContextTypes

# Авторизация Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", scope)
client = gspread.authorize(creds)
sheet = client.open("bot_clients").sheet1

# Этапы диалога
NAME, PHONE = range(2)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Как тебя зовут?")
    return NAME

async def get_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["name"] = update.message.text
    await update.message.reply_text("Отлично! А теперь введи номер телефона:")
    return PHONE

async def get_phone(update: Update, context: ContextTypes.DEFAULT_TYPE):
    phone = update.message.text
    name = context.user_data["name"]
    telegram_id = update.message.from_user.id
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Запись в Google Таблицу
    sheet.append_row([name, phone, str(telegram_id), now])
    await update.message.reply_text("Спасибо! Ты записан(а) ✅")
    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Запись отменена.")
    return ConversationHandler.END

if __name__ == "__main__":
    app = ApplicationBuilder().token("7707441254:AAH99_aKYd9cp7dg8gjffGrKzGqmEuRFSHs").build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_name)],
            PHONE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_phone)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    app.add_handler(conv_handler)
    print("Бот запущен!")
    app.run_polling()

