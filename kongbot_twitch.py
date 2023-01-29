import kongbot_parse
import os
import sys
from dotenv import load_dotenv
from twitchio.ext import commands


class Bot(commands.Bot):
    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        # prefix can be a callable, which returns a list of strings or a string...
        # initial_channels can also be a callable which returns a list of strings...

        if "TWITCH_TOKEN" in os.environ and "Channels" in os.environ:
            super().__init__(token=os.environ["TWITCH_TOKEN"], prefix='~', initial_channels=os.environ["Channels"].split(','))
        else:
            super().__init__(token=sys.argv[1], prefix='~', initial_channels=sys.argv[2].split(','))

    async def event_ready(self):
        # Notify us when everything is ready!
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')

    async def event_message(self, message):

        if message.echo:
            return

        #Ensure it only works in chat
        if(message.channel):
            response = kongbot_parse.parse(message.content, "twitch")
            await(message.channel.send(response))
                
    
if __name__ == "__main__":
    load_dotenv()
    bot = Bot()
    bot.run()