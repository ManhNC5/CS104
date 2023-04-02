import telegram
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
import time

# Define your bot token obtained from BotFather
TOKEN = '6086644494:AAHsovr3fEw8VX7forONfjlcAqlrLydvisc'

# Create an instance of the Telegram API bot
bot = telegram.Bot(token=TOKEN)

# Create an instance of the Updater class to handle updates from Telegram
updater = Updater(TOKEN)

# Define a function to leave all channels that the bot has joined
def leave_all_channels(update, context):
    # Get the list of all channels that the bot has joined
    channels = bot.get_chat_memberships()
    
    # Loop through each channel and leave it
    for channel in channels:
        bot.leave_chat(channel.chat.id)

        # Send a message to the user confirming that the bot has left all channels
        update.message.reply_text('I have left all channels.')
        
        time.sleep(2)

# Set up a command handler to trigger the leave_all_channels function when the user sends the /leaveall command
updater.dispatcher.add_handler(CommandHandler('leaveall', leave_all_channels))

# Start the bot
updater.start_polling()
updater.idle()
