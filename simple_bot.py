from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

TOKEN = "7512357024:AAEna0UEhcQjd0xktKBd2wAhZ_yJ9j0aG08"

import random
motivational_quotes = ["Ты способен(на) на большее, чем думаешь 💪",
    "Каждый шаг вперёд — это шаг к победе 🚀",
    "Никогда не сдавайся. Самое трудное — начать 💥",
    "Будь тем, кто делает, а не тем, кто ждёт 🌟",
    "Сегодня — идеальный день, чтобы начать 🌈"]

random_facts = ["🧠 Мозг человека работает быстрее, чем любой компьютер.",
    "🌍 На Земле больше деревьев, чем звёзд в галактике.",
    "🐙 У осьминога три сердца!",
    "🚀 Свет от Солнца доходит до Земли за 8 минут и 20 секунд.",
    "🎵 Музыка может улучшать память и внимание."]

# --- Доп. клавиатура с кнопками
user_keyboard = ReplyKeyboardMarkup(
    [["О боте", "Картинка"], ["Помощь", "Мотивация"], ["Факт"]],
    resize_keyboard=True)

# --- Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я твой Telegram-бот. Выбери, что хочешь сделать:",
        reply_markup=user_keyboard
    )

# --- Команда /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
    "Я помогу тебе! Вот что я умею:\n"
    "/start - запустить бота\n"
    "/help - получить это сообщение\n"
    "\nВ будущем я буду ещё умнее ❤️",
    reply_markup=user_keyboard
)


# --- Команда /about или кнопка "О боте"
async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
    "Я — простой бот, созданный для практики.\n"
    "Могу повторять твои сообщения и прислать картинку!",
    reply_markup=user_keyboard
)

# --- Команда /pic или кнопка "Картинка"
async def send_pic(update: Update, context: ContextTypes.DEFAULT_TYPE):
    with open("smart.jpg", "rb") as photo:
        await update.message.reply_photo(photo, caption="Вот твоя картинка!")

# --- Обработка любого текста
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if text == "о боте":
        await about_command(update, context)
    elif text == "картинка":
        await send_pic(update, context)
    elif text == "помощь":
        await help_command(update, context)
    elif text == "мотивация":
        await motivation_command(update, context)
    elif text == "факт":
        await random_fact_command(update, context)
    else:
        await update.message.reply_text(f"Ты сказал: {update.message.text}")
  
# --- Меню
async def menu_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Вот меню:",
        reply_markup=user_keyboard
    )

# --- Команда /motivation или кнопка "Мотивация"
async def motivation_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    quote = random.choice(motivational_quotes)
    await update.message.reply_text(quote, reply_markup=user_keyboard)     

# --- Команда /facts или кнопка "Факт"
async def random_fact_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    fact = random.choice(random_facts)
    await update.message.reply_text(fact, reply_markup=user_keyboard)

# --- Точка входа
if __name__== "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("about", about_command))
    app.add_handler(CommandHandler("pic", send_pic))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    app.add_handler(CommandHandler("menu", menu_command))
    app.add_handler(CommandHandler("motivation", motivation_command))
    app.add_handler(CommandHandler("fact", random_fact_command))

    print("Бот запущен! Жду команд в Telegram...")
    app.run_polling()