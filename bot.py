from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from messaging import send_message_with_buttons, delete_message
from spreadsheet import add_reminder_to_sheet, update_reminder_status

# Обработчик команды /setreminder
def set_reminder(update, context):
    chat_id = update.message.chat_id
    text = update.message.text.split()

    if len(text) < 6:
        context.bot.send_message(chat_id=chat_id, text="Неверный формат команды. Пример: /setreminder <tel_id> <тест> <дата> <время> <время_на_ответ>")
        return

    tel_id = text[1]
    test = text[2]
    date = text[3]
    time = text[4]
    answer_time = int(text[5])

    # Добавляем напоминание в таблицу
    add_reminder_to_sheet(tel_id, test, date, time, answer_time)

    # Отправляем сообщение с кнопкой выполнено / не сделано
    buttons = ["Выполнено", "Не сделано"]
    send_message_with_buttons(context, chat_id, "Напоминание установлено. Пожалуйста, выберите одну из кнопок:", buttons)

# Обработчик нажатия на кнопку
def button(update, context):
    query = update.callback_query
    chat_id = query.message.chat_id
    message_id = query.message.message_id
    button_text = query.data

    # Обновляем статус напоминания в таблице
    update_reminder_status(message_id, button_text)

    # Отправляем сообщение менеджеру о том, какая кнопка нажата
    context.bot.send_message(chat_id=manager_chat_id, text=f"Сотрудник нажал кнопку: {button_text}")

    # Удаляем сообщение с кнопками
    delete_message(context, chat_id, message_id)

# Устанавливаем токен вашего бота
updater = Updater(token="Ваш_токен", use_context=True)
dispatcher = updater.dispatcher

# Добавляем обработчики команд и нажатий на кнопки
dispatcher.add_handler(CommandHandler("setreminder", set_reminder))
dispatcher.add_handler(CallbackQueryHandler(button))

# Запускаем бота
updater.start_polling()
