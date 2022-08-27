from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from spy import *
from XO import *


async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update,context)
    await update.message.reply_text(f'Hi {update.effective_user.first_name}')
# hi_command
# time_command
# help_command
# sum_command

print(datetime.datetime.now().time());

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update,context)
    await update.message.reply_text(f'{datetime.datetime.now().time()}')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update,context)
    tempStr = ""
    tempStr += "/hello\n"
    tempStr += "/time\n"
    tempStr += "/help\n"
    tempStr += "/sum\n"
    tempStr += "/xo start\n"
    tempStr += "/xo цифра 1-9\n"
    await update.message.reply_text(tempStr)

async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update,context)
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'Hi {x}+{y}= {x+y}')


async def XO_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update,context)
    if ( len(update.message.text) > 4 ):
        msg = update.message.text[4:]
        if ( msg ==  "start"):
            await update.message.reply_text(XO_startGame())
        elif ( msg in  ["1","2","3","4","5","6","7","8","9",]):
            await update.message.reply_text(XO_gameIter(int(msg)-1))
        else :
            await update.message.reply_text(f"Неккоректная команда {msg}")
    else :
        await update.message.reply_text(f"Некоректная команда нет аргумента")
