from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

# ===== BOT CONFIG =====
TOKEN = "8518838923:AAFkB3Pfzn7z5qKRG_LmHzazg-hJSlyWcO4"

OWNER_USERNAME = "@imabhi3030"
GROUP_LINK = "https://t.me/BCA_bachelor_of_computer_app"
CHANNEL_LINK = "https://t.me/L0L9D9/6"
# ======================


# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📘 Question Papers", callback_data="qp")],
        [InlineKeyboardButton("📚 Notes", callback_data="notes")],
        [InlineKeyboardButton("🎯 Guess Papers", callback_data="guess")],
        [InlineKeyboardButton("📝 Solved Assignments", callback_data="assignment")],
        [InlineKeyboardButton("👤 Owner Help", callback_data="owner")],
        [InlineKeyboardButton("👥 Study Groups", url=GROUP_LINK)],
        [InlineKeyboardButton("📢 Official Channel", url=CHANNEL_LINK)],
        [InlineKeyboardButton("ℹ️ About Bot", callback_data="about")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "👋 *Welcome to IGNOU HELP BOT*\n\n"
        "📚 Question Papers • Notes • Guess Papers\n"
        "📝 Solved Assignments & Student Support\n\n"
        "👇 Select an option:",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )


# Button handler
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "qp":
        await query.edit_message_text("📘 *Question Papers*\n\nCourse-wise papers coming soon 🔜", parse_mode="Markdown")

    elif query.data == "notes":
        await query.edit_message_text("📚 *Notes*\n\nSubject-wise notes will be available 🔜", parse_mode="Markdown")

    elif query.data == "guess":
        await query.edit_message_text("🎯 *Guess Papers*\n\nHigh probability exam questions 🔥", parse_mode="Markdown")

    elif query.data == "assignment":
        await query.edit_message_text("📝 *Solved Assignments*\n\nLatest IGNOU solved assignments 🔜", parse_mode="Markdown")

    elif query.data == "owner":
        await query.edit_message_text(
            f"👤 *Owner Support*\n\n"
            f"Any problem or suggestion?\n"
            f"Contact here 👉 {OWNER_USERNAME}",
            parse_mode="Markdown"
        )

    elif query.data == "about":
        await query.edit_message_text(
            "ℹ️ *About IGNOU HELP BOT*\n\n"
            "✅ Question Papers\n"
            "✅ Notes\n"
            "✅ Guess Papers\n"
            "✅ Solved Assignments\n"
            "✅ Student Help & Support\n\n"
            "Made with ❤️ for IGNOU students",
            parse_mode="Markdown"
        )


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))

app.run_polling(drop_pending_updates=True)
