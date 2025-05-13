import random
import difflib

def randomKong(homePath):

    file = open(homePath+"kongpendium.txt", "r", encoding="utf8")
    lines = file.readlines()
    kong = random.randrange(0, len(lines))
    
    file.close()
    return lines[kong]

def addKong(newKong, homePath):
    file = open(homePath+"kongpendium.txt", "r", encoding="utf8")
    lines = file.readlines()
    if newKong in lines:
        file.close()
        return "Duplicate Kong Detected"
    else:
        writefile = open(homePath+"kongpendium.txt", "a")
        writefile.write(newKong)
        writefile.close()
        return "New Kong just dropped"

def similarKong(similarKong, homePath):
    file = open(homePath+"kongpendium.txt", "r", encoding="utf8")
    lines = file.readlines()
    similarKongs =  difflib.get_close_matches(similarKong, lines)

    return "These are the closest kongs:\n" + ''.join(similarKongs)

def help(homePath):
    helpfile = open(homePath+"help.txt", "r")
    helpText = helpfile.read()
    helpfile.close()
    return helpText
