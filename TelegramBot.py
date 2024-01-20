import telebot
import subprocess

# bot = telebot.TeleBot('6738924321:AAEMBZ8ajv3aj6r2whweA4o7vk5bN-qEt5k') бот Никиты
bot = telebot.TeleBot('5217568813:AAERGQ5GDeiyEip0XRiOgtQHCP2JPsvRkAs')

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Привет! Я бот для игры в крестики-нолики. Используй /help для получения инструкций.")

@bot.message_handler(commands=['jumanji'])
def handle_jumanji(message):
    bot.send_message(message.chat.id, "Игра началась! Введите размер доски, символ 1 пользователя и символ 2 пользователя через пробел (например, '3 X O').")

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text.startswith("/jumanji"):
        # command = message.text[9:]
        # result = execute_csharp_application(command)
        # bot.send_message(message.from_user.id, result)
        bot.send_message(message.from_user.id, "ДЖУМАНДЖИ")
    elif message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "И чтобы начать играть, вы слово /jumanji должны прокричать!")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


# def execute_csharp_application(command):
#   process = subprocess.Popen(['C:/Users/apevk/OneDrive/Рабочий стол/TicTacToe/TicTacToe/bin/Debug/net7.0/Tic Tac Toe.exe'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
#   process.stdin.write(command + '\n')
#   process.stdin.flush()
#   result = process.stdout.read()
#   process.stdin.close()
#   process.wait()
#   return result.strip()



def main():
  bot.polling(none_stop=True, interval=0)


if __name__ == "__main__":
  main()
