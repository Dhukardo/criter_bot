import telegram
from telegram.ext import Updater, CommandHandler

token = "531793124:AAG4aWW484TmfQL8YrdhU_jfmM_fCBVs01M"

def hola (bot,update):
	msg = update.message.text
	bot.send_message(
                chat_id=update.message.chat_id,
                text= "Ñiargh! Deja de molestar!"
            )
updater = Updater(token)
dp = updater.dispatcher
start_handler = CommandHandler('hola', hola)
dp.add_handler(start_handler)
updater.start_polling()