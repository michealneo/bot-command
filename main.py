from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

Token: Final = "6704443537:AAFobi4Flxmm7pto_tIADoM0tTsrFLD7Z64"
BOT_USERNAME: Final = "@michealneo_bot"


# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello,Thanks for chatting... I be your favorite bot and my work na giude my "
                                    "fellow Nigerians grow in the tech world.")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """
Python na very sweet programming language and most most Nigeria wey get interest no fit afford the course. 
So i wan help myself and also help those wey wan learn as we grow together.
        """
    )


async def goal_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("My goal na to create and build sharp minds wey go excel in the world of tech.")


async def contact_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """
Follow me at...
Twitter: http://X.com/CODEWITHFRAYO
Phone No: 070xxxxxx37
Email: amosfridayogb@gmail.com
        """
    )


# Responses
def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'hello' in processed:
        return 'Hey there!'

    if 'how are you' in processed:
        return 'I am good!'

    if 'I love python' in processed:
        return 'Remember to subcribe!'

    return "I don't understand what you've written"


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f"User ({update.message.chat.id}) in {message_type}: '{text}'")

    if message_type == "group":
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, "").strip()
            response: str = handle_response(new_text)
        else:
            response: str = handle_response(text)

        print("Bot", response)
        await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")

if __name__ == "__main__":
    print("Starting bot...")
    app = Application.builder().token(Token).build()

    # Commands
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("goal", goal_command))
    app.add_handler(CommandHandler("contact", contact_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    # Polls the bot
    print("Polling...")
    app.run_polling(poll_interval=1)
