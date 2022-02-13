import telebot
from random import randint

TOKEN = "5069299807:AAEuDYmkrBV1za4QsfoQUQn96_Q_XQ9s7cw"
client = telebot.TeleBot(TOKEN)

with open("comp.txt", 'r', encoding="UTF-8") as file:
    comp_list = file.readlines()


@client.message_handler(commands=['start', 'help'])
def start(message):
    msg = 'Этого бота я (Женя) писал только для той, что представлена на фото ниже<3\nЧтобы получить комплимент, напиши:\n    /комплимент или /Комплимент'
    client.send_message(message.chat.id, msg)
    client.send_photo(message.chat.id, open("photo.jpg", "rb"))


@client.message_handler(commands=['Комплимент', 'комплимент'])
def main(message):
    global comp_list

    chose = randint(0, 99)

    chose = comp_list[chose]

    client.send_message(message.chat.id, chose)


client.polling(none_stop=True)
