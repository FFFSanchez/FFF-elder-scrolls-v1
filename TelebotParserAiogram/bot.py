import config
import logging
import asyncio
from datetime import datetime

from aiogram import Bot, Dispatcher, executor, types
from sqlighter import SQLighter

from stopgame import StopGame


# set logs level
logging.basicConfig(level=logging.INFO)

# init bot
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

# init DB connection
db = SQLighter('SQLdb.db')

# init parser
sg = StopGame('lastkey.txt')

# Subscription activate command
@dp.message_handler(commands=['subscribe'])
async def subscribe(message: types.Message):
	if not db.subscriber_exists(message.from_user.id):
		# if user not in base - lets add him
		db.add_subscriber(message.from_user.id)
	else:
		# if user already in base - update his status
		db.update_subscription(message.from_user.id, status=True)

	await message.answer('You were subscribed to news!\nWait for more content :)')	


# Subscription deactivate command
@dp.message_handler(commands=['unsubscribe'])
async def unsubscribe(message: types.Message):
	if not db.subscriber_exists(message.from_user.id):
		# if user not in base - lets just remember him
		db.add_subscriber(message.from_user.id, False)
		await message.answer("However you were not a subscriber")
	else:
		# if user already in base - update his status
		db.update_subscription(message.from_user.id, False)

	await message.answer('You were unsubscribed successfully :)')	

# check new games and send messages
async def scheduled(wait_for):
	while True:
		await asyncio.sleep(wait_for)

		# check games
		new_games = sg.new_games()

		if new_games:
			# if yes reverse list and iterate
			new_games.reverse()
			for ng in new_games:
				# parse info about new game
				nfo = sg.game_info(ng)

				# get list of subscribers
				subscriptions = db.get_subscriptions()

				# send new to subs
				with open(sg.download_image(nfo['image']), 'rb') as photo:
					for s in subscriptions:
						await bot.send_photo(
								s[1],
								photo,
								caption = nfo['title'] + '\n' + 'Score: ' + nfo['score'] + '\n' + nfo['except'] + '\n\n' + nfo['link'],
								disable_notification = True

							)
				# refresh key
				sg.update_lastkey(nfo['id'])

'''
#timer test
async def scheduled(wait_for):
	while True:
		await asyncio.sleep(wait_for)

		now = datetime.utcnow()
		await bot.send_message(316117232, f'{now}', disable_notification=True)

# echo
@dp.message_handler()
async def echo(message: types.Message):
	await message.answer(message.text)
'''


# launch long polling
if __name__== '__main__':
	loop = asyncio.get_event_loop()
	loop.create_task(scheduled(10))
	executor.start_polling(dp, skip_updates=True)

	