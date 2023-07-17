import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Устанавливаем доступы к Google Sheets API
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(credentials)
sheet = client.open("Название_вашей_таблицы").sheet1

# Функция для добавления записи в таблицу
def add_reminder_to_sheet(tel_id, test, date, time, answer_time):
    row = [tel_id, test, date, time, answer_time]
    sheet.append_row(row)

# Функция для обновления записи в таблице
def update_reminder_status(message_id, button_text):
    cell = sheet.find(str(message_id))
    row = cell.row
    column = cell.col + 1
    sheet.update_cell(row, column, button_text)
