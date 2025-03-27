import telebot
from telebot import types

from config import token, support_users

bot = telebot.TeleBot(token=token, parse_mode='HTML') 

@bot.message_handler()
def main_handler(message):
    if message.text == '/start':
        bot.reply_to(message, "⚡ <b>Добро пожаловать в поддержку GenChatAI</b>\n\nНапишите ваше сообщение, и ожидайте ответа от администрации")
    elif message.text.startswith("/rep"):
        user_id = message.text.split(' ')[1]
        message_text = message.text.split(' ')[2]
        if message.from_user.id in support_users:
            bot.send_message(user_id, message_text)
            bot.reply_to(message, "🟢 Отправлено")
        else:
            bot.reply_to(message, "🛡️ Вам запрещена эта комманда.")
    else:
        for support in support_users:
            bot.send_message(support, f"<b>🟢 Новое сообщение в поддержку!</b>\n\n<blockquote>{message.text}</blockquote>\n\n#ID{message.from_user.id} | @{message.from_user.username}\nОтветить: <code>/rep {message.from_user.id} СООБЩЕНИЕ</code>")
        bot.reply_to(message, "<b>💎 Обращение отправлено в поддержку.</b>")