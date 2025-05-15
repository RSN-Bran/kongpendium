import kongbot_functions

def parse(message, mode, homePath):

    message = message.lower()

    response = ""

    if message.startswith("!kong") and mode in ["twitter", "twitch", "discord"]:
        response = kongbot_functions.randomKong(homePath).strip()

    elif (message.startswith("!newkong ") or message.lower().startswith("!addkong ")) and mode in ["twitch", "discord"]:
        command = ""
        if("!newkong " in message):
            command = "!newkong "
        elif("!addkong " in message):
            command = "!addkong "
        newKong = message.replace(command, "")

        response = kongbot_functions.addKong(newKong+"\n", homePath)

    elif message == "!help" and mode in ["twitch", "discord"]:
        response = kongbot_functions.help(homePath)

    elif message.startswith("!similarkong "):
        similarKong = message.replace("!similarkong ", "")
        response = kongbot_functions.similarKong(similarKong, homePath)

    return response
