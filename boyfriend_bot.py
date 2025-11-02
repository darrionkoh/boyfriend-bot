from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8211990989:AAHXzCP0griHiRlu-3gPgnx4lhJoISHeECc"

async def assure(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("You’re strong. I’m proud of you. You’ve got this — always.")

async def ily(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I love you more than anything 💖")

async def gn(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Goodnight, sleep well and dream of me 🌙")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I’m here with you ❤️")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("assure", assure))
app.add_handler(CommandHandler("ily", ily))
app.add_handler(CommandHandler("gn", gn))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

app.run_polling()
