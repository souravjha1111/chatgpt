from pyChatGPT import ChatGPT
import requests
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
def func(msgs):
	session_token = ''
	api = ChatGPT(session_token)  # auth with session token
	resp = api.send_message(msgs)
	api.refresh_auth()  # refresh the authorization token
	api.reset_conversation()
	return resp['message']

# Replace TOKEN with your bot's token
bot = telegram.Bot(token='')
def start(update, context):
    # Handle the /start command
    # ...
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text="ask me anything")


def handle_message(update, context):
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text="Ohk searching for that")
    response = func(update.message.text)
    bot.send_message(chat_id=chat_id, text=response)
    print(response)
def main():
    # Create the Updater and pass it the bot's token
    updater = Updater(bot.token, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add the command handler for the /start command
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
