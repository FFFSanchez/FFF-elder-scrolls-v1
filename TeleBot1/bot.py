import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
	'''welcome sticker and welcome msg'''
	sti = open('stickers/sticker_owl.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)

	#keyboard
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton('Random number')
	item2 = types.KeyboardButton('Wazzup?')

	markup.add(item1, item2)

	bot.send_message(message.chat.id, 'Welcome, {0.username}!\nThis is <b>{1.first_name}</b>, bot for downloading Youtube videos.'.format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def lalala(message):
	#'''echo message'''
	#bot.send_message(message.chat.id, message.text)
	if message.chat.type == 'private':
		if message.text == 'Random number':
			bot.send_message(message.chat.id, str(random.randint(0,100)))
		elif message.text == 'Wazzup?':

			markup = types.InlineKeyboardMarkup(row_width=2)
			item1 = types.InlineKeyboardButton('Good', callback_data='good')
			item2 = types.InlineKeyboardButton('So-so', callback_data='bad')

			markup.add(item1, item2)

			bot.send_message(message.chat.id, 'I am fine cause im bot!', reply_markup=markup)
		else:
			bot.send_message(message.chat.id, 'Soo, impossible :)')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	try:
		if call.message:
			if call.data == 'good':
				bot.send_message(call.message.chat.id, 'Im glad to see it!')
			elif call.data == 'bad':
				bot.send_message(call.message.chat.id, 'I wish it will be getting better bro!')
			#remove inline buttons
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Wazzup?', reply_markup=None)
			# show alert
			bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text='This is test alertion!!!1!')


	except Exception as e:
		print(repr(e))


# RUN
bot.polling(none_stop=True)