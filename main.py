
import telebot
import constants
import random
import time

shablon = '''Имя: %s
user_name: %s
Город: %s
Район: %s
id_user_Telegram: %s
Номер перевода: %s
Номер заказа: %s
Товар: %s
Кол-во: %s'''

the_end = '''Вы Бронируете 🌫 %s
У вас есть 60 минут что бы оплатить закакз или он будет отменён.
Ваш номер заказа %s
➖➖➖➖➖➖
📞 Тех. Поддержка: @kiffirua
➖➖➖➖➖➖
Оплата Easypay ➡️: 56876594
После оплаты ID квитанции написать сюда. После оплаты клад будет выдан сразу!
➖➖➖➖➖➖
Сим-карта Киевстар ➡️ +380979810815
Для подтверждения оплаты нужно прислать id квитанции После оплаты клад будет выдан сразу!
➖➖➖➖➖➖
Где находиться ID - http://prntscr.com/kspcml'''

region_text = '''Трип-репорты, описание и фото товара, правила работы и на Форуме:
🌟 Оператор - @kiffirua
🌃 Чат - @smokekiff
Форум - https://goo.gl/HpRiTL
➖➖➖➖➖➖➖➖➖➖
Выберите Район:
➖➖➖➖➖➖➖➖➖'''

tovar_text = '''Внимание! Все клады исключительно свежие и только на магните.
Помощь:
Оператор - @kiffirua
Чат - @smokekiff
Форум - https://goo.gl/HpRiTL
➖➖➖➖➖➖➖➖➖➖
%s, выберите товар:'''

mix = '''🎊Микс:

2 г - 250 грн
3 г - 380 грн
5 г - 500 грн'''

met = '''📏Метамфетамин Рецемат Идеальное Качество:

0,3 г = 400 грн
0.5 г. = 700 грн
1 г. = 1200 грн'''


shish = '''⚜️Шишки (G13) (G13)

1г - 230
2 г = 400
5 г = 1100'''

ext = '''ЭКСТАЗИ (M&M 260 mg):

1 шт. = 380 грн
2 шт. = 650 грн'''

amf = '''💭Амфетамин Фосфат САМЫЙ ЧИСТЫЙ НА RC

0.5 г = 220 грн
1 г = 360 грн'''

alfa = '''Alfa Белая, Синяя Крис

0.25 - 230 грн
0,5 - 350 грн
1 г - 550 грн'''


bot = telebot.TeleBot(constants.token)

@bot.message_handler(commands=["start"])  # Действия вначале
def start(message):
    if message.text == "/start":
        user_markup = telebot.types.ReplyKeyboardMarkup(True) #создаем кнопки
        user_markup.row("Днепр", "Киев")
        user_markup.row("Харьков", "Одесса")
        user_markup.row("Николаев", "Запорожье", "Винница") # Чтобы добавить кнопку напишите user_markup.row("Ваша кнопка")
        sent = bot.send_message(message.chat.id,'''Привет! Ты попал к самому легендарному продавцу в Rc индустрии @kiffirua 🌫 для того что бы сделать заказ выберите город 🌃
✨✨✨
Покупая у нас, Вы получаете:
✅ Первый СЕРВИС.
Это тот самый сервис, который был первопроходцем в этой сфере, чей карточный домик не сдует ветер перемен. На который ровняются, копируют и консультируются другие магазины.
✅ Опытный СЕРВИС.
Мы на рынке более 4 лет и точно знаем как делать правильно.
✅ Выгодный СЕРВИС.
Цена всегда соответствует качеству товара и уровню работы сервиса, с трип репортами и фото товара вы можете ознакомиться на форуме
✅ Популярный СЕРВИС.
Наш сервис уже выбрали те, кто ценит своё время и безопасность, как RAP-исполнители Украины, так и депутаты, о которых Вы, несомненно, слышали из новостей и соцсетей.
✅ Качественный СЕРВИС.
В прайс добавляются только товары из ТОП лабораторий Голландии, Англии, Нидерланд, Китая.
✅ Моментальный СЕРВИС.
Фото с описанием закладки Вы получаете моментально после оплаты.

Вы экономите время и 💰 :
✅ Благодаря многолетнему опыту безупречной работы нашего магазина вероятность успешно найти свой заказ максимально приближен к100%.
✅ У других магазинов вы в пустую тратите своё время, у нас вы получите моментальный клад после оплаты!

Вы в безопасности:
✅ Все сделки проводятся только по правилам анонимности. С использованием шифрования данных на сервере бота.
✅ Данные о текущих сделках зашифрованы и удаляются в течении 3 часов.
✅ Бот выдаёт клады моментально после ID квитанции
⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆
Если бот не отвечает наберите комманду
/start
⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆
✅Ежедневная техподдержка и опт:
✅В случае удаления бота писать оператору.
🌟 Оператор - @kiffirua
❤️ Чат - @smokekiff
Актуальные контакты Смотреть на форуме - https://goo.gl/HpRiTL
⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆
Выбери свой Город:''', reply_markup=user_markup)
        bot.register_next_step_handler(sent, region)

def region(message):
    if message.text == "Днепр":
        constants.town = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("Левый-3 (Ашан)", "Центр")  # Чтобы добавить кнопку напишите user_markup.row("Ваша кнопка")
        user_markup.row("Правда", "Кирова")
        user_markup.row("Назад")
        sent = bot.send_message(message.chat.id, region_text, reply_markup=user_markup)
        bot.register_next_step_handler(sent, tovar_Dnepr)
    elif message.text == "Киев":
        constants.town = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("Кпи", "Троещина")  # Чтобы добавить кнопку напишите user_markup.row("Ваша кнопка")
        user_markup.row("Дарница", "Дружба народов")
        user_markup.row("Назад")
        sent = bot.send_message(message.chat.id, region_text, reply_markup=user_markup)
        bot.register_next_step_handler(sent, tovar_Kiev)
    elif message.text == "Харьков":
        constants.town = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("Хтз", "Хг")  # Чтобы добавить кнопку напишите user_markup.row("Ваша кнопка")
        user_markup.row("Салтовка", "Алексеевка")
        user_markup.row("Назад")
        sent = bot.send_message(message.chat.id, region_text, reply_markup=user_markup)
        bot.register_next_step_handler(sent, tovar_X)
    elif message.text == "Одесса":
        constants.town = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("Таирово", "Фонтан")  # Чтобы добавить кнопку напишите user_markup.row("Ваша кнопка")
        user_markup.row("Центр")
        user_markup.row("Назад")
        sent = bot.send_message(message.chat.id, region_text, reply_markup=user_markup)
        bot.register_next_step_handler(sent, tovar_Odessa)
    elif message.text == "Николаев":
        constants.town = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("Заводской")  # Чтобы добавить кнопку напишите user_markup.row("Ваша кнопка")
        user_markup.row("Ингульский")
        user_markup.row("Назад")
        sent = bot.send_message(message.chat.id, region_text, reply_markup=user_markup)
        bot.register_next_step_handler(sent, tovar_N)
    elif message.text == "Запорожье":
        constants.town = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("Александровский р.")  # Чтобы добавить кнопку напишите user_markup.row("Ваша кнопка")
        user_markup.row("Шевченкосвий", "Днепровский")
        user_markup.row("Назад")
        sent = bot.send_message(message.chat.id, region_text, reply_markup=user_markup)
        bot.register_next_step_handler(sent, tovar_Z)
    elif message.text == "Винница":
        constants.town = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("Вишенка")  # Чтобы добавить кнопку напишите user_markup.row("Ваша кнопка")
        user_markup.row("Центр")
        user_markup.row("Назад")
        sent = bot.send_message(message.chat.id, region_text, reply_markup=user_markup)
        bot.register_next_step_handler(sent, tovar_Vin)
    elif message.text == "Назад":
        message.text = "/start"
        start(message)
    else:
        sent = bot.send_message(message.chat.id, "Данный город не обслуживается. Проверьте, пожалуйста, правильность названия. Или выберете из списка")
        message.text = "/start"
        bot.register_next_step_handler(sent, start)




def tovar_Dnepr(message):
    if message.text == "Правда": #🎊Микс, ⚜️Шишки (G13), 💤Alfa Белая Синяя, амф
        constants.region = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("🎊Микс", "⚜️Шишки (G13)")
        user_markup.row("💤Alfa Белая Синяя", "💭Амфетамин Фосфат")
        user_markup.row("Назад")
        sent = bot.send_message(message.chat.id, tovar_text %(message.from_user.first_name), reply_markup=user_markup)
        bot.register_next_step_handler(sent, end)

    elif message.text == "Левый-3 (Ашан)":
        constants.region = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("⚜️Шишки (G13)")
        user_markup.row("💤Alfa Белая Синяя", "🎊Микс")
        user_markup.row("Назад")
        sent = bot.send_message(message.chat.id, tovar_text %(message.from_user.first_name), reply_markup=user_markup)
        bot.register_next_step_handler(sent, end)

    elif message.text == "Кирова":
        constants.region = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("🎊Микс", "⚜️Шишки (G13)")
        user_markup.row("💤Alfa Белая Синяя", "💭Амфетамин Фосфат")
        user_markup.row("Назад")
        sent = bot.send_message(message.chat.id, tovar_text %(message.from_user.first_name), reply_markup=user_markup)
        bot.register_next_step_handler(sent, end)

    elif message.text == "Центр":
        constants.region = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("🍀Гаш марокканский")
        user_markup.row("📏Метамфетамин", "♥️ЭКСТАЗИ (m&m260mg)")
        user_markup.row("💤Alfa Белая Синяя", "⚜️Шишки (G13)")
        user_markup.row("Назад")
        sent = bot.send_message(message.chat.id, tovar_text %(message.from_user.first_name), reply_markup=user_markup)
        bot.register_next_step_handler(sent, end)
    elif message.text == "Назад":
        message.text = "/start"
        start(message)

def tovar_Vin(message):
    if message.text == "Вишенка":
        constants.region = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("🍀Гаш марокканский", "🎊Микс")
        user_markup.row("💭Амфетамин Фосфат Фосфат")
        user_markup.row("📏Метамфетамин", "♥️ЭКСТАЗИ (m&m260mg)")
        user_markup.row("💤Alfa Белая Синяя", "⚜️Шишки (G13)")

        user_markup.row("Назад")
        sent = bot.send_message(message.chat.id, tovar_text %(message.from_user.first_name), reply_markup=user_markup)
        bot.register_next_step_handler(sent, end)
    elif message.text == "Центр":
        constants.region = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("🍀Гаш марокканский", "🎊Микс")
        user_markup.row("💭Амфетамин Фосфат Фосфат")
        user_markup.row("📏Метамфетамин", "♥️ЭКСТАЗИ (m&m260mg)")
        user_markup.row("💤Alfa Белая Синяя", "⚜️Шишки (G13)")

        user_markup.row("Назад")
        sent = bot.send_message(message.chat.id, tovar_text %(message.from_user.first_name), reply_markup=user_markup)
        bot.register_next_step_handler(sent, end)
    elif message.text == "Назад":
        message.text = "/start"
        start(message)


def tovar_Kiev(message):
    if message.text == "Кпи":
        constants.region = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("⚜️Шишки (G13)", "📏Метамфетамин")
        user_markup.row("💤Alfa Белая Синяя", "💭Амфетамин Фосфат")
        user_markup.row("♥️ЭКСТАЗИ (m&m260mg)")
        user_markup.row("Назад")
        sent = bot.send_message(message.chat.id, tovar_text %(message.from_user.first_name), reply_markup=user_markup)
        bot.register_next_step_handler(sent, end)
    elif message.text == "Троещина":
        constants.region = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("⚜️Шишки (G13)")
        user_markup.row("💤Alfa Белая Синяя", "🎊Микс")
        user_markup.row("Назад")
        sent = bot.send_message(message.chat.id, tovar_text %(message.from_user.first_name), reply_markup=user_markup)
        bot.register_next_step_handler(sent, end)
    elif message.text == "Дарница":
        constants.region = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("⚜️Шишки (G13)", "📏Метамфетамин")
        user_markup.row("🎊Микс", "💭Амфетамин Фосфат")
        user_markup.row("♥️ЭКСТАЗИ (m&m260mg)")
        user_markup.row("Назад")
        sent = bot.send_message(message.chat.id, tovar_text %(message.from_user.first_name), reply_markup=user_markup)
        bot.register_next_step_handler(sent, end)
    elif message.text == "Дружба народов":
        constants.region = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("♥️ЭКСТАЗИ (m&m260mg)")
        user_markup.row("💤Alfa Белая Синяя", "🎊Микс")
        user_markup.row("Назад")
        sent = bot.send_message(message.chat.id, tovar_text %(message.from_user.first_name), reply_markup=user_markup)
        bot.register_next_step_handler(sent, end)
    elif message.text == "Назад":
        message.text = "/start"
        start(message)


def tovar_X(message):
    if message.text == "Хтз":
        constants.region = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("⚜️Шишки (G13)", "📏Метамфетамин")
        user_markup.row("💤Alfa Белая Синяя", "💭Амфетамин Фосфат")
        user_markup.row("Назад")
        sent = bot.send_message(message.chat.id, tovar_text %(message.from_user.first_name), reply_markup=user_markup)
        bot.register_next_step_handler(sent, end)
    elif message.text == "Хг":
        constants.region = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("⚜️Шишки (G13)", "🎊Микс")
        user_markup.row("💤Alfa Белая Синяя", "💭Амфетамин Фосфат")
        user_markup.row("♥️ЭКСТАЗИ (m&m260mg)")
        user_markup.row("Назад")
        sent = bot.send_message(message.chat.id, tovar_text %(message.from_user.first_name), reply_markup=user_markup)
        bot.register_next_step_handler(sent, end)
    elif message.text == "Салтовка":
        constants.region = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("⚜️Шишки (G13)", "🎊Микс")
        user_markup.row("💤Alfa Белая Синяя", "💭Амфетамин Фосфат")
        user_markup.row("Назад")
        sent = bot.send_message(message.chat.id, tovar_text %(message.from_user.first_name), reply_markup=user_markup)
        bot.register_next_step_handler(sent, end)
    elif message.text == "Алексеевка":
        constants.region = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("⚜️Шишки (G13)")
        user_markup.row("💤Alfa Белая Синяя")
        user_markup.row("Назад")
        sent = bot.send_message(message.chat.id, tovar_text %(message.from_user.first_name), reply_markup=user_markup)
        bot.register_next_step_handler(sent, end)
    elif message.text == "Назад":
        message.text = "/start"
        start(message)

def tovar_Odessa(message):
    if message.text == "Таирово":
        constants.region = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("⚜️Шишки (G13)", "🎊Микс")
        user_markup.row("💤Alfa Белая Синяя")
        user_markup.row("Назад")
        sent = bot.send_message(message.chat.id, tovar_text %(message.from_user.first_name), reply_markup=user_markup)
        bot.register_next_step_handler(sent, end)
    elif message.text == "Назад":
        message.text = "/start"
        start(message)

    elif message.text == "Фонтан":
        constants.region = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("⚜️Шишки (G13)", "📏Метамфетамин")
        user_markup.row("💭Амфетамин Фосфат", "♥️ЭКСТАЗИ (m&m260mg)")
        user_markup.row("Назад")
        sent = bot.send_message(message.chat.id, tovar_text %(message.from_user.first_name), reply_markup=user_markup)
        bot.register_next_step_handler(sent, end)
    elif message.text == "Назад":
        message.text = "/start"
        start(message)

    elif message.text == "Центр":
        constants.region = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("🍀Гаш марокканский")
        user_markup.row("⚜️Шишки (G13)", "💭Амфетамин Фосфат")
        user_markup.row("💤Alfa Белая Синяя", "♥️ЭКСТАЗИ (m&m260mg)")
        user_markup.row("Назад")
        sent = bot.send_message(message.chat.id, tovar_text %(message.from_user.first_name), reply_markup=user_markup)
        bot.register_next_step_handler(sent, end)
    elif message.text == "Назад":
        message.text = "/start"
        start(message)


def tovar_N(message):
    if message.text == "Заводской":
        constants.region = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("⚜️Шишки (G13)", "🎊Микс")
        user_markup.row("💤Alfa Белая Синяя", "♥️ЭКСТАЗИ (m&m260mg)")
        user_markup.row("Назад")
        sent = bot.send_message(message.chat.id, tovar_text %(message.from_user.first_name), reply_markup=user_markup)
        bot.register_next_step_handler(sent, end)
    elif message.text == "Назад":
        message.text = "/start"
        start(message)

    elif message.text == "Ингульский":
        constants.region = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("⚜️Шишки (G13)", "📏Метамфетамин")
        user_markup.row("💭Амфетамин Фосфат", "💤Alfa Белая Синяя")
        user_markup.row("Назад")
        sent = bot.send_message(message.chat.id, tovar_text %(message.from_user.first_name), reply_markup=user_markup)
        bot.register_next_step_handler(sent, end)
    elif message.text == "Назад":
        message.text = "/start"
        start(message)

def tovar_Z(message):
    if message.text == "Александровский р.":
        constants.region = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("⚜️Шишки (G13)", "💭Амфетамин Фосфат")
        user_markup.row("💤Alfa Белая Синяя", "♥️ЭКСТАЗИ (m&m260mg)")
        user_markup.row("Назад")
        sent = bot.send_message(message.chat.id, tovar_text %(message.from_user.first_name), reply_markup=user_markup)
        bot.register_next_step_handler(sent, end)
    elif message.text == "Назад":
        message.text = "/start"
        start(message)

    elif message.text == "Шевченкосвий":
        constants.region = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("⚜️Шишки (G13)", "🎊Микс")
        user_markup.row("💤Alfa Белая Синяя")
        user_markup.row("Назад")
        sent = bot.send_message(message.chat.id, tovar_text %(message.from_user.first_name), reply_markup=user_markup)
        bot.register_next_step_handler(sent, end)
    elif message.text == "Назад":
        message.text = "/start"
        start(message)

    elif message.text == "Днепровский":
        constants.region = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("⚜️Шишки (G13)", "🎊Микс")
        user_markup.row("💤Alfa Белая Синяя")
        user_markup.row("Назад")
        sent = bot.send_message(message.chat.id, tovar_text %(message.from_user.first_name), reply_markup=user_markup)
        bot.register_next_step_handler(sent, end)
    elif message.text == "Назад":
        message.text = "/start"
        start(message)



def end(message):
    if message.text == "🎊Микс":
        constants.tovar = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("🎉2 г - 250 грн")
        user_markup.row("Назад")
        sent = bot.send_message(message.chat.id, "🎊Микс:",  reply_markup=user_markup)
        bot.register_next_step_handler(sent, pay_Mix)

    elif message.text == "⚜️Шишки (G13)":
        constants.tovar = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("🔱 1г - 230 грн")
        user_markup.row("🔱 2 г = 400 грн")
        user_markup.row(" 🔱 5г - 900 грн")
        user_markup.row("Назад")
        sent = bot.send_message(message.chat.id, "⚜️Шишки (G13) (G13):", reply_markup=user_markup)
        bot.register_next_step_handler(sent, pay_Shi)

    elif message.text == "💤Alfa Белая Синяя":
        constants.tovar = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("🔹0.25 - 230 грн")
        user_markup.row("🔹0,5 - 350 грн")
        user_markup.row("🔹1 г - 550 грн")
        user_markup.row("Назад")
        sent = bot.send_message(message.chat.id, "💤Alfa Белая Синяя:", reply_markup=user_markup)
        bot.register_next_step_handler(sent, pay_Alf)

    elif message.text == "💭Амфетамин Фосфат":
        constants.tovar = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("🗯0.5 г = 220 грн")
        user_markup.row("🗯1 г = 360 грн")
        user_markup.row("Назад")
        sent = bot.send_message(message.chat.id, "💭Амфетамин Фосфат САМЫЙ ЧИСТЫЙ НА RC:", reply_markup=user_markup)
        bot.register_next_step_handler(sent, pay_Amf)
    elif message.text == "Назад":
        message.text = "/start"
        start(message)

    elif message.text == "📏Метамфетамин":
        constants.tovar = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("📏 0,25 г = 400 грн")
        user_markup.row("📏 0.5 г. = 700 грн")
        user_markup.row("📏 1 г. = 1200 грн")
        user_markup.row("Назад")
        sent = bot.send_message(message.chat.id, "📏Метамфетамин Рецемат Идеальное Качество:", reply_markup=user_markup)
        bot.register_next_step_handler(sent, pay_Met)

    elif message.text == "🍀Гаш марокканский":
        constants.tovar = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("🍃1 - 350 грн")
        user_markup.row("🍃2 - 600 грн")
        user_markup.row("🍃3 - 900 грн")
        user_markup.row("Назад")
        sent = bot.send_message(message.chat.id, "🍀Гаш марокканский наличие узнавать в лс:", reply_markup=user_markup)
        bot.register_next_step_handler(sent, pay_Ga)

    elif message.text == "♥️ЭКСТАЗИ (m&m260mg)":
        constants.tovar = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("♦️1 шт. = 380 грн")
        user_markup.row("♦️2 шт. = 650 грн")
        user_markup.row("Назад")
        sent = bot.send_message(message.chat.id, "ЭКСТАЗИ (M&M 260 mg):", reply_markup=user_markup)
        bot.register_next_step_handler(sent, pay_Ex)
    elif message.text == "Назад":
        message.text = "/start"
        start(message)

def pay_Mix(message):
    constants.number = random.randint(1, 100000)
    if message.text == "🎉2 г - 250 грн":
        constants.volume = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("Отмена")
        sent = bot.send_message(message.chat.id, the_end %(message.text, constants.number), reply_markup=user_markup)
        bot.register_next_step_handler(sent, id_pay)
    elif message.text == "Назад":
        message.text = "/start"
        start(message)

def pay_Shi(message):
    constants.number = random.randint(1, 100000)
    if message.text == "🔱 1г - 230 грн":
        constants.volume = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("Отмена")
        sent = bot.send_message(message.chat.id, the_end % (message.text, constants.number), reply_markup=user_markup)
        bot.register_next_step_handler(sent, id_pay)
    elif message.text == "🔱 2г - 400 грн ":
        constants.volume = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("Отмена")
        sent = bot.send_message(message.chat.id, the_end % (message.text, constants.number), reply_markup=user_markup)
        bot.register_next_step_handler(sent, id_pay)
    elif message.text == "🔱 5г - 900 грн":
        constants.volume = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("Отмена")
        sent = bot.send_message(message.chat.id, the_end % (message.text, constants.number), reply_markup=user_markup)
        bot.register_next_step_handler(sent, id_pay)
    elif message.text == "Назад":
        message.text = "/start"
        start(message)

def pay_Alf(message):
    constants.number = random.randint(1, 100000)
    if message.text == "🔹0.25 - 230 грн":
        constants.volume = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("Отмена")
        sent = bot.send_message(message.chat.id, the_end % (message.text, constants.number), reply_markup=user_markup)
        bot.register_next_step_handler(sent, id_pay)
    elif message.text == "🔹0,5 - 350 грн":
        constants.volume = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("Отмена")
        sent = bot.send_message(message.chat.id, the_end % (message.text, constants.number), reply_markup=user_markup)
        bot.register_next_step_handler(sent, id_pay)
    elif message.text == "🔹1 г - 550 грн":
        constants.volume = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("Отмена")
        sent = bot.send_message(message.chat.id, the_end % (message.text, constants.number), reply_markup=user_markup)
        bot.register_next_step_handler(sent, id_pay)
    elif message.text == "Назад":
        message.text = "/start"
        start(message)

def pay_Amf(message):
    constants.number = random.randint(1, 100000)
    if message.text == "🗯0.5 г = 220 грн":
        constants.volume = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("Отмена")
        sent = bot.send_message(message.chat.id, the_end % (message.text, constants.number), reply_markup=user_markup)
        bot.register_next_step_handler(sent, id_pay)
    elif message.text == "🗯1 г = 360 грн":
        constants.volume = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("Отмена")
        sent = bot.send_message(message.chat.id, the_end % (message.text, constants.number), reply_markup=user_markup)
        bot.register_next_step_handler(sent, id_pay)
    elif message.text == "Назад":
        message.text = "/start"
        start(message)

def pay_Met(message):
    constants.number = random.randint(1, 100000)
    if message.text == "📏 0,25 г = 400 грн":
        constants.volume = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("Отмена")
        sent = bot.send_message(message.chat.id, the_end % (message.text, constants.number), reply_markup=user_markup)
        bot.register_next_step_handler(sent, id_pay)
    elif message.text == "📏 0.5 г. = 700 грн":
        constants.volume = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("Отмена")
        sent = bot.send_message(message.chat.id, the_end % (message.text, constants.number), reply_markup=user_markup)
        bot.register_next_step_handler(sent, id_pay)
    elif message.text == "📏 1 г. = 1200 грн":
        constants.volume = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("Отмена")
        sent = bot.send_message(message.chat.id, the_end % (message.text, constants.number), reply_markup=user_markup)
        bot.register_next_step_handler(sent, id_pay)
    elif message.text == "Назад":
        message.text = "/start"
        start(message)

def pay_Ex(message):
    constants.number = random.randint(1, 100000)
    if message.text == "♦️1 шт. = 380 грн":
        constants.volume = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("Отмена")
        sent = bot.send_message(message.chat.id, the_end % (message.text, constants.number), reply_markup=user_markup)
        bot.register_next_step_handler(sent, id_pay)
    elif message.text == "♦️2 шт. = 650 грн":
        constants.volume = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("Отмена")
        sent = bot.send_message(message.chat.id, the_end % (message.text, constants.number), reply_markup=user_markup)
        bot.register_next_step_handler(sent, id_pay)

    elif message.text == "Назад":
        message.text = "/start"
        start(message)

def pay_Ga(message):
    constants.number = random.randint(1,100000)
    if message.text == "🍃1 - 350 грн":
        constants.volume = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("Отмена")
        sent = bot.send_message(message.chat.id, the_end % (message.text, constants.number), reply_markup=user_markup)
        bot.register_next_step_handler(sent, id_pay)
    elif message.text == "🍃2 - 600 грн":
        constants.volume = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("Отмена")
        sent = bot.send_message(message.chat.id, the_end % (message.text, constants.number), reply_markup=user_markup)
        bot.register_next_step_handler(sent, id_pay)
    elif message.text == "🍃3 - 900 грн":
        constants.volume = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("Отмена")
        sent = bot.send_message(message.chat.id, the_end % (message.text, constants.number), reply_markup=user_markup)
        bot.register_next_step_handler(sent, id_pay)
    elif message.text == "Назад":
        message.text = "/start"
        start(message)

def id_pay(message):
    if message.text != "Отмена":
        sent = bot.send_message(message.chat.id, '''💰Easypay ➡️ 62826206
Для подтверждения оплаты нужно прислать 📸 чека или экрана, в текстовом варианте id квитанции или время и сумму. После оплаты клад будет выдан сразу
———————-
💎Сим-карта Киевстар ➡️ +380965207704
Для подтверждения оплаты нужно прислать 📸 чека или экрана, в текстовом варианте id квитанции или время и сумму. После оплаты клад будет выдан сразу!

Помощь - @Kiffirua''')
        bot.send_message(constants.admin_id, shablon %(message.from_user.first_name, message.from_user.username, constants.town, constants.region, message.from_user.id, message.text,constants.number ,constants.tovar, constants.volume))
        bot.send_message(constants.a, shablon %(message.from_user.first_name, message.from_user.username, constants.town, constants.region, message.from_user.id, message.text,constants.number ,constants.tovar, constants.volume))
        message.text = "/start"
        start(message)
        bot.register_next_step_handler(sent, start)
    else:
        sent = bot.send_message(message.chat.id, '''Ваш заказ отменен''')
        message.text = "/start"
        bot.register_next_step_handler(sent, start)
        start(message)

bot.polling(none_stop=True, timeout=30)
