import telebot
import random


class StateCreator:
    def __init__(self, start_state):
        self.state = start_state

    def __call__(self, state):
        self.state = state
class SaveName:
    def __init__(self, start_state):
        self.state = start_state

    def __call__(self, state):
        self.state = state

global value
value = StateCreator(False)
global name
name = SaveName("")

bot = telebot.TeleBot("1379135517:AAHkIByX1-3Mwn0Jux4MbknGuEOaYaRNGiU")
@bot.message_handler(commands=['start', 'help'])
def send_echo(message):
    if True:
        bot.reply_to(message, "Как тебя зовут?")
        value(False) 
        name("")





my_list = ["пидар", "лох", "жекан", "аутист", "долбоеб", "хуесос", "овцееб", "ссыкун", "жопа", "чмо"]
@bot.message_handler(content_types=['text'])
def send_echo(message):
    if value.state == False:
        answer = "Иди нахуй, " + message.text
        bot.send_message(message.chat.id, answer)
        value(True)
        if name.state == "":
            name(message.text)
    elif message.text == "нет" or  message.text == "Нет":
        answer = "Пидора Ответ"
        bot.send_message(message.chat.id, answer)
    elif message.text == "сам такой" or message.text == "Сам такой" or  message.text == "не правда" or  message.text == "Не правда":
        answer = "ебать ты тупой"
        bot.send_message(message.chat.id, answer)
    else:  
        number = int(random.randrange(0,10,1))
        if number == 1 or number == 4:
            fuckName = random.randrange(0,10,1)
            answer = name.state + " ты " + my_list[fuckName] + ", перезапусти бота " 
            bot.send_message(message.chat.id, answer)
        elif number == 3 or number == 8:
            answer = "твои умственные способности находятся там же, где и твоя жизнь - на дне"
            bot.send_message(message.chat.id, answer)
        else:
            fuckName = random.randrange(0,10,1)
            answer = name.state + " ты " + my_list[fuckName]
            bot.send_message(message.chat.id, answer)
    

bot.polling( none_stop = True )