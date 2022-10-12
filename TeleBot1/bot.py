import telebot
import config

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
	'''welcome sticker and welcome msg'''
	sti = open('stickers/sticker_owl.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)
	bot.send_message(message.chat.id, 'Welcome, {0.username}!\nThis is <b>{1.first_name}</b>, bot for downloading Youtube videos.'.format(message.from_user, bot.get_me()), parse_mode='html')


@bot.message_handler(content_types=['text'])
def lalala(message):
	'''echo message'''
	bot.send_message(message.chat.id, message.text)

# RUN
bot.polling(none_stop=True)