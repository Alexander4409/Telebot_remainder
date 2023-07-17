from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# Функция для отправки сообщения с кнопками
def send_message_with_buttons(context, chat_id, text, buttons):
    keyboard = [[InlineKeyboardButton(label, callback_data=label)] for label in buttons]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=chat_id, text=text, reply_markup=reply_markup)

# Функция для удаления сообщения
def delete_message(context, chat_id, message_id):
    context.bot.delete_message(chat_id=chat_id, message_id=message_id)
