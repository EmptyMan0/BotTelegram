import telebot
from telebot import types

bot = telebot.TeleBot('5366337847:AAHT6Ell4xClauPGeKzP76fNerDdbkclnuo')

user_list = {}


class User:
    def __init__(self, Installation_location):
        self.Installation_location = Installation_location
        self.amount = None
        self.sex = None


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    btn2 = types.KeyboardButton("🍀 Расчитать стоимость")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Я тестовый бот".format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "👋 Поздороваться"):
        bot.send_message(message.chat.id, text="Привеет.. Можешь сделать заказ!)")
    elif (message.text == "🍀 Расчитать стоимость"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton("🏕Для дома/дачи")
        btn2 = types.KeyboardButton("🏠Для квартиры")
        back = types.KeyboardButton("⬅ Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        msg = bot.send_message(message.chat.id, text="Выберите тип видеонаблюдения", reply_markup=markup)
        bot.register_next_step_handler(msg, video_surveillance_system)

    elif (message.text == "⬅ Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        button1 = types.KeyboardButton("👋 Поздороваться")
        button2 = types.KeyboardButton("🍀 Расчитать стоимость")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")


def video_surveillance_system(message):
    if (message.text == "⬅ Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        button1 = types.KeyboardButton("👋 Поздороваться")
        button2 = types.KeyboardButton("🍀 Расчитать стоимость")
        markup.add(button1, button2)
        msg = bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
        bot.register_next_step_handler(msg, func)
    else:
        user_list[0] = message.text
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton("1⃣ 1")
        btn2 = types.KeyboardButton("2⃣ 2")
        btn3 = types.KeyboardButton("3⃣ 3")
        btn4 = types.KeyboardButton("4⃣ 4")
        back = types.KeyboardButton("⬅ Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, btn4, back)
        msg = bot.send_message(message.chat.id, text="Cколько Вам понадобиться камер видеонаблюдения?", reply_markup=markup)
        bot.register_next_step_handler(msg, amount)


def amount(message):
    if (message.text == "⬅ Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        button1 = types.KeyboardButton("👋 Поздороваться")
        button2 = types.KeyboardButton("🍀 Расчитать стоимость")
        markup.add(button1, button2)
        msg = bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
        bot.register_next_step_handler(msg, func)
    else:
        user_list[1] = message.text
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton("5⃣ 5 дней")
        btn2 = types.KeyboardButton("🔟 10 дней")
        btn3 = types.KeyboardButton("2⃣0⃣ 20 дней")
        back = types.KeyboardButton("⬅ Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, back)
        msg = bot.send_message(message.chat.id, text="Сколько хранить запись с камер?", reply_markup=markup)
        bot.register_next_step_handler(msg, storage_days)


def storage_days(message):
    if (message.text == "⬅ Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        button1 = types.KeyboardButton("👋 Поздороваться")
        button2 = types.KeyboardButton("🍀 Расчитать стоимость")
        markup.add(button1, button2)
        msg = bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
        bot.register_next_step_handler(msg, func)
    else:
        user_list[2] = message.text
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton("🏃  Как можно быстрее")
        btn2 = types.KeyboardButton("📅 В ближайшую неделю")
        btn3 = types.KeyboardButton("🔥 Не горит, просто проверяю цены")
        back = types.KeyboardButton("⬅ Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, back)
        msg = bot.send_message(message.chat.id, text="Как срочно Вам нужна система?", reply_markup=markup)
        bot.register_next_step_handler(msg, urgency)


def urgency(message):
    if (message.text == "⬅ Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        button1 = types.KeyboardButton("👋 Поздороваться")
        button2 = types.KeyboardButton("🍀 Расчитать стоимость")
        markup.add(button1, button2)
        msg = bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
        bot.register_next_step_handler(msg, func)
    else:
        user_list[3] = message.text
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton("✔Да")
        btn2 = types.KeyboardButton("❌ Нет, нужно установить")
        back = types.KeyboardButton("⬅ Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        msg = bot.send_message(message.chat.id, text="Eсть на объекте интернет?", reply_markup=markup)
        bot.register_next_step_handler(msg, price_or_quality)


def price_or_quality(message):
    if (message.text == "⬅ Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        button1 = types.KeyboardButton("👋 Поздороваться")
        button2 = types.KeyboardButton("🍀 Расчитать стоимость")
        markup.add(button1, button2)
        msg = bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
        bot.register_next_step_handler(msg, func)
    else:
        user_list[4] = message.text
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton("🧻 Важнее сделать как можно дешевле")
        btn2 = types.KeyboardButton("👌 Нужно сделать хорошо")
        btn3 = types.KeyboardButton("🤑 Качество важнее, чем цена")
        back = types.KeyboardButton("⬅ Вернуться в главное меню")
        markup.add(btn1, btn2,btn3, back)
        msg = bot.send_message(message.chat.id, text="Вам важнее цена или качество?", reply_markup=markup)
        bot.register_next_step_handler(msg, kit_or_installation)


def kit_or_installation(message):
    if (message.text == "⬅ Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        button1 = types.KeyboardButton("👋 Поздороваться")
        button2 = types.KeyboardButton("🍀 Расчитать стоимость")
        markup.add(button1, button2)
        msg = bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
        bot.register_next_step_handler(msg, func)
    else:
        user_list[5] = message.text
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton("😀 нужна установка")
        btn2 = types.KeyboardButton("😞 установлю самостоятельно")
        back = types.KeyboardButton("⬅ Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        msg = bot.send_message(message.chat.id, text="Вам нужен готовый комплект или монтаж под ключ?", reply_markup=markup)
        bot.register_next_step_handler(msg, vivod)


def vivod(message):
    if (message.text == "⬅ Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        button1 = types.KeyboardButton("👋 Поздороваться")
        button2 = types.KeyboardButton("🍀 Расчитать стоимость")
        markup.add(button1, button2)
        msg = bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
        bot.register_next_step_handler(msg, func)
    else:
        user_list[6] = message.text
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        bot.send_message(message.chat.id, '💰 Вывод '
                         + '\n Выберите тип видеонаблюдения -------' + user_list[0]
                         + '\n Cколько Вам понадобиться камер видеонаблюдения? -------' + user_list[1]
                         + '\n Сколько хранить запись с камер? -------' + user_list[2]
                         + '\n Как срочно Вам нужна система? -------' + user_list[3]
                         + '\n Eсть на объекте интернет? -------' + user_list[4]
                         + '\n Вам важнее цена или качество? -------' + user_list[5]
                         + '\n Вам нужен готовый комплект или монтаж под ключ? -------' + user_list[6])
        button1 = types.KeyboardButton("👋 Поздороваться")
        button2 = types.KeyboardButton("🍀 Расчитать стоимость")
        markup.add(button1, button2)
        msg = bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
        bot.register_next_step_handler(msg, func)


bot.polling(none_stop=True)
