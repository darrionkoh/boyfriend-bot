import random
from flask import Flask
from threading import Thread
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os

TOKEN = "8211990989:AAHXzCP0griHiRlu-3gPgnx4lhJoISHeECc"

# --- Bot functions (your existing ones) ---
async def assure(update: Update, context: ContextTypes.DEFAULT_TYPE):
    messages = [
        "hii my lovee, i promise to get back to you safelyy, JUST A FEW MORE DAYS!!",
        "you're doing so well my princess, i cant wait till i see you againn ❤️",
        "YOURE ALWAYS IN MY HEART AND SOUL BABY GIRLLL",
        "i cant wait to be in your arms againn",
        "jiayou baobaoo you can do itt 💪💪",
        "there isnt a time when im not thinking of you my lovee",
        "promise we'll get good food and dessert when im backkk hehe",
        "day by day my clairebearr <3",
        "youre doing amazing baby girl <33",
        "jia youuu you're the goat hehe",
        "everyday brings me closer to kissing you againnnn hehehe",
        "just hang in there okayy, soon i’ll be home making you laugh again",
        "i hope you had a goood meal my baby girlll, you're doing amazing"
    ]
    await update.message.reply_text(random.choice(messages))

async def ily(update: Update, context: ContextTypes.DEFAULT_TYPE):
    messages = [
        "I LOVE YOU SOO MUCH MY PRINCESSSS",
        "muah i love you babyy",
        "i love you darlinggg",
        "hehe I LOVE YOUUUUU",
        "kisskisss i love you princess",
        "i love you so much clairebearr",
        "few more days baby i love youuu",
        "i love youuu",
        "i love you so farking much baby girl",
        "wo ai niiiii toooo",
        "i love you tooo",
        "hehe i love you too darling",
        "if i could spam you with hugs and kisses rn i woulddd"
    ]
    await update.message.reply_text(random.choice(messages))

async def gn(update: Update, context: ContextTypes.DEFAULT_TYPE):
    messages = [
        "goooniii, sleep well okii and dream of me hehe",
        "sleep tight my baby, i’ll be dreaming of youu",
        "goodnight my princess, rest well okayy",
        "close your eyes and feel me hugging you to sleep",
        "sweet dreams baobaoo, i’ll see you in my dreamss",
        "goodnight my babyyy jiayous for tmr okiii you can do this",
        "JIAYOU TMR BABYYY LEFT A BIT MORE TILL IM OUTT",
        "sleep tight baobaooo have a goood eep",
        "I’ll be hugging my rifle pretending it’s you tonite 🥹💞",
        "sleep early okayy i’ll be sad if u tiredtired tomorroww"
    ]
    await update.message.reply_text(random.choice(messages))

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    messages = [
        "im prolly digging a hole rn so shag but youre always with me babyy",
        "i hope youre doing okay my loveee jiayouu",
        "i hope school will go wellll",
        "JIAYOU AT WORKYYY",
        "god i wish i cld be there with you rn",
        "i miss you so much :((",
        "i'll be safe i promiseee",
        "i cant wait to complain to you abt everything im going through",
        "dont forget to tell me about your dayyy (in our chat ofc)",
        "please dont forget to eat and drink more waterrr",
        "i miss your face so bad rn",
        "I MISS YOUUU UGHHHH",
        "im so tired but thinking of you keeps me going hehe"
    ]
    await update.message.reply_text(random.choice(messages))

# --- Dummy Flask server so Render is happy ---
flask_app = Flask("bot_server")

@flask_app.route("/")
def home():
    return "Bot is running!"

# --- Run Flask in separate thread ---
def run_flask():
    port = int(os.environ.get("PORT", 5000))
    flask_app.run(host="0.0.0.0", port=port)

# --- Main bot ---
def main():
    # Start Flask thread
    Thread(target=run_flask).start()

    # Start Telegram polling
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("assure", assure))
    app.add_handler(CommandHandler("ily", ily))
    app.add_handler(CommandHandler("gn", gn))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
