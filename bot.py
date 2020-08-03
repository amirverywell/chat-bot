import telebot
import config
import random
from telebot import types
from datetime import datetime as dt
import pyowm



bot = telebot.TeleBot(config.TOKEN)
owm = pyowm.OWM('6489d11e205a2e00108a6eb88c195bc5', language='ru')
#@bot.message_handler(content_types=["text"]) #не нужно
#def repeatMessage(message):#не нужно
    #bot.send_message(message.chat.id, message.text) #не нужно
@bot.message_handler(commands=['start'])
def welcomeMessage(message):
    sticker = open('welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sticker)
    bot.send_message(message.chat.id, 'Вы написали мне /start\nВы можете прочитать инструкцию всех команд бота.\nДля этого Вы можете написать "Команды" или нажать на кнопку "Команды".\nВы можете написать или нажать на кнопку "Пока", когда закончите чат с ботом, и бот Вам ответит,') #+
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('/start')
    item3 = types.KeyboardButton('Пока')
    item2 = types.KeyboardButton('Команды')
    item4 = types.KeyboardButton('Сотрудничество и вопросы')
    item5 = types.KeyboardButton('Время')
    item6 = types.KeyboardButton('Играть')
    item7 = types.KeyboardButton('Погода')
    #item8 = types.KeyboardButton('Пообщаться с ботом')
    markup.add(item1, item2, item4, item5, item6, item7, item3)
    bot.send_message(message.chat.id, "{0.first_name}".format(message.from_user, bot.get_me()),parse_mode='html', reply_markup=markup)
@bot.message_handler(content_types=['text'])#+
def send_text(message):
    if message.chat.type == 'private':
        if message.text == 'Пока': #+
            bot.send_message(message.chat.id, 'Прощайте, дорогой пользователь!')#+
        elif message.text == 'Команды':
            bot.send_message(message.chat.id, '/start - начать чат с ботом\nПока - Закончить чат с ботом\nКоманды - узнаёте все команды бота\nСотрудничество и вопросы - можете написать вопросы о боте или по сотрудничеству.')
            bot.send_message(message.chat.id, 'Время - Вы узнаете время в разных городах, смотря где Вы живёте.\nПогода - Вы узнаете погоду в разных городах, которые Вам нужны.\nИграть - Вы сможете поиграть в мини игры бота.\nМеню - выводит Вас в главное меню бота.')
        elif message.text == 'Сотрудничество и вопросы':
            bot.send_message(message.chat.id, 'Если у Вас возникнут вопросы по боту или Вы захотите сотрудничать, перейдите по ссылке https://vk.com/nikolay_morozov1\nПишите ввсе ваши предложения по боту или вопросы по сотрудничеству.')
        elif message.text == ('Время'):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item7 = types.KeyboardButton('Время в Казани')
            markup.add(item7)
            item8 = types.KeyboardButton('Время в Москве')
            markup.add(item8)
            item9 = types.KeyboardButton('Время в Екатеринбурге')
            markup.add(item9)
            item11 = types.KeyboardButton('Время в Тольятти')
            markup.add(item11)
            item10 = types.KeyboardButton('Меню')
            markup.add(item10)
            bot.send_message(message.chat.id, 'Выберите город:'.format(message.from_user, bot.get_me()),parse_mode='html', reply_markup=markup)
        elif message.text == 'Время в Казани':
            time = dt.now().time()
            bot.send_message(message.chat.id,'Время в городе Казань сейчас: ' +  str((time.hour)%24) + ':' + str(time.minute))
        elif message.text == 'Время в Москве':
            time = dt.now().time()
            bot.send_message(message.chat.id,'Время в городе Москва сейчас: ' + str((time.hour)%24) + ':' + str(time.minute))
        elif message.text == 'Время в Екатеринбурге':
            time = dt.now().time()
            bot.send_message(message.chat.id,'Время в городе Екатеринбург сейчас: ' + str((time.hour + 2)%24) + ':' +  str(time.minute))
        elif message.text == 'Время в Тольятти':
            time = dt.now().time()
            bot.send_message(message.chat.id,'Время в городе Тольятти сейчас: ' + str((time.hour + 1)%24) + ':' +  str(time.minute))

        elif message.text == 'Играть':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item7 = types.KeyboardButton('Рандомайзер')
            markup.add(item7)
            item9 = types.KeyboardButton('Крестики Нолики')
            markup.add(item9)
            item8 = types.KeyboardButton('Меню')
            markup.add(item8)
            bot.send_message(message.chat.id, 'Во что Вы хотите сыграть?'.format(message.from_user, bot.get_me()),parse_mode='html', reply_markup=markup)

        elif message.text == 'Меню':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('/start')
            item3 = types.KeyboardButton('Пока')
            item2 = types.KeyboardButton('Команды')
            item4 = types.KeyboardButton('Сотрудничество и вопросы')
            item5 = types.KeyboardButton('Время')
            item6 = types.KeyboardButton('Играть')
            item7 = types.KeyboardButton('Погода')
            markup.add(item1, item2, item4, item5, item6, item7, item3)
            bot.send_message(message.chat.id, 'Вы перешли в главное меню бота.'.format(message.from_user, bot.get_me()),parse_mode='html', reply_markup=markup)

        elif message.text == 'Рандомайзер':
            bot.send_message(message.chat.id, str(random.randint(0, 100)))
        elif message.text == 'Крестики Нолики':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('1')
            item2 = types.KeyboardButton('2')
            item3 = types.KeyboardButton('3')
            item4 = types.KeyboardButton('4')
            item5 = types.KeyboardButton('5')
            item6 = types.KeyboardButton('6')
            item7 = types.KeyboardButton('7')
            item8 = types.KeyboardButton('8')
            item9 = types.KeyboardButton('9')
            item10 = types.KeyboardButton('Назад')
            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10)
            bot.send_message(message.chat.id, 'Игра <Крестики-Нолики> началась')
            bot.send_message(message.chat.id, 'Выберите число на которое Вы хотите поставить "Х"'.format(message.from_user, bot.get_me()),parse_mode='html', reply_markup=markup)

            board = list(range(1, 10))
            def draw_board(board):
                bot.send_message(message.chat.id, "-" * 13)
                for i in range(3):
                    bot.send_message(message.chat.id, "|" + str(board[0 + i * 3]) + "|" + str(board[1 + i * 3]) + "|" + str(board[2 + i * 3]) + "|")
                    bot.send_message(message.chat.id, "-" * 13)

            def take_input(player_token):
                valid = False
                while not valid:
                    player_answer = input("Куда поставим " + player_token + "? ")
                    try:
                        player_answer = int(player_answer)
                    except:
                        bot.send_message(message.chat.id, "Некорректный ввод. Вы уверены, что ввели число?")
                        continue
                    if player_answer >= 1 and player_answer <= 9:
                        if (str(board[player_answer - 1]) not in "XO"):
                            board[player_answer - 1] = player_token
                            valid = True
                        else:
                            bot.send_message(message.chat.id, "Эта клетка уже занята!")
                    else:
                        bot.send_message(message.chat.id, "Некорректный ввод. Введите число от 1 до 9.")

            def check_win(board):
                win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
                for each in win_coord:
                    if board[each[0]] == board[each[1]] == board[each[2]]:
                        return board[each[0]]
                return False

            def main(board):
                counter = 0
                win = False
                while not win:
                    draw_board(board)
                    if counter % 2 == 0:
                        take_input("X")
                    else:
                        take_input("O")
                    counter += 1
                    if counter > 4:
                        tmp = check_win(board)
                        if tmp:
                            bot.send_message(message.chat.id, tmp + "выиграл!")
                            win = True
                            break
                    if counter == 9:
                        bot.send_message(message.chat.id, "Ничья!")
                        break
                draw_board(board)

            main(board)

        elif message.text == 'Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Рандомайзер')
            markup.add(item1)
            item2 = types.KeyboardButton('Крестики Нолики')
            markup.add(item2)
            item3 = types.KeyboardButton('Меню')
            markup.add(item3)
            bot.send_message(message.chat.id, 'Вы перешли в меню игр.')

        elif message.text == 'Меню':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('/start')
            item3 = types.KeyboardButton('Пока')
            item2 = types.KeyboardButton('Команды')
            item4 = types.KeyboardButton('Сотрудничество и вопросы')
            item5 = types.KeyboardButton('Время')
            item6 = types.KeyboardButton('Играть')
            item7 = types.KeyboardButton('Погода')
            markup.add(item1, item2, item4, item5, item6, item7, item3)
            bot.send_message(message.chat.id, 'Вы перешли в главное меню бота.'.format(message.from_user, bot.get_me()),
                             parse_mode='html', reply_markup=markup)


        elif message.text == 'Погода':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item7 = types.KeyboardButton('Погода в Казани')
            markup.add(item7)
            item8 = types.KeyboardButton('Погода в Москве')
            markup.add(item8)
            item9 = types.KeyboardButton('Погода в Тольятти')
            markup.add(item9)
            item11 = types.KeyboardButton('Погода в Санкт-Петербурге')
            markup.add(item11)
            item12 = types.KeyboardButton('Погода в Набережных Челнах')
            markup.add(item12)
            item13 = types.KeyboardButton('Погода в Альметьевске')
            markup.add(item13)
            item14 = types.KeyboardButton('Погода в Сочи')
            markup.add(item14)
            item15 = types.KeyboardButton('Погода в Екатеринбурге')
            markup.add(item15)
            item10 = types.KeyboardButton('Меню')
            markup.add(item10)
            bot.send_message(message.chat.id, 'Выберите город:'.format(message.from_user, bot.get_me()),parse_mode='html', reply_markup=markup)        #elif message.text == 'Погода':
        elif message.text == 'Меню':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('/start')
            item3 = types.KeyboardButton('Пока')
            item2 = types.KeyboardButton('Команды')
            item4 = types.KeyboardButton('Сотрудничество и вопросы')
            item5 = types.KeyboardButton('Время')
            item6 = types.KeyboardButton('Играть')
            item7 = types.KeyboardButton('Погода')
            #item8 = types.KeyboardButton('Пообщаться с ботом')
            markup.add(item1, item2, item4, item5, item6, item7, item3)
        elif message.text == 'Погода в Казани':
            observation = owm.weather_at_place("Казань")
            w = observation.get_weather()
            temp = w.get_temperature('celsius')['temp']
            answer = f"В городе Казань сейчас {w.get_detailed_status()}, \n"
            answer += f"Температура в районе {round(temp)} градусов\n\n"
            bot.send_message(message.chat.id, answer)
        elif message.text == 'Погода в Москве':
            observation = owm.weather_at_place("Москва")
            w = observation.get_weather()
            temp = w.get_temperature('celsius')['temp']
            answer = f"В городе Моксва сейчас {w.get_detailed_status()}, \n"
            answer += f"Температура в районе {round(temp)} градусов\n\n"
            bot.send_message(message.chat.id, answer)
        elif message.text == 'Погода в Тольятти':
            observation = owm.weather_at_place("Тольятти")
            w = observation.get_weather()
            temp = w.get_temperature('celsius')['temp']
            answer = f"В городе Тольятти сейчас {w.get_detailed_status()}, \n"
            answer += f"Температура в районе {round(temp)} градусов\n\n"
            bot.send_message(message.chat.id, answer)
        elif message.text == 'Погода в Санкт-Петербурге':
            observation = owm.weather_at_place("Санкт-Петербург")
            w = observation.get_weather()
            temp = w.get_temperature('celsius')['temp']
            answer = f"В городе Санкт-Петербург сейчас {w.get_detailed_status()}, \n"
            answer += f"Температура в районе {round(temp)} градусов\n\n"
            bot.send_message(message.chat.id, answer)
        elif message.text == 'Погода в Набережных Челнах':
            observation = owm.weather_at_place("Набережные Челны")
            w = observation.get_weather()
            temp = w.get_temperature('celsius')['temp']
            answer = f"В городе Набережные Челны сейчас {w.get_detailed_status()}, \n"
            answer += f"Температура в районе {round(temp)} градусов\n\n"
            bot.send_message(message.chat.id, answer)
        elif message.text == 'Погода в Альметьевске':
            observation = owm.weather_at_place("Альметьевск")
            w = observation.get_weather()
            temp = w.get_temperature('celsius')['temp']
            answer = f"В городе Альметьевск сейчас {w.get_detailed_status()}, \n"
            answer += f"Температура в районе {round(temp)} градусов\n\n"
            bot.send_message(message.chat.id, answer)
        elif message.text == 'Погода в Сочи':
            observation = owm.weather_at_place("Сочи")
            w = observation.get_weather()
            temp = w.get_temperature('celsius')['temp']
            answer = f"В городе Сочи сейчас {w.get_detailed_status()}, \n"
            answer += f"Температура в районе {round(temp)} градусов\n\n"
            bot.send_message(message.chat.id, answer)
        elif message.text == 'Погода в Екатеринбурге':
            observation = owm.weather_at_place("Екатеринбург")
            w = observation.get_weather()
            temp = w.get_temperature('celsius')['temp']
            answer = f"В городе Екатеринбург сейчас {w.get_detailed_status()}, \n"
            answer += f"Температура в районе {round(temp)} градусов\n\n"
            bot.send_message(message.chat.id, answer)
        else:
            bot.send_message(message.chat.id, "Извините, я Вас не понимаю. Попробуйте ввести другую команду.")


bot.polling(none_stop=True)
