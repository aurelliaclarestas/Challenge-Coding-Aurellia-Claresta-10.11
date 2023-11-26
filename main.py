from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "6765684315:AAFNh7jZMPX2_B5NoQdJpM9BM-sP_fBqgV8"
USERNAME_BOT = "@AurelliaClarestaIGS_bot"

async def start_command(update : Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Gunakan /help untuk melihat apa yang anda butuhkan.')

async def help_command(update : Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Thank you sudah menggunakan bot ini. Gunakan perintah dengan huruf kecil saja. Berikut Daftar perintah yang bisa anda pilih :\n halo \n tentang kamu \n siapa kamu? \n kamu bersekolah dimana? \n kamu kelas berapa? \n minta ig nya dong \n siapa pacar kamu \n')

async def text_massage(update : Update, context: ContextTypes.DEFAULT_TYPE):
    text_diterima: str = update.message.text

    print('text diterima: ', text_diterima)

    if 'halo' in text_diterima:
        await update.massage.reply_text('halo juga... ')
    elif 'tentang kamu' in text_diterima:
        await update.message.reply_text('hai namaku bot di buat oleh Aurellia')
    elif 'siapa kamu?' in text_diterima:
        await update.message.reply_text('saya adalah bot yang akan membantu anda...')
    elif 'kamu bersekolah dimana?' in text_diterima:
        await update.message.reply_text(' Saya bersekolah di IGS')
    elif 'kamu kelas berapa?' in text_diterima:
        await update.message.reply_text(' saya kelas 10 SMA')
    elif 'minta ig nya dong' in text_diterima:
        await update.message.reply_text('bolehh.. zouzeraq di follow ya')
    elif 'siapa pacar kamu' in text_diterima:
        await update.message.reply_text('kenalin pacar aku Sakusa Kiyoomi, atlet voli elit')
    

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'eror : {context.error}')

if __name__ == '__main__':
    print('Bot Dimulai...')
    
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler( 'start', start_command ))

    app.add_handler(CommandHandler( 'help', help_command))

    app.add_handler(MessageHandler( filters.TEXT, text_massage))

    app.add_error_handler(error)

    app.run_polling(poll_interval=1)