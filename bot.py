import config
import telebot
import time
import os

import wolfram

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types = ["text"])
def repeat_all_messages(message):
    ans = wolfram.wolfram_req(message.text)
    if ans=="":
	    bot.send_message(message.chat.id, "Sorry, I don't understand your equation :(")
    else:
        # bot.send_photo(message.chat.id, ans)
        for a in ans:
            # bot.send_message(message.chat.id, a)
            bot.send_document(message.chat.id, a)

if __name__ == '__main__':
	bot.polling(none_stop=True, timeout=100)