import config
import logging
import re
import random
import pafy
import btc_currency

from filters import IsAdminFilter
from aiogram import Bot, Dispatcher, executor, types
'''for this chat admin bot: BotFather /setprivacy DISABLE'''


# log lvl
logging.basicConfig(level=logging.INFO)

# bot init
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

# activate filters
dp.filters_factory.bind(IsAdminFilter)

# ban command (admin only)
@dp.message_handler(is_admin=True, commands=['ban'], commands_prefix='!/')
async def cmd_ban(message: types.Message):
	if not message.reply_to_message:
		await message.reply('This command must be reply to message!')
		return

	await message.bot.delete_message(config.GROUP_ID, message.message_id)	
	await message.bot.kick_chat_member(chat_id=config.GROUP_ID, user_id=message.reply_to_message.from_user.id)
	await message.reply_to_message.reply('User was banned!\nxxxxxxxxxxxxx')

# remove user join/left msges
@dp.message_handler(content_types=['new_chat_members', 'left_chat_member'])
async def on_user_joined(message: types.Message):
	print('JOIN/LEFT msg removed')
	await message.delete()


# check profanity
@dp.message_handler()
async def filter_messages(message: types.Message): #just types annotation?
	if re.search(r'[Ff]uck|\b[Бб]ля.*|\b[ЕеЁё]б.*|[Хх]у[йеё\?].*', message.text):
		# profanity detected, delete
		with open('log.txt', 'a') as l:
			print('MSG with bad word deleted', file=l)
		await message.delete()

	elif re.search(r'\b[Пп]изд.*', message.text):
		await message.reply(random.choice(['Оскорбление администрации расстрел', 'Кемперство бан', 'Читы бан пацанчик']))

	elif message.text == 'Биток скока там ща':
		await message.answer(btc_currency.get_data())


# echo
'''
@dp.message_handler()
async def echo(message: types.Message):
	await message.answer(message.text)
'''

# run long-polling
if __name__ == "__main__":
	executor.start_polling(dp, skip_updates=True)