import Location
import Hero
import random
from pprint import pprint
import telebot
from telebot import types

TOKEN = "1701739381:AAH_F8BsVgn1b-34nqYSUNCmuM0dZH4ATbs"
locations = []
hero = []
bot = telebot.TeleBot(TOKEN)

def Button():
	markup = types.ReplyKeyboardMarkup(row_width=2)
	key1 = types.KeyboardButton('влево')
	key2 = types.KeyboardButton('вправо')
	key3 = types.KeyboardButton('вверх')
	key4 = types.KeyboardButton('вниз')
	key5 = types.KeyboardButton('осмотреться')
	markup.add(key1, key2, key3, key4, key5)

	return markup

def SpawHero(locations):

	start_location = random.randint(0,len(locations)-1)
	for i in range(len(locations[start_location].field)-1):
		for j in range(len(locations[start_location].field[i])-1):
			if locations[start_location].field[i][j]==0:
				hero.currentLocation = locations[start_location]
				locations[start_location].field[i][j] = hero
				locations[start_location].positionHero = [i,j]
				return



@bot.message_handler(commands=['info'])
def send_welcome(message):
	bot.send_message(message.chat.id,'Добро пожаловать в Игру "XXXX"')
	bot.send_message(message.chat.id,'1. Эта игра про выживание и приключения')	
	bot.send_message(message.chat.id,'2. В игре перманентная смерть! Если вы умерли это означает конец игры    :[')
	bot.send_message(message.chat.id,'3. В игре процедурная генерация уровней, врагов, и т.д')
	bot.send_message(message.chat.id,'4. Чтобы начать новую игру введите /newgame')	
	bot.send_message(message.chat.id,'Приятной игры :з')	


@bot.message_handler(commands = ['newgame'])
def start_game(message):
	global locations
	global hero
	locations = [Location.Location(i,1,1,random.randint(5,7),random.randint(5,7)) for i in range(4)]

	Location.SetBridges(locations)

	for i in range(len(locations)):
		locations[i].CreateField()


	hero = Hero.Hero()
	SpawHero(locations)

	bot.send_message(message.chat.id,'Можете двигаться!', reply_markup=Button())


@bot.message_handler(content_types = ['text'])
def function_name(message):
	try:
		global hero

		if message.text == 'осмотреться':
			bot.send_message(message.chat.id, hero.WhatISee())

			return
		else:
			bot.send_message(message.chat.id, hero.Move(message.text))			
			#bot.reply_to(message, str(hero.currentLocation.positionHero))

	except Exception as ex:
		pass


bot.polling()
