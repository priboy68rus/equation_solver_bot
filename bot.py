import config
import telebot
import time
import os

import wolfram

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types = ["text"])
def handle_equation(message):
    if message.text.split()[0] == "plot":
        keyword = "plot"
    else:
        keyword = "solution"
    ans = wolfram.wolfram_req(keyword, message.text)
    if ans=="":
	    bot.send_message(message.chat.id, "Sorry, I don't understand your equation :(")
    else:
        # bot.send_photo(message.chat.id, ans)
        for a in ans:
            # bot.send_message(message.chat.id, a)
            bot.send_document(message.chat.id, a)


if __name__ == '__main__':
	bot.polling(none_stop=True, timeout=100)