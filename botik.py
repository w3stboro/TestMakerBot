import telebot
import time
from random import shuffle
bot = telebot.TeleBot('6038371464:AAFe3Buf4G-WXV4GrVclEXt7rdl8FU98ZFs')
baza = {}
test = {}
vop = {}
vopros = {}
current_question_numbers = {}
current_question_order = {}
m = {}
o = {}
k = {}
@bot.message_handler(content_types=['text'])

def start(message):
    if message.chat.id not in baza:
        baza[message.chat.id] = {}
    bot.send_message(message.chat.id, """/nov - создать новый тест
/izm - изменить существующий тест
/sps - вывести список тестов
/otk - пройти существующий тест""")
    bot.register_next_step_handler(message, glav)

def glav(message):
    if message.text == "/nov":
        bot.send_message(message.chat.id, "Введите название теста")
        bot.register_next_step_handler(message, nov)
    elif message.text == "/izm":
        bot.send_message(message.chat.id, "Введите название теста")
        bot.register_next_step_handler(message, izm)
    elif message.text == "/otk":
        bot.send_message(message.chat.id, "Введите название теста")
        bot.register_next_step_handler(message, otk)
    elif message.text == "/sps":
        if len(list(baza[message.chat.id])) > 0:
            bot.send_message(message.chat.id, '\n'.join(list(baza[message.chat.id])))
        else:
            bot.send_message(message.chat.id, "Список пока что пуст :(")
        time.sleep(2)
        bot.send_message(message.chat.id, """/nov - создать новый тест
/izm - изменить существующий тест
/sps - вывести список тестов
/otk - пройти существующий тест""")
        bot.register_next_step_handler(message, glav)
    else:
        bot.register_next_step_handler(message, start)

def nov(message):
    test[message.chat.id] = message.text
    if test[message.chat.id] in baza[message.chat.id]:
        bot.send_message(message.chat.id, "Тест с таким названием уже существует, хотите его изменить?")
        time.sleep(1)
        bot.send_message(message.chat.id, """/izm - изменить,
/vern - вернуться к выбору действия""")
        bot.register_next_step_handler(message, nov5)
    else:
        baza[message.chat.id][test[message.chat.id]] = {}
        bot.send_message(message.chat.id, """/vop - добавить новый вопрос
/zak - закончить создание теста""")
    bot.register_next_step_handler(message, nov2)

def nov2(message):
    if message.text == "/vop":
        bot.send_message(message.chat.id, "Введите вопрос")
        bot.register_next_step_handler(message, nov3)
    elif message.text == "/Del":
        bot.send_message(message.chat.id, "Введите вопрос")
        bot.register_next_step_handler(message, Del)
    elif message.text == "/zak":
        bot.send_message(message.chat.id, "Тест создан,теперь вы можете пройти его или изменить")
        bot.send_message(message.chat.id, """/nov - создать новый тест
/izm - изменить существующий тест
/sps - вывести список тестов
/otk - пройти существующий тест""")
        bot.register_next_step_handler(message, glav)
    elif message.text == "/sps":
        if len(list(baza[message.chat.id])) > 0:
            bot.send_message(message.chat.id, '\n'.join(list(baza[message.chat.id][test[message.chat.id]])))
        else:
            bot.send_message(message.chat.id, "Список пока что пуст :(")
        time.sleep(2)
        bot.send_message(message.chat.id, """/vop - добавить новый вопрос
/Del - удалить вопрос
/sps - вывести список вопросов
/zak - закончить создание теста""")
        bot.register_next_step_handler(message, nov2)
    else:
        bot.send_message(message.chat.id, """/vop - добавить новый вопрос
/Del - удалить вопрос
/sps - вывести список вопросов
/zak - закончить создание теста""")
        bot.register_next_step_handler(message, nov2)

def nov3(message):
    vop[message.chat.id] = message.text
    if vop[message.chat.id] not in baza[message.chat.id][test[message.chat.id]]:
        bot.send_message(message.chat.id, "Введите ответ")
        bot.register_next_step_handler(message, nov4)
    else:
        bot.send_message(message.chat.id, "Такой вопрос уже существует")
        time.sleep(1)
        bot.send_message(message.chat.id, """/izm - изменить ответ на этот вопрос
/vern - вернуться к созданию теста""")
        bot.register_next_step_handler(message, nov6)

def nov4(message):
    baza[message.chat.id][test[message.chat.id]][vop[message.chat.id]] = message.text
    bot.send_message(message.chat.id, "Вопрос создан")
    time.sleep(1)
    bot.send_message(message.chat.id, """/vop - добавить новый вопрос
/Del - удалить вопрос
/sps - вывести список вопросов
/zak - закончить создание теста""")
    bot.register_next_step_handler(message, nov2)

def Del(message):
    vop[message.chat.id] = message.text
    if test[message.chat.id] in baza[message.chat.id]:
        del(baza[message.chat.id][test[message.chat.id]][vop[message.chat.id]])
        bot.send_message(message.chat.id, "Вопрос удалён")
        time.sleep(1)
        bot.send_message(message.chat.id, """/vop - добавить новый вопрос
/Del - удалить вопрос
/sps - вывести список вопросов
/zak - закончить создание теста""")
        bot.register_next_step_handler(message, nov2)
    else:
        bot.send_message(message.chat.id, "Такого вопроса нет")
        test[message.chat.id] = message.text
        bot.send_message(message.chat.id, """/vop - добавить новый вопрос
/Del - удалить вопрос
/sps - вывести список вопросов
/zak - закончить создание теста""")
        bot.register_next_step_handler(message, nov2)

def nov5(message):
    if message.text == "/izm":
        bot.send_message(message.chat.id, """/vop - добавить новый вопрос
/Del - удалить вопрос
/sps - вывести список вопросов
/zak - закончить создание теста""")
        bot.register_next_step_handler(message, nov2)
    elif message.text == "/vern":
        bot.send_message(message.chat.id, """/nov - создать новый тест
/izm - изменить существующий тест
/sps - вывести список тестов
/otk - пройти существующий тест""")
        bot.register_next_step_handler(message, glav)
    else:
        bot.send_message(message.chat.id, """/nov - создать новый тест
/izm - изменить существующий тест
/sps - вывести список тестов
/otk - пройти существующий тест""")
        bot.register_next_step_handler(message, glav)

def nov6(message):
    if message.text == "/izm":
        bot.send_message(message.chat.id, "Введите ответ")
        bot.register_next_step_handler(message, nov4)
    else:
        bot.send_message(message.chat.id, """/vop - добавить новый вопрос
/Del - удалить вопрос
/sps - вывести список вопросов
/zak - закончить создание теста""")
        bot.register_next_step_handler(message, nov2)


def izm(message):
    test[message.chat.id] = message.text
    if test[message.chat.id] in baza[message.chat.id]:
        bot.send_message(message.chat.id, """/vop - добавить новый вопрос
/Del - удалить вопрос
/sps - вывести список вопросов
/zak - закончить создание теста""")
        bot.register_next_step_handler(message, nov2)
    else:
        bot.send_message(message.chat.id, "Теста с таким названием не существует")
        bot.send_message(message.chat.id, """/nov - создать новый тест
/izm - изменить существующий тест
/sps - вывести список тестов
/otk - пройти существующий тест""")
        bot.register_next_step_handler(message, glav)

def vopr2(message):
    current_question_numbers[message.chat.id] = current_question_order[message.chat.id][m[message.chat.id]]
    if baza[message.chat.id][test[message.chat.id]][vopros[message.chat.id]] == message.text:
        bot.send_message(message.chat.id, "Правильно, молодец!")
        o[message.chat.id] += 1
    else:
        bot.send_message(message.chat.id, "Правильный ответ - "+baza[message.chat.id][test[message.chat.id]][vopros[message.chat.id]])
    time.sleep(2)
    m[message.chat.id] += 1
    current_question_numbers[message.chat.id] = current_question_order[message.chat.id][m[message.chat.id]]
    vopros[message.chat.id] = list(baza[message.chat.id][test[message.chat.id]])[current_question_numbers[message.chat.id]]
    bot.send_message(message.chat.id, vopros[message.chat.id])
    if m[message.chat.id] < len(current_question_order[message.chat.id])-1:
        bot.register_next_step_handler(message, vopr2)
    else:
        bot.register_next_step_handler(message, vopr3)

def vopr3(message):
    if baza[message.chat.id][test[message.chat.id]][vopros[message.chat.id]] == message.text:
        bot.send_message(message.chat.id, "Правильно, молодец!")
        o[message.chat.id] += 1
    else:
        bot.send_message(message.chat.id, "Правильный ответ - "+baza[message.chat.id][message.text][vopros[message.chat.id]])
    time.sleep(2)
    bot.send_message(message.chat.id, "твой результат - " + str(o[message.chat.id] / len(current_question_order[message.chat.id]) * 100) + "%" + "(" + str(o[message.chat.id]) + " из " + str(len(current_question_order[message.chat.id])) + ")")
    time.sleep(4)
    bot.send_message(message.chat.id, """/perepr - пройти тест ещё раз
/nov - создать новый тест
/izm - изменить существующий тест
/sps - вывести список тестов
/otk - пройти существующий тест""")
    bot.register_next_step_handler(message, otk2)

def otk(message):
    test[message.chat.id] = message.text
    if test[message.chat.id] in baza[message.chat.id]:
        o[message.chat.id] = 0
        current_question_order[message.chat.id] = []
        c = 0
        for cc in baza[message.chat.id][message.text]:
            current_question_order[message.chat.id].append(c)
            c += 1
        shuffle(current_question_order[message.chat.id])
        m[message.chat.id] = 0
        current_question_numbers[message.chat.id] = current_question_order[message.chat.id][m[message.chat.id]]
        vopros[message.chat.id] = list(baza[message.chat.id][test[message.chat.id]])[current_question_numbers[message.chat.id]]
        bot.send_message(message.chat.id, vopros[message.chat.id])
        bot.register_next_step_handler(message, vopr2)
    else:
        bot.send_message(message.chat.id, "Теста с таким названием не существует")
        bot.send_message(message.chat.id, """/nov - создать новый тест
/izm - изменить существующий тест
/sps - вывести список тестов
/otk - пройти существующий тест""")
        bot.register_next_step_handler(message, glav)


def otk2(message):
    if message.text == "/perepr":
        o[message.chat.id] = 0
        current_question_order[message.chat.id] = []
        c = 0
        for cc in baza[message.chat.id][message.text]:
            current_question_order[message.chat.id].append(c)
            c += 1
        shuffle(current_question_order[message.chat.id])
        m[message.chat.id] = 0
        current_question_numbers[message.chat.id] = current_question_order[message.chat.id][m[message.chat.id]]
        vopros[message.chat.id] = list(baza[message.chat.id][test[message.chat.id]])[current_question_numbers[message.chat.id]]
        bot.send_message(message.chat.id, vopros[message.chat.id])
        bot.register_next_step_handler(message, vopr2)
    elif message.text == "/nov":
        bot.send_message(message.chat.id, "Введите название теста")
        bot.register_next_step_handler(message, nov)
    elif message.text == "/izm":
        bot.send_message(message.chat.id, "Введите название теста")
        bot.register_next_step_handler(message, izm)
    elif message.text == "/otk":
        bot.send_message(message.chat.id, "Введите название теста")
        bot.register_next_step_handler(message, otk)
    elif message.text == "/sps":
        if len(list(baza[message.chat.id])) > 0:
            bot.send_message(message.chat.id, '\n'.join(list(baza[message.chat.id])))
        else:
            bot.send_message(message.chat.id, "Список пока что пуст :(")
        time.sleep(2)
        bot.send_message(message.chat.id, """/nov - создать новый тест
/izm - изменить существующий тест
/sps - вывести список тестов
/otk - пройти существующий тест""")
        bot.register_next_step_handler(message, glav)
    else:
        bot.register_next_step_handler(message, start)

bot.polling(none_stop=True)