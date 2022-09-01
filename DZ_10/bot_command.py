from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from spy import *
from XO import *
import curs
import google_currency 


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
    tempStr += "/curs currency1 currency2 value"
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


async def curs_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update,context)
    errorFlag = False
    currency1 = "RUB"
    currency2 = "USD"
    value = 1


    msg = update.message.text
    items = msg.split()
    if ( len(items) == 2 ):
        if ( items[1].isdigit() ):
            value = float(items[1])
        else :
            currency2  = items[2]
    elif ( len(items) == 3 ):
        if ( items[2].isdigit() ):
            currency2  = items[1]
            value = float(items[2])
        else :
            currency1  = items[1]
            currency2  = items[2]
    elif ( len(items) == 4 ):
        currency1  = items[1]
        currency2  = items[2]    
        if ( items[3].isdigit() ):
            value = float(items[3])
        else:   
            errorFlag = True
    if (currency1.upper() in google_currency.CODES) and (currency2.upper() in google_currency.CODES) and ( not errorFlag ):
        await update.message.reply_text( curs.curd_found(currency1,currency2,value) )
    else:
         await update.message.reply_text( "Неккоректные данные "+msg )
