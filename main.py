# setup --------------------------------------------------------
import importlib.util, subprocess, sys, os

# functions ---------------------
# installs a module
def installmod(pipname, modname):
    installed = importlib.util.find_spec(modname)
    while True:
        if installed == None:
            print(f'{pipname} not installed. Installing...')
            subprocess.check_call([sys.executable, "-m", "pip", "install", pipname])
        else:
            newmodname = __import__(modname)
            print(f'imported {modname}')
            break
    return newmodname
        
# install imports -----------------------
# for telegram bot API
telebot = installmod('pyTelegramBotAPI', 'telebot')

# for loading .env file
dotenv = installmod('python-dotenv', 'dotenv')
from dotenv import load_dotenv

# get telegram API key from .env file --
load_dotenv()
API_KEY = os.getenv('API_KEY')

# create bot ---------------------------
bot = telebot.TeleBot(API_KEY)

# main ---------------------------------------------------------
# 1. reply to message (from command)
@bot.message_handler(commands=['hi'])
def hi(message):
    bot.reply_to(message, 'hi')

# 2. send message (from command)
@bot.message_handler(commands=['hello'])
def hello(message):
    bot.send_message(message.chat.id, 'hello')

# 3. sends message automatically
# bot.send_message(chat_id, text)

# leep bot active
print('bot running...')
bot.polling()

# ctrl + c to end
print('bot ended')