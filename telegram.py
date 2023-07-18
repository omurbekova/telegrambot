from email import message
import telebot 
from telebot import types


bot = telebot.TeleBot('6388502328:AAHf6hsQQdwYYOqFpcuqt7rcDRoy980M6Vs')


@bot.message_handler(commands=['start'])
def start_message(message): 
  markup= types.ReplyKeyboardMarkup(resize_keyboard= True)  
  button1 = types.KeyboardButton('почему я не могу выложить игру?')
  button2 = types.KeyboardButton('как авторизоваться?')
  button3 = types.KeyboardButton('как купить игру?')
  button4 = types.KeyboardButton('информация о сайте')  
  markup.row(button1)
  markup.row(button2) 
  markup.row(button3) 
  markup.row(button4)
  bot.send_message(message.chat.id, 'Добро пожаловать! Чем я вам могу помочь?', reply_markup = markup)


@bot.message_handler(content_types=['text'])
def message_bot(message):
    if message.text == 'почему я не могу выложить игру?':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('перейти на сайт по ссылке')
        back = types.KeyboardButton('назад')
        markup.row(btn)
        markup.row(back)
        bot.send_message(message.chat.id, 'Для того чтобы выложить игру,  вам необходимо пройти регистрацию в качестве издателя.\n После регистрации вам будет доступна функция выкладывать игру.', reply_markup=markup)
    

    elif message.text == 'как авторизоваться?':
        markup= types.ReplyKeyboardMarkup(resize_keyboard= True)  
        button1 = types.KeyboardButton('перейти на сайт по ссылке')
        back = types.KeyboardButton('назад')
        markup.row(button1)
        markup.row(back)
        bot.send_message(message.chat.id, 'Для авторизации вам необходимо перейти на сайт и выбрать способ авторизации: как покупатель или как издатель. \nПосле чего вам необходимо перейти на указанную ранее почту и перейти по ссылке чтобы активировать аккаунт.',
                          reply_markup=markup)
    
    elif message.text == 'как купить игру?':
        markup= types.ReplyKeyboardMarkup(resize_keyboard= True)  
        button1 = types.KeyboardButton('перейти на сайт по ссылке')
        back = types.KeyboardButton('назад')
        markup.row(button1)
        markup.row(back)

        bot.send_message(message.chat.id, 'Для того чтобы купить игру, вам необходимо перейти на сайт, пройти регистрацию и активировать аккаунт. \nПосле чего вам будет доступна функция покупки игр.', 
                         reply_markup=markup)
    
    elif message.text == 'информация о сайте':
        markup= types.ReplyKeyboardMarkup(resize_keyboard= True)  
        button1 = types.KeyboardButton('перейти на сайт по ссылке')
        back = types.KeyboardButton('назад')
        markup.row(button1)
        markup.row(back)
        bot.send_message(message.chat.id, 'Наш сайт EpicGames является игровой площадкой для покупки и продажи игр.\nНа сайте можно преобрести самые свежие игровые новинки, а также если вы являетесь разработчиком игр, поделиться со всеми своими работами.', 
                         reply_markup=markup)

    elif message.text == 'перейти на сайт по ссылке':
        bot.send_message(message.chat.id, 'вы перешли на сайт')

    elif message.text == 'назад':
        markup= types.ReplyKeyboardMarkup(resize_keyboard= True)  
        button1 = types.KeyboardButton('почему я не могу выложить игру?')
        button2 = types.KeyboardButton('как авторизоваться?')
        button3 = types.KeyboardButton('как купить игру?')
        button4 = types.KeyboardButton('информация о сайте')  
        markup.row(button1)
        markup.row(button2) 
        markup.row(button3) 
        markup.row(button4)
        bot.send_message(message.chat.id, 'вы перешли в главное меню', reply_markup = markup)



bot.polling(none_stop=True)