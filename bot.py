import telebot
from telebot import types

bot = telebot.TeleBot('TOKEN') #Enter here your token

# Start
@bot.message_handler(commands=['start'])
def start(message):
    main_menu(message)

# Main menu
def main_menu(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    button1 = types.KeyboardButton("День 1")
    button2 = types.KeyboardButton("День 2")
    
    keyboard.add(button1, button2)

    bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}! Я буду твоим экскурсоводом по Калининграду", reply_markup=keyboard)

# Обработка текстовых сообщений
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "День 1":
        option_1_menu(message)
    elif message.text == "День 2":
        option_2_menu(message)
    elif message.text == "Руины Королевского замка":
        photo = open('castle.png', 'rb')
        bot.send_photo(message.chat.id, photo, caption="Руины королевского замка в Калининграде, известного также как Кёнигсбергский замок, представляют собой остатки величественного сооружения, построенного в XIII веке Тевтонским орденом. Замок служил резиденцией прусских королей и был важным культурным и политическим центром. В годы Второй мировой войны он сильно пострадал и позже был частично разобран, однако его руины до сих пор привлекают туристов и историков, сохраняя атмосферу средневековой истории и величия.")
    elif message.text == "Остров Канта":
        photo = open('kant.png', 'rb')
        bot.send_photo(message.chat.id, photo, caption="Остров Канта. Расположен остров Канта в сердце Калининграда. Это старинный район с Кафедральным собором - величественным готическим сооружением и могилой Иммануила Канта. История данного острова началась ещё в 13 веке, за всё это время остров не пострадал и сохранил свой исторический вид до наших дней. На острове есть также парк скульптур в котором можно увидеть Гагарина, Блока и прочих личностей в виде скульптур.")
    elif message.text == "Музей янтаря":
        photo = open('amber.png', 'rb')
        bot.send_photo(message.chat.id, photo, caption="Музей янтаря расположен в крепостной башне К.-Ф. Доны, которая была построена в 1853 г. и входила во внутреннее кольцо укреплений г. Кёнигсберга. В коллекции музея более 16 тысяч экспонатов. После экскурсии вы будете знать все о янтаре: о его происхождении, стоимости, особенностях добычи и обработки. В поселке Янтарном Калининградской области, по разным оценкам, сосредоточено от 70 до 90 мировых запасов «солнечного камня».")
    elif message.text == "пивоварня Понарт":
        photo = open('beer.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, caption="Современная пивоварня Ponarth известна не только вкусным пивом, но и гостеприимством - в стенах пивоварни организуются интереснейшие экскурсии, вы познакомитесь с историей создания которая начинается с 1849 года, а так же попробуете 8 сортов пива!")
    elif message.text == "Форт Дёнхофф":
        photo = open('fortress.png', 'rb')
     bot.send_photo(message.chat.id, photo, caption="Названный в честь губернатора города Мемель (теперь Клайпеда в составе Литвы) форт №11 «Фридрих фон Денхофф» в Калининграде не так известен, как форт №5, но как музейный комплекс он не менее интересен. Это единственный из фортов Кенигсберга (а всего их 15), который сохранился практически в первозданном виде.")
    elif message.text == "Музей мирового океана":
        photo = open('oceanMuseum.png', 'rb')
        bot.send_photo(message.chat.id, photo, caption="Музей Мирового Океана - уникальный выставочный комплекс в Калининграде. Пришвартованные музеи-на-борту кораблей, припаркованный самолет, несколько разнообразных павильонов тематических и, как вишенка на кусочке торта - музей-подводная лодка, единственная в России, что находится на плаву при том. Так же водные экскурсия позволяет оценить всю красоту Калининграда и речки Преголи.")
    elif message.text == "Памятник 1200 гвардейцам":
        photo = open('guardsman.png', 'rb')
        bot.send_photo(message.chat.id, photo, caption="Памятник «1200 гвардейцам» находится в Калининграде и посвящен советским воинам, павшим в боях за город в 1945 году. Открытый в 1945 году, он представляет собой братскую могилу, в которой захоронены останки 1200 солдат и офицеров. Композиция памятника включает в себя обелиск и скульптурную группу, символизирующую героизм и жертвенность защитников. Это один из первых и самых значимых памятников советским воинам, установленный после Великой Отечественной войны.")
    elif message.text == "Парк победы":
        print("it's works")
        photo = open('TourBot/victoryPark.png', 'rb')
        bot.send_photo(message.chat.id, photo, caption="Парк Победы в Калининграде — это живописное место для отдыха и прогулок, посвященное памяти героев Великой Отечественной войны. Расположенный в центральной части города, парк представляет собой зеленую зону с ухоженными аллеями, памятниками и мемориалами. Здесь часто проводятся культурные и общественные мероприятия, а также работают детские и спортивные площадки, что делает его популярным местом для семейного отдыха. Парк Победы служит как местом для спокойных прогулок, так и для активного времяпрепровождения на свежем воздухе.")
    elif message.text == "⬅️ Назад":
        main_menu(message)

# Меню для "День 1"
def option_1_menu(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    sub_button1 = types.KeyboardButton("Остров Канта")
    sub_button2 = types.KeyboardButton("Руины Королевского замка")
    sub_button3 = types.KeyboardButton("пивоварня Понарт")
    sub_button4 = types.KeyboardButton("Форт Дёнхофф")
    back_button = types.KeyboardButton("⬅️ Назад")

    keyboard.add(sub_button1, sub_button2, sub_button3, sub_button4, back_button)
    

    bot.send_message(message.chat.id, "День 1. Выберите достопримечательность:", reply_markup=keyboard)

# Меню для "Опция 2"
def option_2_menu(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    sub_button1 = types.KeyboardButton("Музей мирового океана")
    sub_button2 = types.KeyboardButton("Музей янтаря")
    sub_button3 = types.KeyboardButton("Памятник 1200 гвардейцам")
    sub_button4 = types.KeyboardButton("Парк победы")
    back_button = types.KeyboardButton("⬅️ Назад")

    keyboard.add(sub_button1, sub_button2, sub_button3, sub_button4)
    keyboard.add(back_button)

    bot.send_message(message.chat.id, "День 2. Выберите достопримечательность:", reply_markup=keyboard)

# Запуск бота
bot.polling(non_stop=True)