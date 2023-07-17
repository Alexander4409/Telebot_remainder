# Telebot_remainder
This telegram bot allows you to send reminders to employees and also add an entry to the Google spreadsheet about whether the employee ignored the message or not
In this solution, the manager sends the /setreminder command to the bot's Telegram, and the bot processes this command, adds an entry to the Google Sheets table, and sends a notification to the employee.

The workflow looks like this:

1. The manager sends the /setreminder command via the bot's Telegram with the required parameters, such as tel_id, test, date, time, and time_for_response.

2. The bot receives this command and processes it in the set_reminder() function. It fetches the parameter values, creates a new reminder entry, and adds it to the Google Sheets using the add_row_to_sheet() function from the spreadsheet.py module.

3. After adding an entry to the table, the bot sends a notification to the employee using the send_message_with_buttons() function from the messaging.py module. The notification contains "Done" and "Not Done" buttons so that the employee can select the appropriate option.

4. When an employee clicks on one of the buttons, the bot handles this event in the button() function. It updates a record in a Google Sheets table using the update_sheet_cell() function from the spreadsheet.py module, indicating which button the employee clicked.

In this way, the bot acts as an intermediary between the manager and the employee, intercepting the command from the manager, adding entries to the Google Sheets and sending notifications to the employee.
