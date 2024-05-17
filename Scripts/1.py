from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(update, context):
    update.message.reply_text('Hello! I am a Telegram bot.')

def echo(update, context):
    update.message.reply_text(update.message.text)

def main():
    updater = Updater("6853278221:AAFXnkqqlafM9KW4Nrdegx9dOzUF6rfwnwM")

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()

    updater.idle()

if __name__ == "__main__":
    main()