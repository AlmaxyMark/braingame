import telebot
import random
from telebot import types
import json

token = "6986134803:AAEnbuLX2GdD7ayvRGL8nKGaFLeXstFFfMg"

greetings = ["Приветствую, искатель знаний! Добро пожаловать в мир бесконечного развития и обучения. Давай вместе создадим будущее!",
             "Привет! Мы тут заняты делом - развитием. А ты готов стать лучшей версией себя? Начнем это сейчас!",
             "Здравствуй! Добро пожаловать в бота-мотиватора. Пойдем вместе по пути к успеху и развитию!",
             "Приветствую, искатель мудрости! Стремимся к знаниям и развитию - вот наш девиз. Давай начнем этот увлекательный путь прямо сейчас!"]
option = ["Поехали, выбирай: либо числа и логика, либо слова и загадки. Твой мозг готов к крепким умственным тяжелым штангам?",
"Загадки или математика - выбирай мудро!",
"А сейчас наш бот представит: феерический конкурс математических мастеров или дух захватывающего путешествия между буквами. Сделай свой выбор!",
"Математическая викторина или Угадай слово - в обоих случаях тебе предстоит напрячься. Какой путь выберешь?"]
math = ["Готов проверить свои математические знания? Викторина начинается!",
        "Добро пожаловать в Математическую викторину! Готовы проверить свои знания чисел?",
        "Добро пожаловать в Математическую викторину! Уверен, ты справишься с заданиями. Вперёд, давай начнем!",
        "Добро пожаловать в Математическую викторину! Приготовьтесь к интересным математическим задачкам и возможности проверить свои навыки. Готовы начать? А если готовы, то поехали!"]
a1 = [
    "Выберите букву и посмотрим, есть ли она в слове.",
    "У вас есть 7 попыток, чтобы отгадать слово.",
    "У вас всего 7 попыток. Давайте начнем!",
    "Говорят, что чем меньше букв имеет загаданное слово, тем проще его угадать. Но так ли это? Что ж, давайте проверим"]
a2 = ["Осталось 6 попыток. Не отчаивайтесь! Продолжайте отгадывать буквы.",
      "Ой, вы ошиблись! Данной буквы в слове нет.",
      "У вас осталось 6 попыток. Ваше предположение неверно.",
      "Неправильно! Осталось 6 попыток."]
a3 = ["Вы не на верном пути, но продолжайте отгадывать!",
      "Нет, ошибочка! Данная буква не является частью загаданного слова. Осталось 5 попыток...",
      "К сожалению, вы снова ошиблись.",
      "Эта буква не входит в слово. У вас осталось 5 попыток."]
a4 = ["Осталось 4 попытки.\nУбедитесь, что выбираете буквы внимательно.",
      "Вам осталось 4 попытки. Не отчаивайтесь!",
      "У вас осталось 4 попытки. Вы снова не угадали.",
      "Ещё неверно! Осталось 4 попытки."]
a5 = ["Очередная неправильная буква. Вам осталось всего 3 попытки. Продолжайте искать!",
      "Ой, увы! Эта буква неправильная. У вас осталось 3 попытки. Не сдавайтесь!",
      "Упс! Эта буква не входит в загаданное слово. У вас осталось 3 попытки.",
      "Неправильно. У вас осталось 3 попытки."]
a6 = ["У вас осталось 2 попытки.\nНе дайте себе сдаться! Вперед, отгадывайте!",
      "Ай-яй-яй! Ваша буква не помогла нам приблизиться к отгадке. Осталось всего 2 попытка!",
      "У вас осталось всего 2 попытки, не отчаивайтесь!",
      "Упс, вы ошиблись! Данной буквы в слове нет."]
a7 = ["Ох, вы ошиблись снова. Осталась всего 1 попытка. Неужели вы не можете угадать?",
      "Последняя попытка! При неверном ответе вы проиграете.",
      "Нечасто можно побывать в таком положении. Сосредоточьтесь! У вас всего 1 попытка!",
      "Мда... Осталась всего 1 попытка."]
a0 = ["Привет! Если ты не знаком с Математической викториной и Угадай слово, то я с радостью расскажу тебе об этих играх. Математическая викторина - это игра, в которой тебе будут задавать вопросы по математике, а ты должен будешь выбрать правильный ответ из предложенных вариантов. Угадай слово же - это классическая игра, где тебе нужно отгадать загаданное слово, угадывая по одной букве за раз.",
      "Приветствую! Нажав на кнопку 'Игры', ты можешь выбрать Математическую викторину или Угадай слово. В Математической викторине тебе будут задавать математические вопросы, а в Угадай слово тебе нужно будет отгадать загаданное слово. Кстати, в обеих играх есть встроенная статистика, которая позволит тебе отслеживать свой прогресс. Приятного времяпрепровождения!",
      "Привет! С кнопкой 'Игры' тебе доступны две увлекательные игры: Математическая викторина и Угадай слово. Математическая викторина предлагает тебе ответить на интересные математические вопросы и проверить свои знания. Угадай слово - это классическая игра, где твоя задача отгадать слово, имея ограниченное количество попыток. Обе игры имеют статистику, которая позволит тебе отслеживать свой прогресс. Не бойся нажать на кнопку и попробовать!",
      "Приветствую! Если ты еще не ознакомился с Математической викториной и Угадай слово, то это отличная возможность развлечься и проверить свои способности. Математическая викторина предлагает тебе ответить на математические вопросы, а Угадай слово - угадать слово, имея ограниченное количество попыток. Обе игры сопровождаются статистикой, которая позволит тебе отслеживать свой прогресс.",
      "Привет! Если тебе нужна помощь с играми, я с радостью помогу. Математическая викторина - это игра, где тебе будут задавать математические вопросы, и ты должен выбрать правильный ответ из предложенных вариантов. Угадай слово - это игра, где ты должен отгадывать слово, имея ограниченное количество попыток. Обе игры имеют статистику, так что ты сможешь отслеживать свой прогресс."]
HANGMAN = (
f"""
{random.choice(a2)} 😆
""",
f"""
{random.choice(a3)} 😀
""",
f"""
{random.choice(a4)} 🙂
""",
f"""
{random.choice(a5)} 😐
""",
f"""
{random.choice(a6)} 😕
""",
f"""
{random.choice(a7)} ☹
""",
"""
Вы проиграли. Попытайтесь снова и продолжайте тренироваться, чтобы улучшить свои навыки в игре Угадай слово. 😞
""")

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# with open("vocabulary.json", encoding="utf- 8") as v:
#     dataWords = json.load(v)

primte = list("ёйцукенгшщзхъфывапролджэячсмитьбю")

tems = []
nameMoney = "Сияны"

bot = telebot.TeleBot(token)

def SaveData():
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent = 4, ensure_ascii = False)



@bot.message_handler(commands=["start"])
def start(message):
    userId = str(message.from_user.id)
    if not userId in data:
        data[userId] = {"isState": None,
                        "MathVictorina": {"rightAnswerLast": 0,
                                          "rightAnswerAllTime": 0,
                                          "maxRightAnswer": 0,
                                          "attempts": 3,
                                          "listWrongAnswer": [],
                                          "answer": 0},
                        "GuessTheWord":    {"listRightAnswer": [],
                                          "listWrongAnswer": [],
                                           "countGame": 0,
                                          },
                        "Money": 100
                        }
    else:
        data[userId]["isState"] = None

    boardkeyboard = types.ReplyKeyboardMarkup()
    but1 = types.KeyboardButton("Игры")
    but2 = types.KeyboardButton("Профиль")
    but3 = types.KeyboardButton("Помощь")

    boardkeyboard.add(but1, but2, but3)
    bot.send_message(userId, random.choice(greetings), reply_markup = boardkeyboard)

    SaveData()


@bot.message_handler(content_types=['web_app_data'])
def handle_web_app_data(message):
    print(message)
    # Получаем данные из веб-приложения
    site_data = message.web_app_data.data
    user_id = str(message.from_user.id)
    print(site_data)
    dataWeb = HandlerWeb(site_data)
    if dataWeb["isWin"] != "false":
        data[user_id]["GuessTheWord"]["listRightAnswer"].append(dataWeb["word"])
        # data[user_id]["Money"] += int(dataWeb["isGift"])
    else:
        data[user_id]["GuessTheWord"]["listWrongAnswer"].append(dataWeb["word"])

    if  data[user_id]["GuessTheWord"]["countGame"] != 0:
        oldPercent = round( len(data[user_id]["GuessTheWord"]["listRightAnswer"] ) / data[user_id]["GuessTheWord"]["countGame"], 2) * 100
        data[user_id]["GuessTheWord"]["countGame"] += 1
        newPercent = round( len(data[user_id]["GuessTheWord"]["listRightAnswer"] ) / data[user_id]["GuessTheWord"]["countGame"], 2) * 100
        statisticsPercent = "Предыдущий процент побед " + str(oldPercent) + "%" + "\nТекущий процент побед " + str(newPercent) + "%"
    else:
        data[user_id]["GuessTheWord"]["countGame"] += 1
        #это была ваша первая игра 
        
    bot.send_message(
        message.chat.id,
        f'Слово было {dataWeb["word"]}\n{statisticsPercent}\nМожете убедиться в этом слове \nhttps://yandex.ru/images/search?from=tabbar&text={dataWeb["word"]}+{dataWeb["theme"]}'
    )


@bot.message_handler(content_types=['text'])
def bot_message(message):
    userId = str(message.from_user.id)

    if message.text == "Игры":
        boardkeyboard = types.ReplyKeyboardMarkup()
        but1 = types.KeyboardButton("Викторина")
        but2 = types.KeyboardButton("Угадай слово",
                                    web_app=telebot.types.WebAppInfo(url="https://almaxymark.github.io/braingame/"))

        boardkeyboard.add(but1, but2)
        bot.send_message(userId, random.choice(option), reply_markup=boardkeyboard)
        return

    elif message.text == "Профиль":
        money = str(data[userId]["Money"])
        bot.send_message(userId, f"🤩 Игра Викторина:\nКоличество правильно решённых примеров за всё время: {data[userId]['MathVictorina']['rightAnswerAllTime']}\nКоличество правильно решённых примеров за последнюю игру: {data[userId]['MathVictorina']['rightAnswerLast']}\nРекорд: {data[userId]['MathVictorina']['maxRightAnswer']}\n\nИгра Угадай слово:\nКоличество отгаданных слов: {len(data[userId]['GuessTheWord']['listRightAnswer'])}\nКоличество неотгаданных слов: {len(data[userId]['GuessTheWord']['listWrongAnswer'])}\n{nameMoney}:{money}")

    elif message.text == "Помощь":
        bot.send_message(userId, f"🤔 {random.choice(a0)}")

    if message.text == "Викторина":

        data[userId]["MathVictorina"]["rightAnswerLast"] = 0
        data[userId]["isState"] = "MathVictorina"
        data[userId]["MathVictorina"]["attempts"] = 3

        tupleAnswers = generator_example()
        keyboard, example = tupleAnswers[0], tupleAnswers[1]
        data[userId]["MathVictorina"]["answer"] = tupleAnswers[2]

        bot.send_message(userId, random.choice(math))
        bot.send_message(userId, f"Решай\n{example}", reply_markup=keyboard)

        SaveData()
        return

    elif message.text == "Угадай слово":
        #start_GuessTheWord(userId)
        SaveData()
        return

    elif message.text == "Выход":
        data[userId]["isState"] = None

        boardkeyboard = types.ReplyKeyboardMarkup()
        but1 = types.KeyboardButton("Игры")
        but2 = types.KeyboardButton("Профиль")
        but3 = types.KeyboardButton("Помощь")

        boardkeyboard.add(but1, but2, but3)
        bot.send_message(userId, f"Чем займёмся?", reply_markup=boardkeyboard)
        SaveData()
        return

    if data[userId]["isState"] == "MathVictorina":
        if message.text == str(data[userId]["MathVictorina"]["answer"]):
            bot.send_message(userId, f"Правильно")
            data[userId]["MathVictorina"]["rightAnswerLast"] += 1
        else:
            bot.send_message(userId, f"Не правильно\nОтвет был: {data[userId]['MathVictorina']['answer']}")
            data[userId]["MathVictorina"]["attempts"] -= 1

            if data[userId]["MathVictorina"]["attempts"] == 0:

                data[userId]["MathVictorina"]["rightAnswerAllTime"] += data[userId]["MathVictorina"]["rightAnswerLast"]
                if data[userId]["MathVictorina"]["rightAnswerLast"] > data[userId]["MathVictorina"]["maxRightAnswer"]:
                    data[userId]["MathVictorina"]["maxRightAnswer"] = data[userId]["MathVictorina"]["rightAnswerLast"]

                bot.send_message(userId, f"Игра окончена!\nКоличество правильно решённых примеров: {data[userId]['MathVictorina']['rightAnswerLast']}\nТекущий рекорд: {data[userId]['MathVictorina']['maxRightAnswer']}\n Всего правильно решённых примеров: {data[userId]['MathVictorina']['rightAnswerAllTime']}")
                data[userId]["isState"] = None
                data[userId]["MathVictorina"]["attempts"] = 3

                boardkeyboard = types.ReplyKeyboardMarkup()
                but1 = types.KeyboardButton("Игры")
                but2 = types.KeyboardButton("Профиль")
                but3 = types.KeyboardButton("Помощь")

                boardkeyboard.add(but1, but2, but3)
                bot.send_message(userId, f"Чем займёмся?", reply_markup=boardkeyboard)
                SaveData()
                return


        tupleAnswers = generator_example()
        keyboard, example = tupleAnswers[0], tupleAnswers[1]
        data[userId]["MathVictorina"]["answer"] = tupleAnswers[2]
        bot.send_message(userId, f"Решай\n{example}", reply_markup=keyboard)




    # elif data[userId]["isState"] == "GuessTheWord":
    #     if data[userId]["GuessTheWord"]["word"] != None:
    #         hideWord = ""
    #         word = data[userId]["GuessTheWord"]["word"]
    #         if message.text in word:
    #             data[userId]["GuessTheWord"]["currentLetters"] += message.text

    #         else:
    #             data[userId]["GuessTheWord"]["unCurrentLetters"] += message.text
    #             bot.send_message(userId, HANGMAN[7 - data[userId]["GuessTheWord"]["attempts"]])
    #             data[userId]["GuessTheWord"]["attempts"] -= 1

    #             if data[userId]["GuessTheWord"]["attempts"] == 0:
    #                 bot.send_message(userId, f"'{word}' оказалось тем самым словом, которое вы не смогли угадать.")
    #                 ResetGuessTheWord(data, userId, word, False)

    #                 boardkeyboard = types.ReplyKeyboardMarkup()
    #                 but1 = types.KeyboardButton("Игры")
    #                 but2 = types.KeyboardButton("Профиль")
    #                 but3 = types.KeyboardButton("Помощь")

    #                 boardkeyboard.add(but1, but2, but3)
    #                 bot.send_message(userId, f"Чем займёмся?", reply_markup=boardkeyboard)
    #                 SaveData()
    #                 return

    #         for o in data[userId]["GuessTheWord"]["word"]:
    #             if o in data[userId]["GuessTheWord"]["currentLetters"]:
    #                 hideWord += o
    #             else:
    #                 hideWord += "_ "

    #         if CheckWord(hideWord):
    #             bot.send_message(userId, "Ты отгадал слово, молодец")
    #             ResetGuessTheWord(data, userId, word, True)

    #             boardkeyboard = types.ReplyKeyboardMarkup()
    #             but1 = types.KeyboardButton("Игры")
    #             but2 = types.KeyboardButton("Профиль")
    #             but3 = types.KeyboardButton("Помощь")

    #             boardkeyboard.add(but1, but2, but3)
    #             bot.send_message(userId, f"Чем займёмся?", reply_markup=boardkeyboard)
    #             SaveData()
    #             return
                
    #         Send_TextANDKeyboard(userId, hideWord)
    #         return

    #     else:
    #         word = getRandomWord(message.text)
    #         data[userId]["GuessTheWord"]["word"] = word
    #         SaveData()
    #         Send_TextANDKeyboard(userId, f"Игра началась, вы выбрали тему: {message.text}\nВыберите букву")
    #         return

# def start_GuessTheWord(userId: str):
#     data[userId]["GuessTheWord"]["attempts"] = 7
#     data[userId]["GuessTheWord"]["word"] = None
#     data[userId]["isState"] = "GuessTheWord"
#     data[userId]["GuessTheWord"]["currentLetters"] = ""
#     data[userId]["GuessTheWord"]["unCurrentLetters"] = ""
#     boardkeyboard = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True)

#     boardkeyboard.row("Фрукты", "Овощи", "Спорт", "Страны")
#     boardkeyboard.row("Профессии", "Одежда", "Качества человека", "Цветовая палитра")
#     boardkeyboard.row("Транспорт", "Города", "Птицы", "Рыба")
#     boardkeyboard.row("Выход")

#     bot.send_message(userId, f"Выберите тему:", reply_markup=boardkeyboard)

# def getRandomWord(theme: str):
#     return random.choice(dataWords[theme]).lower()

def generator_example():
    listAnswer = []
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    rand = random.randint(1, 4)

    if rand == 1:
        answer = num1 + num2
        a = str(num1) + "+" + str(num2) + "=?"

    elif rand == 2:
        answer = num1 - num2
        a = str(num1) + "-" + str(num2) + "=?"

    elif rand == 3:
        answer = num1 * num2
        a = str(num1) + "*" + str(num2) + "=?"

    elif rand == 4:
        delimoe = num2 * num1
        answer = num1
        a = str(delimoe) + "/" + str(num2) + "=?"

    listAnswer.append(answer)
    listAnswer.append(answer + random.randint(1, 3))
    listAnswer.append(answer - random.randint(1, 5))
    listAnswer.append(answer + random.randint(4, 6))
    random.shuffle(listAnswer)
    boardkeyboard = types.ReplyKeyboardMarkup( row_width = 2)
    but1 = types.KeyboardButton(listAnswer[0])
    but2 = types.KeyboardButton(listAnswer[1])
    but3 = types.KeyboardButton(listAnswer[2])
    but4 = types.KeyboardButton(listAnswer[3])
    but5 = types.KeyboardButton("Выход")
    boardkeyboard.add(but1, but2, but3, but4, but5)
    return boardkeyboard, a, answer


# def Send_TextANDKeyboard(userId: str, text:str):
#     boardkeyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
#     boardkeyboard.row("ё", "й", "ц", "у", "к", "е", "н", "г", "ш", "щ", "з", "х")
#     boardkeyboard.row("ф", "ы", "в", "а", "п", "р", "о", "л", "д", "ж", "э")
#     boardkeyboard.row("я", "ч", "с", "м", "и", "т", "ь", "ъ", "б", "ю")
#     boardkeyboard.row("Выход")

#     bot.send_message(userId, text, reply_markup=boardkeyboard)


# def CheckWord(word):
#     isWin = True
#     for i in word:
#         if i == "_":
#             isWin = False
#             return isWin
#     return isWin

# def ResetGuessTheWord(data:dict, userId:str, word:str, isWin:bool):
#     if isWin:
#         data[userId]["GuessTheWord"]["listRightAnswer"].append(word)
#     else:
#         data[userId]["GuessTheWord"]["listWrongAnswer"].append(word)


#     data[userId]["GuessTheWord"]["attempts"] = 7
#     data[userId]["isState"] = None
#     data[userId]['GuessTheWord']['word'] = None
#     data[userId]["GuessTheWord"]["currentLetters"] = ""
#     data[userId]["GuessTheWord"]["unCurrentLetters"] = ""

def HandlerWeb(data : str) -> dict:
    data = data.split()
    print(data)
    dictData = {}
    for i in data:
        key = i.split(":")[0]
        value = i.split(":")[1]
        dictData[key] = value
    print(dictData)
    return dictData


if __name__ == "__main__":
    print("Начали")
    bot.infinity_polling()