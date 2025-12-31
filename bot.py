from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8518838923:AAFkB3Pfzn7z5qKRG_LmHzazg-hJSlyWcO4"

OWNER_USERNAME = "@imabhi3030"
GROUP_LINK = "https://t.me/BCA_bachelor_of_computer_app"
CHANNEL_LINK = "https://t.me/L0L9D9/6"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📘 Question Papers", callback_data="qp")],
        [InlineKeyboardButton("📚 Notes", callback_data="notes")],
        [InlineKeyboardButton("🎯 Guess Papers", callback_data="guess")],
        [InlineKeyboardButton("📝 Solved Assignments", callback_data="assignment")],
        [InlineKeyboardButton("👤 Owner Help", callback_data="owner")],
        [InlineKeyboardButton("👥 Study Group", url=GROUP_LINK)],
        [InlineKeyboardButton("📢 Official Channel", url=CHANNEL_LINK)],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "👋 Welcome to IGNOU HELP BOT\n\n"
        "All IGNOU study material in one place 👇",
        reply_markup=reply_markup
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "qp":
        await query.edit_message_text("📘 Question Papers coming soon...")
    elif query.data == "notes":
        await query.edit_message_text("📚 Notes coming soon...")
    elif query.data == "guess":
        await query.edit_message_text("🎯 Guess Papers coming soon...")
    elif query.data == "assignment":
        await query.edit_message_text("📝 Solved Assignments coming soon...")
    elif query.data == "owner":
        await query.edit_message_text(f"👤 Owner Help\n\nContact: {OWNER_USERNAME}")


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))

app.run_polling()
