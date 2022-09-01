
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_command import *





app = ApplicationBuilder().token("5495157332:AAHgpbtMjInlgyH2suerwPQW_UXRHU9MuE0").build()

app.add_handler(CommandHandler("hello", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("xo", XO_command))
app.add_handler(CommandHandler("curs", curs_command))

print('server start ')
app.run_polling()
