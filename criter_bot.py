#LLAMADA AL PROCESO

import telegram
from telegram.ext import Updater, CommandHandler

#LLAMADA AL BOT

token = ("531793124:AAG4aWW484TmfQL8YrdhU_jfmM_fCBVs01M")

#DEFINIENDO FUNCION DE MENSAJES POR COMANDO

def hola(bot, update):
    update.message.reply_text(
        'Ñiargh! Deja de molestar {} !'.format(update.message.from_user.first_name))
	
def ayuda (bot,update):
	msg = update.message.text
	bot.send_message(
                chat_id=update.message.chat_id,
                text= "Patos@! Aun estamos preparando esta seccion!")


# BUSCAR

updater = Updater ("531793124:AAG4aWW484TmfQL8YrdhU_jfmM_fCBVs01M")
dp = updater.dispatcher

	
#LLAMADA A FUNCIONES DE MENSAJE
	
command_handler = CommandHandler('hola', hola)
start_handler = CommandHandler('ayuda', ayuda)

# BUSCAR

dp.add_handler(command_handler)
dp.add_handler(start_handler)
updater.start_polling()
updater.idle()
