import config
import telebot
import dbworker

print("STARTUEM")

bot = telebot.TeleBot(config.TOKEN)


# S_0
@bot.message_handler(commands=["start"])
def cmd_start(message):
    dbworker.create_user(message.chat.id)
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('/да', '/нет', '/start')
    bot.send_message(message.chat.id, "Уважаемый коллега! \n Вам предлагается ознакомиться с рабочим прототипом уникального алгоритма ведения Вашего пациента с ДГПЖ! \n По результату прохождения вопросов этого бота "
                                      "Вы получить персонифицированные рекомендации по тактики ведения пациента с учётом его текущего состояния на приёме здесь и сейчас.")
    bot.send_message(message.chat.id, "1. У вашего пациента IPSS больше 7 баллов?", reply_markup=keyboard)
    dbworker.set_state(message.chat.id, config.States.Q_1.value)


# Q_1
@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.Q_1.value)
def user_entering_surname(message):
    if (message.text == '/да'):
        dbworker.set_state(message.chat.id, config.States.Q_2.value)
        dbworker.set_question(message.chat.id, 1, 'q1')
        # KEYBOARD
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('/да', '/нет', '/start')
        bot.send_message(message.chat.id, "2. Имеет ли он выраженную ночную полиурию?", reply_markup=keyboard)
    elif (message.text == '/нет'):
        dbworker.set_state(message.chat.id, config.States.Q_2.value)
        dbworker.set_question(message.chat.id, 0, 'q1')
        # KEYBOARD
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('/да', '/нет', '/start')
        bot.send_message(message.chat.id, "2. Имеет ли он выраженную ночную полиурию?", reply_markup=keyboard)
    else:
        dbworker.set_state(message.chat.id, config.States.Q_1.value)
        print('ошибка с 1 вопросом')


# Q_2
@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.Q_2.value)
def user_entering_surname(message):
    if (message.text == '/да'):
        dbworker.set_state(message.chat.id, config.States.Q_3.value)
        dbworker.set_question(message.chat.id, 1, 'q2')
        # KEYBOARD
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('/да', '/нет', '/start')
        bot.send_message(message.chat.id, "3. Есть только симптомы накопления?", reply_markup=keyboard)
    elif (message.text == '/нет'):
        dbworker.set_state(message.chat.id, config.States.Q_3.value)
        dbworker.set_question(message.chat.id, 0, 'q2')
        # KEYBOARD
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('/да', '/нет', '/start')
        bot.send_message(message.chat.id, "3. Есть только симптомы накопления?", reply_markup=keyboard)
    else:
        dbworker.set_state(message.chat.id, config.States.Q_2.value)
        print('ошибка с 2 вопросом')


# Q_3
@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.Q_3.value)
def user_entering_surname(message):
    if (message.text == '/да'):
        dbworker.set_state(message.chat.id, config.States.Q_4.value)
        dbworker.set_question(message.chat.id, 1, 'q3')
        # KEYBOARD
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('/да', '/нет', '/start')
        bot.send_message(message.chat.id, "4. Лечение пациента длительное?", reply_markup=keyboard)
    elif (message.text == '/нет'):
        dbworker.set_state(message.chat.id, config.States.Q_4.value)
        dbworker.set_question(message.chat.id, 0, 'q3')
        # KEYBOARD
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('/да', '/нет', '/start')
        bot.send_message(message.chat.id, "4. Лечение пациента длительное?", reply_markup=keyboard)
    else:
        dbworker.set_state(message.chat.id, config.States.Q_3.value)
        print('ошибка с 3 вопросом')


# Q_4
@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.Q_4.value)
def user_entering_surname(message):
    if (message.text == '/да'):
        dbworker.set_state(message.chat.id, config.States.Q_5.value)
        dbworker.set_question(message.chat.id, 1, 'q4')
        # KEYBOARD
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('/да', '/нет', '/start')
        bot.send_message(message.chat.id, "5. Пациент сексуально активен?", reply_markup=keyboard)
    elif (message.text == '/нет'):
        dbworker.set_state(message.chat.id, config.States.Q_5.value)
        dbworker.set_question(message.chat.id, 0, 'q4')
        # KEYBOARD
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('/да', '/нет', '/start')
        bot.send_message(message.chat.id, "5. Пациент сексуально активен?", reply_markup=keyboard)
    else:
        dbworker.set_state(message.chat.id, config.States.Q_4.value)
        print('ошибка с 4 вопросом')


# Q_5
@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.Q_5.value)
def user_entering_surname(message):
    if (message.text == '/да'):
        dbworker.set_state(message.chat.id, config.States.Q_6.value)
        dbworker.set_question(message.chat.id, 1, 'q5')
        # KEYBOARD
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('/да', '/нет', '/start')
        bot.send_message(message.chat.id, "6. Есть ли остаточные симптомы накопления?", reply_markup=keyboard)
    elif (message.text == '/нет'):
        dbworker.set_state(message.chat.id, config.States.Q_6.value)
        dbworker.set_question(message.chat.id, 0, 'q5')
        # KEYBOARD
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('/да', '/нет', '/start')
        bot.send_message(message.chat.id, "6. Есть ли остаточные симптомы накопления?", reply_markup=keyboard)
    else:
        dbworker.set_state(message.chat.id, config.States.Q_5.value)
        print('ошибка с 5 вопросом')


# Q_6
@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.Q_6.value)
def user_entering_surname(message):
    if (message.text == '/да'):
        dbworker.set_state(message.chat.id, config.States.Q_7.value)
        dbworker.set_question(message.chat.id, 1, 'q6')
        # KEYBOARD
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('/после_65', '/до_65', '/start')
        bot.send_message(message.chat.id, "7. Укажите ваш возраст", reply_markup=keyboard)
    elif (message.text == '/нет'):
        dbworker.set_state(message.chat.id, config.States.Q_7.value)
        dbworker.set_question(message.chat.id, 0, 'q6')
        # KEYBOARD
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('/после_65', '/до_65', '/start')
        bot.send_message(message.chat.id, "7. Укажите ваш возраст", reply_markup=keyboard)
    else:
        dbworker.set_state(message.chat.id, config.States.Q_6.value)
        print('ошибка с 6 вопросом')


# Q_7
@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.Q_7.value)
def user_entering_surname(message):
    if (message.text == '/после_65'):
        dbworker.set_state(message.chat.id, config.States.Q_8.value)
        dbworker.set_question(message.chat.id, 1, 'q7')
        # KEYBOARD
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('/больше_80мл', '/40_80мл', '/до_40мл', '/start')
        bot.send_message(message.chat.id, "8. Какой объём простаты пациент имеет?", reply_markup=keyboard)
    elif (message.text == '/до_65'):
        dbworker.set_state(message.chat.id, config.States.Q_8.value)
        dbworker.set_question(message.chat.id, 0, 'q7')
        # KEYBOARD
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('/больше_80мл', '/40_80мл', '/до_40мл', '/start')
        bot.send_message(message.chat.id, "8. Какой объём простаты пациент имеет?", reply_markup=keyboard)
    else:
        dbworker.set_state(message.chat.id, config.States.Q_7.value)
        # KEYBOARD
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('/больше_80мл', '/40_80мл', '/до_40мл', '/start')
        bot.send_message(message.chat.id, "8. Какой объём простаты пациент имеет?", reply_markup=keyboard)
        print('ошибка с 7 вопросом')


# Q_8
@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.Q_8.value)
def user_entering_surname(message):
    if (message.text == '/больше_80мл'):
        dbworker.set_state(message.chat.id, config.States.Q_9.value)
        dbworker.set_question(message.chat.id, 2, 'q8')
        # KEYBOARD
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('/15_более', '/10_15', '/0_10', '/start')
        bot.send_message(message.chat.id, "9. Какой показатель Qmax по данным УФМ?", reply_markup=keyboard)
    elif (message.text == '/40_80мл'):
        dbworker.set_state(message.chat.id, config.States.Q_9.value)
        dbworker.set_question(message.chat.id, 1, 'q8')
        # KEYBOARD
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('/15_более', '/10_15', '/0_10', '/start')
        bot.send_message(message.chat.id, "9. Какой показатель Qmax по данным УФМ?", reply_markup=keyboard)
    elif (message.text == '/до_40мл'):
        dbworker.set_state(message.chat.id, config.States.Q_9.value)
        dbworker.set_question(message.chat.id, 0, 'q8')
        # KEYBOARD
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('/15_более', '/10_15', '/0_10', '/start')
        bot.send_message(message.chat.id, "9. Какой показатель Qmax по данным УФМ?", reply_markup=keyboard)
    else:
        dbworker.set_state(message.chat.id, config.States.Q_8.value)
        # KEYBOARD
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('/15_более', '/10_15', '/0_10', '/start')
        bot.send_message(message.chat.id, "Question 8", reply_markup=keyboard)
        print('ошибка с 8 вопросом')


# Q_9
@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.Q_9.value)
def user_entering_surname(message):
    if (message.text == '/15_более'):
        dbworker.set_state(message.chat.id, config.States.Q_10.value)
        dbworker.set_question(message.chat.id, 2, 'q9')
        # KEYBOARD
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('/2', '/1', '/0', '/start')
        bot.send_message(message.chat.id, "10. Остаточный объем мочи? (выберите диапазон)", reply_markup=keyboard)
        
    elif (message.text == '/10_15'):
        dbworker.set_state(message.chat.id, config.States.Q_10.value)
        dbworker.set_question(message.chat.id, 1, 'q9')
        # KEYBOARD
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('/2', '/1', '/0', '/start')
        bot.send_message(message.chat.id, "10. Остаточный объем мочи? (выберите диапазон)", reply_markup=keyboard)
        
    elif (message.text == '/0_10'):
        dbworker.set_state(message.chat.id, config.States.Q_10.value)
        dbworker.set_question(message.chat.id, 0, 'q9')
        # KEYBOARD
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('/2', '/1', '/0', '/start')
        bot.send_message(message.chat.id, "10. Остаточный объем мочи? (выберите диапазон)", reply_markup=keyboard)
        
    else:
        dbworker.set_state(message.chat.id, config.States.Q_9.value)
        # KEYBOARD
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('/2', '/1', '/0', '/start')
        bot.send_message(message.chat.id, "Question 9", reply_markup=keyboard)
        print('ошибка с 9 вопросом')


# Q_10
@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.Q_10.value)
def user_entering_surname(message):
    if (message.text == '/2'):
        dbworker.set_state(message.chat.id, config.States.S_START.value)
        dbworker.set_question(message.chat.id, 2, 'q10')
        result = dbworker.search(message.chat.id)
        bot.send_message(message.chat.id, result)
        # KEYBOARD
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('/start')
        bot.send_message(message.chat.id, 'Вернуться в начало: /start', result)
        
    elif (message.text == '/1'):
        dbworker.set_state(message.chat.id, config.States.S_START.value)
        dbworker.set_question(message.chat.id, 1, 'q10')
        result = dbworker.search(message.chat.id)
        bot.send_message(message.chat.id, result)
        # KEYBOARD
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('/start')
        bot.send_message(message.chat.id, 'Вернуться в начало: /start', reply_markup=keyboard)
        
    elif (message.text == '/0'):
        dbworker.set_state(message.chat.id, config.States.S_START.value)
        dbworker.set_question(message.chat.id, 0, 'q10')
        result = dbworker.search(message.chat.id)
        bot.send_message(message.chat.id, result)
        # KEYBOARD
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('/start')
        bot.send_message(message.chat.id, 'Вернуться в начало: /start', reply_markup=keyboard)
        
    else:
        dbworker.set_state(message.chat.id, config.States.Q_9.value)
        # KEYBOARD
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('/start')
        bot.send_message(message.chat.id, "Question 9", reply_markup=keyboard)
        print('ошибка с 10 вопросом')


if __name__ == '__main__':
    bot.infinity_polling()

