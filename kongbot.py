import random
def randomKong():
    file = open("kongpendium.txt", "r")
    lines = file.readlines()
    kong = random.randrange(0, len(lines))
    
    file.close()
    return lines[kong]

def addKong(newKong):
    file = open("kongpendium.txt", "r")
    lines = file.readlines()
    if newKong in lines:
        file.close()
        return False
    else:
        writefile = open("kongpendium.txt", "a")
        writefile.write(newKong)
        writefile.close()
        return True