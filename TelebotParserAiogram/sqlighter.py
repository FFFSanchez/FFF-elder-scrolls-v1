import sqlite3

class SQLighter:

	def __init__(self, database_file):
		'''Connect to DB and save connection cursor'''
		self.connection = sqlite3.connect(database_file)
		self.cursor = self.connection.cursor()
	
	def get_subscriptions(self, status=True):
		"""Get all active subscribers"""
		with self.connection:
			return self.cursor.execute("SELECT * FROM `subscriptions` WHERE `status` = ?", (status,)).fetchall()

	def subscriber_exists(self, user_id):
		'''Check if user already in DB'''
		with self.connection:
			result = self.cursor.execute("SELECT * FROM `subscriptions` WHERE `user_id` = ?", (user_id,)).fetchall()
			return bool(len(result))

	def add_subscriber(self, user_id, status=True):
		'''Add a new subscriber'''
		with self.connection:
			return self.cursor.execute("INSERT INTO `subscriptions` (`user_id`, `status`) VALUES (?,?)", (user_id, status))

	def update_subscription(self, user_id, status):
		'''Update subscription status'''
		with self.connection:
			return self.cursor.execute("UPDATE `subscriptions` SET `status` = ? WHERE `user_id` = ?", (status, user_id))

	def close(self):
		'''Close DB connection'''
		self.connection.close()

