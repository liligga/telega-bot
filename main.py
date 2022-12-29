import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

logging.basicConfig(
	format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


########  COMMAND HANDLERS IN TG MENU ###############
def start(bot, update):
	bot.message.reply_text(start_menu_message(),
							reply_markup=start_menu_keyboard())

def big_menu_command_handler(bot, update):
	bot.message.reply_text(menu_page_message(),
							reply_markup=menu_page_keyboard())

def question_menu_handler(bot, update):
	bot.message.reply_text(question_menu_message(),
							reply_markup=question_menu_keyboard())


def aboutus_menu_handler(bot, update):
	bot.message.reply_text(aboutus_message(),
							reply_markup=aboutus_keyboard())

def values_page_handler(bot, update):
	bot.message.reply_text(values_page_message())

def activities_page_handler(bot, update):
	bot.message.reply_text(values_page_message())


###############  FOR BUTTONS ########################

def start_menu(bot, update):
	bot.callback_query.message.edit_text(start_menu_message(),
							reply_markup=start_menu_keyboard())

def question_menu(bot, update):
	bot.callback_query.message.edit_text(question_menu_message(),
							reply_markup=question_menu_keyboard())

def big_menu_page(bot, update):
	bot.callback_query.message.edit_text(menu_page_message(),
							reply_markup=menu_page_keyboard())


def aboutus_menu(bot, update):
	bot.callback_query.message.edit_text(aboutus_message(),
							reply_markup=aboutus_keyboard())

def values_page(bot, update):
	bot.callback_query.message.edit_text(values_page_message())

def activities_page(bot, update):
	bot.callback_query.message.edit_text(values_page_message())

def error(update, context):
	print(f'Update {update} caused error {context.error}')

############################ Keyboards #########################################
def start_menu_keyboard():
	keyboard = [[InlineKeyboardButton('Задать вопрос', callback_data='question')],
				[InlineKeyboardButton('Меню', callback_data='menu')]]
	return InlineKeyboardMarkup(keyboard)

def question_menu_keyboard():
	keyboard = [[InlineKeyboardButton('Назад', callback_data='home')],
				[InlineKeyboardButton('Получить ответ', callback_data='answer')]]
	return InlineKeyboardMarkup(keyboard)

def menu_page_keyboard():
	keyboard = [[InlineKeyboardButton('Узнать о Федерации', callback_data='aboutus')],
				[InlineKeyboardButton('Адаптивные виды хоккея', callback_data='menu_1')],
				[InlineKeyboardButton('Путь чемпиона', callback_data='menu_2')],
				[InlineKeyboardButton('Всё для хоккея', callback_data='menu_3')],
				[InlineKeyboardButton('Сделать пожертвования', callback_data='menu_4')],
				[InlineKeyboardButton('Кто такой Фырк', callback_data='menu_5')],
				[InlineKeyboardButton('Квиз', callback_data='menu_6')],
				[InlineKeyboardButton('Получить стикерпак', callback_data='menu_7')],
				[InlineKeyboardButton('Назад', callback_data='home')]]
	return InlineKeyboardMarkup(keyboard)

def aboutus_keyboard():
	keyboard = [[InlineKeyboardButton('Ценности Федерации', callback_data='values')],
				[InlineKeyboardButton('Направления деятельности', callback_data='activities')],
				[InlineKeyboardButton('Меню', callback_data='menu')],
				[InlineKeyboardButton('На главную', callback_data='home')]]
	return InlineKeyboardMarkup(keyboard)

############################# Messages #########################################
def start_menu_message():
	return 'тут будет логотип федерации'

def question_menu_message():
	return """На связи Фырк. Я енот, но это не мешает мне соединить тебя с сотрудниками
Федерации. Просто напиши свой вопрос и тебе ответят."""

def menu_page_message():
	return 'Я могу помочь в этих вопросах:'

def aboutus_message():
	return """У нас в хоккей играет каждый!
С 2016 года наша семья – Детская следж-хоккейная команда, воплощает мечту: даем
возможность любому особенному ребенку играть в хоккей! Не важно: в каком городе России
ребенок живет, сколько ему лет и занимался ли он когда-либо спортом. Сейчас мы - Федерация
адаптивного хоккея.
Федерация адаптивного хоккея – это некоммерческая организация, которая создает условия для
развития адаптивных видов хоккея в России, повышает их роль в социальной реабилитации
детей и молодежи с инвалидностью.
На данный момент Федерация — единственная в России организация, которая занимается
развитием адаптивного хоккея для детей на системном уровне и объединяет детские команды со
всех уголков страны!"""

def values_page_message():
	return """ХОККЕЙ Это здоровье, а не травмы. Это захватывающая игра и закалка характера, а не цель
	стать чемпионом.
	КОМАНДА Это вера в то, что ты – часть единого целого, и уверенность в том, что тебя не
	оставят. Это – когда играют все, а не один за всех.
	ДРУЖБА Это новые товарищи, а не соперники. Это радость общения и взаимовыручки, даже
	через сотни и тысячи километров.
	СЕМЬЯ Это безоговорочная поддержка ребенка. Даже если он из другой команды. ПОБЕДА Это
	возможность развиваться и стать лучше, а не быть лучшим любой ценой. Это твоя внутренняя
	сила и уверенность в себе, а не только количество забитых шайб. БЕЗГРАНИЧНЫЕ
	ВОЗМОЖНОСТИ Это шанс узнать мир вокруг и принять его многообразие, а не противостоять
	ему вопреки всему. Федерация адаптивного хоккея – это шанс стать тем, кто ты есть, воплотить
	в жизнь свои мечты и возможности!"""

def activities_page_message():
	return """Основные направления деятельности Федерации:
- Поддержка новых и действующих детских команд по адаптивному хоккею;
- Обучение тренеров, судей, координаторов, волонтеров-пушеров (помощников на коньках);
- Содействие разработке специального спортивного инвентаря для адаптивного хоккея;
- Организация мероприятий – турниры, летний инклюзивный лагерь, интенсивы и молодежная
сборная;
- Популяризация адаптивного хоккея в России;
- Развитие и наставничество игроков."""

def help_command(update: Update, context: CallbackContext) -> None:
	"""Displays info on how to use the bot."""
	update.message.reply_text("Use /start to test this bot.")


def main() -> None:
	"""Run the bot."""
	# Create the Updater and pass it your bot's token.
	updater = Updater("TOKEN")

	#############  for handling commands #######################
	updater.dispatcher.add_handler(CommandHandler('start', start))
	updater.dispatcher.add_handler(CommandHandler('menu', big_menu_command_handler))
	updater.dispatcher.add_handler(CommandHandler('question', question_menu_handler))
	updater.dispatcher.add_handler(CommandHandler('aboutus', aboutus_menu_handler))
	updater.dispatcher.add_handler(CommandHandler('values', values_page_handler))
	updater.dispatcher.add_handler(CommandHandler('activities', activities_page_handler))

	############### for buttons ##################################
	updater.dispatcher.add_handler(CallbackQueryHandler(start_menu, pattern='home'))
	updater.dispatcher.add_handler(CallbackQueryHandler(question_menu, pattern='question'))
	updater.dispatcher.add_handler(CallbackQueryHandler(big_menu_page, pattern='menu'))
	updater.dispatcher.add_handler(CallbackQueryHandler(aboutus_menu, pattern='aboutus'))
	updater.dispatcher.add_handler(CallbackQueryHandler(values_page, pattern='values'))
	updater.dispatcher.add_handler(CallbackQueryHandler(activities_page, pattern='activities'))
	updater.dispatcher.add_error_handler(error)
	# Start the Bot
	updater.start_polling()

	# Run the bot until the user presses Ctrl-C or the process receives SIGINT,
	# SIGTERM or SIGABRT
	updater.idle()


if __name__ == '__main__':
	main()