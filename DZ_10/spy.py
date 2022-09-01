from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime



def log(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    try:
        file = open('db.csv','a')

        tempStr = f'{update.effective_user.first_name},{update.effective_user.id},{update.message.text}\n'
        tempStr = tempStr.encode("utf-8").decode()

        file.write(tempStr)
        file.close()
    except Exception as inst:
        print(inst)